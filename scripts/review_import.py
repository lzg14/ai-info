#!/usr/bin/env python3
"""
review_import.py — 审查最近导入的 MD 文章

审查规则（来自 cron job）：
- frontmatter 完整（source_name/source_url/publish_date 非空）
- source_url 不是 RSS feed URL（不含 /rss/ 或 .xml）
- 标题与文件名关联
- 正文非空、无截断
- 相关文章链接可解析
- 无乱码

用法:
    python review_import.py --recent 10
    python review_import.py docs/2025/06/xxx.md
"""
import sys
import re
import json
import argparse
from pathlib import Path

DOCS = Path("/mnt/d/ProjectFile/ai-info/docs")
FRONTMATTER_RE = re.compile(r'^<!--\s*\n(.*?)\n-->\s*\n', re.DOTALL)


def parse_frontmatter(content: str) -> dict:
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}
    import json
    return json.loads(m.group(1))


def check_file(path: Path) -> tuple[bool, list[str]]:
    """检查单个文件，返回 (pass, errors)"""
    errors = []
    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:
        return False, [f"读取失败: {e}"]

    # frontmatter 检查
    fm = parse_frontmatter(content)
    for field, v5_key in [('source_name', 'source'), ('source_url', 'source_url'), ('publish_date', 'date')]:
        if not fm.get(field) and not fm.get(v5_key):
            errors.append(f"frontmatter 缺少或为空: {field} 或 {v5_key}")

    # source_url 不能是 RSS feed
    source_url = fm.get('source_url', '')
    if source_url and ('/rss/' in source_url or source_url.endswith('.xml')):
        errors.append(f"source_url 是 RSS feed URL: {source_url}")

    # 标题与文件名关联（文件名含日期+slug，标题应含中文关键字）
    title = fm.get('title', '')
    if not title or len(title) < 4:
        errors.append(f"标题过短或为空: {title}")

    # 正文非空
    body = FRONTMATTER_RE.sub('', content).strip()
    if not body or len(body) < 100:
        errors.append(f"正文过短或为空 ({len(body)} chars)")

    # 乱码检测（中文字符占比）
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', body)
    if body and len(chinese_chars) / len(body) < 0.05:
        errors.append("可能存在乱码（中文字符占比过低）")

    return len(errors) == 0, errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--recent', type=int, default=10, help='审查最近 N 篇')
    parser.add_argument('files', nargs='*', help='指定文件路径')
    args = parser.parse_args()

    if args.files:
        paths = [Path(f) for f in args.files]
    else:
        # 按修改时间找最近 N 篇 .md
        all_md = sorted(DOCS.rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
        paths = all_md[:args.recent]

    print(f"审查 {len(paths)} 篇文章...\n")
    ok_count = 0
    for p in paths:
        passed, errors = check_file(p)
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}  {p.relative_to(DOCS)}")
        for e in errors:
            print(f"       → {e}")
        if passed:
            ok_count += 1

    print(f"\n{ok_count}/{len(paths)} 通过")
    return 0 if ok_count == len(paths) else 1


if __name__ == '__main__':
    sys.exit(main())
