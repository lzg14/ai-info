#!/usr/bin/env python3
"""
fix_links.py — 修复 MD 文章中的死链接

功能：
1. 修复内部 .html → .md 链接
2. 修复文章间相互引用时指向不存在文件的链接
3. 清理空或失效的相关文章区块

用法:
    python fix_links.py [--dry-run]
"""
import re
import argparse
from pathlib import Path

DOCS = Path("/mnt/d/ProjectFile/ai-info/docs")
FRONTMATTER_RE = re.compile(r'^<!--\s*\n?(.*?)\n?\s*-->\s*\n', re.DOTALL)


def iter_articles():
    """遍历所有文章 MD 文件"""
    return sorted(DOCS.rglob("*.md"))


def get_existing_files() -> set:
    """返回所有相对于 docs/ 的文件路径（如 2024/03/xxx.md）"""
    files = set()
    for p in iter_articles():
        rel = p.relative_to(DOCS)
        files.add(str(rel).replace('\\', '/'))
        # 也存不带 .md 的版本（用于链接匹配）
        files.add(str(rel.with_suffix('')).replace('\\', '/'))
    return files


def fix_html_links(content: str) -> tuple[str, int]:
    """将 .html 内部链接替换为 .md"""
    # 匹配 [...]() 形式中含 .html 的 URL
    def replacer(m):
        url = m.group(1)
        if '.html' in url and not url.startswith('http'):
            url = url.replace('.html', '.md')
        return m.group(0).replace(m.group(1), url)

    fixed = re.sub(r'\[([^\]]+)\]\(([^)]+\.html)\)', replacer, content)
    count = len(re.findall(r'\.html', content)) - len(re.findall(r'\.html', fixed))
    return fixed, count


def fix_related_links(content: str, existing: set) -> tuple[str, int]:
    """清理相关文章中指向不存在文件的链接"""
    lines = content.split('\n')
    in_related = False
    fixed_lines = []
    removed = 0

    for line in lines:
        if '## 相关文章' in line or '## 相关阅读' in line:
            in_related = True
            fixed_lines.append(line)
        elif in_related and line.strip().startswith('- ['):
            # 提取链接路径
            m = re.search(r'\]\(([^)]+)\)', line)
            if m:
                link = m.group(1)
                if link.startswith('http'):
                    fixed_lines.append(line)
                elif link.endswith('.md'):
                    if link in existing or link.lstrip('../') in existing:
                        fixed_lines.append(line)
                    else:
                        removed += 1
                        # 整行移除
                        continue
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)
        elif in_related and (line.strip() == '' or not line.strip().startswith('-')):
            in_related = False
            fixed_lines.append(line)
        else:
            fixed_lines.append(line)

    return '\n'.join(fixed_lines), removed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    existing = get_existing_files()
    total_html = 0
    total_related = 0
    files_changed = 0

    for path in iter_articles():
        content = path.read_text(encoding='utf-8')
        original = content

        content, n_html = fix_html_links(content)
        content, n_rel = fix_related_links(content, existing)
        total_html += n_html
        total_related += n_rel

        if content != original:
            files_changed += 1
            if not args.dry_run:
                path.write_text(content, encoding='utf-8')

    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"{mode}修复完成:")
    print(f"  .html → .md: {total_html} 处")
    print(f"  清理相关文章死链: {total_related} 条")
    print(f"  涉及文件: {files_changed} 个")
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
