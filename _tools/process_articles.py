#!/usr/bin/env python3
"""Process 12 articles from JSON to docs/YYYY/MM/*.md (V4 format) and update docs_url_index.json"""

import json
import os
import re
import unicodedata
from datetime import datetime

ARTICLES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "temp", "articles")
DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")
INDEX_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs", "data", "docs_url_index.json")

HASHES = [
    "18bd6d66839d",
    "55f1507da8bc",
    "d3ffdb709253",
    "6b6a618db297",
    "3956fdd2fafc",
    "348dff95d8e9",
    "d4944f267f47",
    "0073cb028a74",
    "d91b629c2076",
    "ac0e5e086bd5",
    "b022fe9845e1",
    "c256cc4fc6c5",
]


def slugify(title):
    s = title.strip()
    s = s.lower()
    s = s.replace(":", "")
    s = s.replace("，", ",")
    s = s.replace("？", "")
    s = s.replace("！", "")
    s = s.replace("「", "")
    s = s.replace("」", "")
    s = s.replace("《", "")
    s = s.replace("》", "")
    s = s.replace("：", "")
    s = s.replace("、", "")
    s = s.replace("。", "")
    s = s.replace("（", "")
    s = s.replace("）", "")
    s = s.replace("——", "")
    s = s.replace("——", "")
    s = s.replace("—", "")
    s = s.replace("…", "")
    s = s.replace(" ", "-")
    s = s.replace("/", "-")
    s = s.replace("\\", "-")
    s = s.replace("+", "plus")
    s = re.sub(r"-+", "-", s)
    s = re.sub(r"-$", "", s)
    s = re.sub(r"^\-", "", s)
    return s


def make_md_filename(title, publish_date):
    dt = datetime.strptime(publish_date, "%Y-%m-%d")
    slug = slugify(title)
    return f"{dt.strftime('%Y-%m-%d')}_{slug}.md"


results = {"success": [], "skipped": [], "errors": []}

index_entries = []

for h in HASHES:
    path = os.path.join(ARTICLES_DIR, f"{h}.json")
    if not os.path.exists(path):
        results["errors"].append(f"{h}.json: file not found")
        continue

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        results["errors"].append(f"{h}.json: json parse error - {e}")
        continue

    title = data.get("title", "").strip()
    url = data.get("url", "")
    source = data.get("source_name", "")
    source_url = data.get("source_url", "")
    publish_date = data.get("publish_date", "")
    summary = (data.get("summary") or "").strip()
    content = data.get("content", "")

    if not publish_date:
        results["errors"].append(f"{h}.json: missing publish_date")
        continue

    dt = datetime.strptime(publish_date, "%Y-%m-%d")
    year = dt.strftime("%Y")
    month = dt.strftime("%m")

    md_filename = make_md_filename(title, publish_date)
    md_dir = os.path.join(DOCS_DIR, year, month)
    md_path = os.path.join(md_dir, md_filename)

    os.makedirs(md_dir, exist_ok=True)

    if os.path.exists(md_path):
        results["skipped"].append(f"{md_filename} (already exists)")
        # Still add to index
        with open(md_path, "r", encoding="utf-8") as f_md:
            existing_content = f_md.read()
            if f'"{url}"' in existing_content:
                index_entries.append({
                    "url": url,
                    "local_path": f"{year}/{month}/{md_filename}",
                    "title": title,
                    "source": source,
                    "publish_date": publish_date,
                })
        continue

    # Build V4 markdown
    lines = []
    frontmatter = {
        "title": title,
        "url": url,
        "source": source,
        "source_url": source_url,
        "publish_date": publish_date,
        "score": None,
        "tags": [],
    }
    lines.append("<!-- " + json.dumps(frontmatter, ensure_ascii=False) + " -->")
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"📅 {publish_date}")
    lines.append(f"📢 来源：[{source}]({source_url})")
    lines.append("")
    if summary:
        lines.append(f"> {summary}")
        lines.append("")
    lines.append("<!-- 正文开始 -->")
    lines.append("")
    lines.append(content.strip())
    lines.append("")
    lines.append("<!-- 正文结束 -->")
    lines.append("")

    md_content = "\n".join(lines)

    with open(md_path, "w", encoding="utf-8") as f_md:
        f_md.write(md_content)

    results["success"].append(md_filename)
    index_entries.append({
        "url": url,
        "local_path": f"{year}/{month}/{md_filename}",
        "title": title,
        "source": source,
        "publish_date": publish_date,
    })

# Write index
index_dir = os.path.dirname(INDEX_PATH)
os.makedirs(index_dir, exist_ok=True)

existing_index = []
if os.path.exists(INDEX_PATH):
    try:
        with open(INDEX_PATH, "r", encoding="utf-8") as f_idx:
            existing_index = json.load(f_idx)
            if not isinstance(existing_index, list):
                existing_index = []
    except Exception:
        existing_index = []

existing_urls = {e.get("url") for e in existing_index if e.get("url")}
new_entries = []
for entry in index_entries:
    if entry["url"] not in existing_urls:
        new_entries.append(entry)
        existing_urls.add(entry["url"])

all_entries = existing_index + new_entries

with open(INDEX_PATH, "w", encoding="utf-8") as f_idx:
    json.dump(all_entries, f_idx, ensure_ascii=False, indent=2)

results["index_updated"] = True
results["previous_index_count"] = len(existing_index)
results["new_index_count"] = len(new_entries)
results["total_index_count"] = len(all_entries)

print(json.dumps(results, ensure_ascii=False, indent=2))
