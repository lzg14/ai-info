#!/usr/bin/env python3
"""
update_readme.py — 自动更新 ai-info/README.md

用 HTML 注释标记区块边界，精确替换 LATEST 和 YEARLY 两个动态区块：
- <!-- LATEST_BEGIN --> ... <!-- LATEST_END -->  ← 最新文章列表
- <!-- YEARLY_BEGIN --> ... <!-- YEARLY_END -->   ← 年度导航

用法:
    python update_readme.py
"""
import re
from pathlib import Path

AIINFO_DIR  = Path("/mnt/d/ProjectFile/ai-info")
DOCS_DIR    = AIINFO_DIR / "docs"
README_PATH  = AIINFO_DIR / "README.md"


def iter_articles():
    """遍历所有文章 MD，返回 (date_str, title, rel_path)"""
    for p in sorted(DOCS_DIR.rglob("*.md"), key=lambda x: x.name):
        if '/terms/' in str(p) or p.name.startswith('term-'):
            continue
        if re.match(r'^\d{4}\.md$', p.name):
            continue
        fname = p.stem
        m = re.match(r'^(\d{4}-\d{2}-\d{2})', fname)
        if not m:
            continue
        date_str = m.group(1)
        try:
            first_lines = p.read_text(encoding='utf-8', errors='ignore').split('\n')[:10]
        except:
            continue
        title = ''
        for line in first_lines:
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                break
        if not title:
            continue
        rel = p.relative_to(AIINFO_DIR)
        yield date_str, title, str(rel)


def build_latest_block(n: int = 10) -> str:
    """生成最新 N 条的 Markdown 列表（不含注释标记）"""
    # 保留 (date_str, title, rel_path)，排序后再生成行
    articles_raw = []
    for date_str, title, rel_path in iter_articles():
        articles_raw.append((date_str, title, rel_path))

    # 按日期倒序
    articles_raw.sort(key=lambda x: x[0], reverse=True)

    lines = []
    for date_str, title, rel_path in articles_raw[:n]:
        link = f"[{title}]({rel_path})"
        date_part = f"（{date_str[5:7]}-{date_str[8:]}）"
        lines.append(f"- {link}{date_part}")
    return '\n'.join(lines)


def build_yearly_block() -> str:
    """生成年度导航表格（不含注释标记）"""
    rows = ["| 年份 | 文章数 |", "|------|--------|"]
    for y in range(2011, 2027):
        # 文章在 YYYY/MM/*.md，按年递归统计
        y_count = len(list((DOCS_DIR / str(y)).rglob("*.md")))
        if y_count > 0:
            rows.append(f"| [{y}](docs/{y}.md) | {y_count} |")
        else:
            rows.append(f"| {y} | — |")
    return '\n'.join(rows)


def replace_block(readme: str, begin_marker: str, end_marker: str, new_content: str) -> str:
    """
    在 readme 中找到 begin_marker 和 end_marker 之间的所有内容，
    替换为 new_content。找不到标记时抛出 ValueError。
    """
    b = readme.find(begin_marker)
    if b == -1:
        raise ValueError(f"找不到标记: {begin_marker!r}")
    e = readme.find(end_marker, b)
    if e == -1:
        raise ValueError(f"找不到标记: {end_marker!r}")
    # 替换 marker 之后、end_marker 之前的内容
    return readme[:b + len(begin_marker)] + '\n' + new_content + '\n' + readme[e:]


def main():
    new_latest = build_latest_block(10)
    new_yearly = build_yearly_block()

    readme = README_PATH.read_text(encoding='utf-8')

    readme = replace_block(readme,
                           "<!-- LATEST_BEGIN -->",
                           "<!-- LATEST_END -->",
                           new_latest)

    readme = replace_block(readme,
                           "<!-- YEARLY_BEGIN -->",
                           "<!-- YEARLY_END -->",
                           new_yearly)

    README_PATH.write_text(readme, encoding='utf-8')
    print("README.md 已更新")


if __name__ == '__main__':
    main()
