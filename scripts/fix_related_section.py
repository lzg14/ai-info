#!/usr/bin/env python3
"""
fix_related_section.py — 修复 2026 年文章末尾的裸相关链接

问题：部分 2026 年文章正文结束后有裸相关链接（- 标题YYYY-MM-DD 格式），
没有标准 ## 相关文章 区块。

处理方式：
1. 提取正文结束后、<!-- 正文结束 --> 之后的裸相关链接
2. 去掉正文中的参考链接（保留播客链接等外部参考）
3. 把裸相关链接整理成标准 ## 相关文章 区块
4. 在 <!-- 正文结束 --> 之后插入标准区块

注意：只处理有裸相关链接的文章，其他文章不动。
"""
import re
import os
from pathlib import Path

DOCS = Path("/mnt/d/ProjectFile/ai-info/docs")

# 相关链接识别：- 标题YYYY-MM-DD 或 - 标题（含中文标题、带日期后缀）
RELATED_TITLE_RE = re.compile(r'^-\s+.+\d{4}-\d{2}-\d{2}.*$', re.M)


def extract_related_links(content: str) -> list[str]:
    """从正文章节中提取裸相关链接"""
    links = []
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('- ') and '](' not in stripped:
            # 排除明显是正文引用的行（如 lecu 最后的观点引用）
            # 相关链接特征：标题中有日期 YYYY-MM-DD
            if re.search(r'\d{4}-\d{2}-\d{2}', stripped):
                links.append(stripped)
    return links


def remove_related_from_body(content: str) -> str:
    """从正文中移除裸相关链接行"""
    lines = []
    skip_mode = False
    for line in content.split('\n'):
        stripped = line.strip()
        # 遇到参考链接行时进入跳过模式
        if '参考链接：' in line:
            skip_mode = True
            lines.append(line)
        elif skip_mode:
            # 在参考链接区块，检查是否裸相关链接
            if stripped.startswith('- ') and re.search(r'\d{4}-\d{2}-\d{2}', stripped):
                continue  # 跳过这行
            elif stripped.startswith('[1]') or stripped.startswith('https://'):
                lines.append(line)  # 保留实际URL
            elif stripped and not stripped.startswith('-'):
                # 非链接行，退出跳过模式（参考链接区块结束）
                skip_mode = False
                lines.append(line)
            else:
                lines.append(line)
        else:
            lines.append(line)
    return '\n'.join(lines)


def build_related_block(links: list[str]) -> str:
    """构建 ## 相关文章 区块"""
    if not links:
        return ""
    block = ["", "## 相关文章", "<!-- 相关文章开始 -->"]
    for link in links:
        block.append(link)
    block.extend(["", "<!-- 相关文章结束 -->"])
    return '\n'.join(block)


def process_file(fp: Path) -> bool:
    """处理单个文件，返回是否修改"""
    c = fp.read_text(encoding='utf-8')
    original = c

    # 找正文结束标记
    ee_idx = c.find('<!-- 正文结束 -->')
    if ee_idx < 0:
        return False

    before_ee = c[:ee_idx]
    after_ee = c[ee_idx:]

    # 提取裸相关链接（只在参考链接区块中找）
    related_links = []
    in_ref_section = False
    for line in before_ee.split('\n'):
        if '参考链接：' in line:
            in_ref_section = True
            continue
        if in_ref_section:
            stripped = line.strip()
            if stripped.startswith('- ') and re.search(r'\d{4}-\d{2}-\d{2}', stripped):
                related_links.append(stripped)
            elif stripped and not stripped.startswith('-') and not stripped.startswith('[') and not stripped.startswith('http') and not stripped.startswith('-'):
                # 参考区块结束（非链接、非空行）
                in_ref_section = False

    if not related_links:
        return False

    # 去掉正文中的裸相关链接
    new_before_ee = before_ee
    for link in related_links:
        # 精确匹配整行
        new_before_ee = new_before_ee.replace('\n' + link, '\n')
        new_before_ee = new_before_ee.replace(link + '\n', '\n')

    # 构建相关文章区块
    related_block = build_related_block(related_links)

    # 重组：正文结束标记后的内容替换为相关文章区块
    # 注意：原来 <!-- 正文结束 --> 之后可能还有空行，要清理
    new_content = new_before_ee.rstrip() + '\n\n<!-- 正文结束 -->' + related_block

    if new_content != original:
        fp.write_text(new_content, encoding='utf-8')
        return True
    return False


def main():
    changed = 0
    for root, dirs, files in os.walk(DOCS / '2026'):
        dirs.sort()
        for f in sorted(files):
            if not f.endswith('.md'):
                continue
            fp = Path(root) / f
            try:
                if process_file(fp):
                    print(f'  ✓ {f}')
                    changed += 1
            except Exception as e:
                print(f'  ✗ {f}: {e}')

    print(f'\n修改完成: {changed} 篇')


if __name__ == '__main__':
    main()