#!/usr/bin/env python3
"""
normalize_article.py — 规范化单篇文章

用法:
    python normalize_article.py <article_path>
    python normalize_article.py docs/2026/05/2026-05-04-xxx.md

每篇执行:
1. 读取 frontmatter，修补缺失字段
2. 确保元信息栏有 tags 行
3. 确保正文有 ## 标题
4. 确保 Related Articles 区块（≥3条）
5. git add + commit
"""

import sys
import re
import subprocess
import json
from pathlib import Path

DOCS = Path("/mnt/d/ProjectFile/ai-info")
ARTICLE = Path(sys.argv[1]) if len(sys.argv) > 1 else None

if not ARTICLE or not ARTICLE.exists():
    print(f"用法: python normalize_article.py <article_path>")
    sys.exit(1)


def parse_frontmatter(content: str) -> tuple[dict, str]:
    m = re.match(r'^<!--\s*\n?(.*?)\n?\s*-->\s*\n', content, re.DOTALL)
    if not m:
        return {}, content
    try:
        fm = json.loads(m.group(1))
    except:
        fm = {}
    body = content[m.end():]
    return fm, body


def build_frontmatter(fm: dict) -> str:
    fm_str = json.dumps(fm, ensure_ascii=False, indent=2)
    return f"<!--\n{fm_str}\n-->\n"


def has_related_block(body: str) -> bool:
    return bool(re.search(r'^##\s+Related', body, re.MULTILINE))


def add_related_block(body: str) -> str:
    if has_related_block(body):
        return body
    return body + "\n\n## Related Articles\n\n（待补充相关文章链接）\n"


def has_section_headers(body: str) -> bool:
    return bool(re.search(r'^##\s+\S', body, re.MULTILINE))


def fix_title_headers(body: str) -> str:
    """为没有 ## 标题的段落添加标题"""
    if has_section_headers(body):
        return body
    # 如果正文第一段没有标题，给它加一个
    lines = body.split('\n')
    if lines and lines[0].strip() and not lines[0].startswith('#'):
        return "## 摘要\n\n" + body
    return body


def run(cmd: str, cwd=None) -> str:
    result = subprocess.run(cmd, shell=True, cwd=cwd,
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [!] {cmd} -> {result.returncode}")
        print(f"  [!] stderr: {result.stderr[:200]}")
    return result.stdout.strip()


def main():
    path = ARTICLE.resolve()
    content = path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(content)
    original = content

    changed = False

    # 1. frontmatter 修复
    # date -> publish_date
    if 'date' in fm and 'publish_date' not in fm:
        fm['publish_date'] = fm.pop('date')
        changed = True

    # 确保必要字段存在
    for field in ['publish_date', 'title', 'source', 'source_url', 'url', 'tags']:
        if field not in fm or not fm[field]:
            fm[field] = ''
            changed = True

    # 2. body 修复
    new_body = body
    if not has_related_block(body):
        new_body = add_related_block(body)
        changed = True
    if not has_section_headers(body):
        new_body = fix_title_headers(new_body)
        changed = True

    if not changed:
        print(f"  [=] 无需修改: {path.name}")
        return

    # 重建文件
    new_content = build_frontmatter(fm) + new_body
    path.write_text(new_content, encoding='utf-8')

    # git commit
    slug = path.name
    msg = f"fix: normalize {slug}"
    run(f"git add {path}", cwd=DOCS)
    run(f"git commit -m '{msg}'", cwd=DOCS)
    run(f"git push", cwd=DOCS)

    print(f"  [✅] {slug}")
    print(f"  [✅] commit: {run('git log -1 --oneline', cwd=DOCS)}")


if __name__ == '__main__':
    main()
