#!/usr/bin/env python3
"""
导入器：import_one.py（文件永存架构）
- 从 DB 读 scored（score >= 8）且未 done 的 URL
- 从固定路径读文件内容
- 对英文文章用 MiniMax 生成中文摘要（description_cn）
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

# ===== MiniMax API 配置（复用 ai_scorer.py 的加载逻辑）
API_KEY = os.getenv("MINIMAX_API_KEY") or os.getenv("MINIMAX_CN_API_KEY") or ""
if not API_KEY:
    from dotenv import load_dotenv
    load_dotenv(BASE / ".env")
    API_KEY = os.getenv("MINIMAX_API_KEY") or os.getenv("MINIMAX_CN_API_KEY") or ""
BASE_URL = os.getenv("LLM_API_BASE", "https://api.minimaxi.com/v1")
MODEL = os.getenv("LLM_MODEL", "MiniMax-M2.7")


def is_english(text: str) -> bool:
    """判断文本是否主要为英文（字母字符占比 > 60%）"""
    if not text:
        return False
    letters = sum(c.isalpha() for c in text)
    if letters == 0:
        return False
    latin = sum(c.isascii() and c.isalpha() for c in text)
    return latin / letters > 0.6


def call_minimax(prompt: str, system: str = "", max_tokens: int = 300) -> str:
    """调用 MiniMax API，返回文本响应。失败返回空字符串。"""
    if not API_KEY:
        return ""
    try:
        import requests
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system} if system else {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": 0.3,
        }
        resp = requests.post(
            f"{BASE_URL}/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json=payload,
            timeout=(10, 30),
        )
        if resp.status_code != 200:
            return ""
        data = resp.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except Exception:
        return ""


def generate_description_cn(article: dict) -> str:
    """
    对英文文章生成中文摘要，写入 article['description_cn']。
    已存在则跳过。
    返回 description_cn 值。
    """
    if article.get("description_cn"):
        return article["description_cn"]

    title = article.get("title", "")
    content = article.get("content", "") or article.get("summary", "")
    url = article.get("url", "")

    # 判断是否英文
    if not is_english(title + " " + content[:500]):
        article["description_cn"] = ""
        return ""

    # 取正文前 1500 字符作为上下文
    body = content[:1500].strip()

    prompt = f"""请为以下文章写一段简洁的中文摘要（100-150字），涵盖文章的核心主题和关键信息。用第一人称或客观陈述均可。

标题: {title}
正文摘录:
{body}

中文摘要:"""

    system = "你是一个专业的内容摘要助手。请用简洁的中文（100-150字）概括文章的核心内容。"

    desc = call_minimax(prompt, system, max_tokens=250).strip()
    if not desc:
        # fallback：用标题的简单翻译
        fallback_prompt = f"把以下英文标题翻译成中文（不超过20字）：{title}"
        desc = call_minimax(fallback_prompt, max_tokens=30).strip()

    article["description_cn"] = desc
    return desc


def load_article(url: str) -> dict | None:
    """从固定路径加载文章文件"""
    h = hashlib.md5(url.encode()).hexdigest()[:12]
    fp = os.path.join(ARTICLES_PREFIX, f"{h}.json")
    if not os.path.exists(fp):
        return None
    with open(fp, encoding="utf-8") as f:
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

    格式：HTML comment frontmatter
    <!-- {"title": "...", "source": "...", "source_url": "...", "publish_date": "YYYY-MM-DD", "score": 9, "tags": [...], "description_cn": "..."} -->
    # 标题
    📅 YYYY-MM-DD
    📢 来源：[名称](URL)
    📝 中文摘要（仅英文文章有）

    🏷️ tag1 · tag2

    <!-- 正文开始 -->
    正文内容（保留英文）
    <!-- 正文结束 -->
    """
    url = article.get('url', '')
    title = article.get('title', 'untitled')
    source_name = article.get('source_name', '') or article.get('source', '')
    source_url = article.get('source_url', '')
    publish_date = article.get('publish_date', '')
    content = article.get('content', '') or article.get('summary', '')
    summary = article.get('summary', '')
    tags = article.get('tags', [])
    score = article.get('score')

    # 生成中文摘要（仅英文文章）
    desc_cn = generate_description_cn(article)

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

    # 生成 frontmatter
    fm = {
        "title": title,
        "url": url,
        "source": source_name,
        "source_url": source_url,
        "publish_date": date_str,
        "score": score,
        "tags": tags,
    }
    if desc_cn:
        fm["description_cn"] = desc_cn
    fm_json = json.dumps(fm, ensure_ascii=False)

    # 组装正文
    lines = [f"<!-- {fm_json} -->", f"# {title}", ""]

    if publish_date:
        lines.append(f"📅 {date_str}")

    if source_name and source_url:
        lines.append(f"📢 来源：[{source_name}]({source_url})")
    elif source_name:
        lines.append(f"📢 来源：{source_name}")

    if desc_cn:
        lines.extend(["", f"📝 {desc_cn}"])

    if summary:
        body_stripped = content.strip()
        body_start = body_stripped[:200].lower()
        body_start = ' '.join(body_start.split())
        s = summary.strip().lower()
        s_clean = ' '.join(s.split())
        if len(s_clean) < 20 or s_clean not in body_start[:500]:
            lines.extend(["", f"> {summary}"])

    if tags:
        tags_str = " · ".join(str(t) for t in tags)
        lines.extend(["", f"🏷️ {tags_str}"])

    lines.extend(["", "<!-- 正文开始 -->", "", content, "", "<!-- 正文结束 -->"])

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return str(filepath.relative_to(BASE))


