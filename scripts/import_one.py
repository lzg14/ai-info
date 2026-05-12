#!/usr/bin/env python3
"""
单篇入库：import_one.py
- 从 DB 读取所有 important 记录（不再读 important/ 目录）
- 对每篇：读文件 → 格式化 → 写入 docs/YYYY/MM/ → mark(done)
- 支持两种调用：
    python import_one.py                    # 全量处理所有 important
    python import_one.py <url_or_file>      # 单篇处理
"""
import sys
import os
import re
import json
import unicodedata
import subprocess
from pathlib import Path
from datetime import datetime

BASE = Path("/mnt/d/ProjectFile/ai-info")
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "scripts"))

from config_loader import Config
from state_manager import (
    IMPORTANT, PENDING,
    mark, get_status, get_score,
    S_IMPORTANT, S_DONE,
    init as sm_init
)
sm_init()


def load_article_from_file(filepath: Path) -> dict | None:
    """读取文件内容"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None


def url_to_hash(url: str) -> str:
    import hashlib
    return hashlib.md5(url.encode('utf-8')).hexdigest()[:12]


def get_docs_dir(article: dict) -> Path:
    """根据 publish_date 决定 docs/YYYY/MM/ 目录"""
    date_str = article.get('publish_date') or datetime.now().strftime('%Y-%m-%d')
    year, month = date_str[:4], date_str[5:7]
    docs_dir = BASE / "docs" / year / month
    docs_dir.mkdir(parents=True, exist_ok=True)
    return docs_dir


def slugify(title: str) -> str:
    """生成 URL-safe 的 slug"""
    slug = unicodedata.normalize('NFKC', title)
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    return slug[:80]


def format_v5(article: dict) -> str:
    """V5 MD 格式"""
    title = article.get('title') or 'Untitled'
    date = article.get('publish_date') or datetime.now().strftime('%Y-%m-%d')
    source_name = article.get('source_name', '')
    url = article.get('url', '')
    summary = article.get('summary', '')
    content = article.get('content', '')

    blocks = []
    blocks.append(f'<!-- {json.dumps({"title": title, "date": date}, ensure_ascii=False)} -->')
    blocks.append(f'# {title}')
    blocks.append(f'📅 {date}')
    blocks.append(f'📢 来源：[{source_name}]({url})')
    if summary:
        blocks.append(f'\n> {summary}')
    blocks.append('\n<!-- 正文开始 -->\n')
    blocks.append(content.strip())
    blocks.append('\n<!-- 正文结束 -->')

    return '\n'.join(blocks)


def import_article(article: dict, filepath: Path) -> bool:
    """写入 docs/，成功返回 True"""
    try:
        docs_dir = get_docs_dir(article)
        title = article.get('title', 'untitled')
        slug = slugify(title)
        date_str = article.get('publish_date', datetime.now().strftime('%Y-%m-%d'))
        basename = f"{date_str}_{slug}.md"
        dest_path = docs_dir / basename

        # 防止重名
        if dest_path.exists():
            basename = f"{date_str}_{slug}_2.md"
            dest_path = docs_dir / basename

        content = format_v5(article)
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✅ {dest_path.relative_to(BASE)}")
        return True
    except Exception as e:
        print(f"  ❌ 写入失败: {e}")
        return False


def get_important_records() -> list[tuple]:
    """从 DB 读取所有 important 记录"""
    import sqlite3
    conn = sqlite3.connect(BASE / "data" / "state.db")
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT url, file FROM seen_urls WHERE status = ?",
            (S_IMPORTANT,)
        )
        return [(r[0], r[1]) for r in cur.fetchall()]
    finally:
        conn.close()


def process_record(url: str, filename: str) -> bool:
    """处理单条 important 记录"""
    h = url_to_hash(url)
    filepath = IMPORTANT / f"{h}.json"

    # 如果 important 目录没有，尝试 pending 目录（罕见）
    if not os.path.exists(str(filepath)):
        filepath = PENDING / f"{h}.json"

    if not os.path.exists(str(filepath)):
        print(f"  ⚠️ 文件不存在: {url}")
        return False

    article = load_article_from_file(filepath)
    if article is None:
        print(f"  ⚠️ 文件解析失败: {filepath}")
        return False

    success = import_article(article, filepath)

    if success:
        # 入库成功：mark done，删文件
        score = article.get("ai_score") or get_score(url)
        mark(url, S_DONE, score=score)
        try:
            os.remove(str(filepath))
        except Exception:
            pass
        return True
    else:
        return False


def main_single(url_or_file: str):
    """处理单篇文章（URL 或文件路径）"""
    # 判断是 URL 还是文件
    if url_or_file.startswith('http'):
        url = url_or_file
        status = get_status(url)
        if status == S_DONE:
            print(f"已入库，跳过: {url}")
            return
        h = url_to_hash(url)
        filepath = IMPORTANT / f"{h}.json"
        if not os.path.exists(str(filepath)):
            filepath = PENDING / f"{h}.json"
    else:
        filepath = Path(url_or_file)
        if not filepath.exists():
            print(f"文件不存在: {filepath}")
            return
        article = load_article_from_file(filepath)
        if article is None:
            print(f"文件解析失败: {filepath}")
            return
        url = article.get('url', '')

    if not os.path.exists(str(filepath)):
        print(f"文件不存在: {filepath}")
        return

    article = load_article_from_file(filepath)
    if article is None:
        print(f"文件解析失败: {filepath}")
        return

    success = import_article(article, filepath)
    if success:
        score = article.get("ai_score") or get_score(url)
        mark(url, S_DONE, score=score)
        try:
            os.remove(str(filepath))
        except Exception:
            pass


def main():
    """全量处理所有 important"""
    records = get_important_records()
    if not records:
        print("无重要文章待入库（DB 中无 important 记录）")
        return

    print(f"待入库: {len(records)}篇")
    cfg = Config.load_from_file(str(BASE / "config" / "config.json"))

    success_count = 0
    for url, filename in records:
        print(f"\n处理: {url}")
        if process_record(url, filename):
            success_count += 1

    print(f"\n入库完成: {success_count}/{len(records)} 篇")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main_single(sys.argv[1])
    else:
        main()
