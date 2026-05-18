#!/usr/bin/env python3
"""
update_year_summary.py — 重建指定年份的年度汇总 docs/YYYY.md

每次导入新文章后调用，确保汇总与实际文章一致。
重建而非追加：扫描 docs/YYYY/MM/ 下所有文章，按月分组。

两个 HTML 注释标记的动态区块：
- <!-- FEATURED_BEGIN --> ... <!-- FEATURED_END -->  ← 年度精品（按评分倒序）
- <!-- FULL_LIST_BEGIN --> ... <!-- FULL_LIST_END -->    ← 全部文章（按时间倒序）

用法:
    python update_year_summary.py 2026
    python update_year_summary.py 2026 2025 2024
"""
import re
import sys
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

AIINFO_DIR = Path("/mnt/d/ProjectFile/ai-info")
DOCS_DIR   = AIINFO_DIR / "docs"

MONTH_NAMES = {
    "01": "1月", "02": "2月", "03": "3月", "04": "4月",
    "05": "5月", "06": "6月", "07": "7月", "08": "8月",
    "09": "9月", "10": "10月", "11": "11月", "12": "12月",
}

FEATURED_THRESHOLD = 7.0   # 评分 >= 7.0 视为精品


def iter_year_articles(year: str):
    """扫描 docs/YYYY/ 下的所有文章，返回 [(date_str, month, day, title, rel_path, score), ...]"""
    year_dir = DOCS_DIR / year
    if not year_dir.exists():
        return []

    articles = []
    for month_dir in sorted(year_dir.iterdir()):
        if not month_dir.is_dir():
            continue
        if not re.match(r'^\d{2}$', month_dir.name):
            continue
        for fp in sorted(month_dir.glob("*.md")):
            if '/terms/' in str(fp) or fp.name.startswith('term-'):
                continue
            if fp.stem == year:
                continue

            m = re.match(r'^(\d{4})-(\d{2})-(\d{2})', fp.stem)
            if not m:
                continue
            _, month, day = m.groups()
            date_str = f"{year}-{month}-{day}"

            # 读 frontmatter 提取评分
            score = None
            title = ''
            try:
                content = fp.read_text(encoding='utf-8', errors='ignore')
                fm_m = re.search(r'<!--\s*\n?(.*?)\n?\s*-->', content, re.DOTALL)
                if fm_m:
                    try:
                        fm = json.loads(fm_m.group(1))
                        score = fm.get('score') or fm.get('ai_score')
                    except Exception:
                        pass
                # 读标题
                for line in content.split('\n')[:15]:
                    line = line.strip()
                    if line.startswith('# '):
                        title = line[2:].strip()
                        break
            except Exception:
                pass

            if not title:
                title = fp.stem

            rel = f"../{year}/{month_dir.name}/{fp.name}"
            articles.append((date_str, month, day, title, rel, score))

    return articles


def build_featured_block(articles, threshold=FEATURED_THRESHOLD):
    """精品区块：评分 >= threshold 的文章，按评分倒序"""
    featured = [(s, d, m, t, p) for d, m, _, t, p, s in articles
                if s is not None and float(s) >= threshold]
    featured.sort(key=lambda x: float(x[0]), reverse=True)

    if not featured:
        return "（暂无精品文章）"

    lines = []
    for score, date_str, month, title, rel in featured:
        date_short = f"{month}-{date_str[8:]}"
        score_mark = f"[{float(score):.1f}]"
        lines.append(f"- {score_mark} [{title}]({rel})（{date_short}）")
    return '\n'.join(lines)


def build_full_list_block(articles):
    """完整列表区块：所有文章，按时间倒序，按月分组"""
    by_month = defaultdict(list)
    for date_str, month, day, title, rel, _ in articles:
        by_month[month].append((day, title, rel))

    lines = []
    for month in sorted(by_month.keys(), reverse=True):
        month_name = MONTH_NAMES.get(month, f"{int(month)}月")
        lines.append(f"## {month_name}")
        lines.append("")
        for day, title, rel in sorted(by_month[month], reverse=True):
            date_short = f"{month}-{day}"
            lines.append(f"- [{title}]({rel})（{date_short}）")
        lines.append("")

    return '\n'.join(lines).strip()


def build_year_summary(year: str) -> str:
    """构建单个年份的汇总 MD 内容"""
    articles = iter_year_articles(year)
    total = len(articles)
    featured_count = len([a for a in articles if a[-1] is not None and float(a[-1]) >= FEATURED_THRESHOLD])

    featured_block = build_featured_block(articles)
    full_list_block = build_full_list_block(articles)

    return f"""# {year} 年

共 {total} 篇文章（{featured_count} 篇精品）

## 年度精品
<!-- FEATURED_BEGIN -->
{featured_block}
<!-- FEATURED_END -->

## 全部文章
<!-- FULL_LIST_BEGIN -->
{full_list_block}
<!-- FULL_LIST_END -->

← [返回 README](../README.md)
"""


def update_year(year: str):
    """重建单个年份的汇总文件"""
    content = build_year_summary(year)
    out_path = DOCS_DIR / f"{year}.md"
    out_path.write_text(content, encoding='utf-8')
    articles = iter_year_articles(year)
    print(f"[OK] {year}.md — {len(articles)} 篇")


def main():
    years = sys.argv[1:] if len(sys.argv) > 1 else [datetime.now().strftime('%Y')]
    for year in years:
        if not re.match(r'^\d{4}$', year):
            print(f"[SKIP] 非有效年份: {year}")
            continue
        update_year(year)


if __name__ == '__main__':
    main()
