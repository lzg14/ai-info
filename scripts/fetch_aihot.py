#!/usr/bin/env python3
"""
fetch_aihot.py — AIHOT API 数据源
- 调用 AIHOT 公开 API 获取精选 AI 动态
- /api/public/daily：精编日报，已编辑筛选，直接标记 score=8（跳过评分）
- /api/public/items：原始条目池，作为补充，评分流程同 crawler_new.py
- 写入 temp/articles/{hash}.json
- 每日两次运行
"""
import sys, os, json, hashlib
from datetime import datetime
from pathlib import Path

BASE = Path("/mnt/d/ProjectFile/ai-info")
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "scripts"))

from state_manager import mark, has, ARTICLES_DIR, S_SCORED

sm_init = __import__("state_manager").init
sm_init()
os.makedirs(ARTICLES_DIR, exist_ok=True)

BASE_URL = "https://aihot.virxact.com"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def url_hash(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:12]


def article_path(url: str) -> str:
    return os.path.join(ARTICLES_DIR, f"{url_hash(url)}.json")


def parse_daily_item(item: dict, category: str) -> dict:
    """把 daily section item 映射成 article JSON 格式"""
    url = item.get("sourceUrl", "")
    title = item.get("title", "")
    summary = item.get("summary", "")
    source_name = item.get("sourceName", "")

    tag_map = {
        "模型发布/更新": "AI模型",
        "产品发布/更新": "AI产品",
        "行业动态": "行业",
        "论文研究": "论文",
        "技巧与观点": "技巧",
    }
    tags = json.dumps([tag_map.get(category, category)], ensure_ascii=False)

    return {
        "hash": url_hash(url) if url else url_hash(title),
        "title": title,
        "title_zh": "",
        "url": url,
        "source_name": source_name,
        "source_url": "",
        "publish_date": "",
        "crawl_date": datetime.utcnow().isoformat(),
        "summary": summary,
        "content": summary or title,
        "content_zh": "",
        "tags": tags,
    }


def parse_items_item(item: dict) -> dict:
    """把 items 端点返回的 item 映射成 article JSON 格式"""
    url = item.get("url", "")
    published = item.get("publishedAt", "")

    category = item.get("category", "")
    tag_map = {
        "ai-models": "AI模型",
        "ai-products": "AI产品",
        "industry": "行业",
        "paper": "论文",
        "tip": "技巧",
    }
    tags = json.dumps([tag_map.get(category, category)], ensure_ascii=False)

    if published:
        publish_date = published[:10]
    else:
        publish_date = ""

    content = item.get("summary", "") or item.get("title", "")

    return {
        "hash": url_hash(url) if url else url_hash(item.get("title", "")),
        "title": item.get("title", ""),
        "title_zh": "",
        "url": url,
        "source_name": item.get("source", ""),
        "source_url": "",
        "publish_date": publish_date,
        "crawl_date": datetime.utcnow().isoformat(),
        "summary": item.get("summary", ""),
        "content": content,
        "content_zh": "",
        "tags": tags,
    }


def fetch_daily() -> list[dict]:
    """获取今日精编日报（已编辑筛选，跳过评分）"""
    import requests
    resp = requests.get(
        f"{BASE_URL}/api/public/daily",
        headers={"User-Agent": UA},
        timeout=(10, 20),
    )
    resp.raise_for_status()
    return resp.json()


def fetch_items(since_days: int = 1) -> list[dict]:
    """获取最近 N 天的精选条目"""
    since = (
        datetime.utcnow().replace(hour=0, minute=0, second=0)
        - __import__("datetime").timedelta(days=since_days)
    ).strftime("%Y-%m-%d")
    import requests
    resp = requests.get(
        f"{BASE_URL}/api/public/items",
        headers={"User-Agent": UA},
        params={"mode": "selected", "since": since, "take": 100},
        timeout=(10, 20),
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get("items", [])

def save_and_mark_daily(article: dict, score: int = 8):
    """写入文件 + 直接标记为 scored（跳过评分流程）
    若 URL 已存在但分数低于当前分，也更新分数（AIHOT daily 优先级更高）
    """
    url = article.get("url", "")
    title = article.get("title", "")
    key = url or title
    fp = os.path.join(ARTICLES_DIR, f"{article['hash']}.json")

    with open(fp, "w", encoding="utf-8") as f:
        json.dump(article, f, ensure_ascii=False, indent=2)

    # 强制用当前 score 覆盖（ON CONFLICT 不覆盖 score，所以用 raw SQL）
    import sqlite3
    from state_manager import DB_PATH
    conn = sqlite3.connect(DB_PATH)
    now = datetime.now().isoformat()
    conn.execute("""
        INSERT INTO seen_urls (url, status, file, score, updated_at)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(url) DO UPDATE SET
            status    = excluded.status,
            file      = excluded.file,
            score     = MAX(COALESCE(score, 0), excluded.score),
            updated_at = excluded.updated_at
    """, (key, S_SCORED, fp, score, now))
    conn.commit()
    conn.close()


def main():
    new_daily = 0
    new_items = 0
    skip_count = 0

    # ---- 1. 日报：精编内容，直接给 8 分 ----
    print("[aihot] 抓取日报（直接高分入库）...")
    try:
        daily_data = fetch_daily()
    except Exception as e:
        print(f"[aihot] 日报请求失败: {e}")
        daily_data = {}

    sections = daily_data.get("sections", [])
    section_map = {s["label"]: s["items"] for s in sections}

    # 展平所有 section items
    all_daily_items = []
    for label, items in section_map.items():
        for item in items:
            all_daily_items.append((item, label))

    print(f"[aihot] 日报共 {len(all_daily_items)} 条，分类: {list(section_map.keys())}")

    for item, category in all_daily_items:
        url = item.get("sourceUrl", "")
        title = item.get("title", "")
        key = url or title  # sourceUrl 为空时用 title 做 key

        # AIHOT daily 精编内容：已有人工编辑筛选，全部入库
        # 已存在时（score=5 from items）也用 MAX(score, 8) 升级分数
        article = parse_daily_item(item, category)
        try:
            save_and_mark_daily(article, score=8)
            print(f"  [★8] [{category[:4]}] {title[:50]}")
            new_daily += 1
        except Exception as e:
            print(f"  [ERR] {title[:40]}: {e}")

    # ---- 2. 原始条目：走普通流程（pending + 后续评分） ----
    print("\n[aihot] 抓取原始条目（待评分）...")
    try:
        items = fetch_items(since_days=1)
    except Exception as e:
        print(f"[aihot] 条目请求失败: {e}")
        items = []

    for item in items:
        url = item.get("url", "")
        if not url:
            continue
        if has(url):
            skip_count += 1
            continue

        article = parse_items_item(item)
        fp = os.path.join(ARTICLES_DIR, f"{article['hash']}.json")

        try:
            with open(fp, "w", encoding="utf-8") as f:
                json.dump(article, f, ensure_ascii=False, indent=2)
            mark(url, "pending", file=fp)
            print(f"  [NEW] {article['title'][:50]}")
            new_items += 1
        except Exception as e:
            print(f"  [ERR] {item.get('title', url)[:40]}: {e}")

    print(f"\n[aihot] 完成: 日报★8={new_daily}, 新条目(待评分)={new_items}, 跳过={skip_count}")


if __name__ == "__main__":
    main()
