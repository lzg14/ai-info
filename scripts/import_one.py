#!/usr/bin/env python3
"""
将单篇文章从 temp/important/ 导入到 docs/YYYY/MM/

V5 MD 格式：
  <!-- {"title": "...", "date": "..."} -->
  # 标题
  📅 YYYY-MM-DD
  <!-- 正文开始 -->
  正文...
  <!-- 正文结束 -->
  ## 相关文章
  <!-- 相关文章开始 -->...

用法:
    python import_one.py temp/important/abc123.json
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
DOCS = BASE / "docs"
INDEX_FILE = BASE / "temp" / "data" / "docs_url_index.json"


def slugify(title: str) -> str:
    """从标题生成英文slug（用于文件名）"""
    words = re.findall(r'[A-Za-z]+|[^\s\u4e00-\u9fff]', title)
    words = [w for w in words if len(w) > 2 and w.lower() not in
             ('the', 'and', 'for', 'with', 'from', 'that', 'this', 'they')]
    english_words = [w.lower() for w in words if w.isascii() and w.isalpha()]
    chinese_words = [w for w in words if not w.isascii()]

    if english_words:
        key_words = english_words[:5]
    else:
        key_words = chinese_words[:5]

    if not key_words:
        short_words = [w.lower() for w in words if w.isascii() and w.isalpha()]
        key_words = short_words[:5] if short_words else ['article']

    slug = '-'.join(key_words)
    slug = ''.join(c for c in slug if c.isascii() and (c.isalnum() or c in '-_'))
    return slug[:60].strip('-_')


def build_filename(publish_date: str, title: str) -> str:
    date = publish_date if publish_date else datetime.now().strftime('%Y-%m-%d')
    slug = slugify(title)
    return f"{date}_{slug}.md"


def clean_title(raw_title: str, source_name: str) -> str:
    """去掉标题末尾混入的来源名后缀"""
    if not source_name:
        return raw_title
    cleaned = raw_title.strip()
    src = re.escape(source_name)
    src_extended = src + r'[\u4e00-\u9fff]*' if re.search(r'[\u4e00-\u9fff]', source_name) else src
    while True:
        old = cleaned
        cleaned = re.sub(rf'(?:[-—]+\s*{src_extended}\s*)+$', '', cleaned).strip()
        cleaned = re.sub(rf'\s*[–—]+\s*{src_extended}\s*$', '', cleaned).strip()
        cleaned = re.sub(rf'[｜|]\s*.*?{src_extended}\s*$', '', cleaned).strip()
        cleaned = re.sub(rf'[（(]\s*{src}\s*[）)]\s*$', '', cleaned).strip()
        if cleaned == old:
            break
    return cleaned


def extract_keywords(text: str, max_count: int = 5) -> list:
    TECH_KEYWORDS = [
        'GPT', 'LLM', 'Agent', 'Transformer', 'RLHF', 'LoRA', 'RAG', 'MCP',
        'AI', '大模型', '芯片', 'GPU', '开源', '融资', '算法', '安全', '产品',
        '发布', '合作', '收购', '监管', '突破', '训练', '推理', '部署',
        'Claude', 'OpenAI', 'DeepSeek', 'Google', 'Meta', 'Microsoft',
        'Anthropic', 'Qwen', 'GLM', 'LLaMA', 'Gemini', 'Copilot',
        'AutoGPT', 'Cursor', 'vLLM', 'HuggingFace',
        'Fine-tuning', '量化', '蒸馏', 'MoE', '多模态', '视觉', '语音',
        '代码', '编程', 'IDE', 'DevOps', 'Kubernetes',
        '机器人', '具身智能', '自动驾驶', '医疗', '金融', '教育',
        'AI regulation', 'China policy', 'AI agents', 'AGI',
        '语言模型', '多模态', '向量数据库', '参数', '上下文窗口',
    ]
    text_lower = text.lower()
    found = []
    for kw in TECH_KEYWORDS:
        if kw.lower() in text_lower:
            found.append(kw)
            if len(found) >= max_count:
                break
    return found


def find_related_articles(article: dict, doc: Path) -> list:
    """查找同月份最近的文章作为相关文章"""
    pub = article.get('publish_date', '') or article.get('crawl_date', '')
    if not pub:
        return []
    try:
        ym = pub[:7]
    except:
        return []
    related = []
    index = load_index()
    for url_key, info in sorted(index.items(), key=lambda x: x[1].get('import_time', ''), reverse=True):
        filepath = info.get('filepath', '')
        if not filepath:
            continue
        parts = filepath.split('/')
        if len(parts) >= 2:
            file_ym = f"{parts[0]}/{parts[1]}"
            if file_ym == f"{pub[:4]}/{pub[5:7]}":
                fpath_obj = DOCS / filepath
                if fpath_obj.exists() and str(fpath_obj) != str(doc):
                    first_line = fpath_obj.read_text(encoding='utf-8', errors='ignore').split('\n')[0]
                    r_title = first_line.lstrip('# ').strip() if first_line.startswith('#') else Path(filepath).stem
                    r_path = '/'.join(parts)
                    related.append((r_title, r_path))
                    if len(related) >= 5:
                        break
    return related


def load_index() -> dict:
    if INDEX_FILE.exists():
        return json.loads(INDEX_FILE.read_text(encoding='utf-8'))
    return {}


def save_index(index: dict):
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    INDEX_FILE.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding='utf-8')


def build_content(article: dict, out_path: Path) -> str:
    """
    构建 V5 MD 格式文章内容：

    <!--
    {"title": "...", "date": "..."}
    -->

    # 标题

    📅 YYYY-MM-DD

    <!-- 正文开始 -->
    正文...
    <!-- 正文结束 -->

    ## 相关文章
    <!-- 相关文章开始 -->
    - [...]
    """
    raw_title = article.get('title_zh') or article.get('title', '无标题')
    source_name = article.get('source_name', '')
    title = clean_title(raw_title, source_name)
    url = article.get('url', '')
    source_url = article.get('source_url') or url
    publish_date = article.get('publish_date', '')[:10] or ''
    score = article.get('ai_score', '')

    content = article.get('content_zh') or article.get('summary', '') or article.get('ai_summary', '') or ''

    # tags
    tags_from_ai = article.get('ai_tags', [])
    text_for_tags = f"{title} {content}"
    keyword_tags = extract_keywords(text_for_tags, 5)
    all_tags = []
    seen = set()
    for t in (tags_from_ai + keyword_tags):
        t = t.strip()
        if t and t.lower() not in seen:
            all_tags.append(t)
            seen.add(t.lower())
    all_tags = all_tags[:8]

    lines = []

    # 1. JSON frontmatter（HTML注释包裹）
    fm = {"title": title}
    if publish_date:
        fm["date"] = publish_date
    if source_name:
        fm["source"] = source_name
    if source_url and source_url != url:
        fm["source_url"] = source_url
    if score:
        fm["score"] = score
    lines.append("<!--")
    lines.append(json.dumps(fm, ensure_ascii=False, indent=2))
    lines.append("-->")
    lines.append("")

    # 2. H1 title
    lines.append(f"# {title}")
    lines.append("")

    # 3. Visual metadata bar
    meta_parts = [f"📅 {publish_date}"]
    if source_name:
        if source_url and source_url != url:
            meta_parts.append(f"[{source_name}]({source_url})")
        else:
            meta_parts.append(source_name)
    lines.append(" ".join(meta_parts))
    lines.append("")

    # 4. Tags block（HTML注释）
    if all_tags:
        tags_str = ', '.join(all_tags)
        lines.append(f"<!-- tags: {tags_str} -->")
        lines.append("")

    # 5. Content with markers
    if content:
        lines.append("<!-- 正文开始 -->")
        lines.append(content.strip())
        lines.append("<!-- 正文结束 -->")
        lines.append("")

    # 6. Related articles
    related = find_related_articles(article, out_path)
    if related:
        lines.append("## 相关文章")
        lines.append("<!-- 相关文章开始 -->")
        for r_title, r_path in related:
            # 计算相对路径
            src_parts = str(out_path.relative_to(DOCS)).split('/')
            dst_parts = r_path.split('/')
            # 找到共同祖先
            common = 0
            for i in range(min(len(src_parts) - 1, len(dst_parts))):
                if src_parts[i] == dst_parts[i]:
                    common += 1
                else:
                    break
            up = '../' * (len(src_parts) - 1 - common)
            rel = up + '/'.join(dst_parts[common:])
            lines.append(f"- [{r_title}]({rel})")

    return '\n'.join(lines)


def import_article(filepath: str):
    """将单篇 temp/important/json 导入到 docs"""
    art_path = Path(filepath)
    if not art_path.exists():
        print(f"[ERR] 文件不存在: {filepath}")
        return None

    article = json.loads(art_path.read_text(encoding='utf-8'))
    url = article.get('url', '')

    # 去重检查
    index = load_index()
    if url in index:
        print(f"[SKIP] 已存在: {url}")
        print(f"       文件: {index[url].get('filepath', '?')}")
        return index[url].get('filepath', '')

    publish_date = article.get('publish_date', '') or article.get('crawl_date', '')
    if not publish_date:
        print(f"[ERR] 无日期: {filepath}")
        return None

    # 取前10位 YYYY-MM-DD
    date_str = publish_date[:10]
    year, month = date_str.split('-')[:2]

    raw_title = article.get('title_zh') or article.get('title', '无标题')
    source_name = article.get('source_name', '')
    title = clean_title(raw_title, source_name)

    filename = build_filename(date_str, title)
    output_dir = DOCS / year / month
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename

    if output_path.exists():
        stem = output_path.stem
        counter = 2
        while output_path.exists():
            output_path = output_dir / f"{stem}_{counter}.md"
            counter += 1

    content = build_content(article, output_path)
    output_path.write_text(content, encoding='utf-8')
    print(f"[OK] {output_path.relative_to(BASE)}")

    # 更新索引
    index[url] = {
        'filepath': f"{year}/{month}/{output_path.name}",
        'title': title,
        'import_time': datetime.now().isoformat()
    }
    save_index(index)

    return f"{year}/{month}/{output_path.name}"


def rebuild_indexes(imported_years):
    """导入完成后重建年度汇总和 README"""
    scripts_dir = Path(__file__).parent
    for yr in sorted(set(imported_years)):
        result = subprocess.run(
            [sys.executable, str(scripts_dir / "update_year_summary.py"), yr],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(result.stdout.strip())
        else:
            print(f"[WARN] {yr} 年度汇总更新失败: {result.stderr.strip()}")

    result = subprocess.run(
        [sys.executable, str(scripts_dir / "update_readme.py")],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print(f"[WARN] README 更新失败: {result.stderr.strip()}")


if __name__ == '__main__':
    files = sys.argv[1:]
    if not files:
        print("用法: python import_one.py temp/important/*.json")
        sys.exit(1)

    imported_years = []
    for fp in files:
        rel = import_article(fp)
        if rel:
            yr = rel.split('/')[0]
            imported_years.append(yr)

    if imported_years:
        rebuild_indexes(imported_years)