def get_ext_number() -> int:
    """获取下一个 Ext 编号（从现有文件扫描）"""
    import glob
    course_dir = Path("/mnt/d/ProjectFile/ai-learning/course")
    files = list(course_dir.glob("Ext*_*.md"))
    max_num = 0
    for f in files:
        m = re.search(r'Ext(\d+)', f.name)
        if m:
            max_num = max(max_num, int(m.group(1)))
    return max_num + 1


def write_ai_learning_ext(article: dict, score: int) -> str | None:
    """
    将高分 arxiv 论文写入 ai-learning course/ExtN_xxx.md
    仅当 source_name 含 'arXiv' 且 score >= 9 时调用。
    返回写入的文件路径，失败返回 None。
    """
    title = article.get('title', '')
    url = article.get('url', '')
    source_name = article.get('source_name', '')
    content = article.get('content', '') or article.get('summary', '')
    if not title or not url or 'arxiv' not in source_name.lower():
        return None

    # 生成中文摘要
    desc_cn = generate_description_cn(article) if is_english(title) else ""
    if not desc_cn:
        desc_cn = call_minimax(
            f"为以下论文写一段100字左右的中文摘要，涵盖核心贡献：\n标题：{title}\n内容：{content[:1000]}",
            system="你是一个专业的内容摘要助手，用100字左右概括论文核心贡献。",
            max_tokens=200
        ).strip()

    # 生成 slug
    slug = slugify(title)
    ext_num = get_ext_number()
    filename = f"Ext{ext_num}_{slug}.md"
    dest_path = Path("/mnt/d/ProjectFile/ai-learning/course") / filename

    # 生成正文（参考 Ext17 格式）
    publish_date = article.get('publish_date', '')[:10] if article.get('publish_date') else ''

    lines = [
        f"> ⚠️ **数据更新时间：{publish_date or '2026年'}**",
        "",
        f"> 📢 **来源**：arXiv · [{source_name}]({url})",
        "",
        f"# Ext{ext_num}：{title}",
        "",
        "---",
        "",
        "## 摘要",
        "",
        f"{desc_cn or '（暂无中文摘要）'}",
        "",
        "---",
        "",
        "## 关键信息",
        "",
        f"- **论文链接**：[{url}]({url})",
    ]

    if publish_date:
        lines.append(f"- **发布日期**：{publish_date}")
    lines.extend([
        f"- **评分**：{score}/10（MiniMax AI 评分）",
        "",
        "---",
        "",
        "## 原文摘要",
        "",
        "> " + (content[:1500].strip().replace('\n', '\n> ') if content else '（暂无原文）'),
        "",
        "---",
        "",
        "## 关联课程",
        "",
        "（待补充关联章节）",
    ])

    try:
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text('\n'.join(lines), encoding='utf-8')
        print(f"  [★ Ext{ext_num}] → ai-learning/{dest_path.name}")
        return str(dest_path)
    except Exception as e:
        print(f"  [ERROR] 写 ai-learning 失败: {e}")
        return None


def update_ext_reading_md(new_ext_path: Path):
    """更新 EXT_READING.md 目录和 ai-learning/README.md 链接"""
    ext_reading_path = Path("/mnt/d/ProjectFile/ai-learning/course/EXT_READING.md")
    readme_path = Path("/mnt/d/ProjectFile/ai-learning/README.md")

    # 从文件名提取编号和标题
    m = re.search(r'Ext(\d+)_(.+)\.md', new_ext_path.name)
    if not m:
        return
    ext_num = m.group(1)
    slug = m.group(2)
    title = slug.replace('-', ' ')

    # 读取 EXT_READING.md，找最后一个条目位置插入
    if ext_reading_path.exists():
        lines = ext_reading_path.read_text(encoding='utf-8').splitlines()
        # 在最后一个条目后插入（表格最后一行之后）
        new_entry = f"| Ext{ext_num} | [{title}](../course/{new_ext_path.name}) | 论文 |\n"
        # 简单方案：在 "## 主题分类" 之前插入
        insert_idx = None
        for i, l in enumerate(lines):
            if l.strip() == '## 主题分类':
                insert_idx = i
                break
        if insert_idx:
            # 找到合适位置——在第一个主题分类之前
            lines.insert(insert_idx, new_entry)
            ext_reading_path.write_text('\n'.join(lines), encoding='utf-8')


def run():
    """导入所有 scored 高分文章"""
    conn = sqlite3.connect(DB_PATH)
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

        # 检查是否已入库
        title = article.get('title', '')
        slug = slugify(title)
        date_str = (article.get('publish_date', '') or datetime.now().isoformat())[:10]
        year, month = date_str[:4], date_str[5:7]

        possible = BASE / "docs" / year / month / f"{date_str}_{slug}.md"
        if possible.exists():
            mark(url, S_DONE)
            skipped += 1
            continue

        try:
            rel_path = write_docs(article)
            mark(url, S_DONE)
            print(f"  [★ {score}] → {rel_path}")
            imported += 1
            years_imported.add(year)

            # 高分 arxiv 论文 → 写 ai-learning Ext
            source = article.get('source_name', '') or ''
            if 'arxiv' in source.lower() and score >= 9:
                ext_path = write_ai_learning_ext(article, score)
                if ext_path:
                    update_ext_reading_md(Path(ext_path))

        except Exception as e:
            print(f"  [ERROR] 写入失败: {e}")
            errors += 1

    print(f"\n[import] 完成: 导入={imported}, 跳过={skipped}, 错误={errors}")

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
