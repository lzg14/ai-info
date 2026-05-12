#!/usr/bin/env python3
"""
导入器：import_one.py（文件永存架构）
- 从 DB 读 scored（score >= 8）且未 done 的 URL
- 从固定路径读文件内容
- 写入 docs/YYYY/MM/YYYY-MM-DD_slug.md
- 更新 DB status=done
- 文件永不移动/删除
"""
import sys, os, json, re, hashlib
from pathlib import Path
from datetime import datetime

BASE = Path("/mnt/d/ProjectFile/ai-info")
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "scripts"))

from state_manager import (
    mark,
    init as sm_init,
    S_SCORED,
    S_DONE,
    DB_PATH,
)
from config_loader import Config
import sqlite3

sm_init()
config = Config.load_from_file()

# 固定路径的前缀（article_path 返回完整绝对路径）
ARTICLES_PREFIX = str(BASE / "temp" / "articles")


def load_article(url: str) -> dict | None:
    """从固定路径加载文章文件"""
    h = hashlib.md5(url.encode()).hexdigest()[:12]
    fp = os.path.join(ARTICLES_PREFIX, f"{h}.json")
    if not os.path.exists(fp):
        return None
    with open(fp, encoding='utf-8') as f:
        return json.load(f)


def slugify(title: str) -> str:
    """生成 URL-safe slug"""
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    return slug[:60]


def write_docs(article: dict) -> str | None:
    """
    将文章写入 docs/YYYY/MM/YYYY-MM-DD_slug.md
    返回写入的文件路径（相对于 BASE）

    格式：HTML comment frontmatter（与现有 docs 一致）
    <!-- {"title": "...", "source_name": "...", "source_url": "...", "date": "YYYY-MM-DD"} -->
    # 标题
    📅 YYYY-MM-DD
    📢 来源：[名称](URL)

    > 摘要（如有）

    <!-- 正文开始 -->

    正文内容

    <!-- 正文结束 -->
    """
    url = article.get('url', '')
    title = article.get('title', 'untitled')
    title_zh = article.get('title_zh', '')
    source_name = article.get('source_name', '')
    source_url = article.get('source_url', '')
    publish_date = article.get('publish_date', '')
    content = article.get('content', '') or article.get('summary', '')
    summary = article.get('summary', '')
    tags = article.get('tags', [])

    # 决定目标目录
    if publish_date:
        try:
            dt = datetime.fromisoformat(publish_date.replace('Z', '+00:00'))
            year = dt.year
            month = dt.month
        except:
            year, month = 2026, 5
    else:
        year, month = 2026, 5

    # 生成文件名
    date_str = publish_date[:10] if publish_date else datetime.now().strftime('%Y-%m-%d')
    slug = slugify(title)
    filename = f"{date_str}_{slug}.md"
    docs_dir = BASE / "docs" / str(year) / f"{month:02d}"
    os.makedirs(docs_dir, exist_ok=True)
    filepath = docs_dir / filename

    # 生成 frontmatter（HTML comment + JSON，与现有 docs 格式一致）
    fm = {
        "title": title,
        "title_zh": title_zh,
        "url": url,
        "source": source_name,
        "source_url": source_url,
        "publish_date": date_str,
        "score": article.get("score"),
        "tags": tags,
    }
    fm_json = json.dumps(fm, ensure_ascii=False)

    # 组装正文
    lines = [f"<!-- {fm_json} -->", f"# {title}", ""]

    if publish_date:
        lines.append(f"📅 {date_str}")

    if source_name and source_url:
        lines.append(f"📢 来源：[{source_name}]({source_url})")
    elif source_name:
        lines.append(f"📢 来源：{source_name}")

    if summary:
        # 去重：summary 常常等于标题或正文第一句，只在 summary 与正文开头有明显差异时才展示
        body_stripped = content.strip()
        # 取正文开头 200 字符
        body_start = body_stripped[:200].lower()
        # 去掉换行符
        body_start = ' '.join(body_start.split())
        # summary 转纯文本（去掉 > 等格式）
        s = summary.strip().lower()
        s_clean = ' '.join(s.split())
        # 如果 summary 是 body 开头的子集（重复），则跳过
        if len(s_clean) < 20 or s_clean not in body_start[:500]:
            lines.extend(["", f"> {summary}"])

    if tags:
        tags_str = " · ".join(str(t) for t in tags)
        lines.extend(["", f"🏷️ {tags_str}"])

    lines.extend(["", "<!-- 正文开始 -->", "", content, "", "<!-- 正文结束 -->"])

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return str(filepath.relative_to(BASE))


def run():
    """导入所有 scored 高分文章"""
    conn = sqlite3.connect(DB_PATH)
    # 读所有 scored 且 score >= 8 且未 done 的
    rows = conn.execute(
        "SELECT url, score FROM seen_urls WHERE status=? AND score >= 8",
        (S_SCORED,)
    ).fetchall()
    conn.close()

    print(f"[import] 待导入: {len(rows)} 篇")

    imported = 0
    skipped = 0
    errors = 0
    years_imported = set()

    for url, score in rows:
        article = load_article(url)
        if not article:
            print(f"  [WARN] 文件缺失: {url[:50]}")
            errors += 1
            continue

        # 检查是否已入库（docs 里是否有同名文件）
        title = article.get('title', '')
        slug = slugify(title)
        date_str = (article.get('publish_date', '') or datetime.now().isoformat())[:10]
        year, month = date_str[:4], date_str[5:7]

        # 简单检查：docs/YYYY/MM/date_slug.md 是否存在
        possible = BASE / "docs" / year / month / f"{date_str}_{slug}.md"
        if possible.exists():
            # 已入库，跳过
            mark(url, S_DONE)
            skipped += 1
            continue

        try:
            rel_path = write_docs(article)
            mark(url, S_DONE)
            print(f"  [★ {score}] → {rel_path}")
            imported += 1
            years_imported.add(year)
        except Exception as e:
            print(f"  [ERROR] 写入失败: {e}")
            errors += 1

    print(f"\n[import] 完成: 导入={imported}, 跳过={skipped}, 错误={errors}")

    # 更新 README 和年度汇总
    if imported > 0:
        import subprocess
        for y in sorted(years_imported):
            r = subprocess.run(
                ["python3", "scripts/update_year_summary.py", y],
                cwd=str(BASE)
            )
            if r.returncode != 0:
                print(f"  [WARNING] 年度汇总 {y} 更新失败")
        rr = subprocess.run(
            ["python3", "scripts/update_readme.py"],
            cwd=str(BASE)
        )
        if rr.returncode != 0:
            print(f"  [WARNING] README 更新失败")
        else:
            print(f"[import] README + 年度汇总已更新")


if __name__ == "__main__":
    run()
