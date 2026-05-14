#!/usr/bin/env python3
"""
fetch_aihot.py — AIHOT API 数据源
- 调用 AIHOT 公开 API 获取精选 AI 动态
- 写入 temp/articles/{hash}.json（与 crawler_new.py 相同格式）
- 标记 pending 入 DB
- 每日两次运行，补足 AIHOT 侧的热点资讯
"""
import sys, os, json, hashlib, time
from datetime import datetime, timedelta
from pathlib import Path

BASE = Path("/mnt/d/ProjectFile/ai-info")
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "scripts"))

from state_manager import mark_pending, init as sm_init, has, ARTICLES_DIR

sm_init()
os.makedirs(ARTICLES_DIR, exist_ok=True)

BASE_URL = "https://aihot.virxact.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
}


def url_hash(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:12]


def article_path(url: str) -> str:
    return os.path.join(ARTICLES_DIR, f"{url_hash(url)}.json")


def parse_aihot_item(item: dict) -> dict:
    """把 AIHOT 返回的 item 映射成 article JSON 格式"""
    url = item.get("url", "")
    published = item.get("publishedAt", "")
    # 格式化日期：2026-05-14T15:08:23.000Z → 2026-05-14
    if published:
        publish_date = published[:10]
    else:
        publish_date = datetime.utcnow().strftime("%Y-%m-%d")

    # 分类转 tags
    category = item.get("category", "")
    tag_map = {
        "ai-models": "AI模型",
        "ai-products": "AI产品",
        "industry": "行业",
        "paper": "论文",
        "tip": "技巧",
    }
    tags = json.dumps([tag_map.get(category, category)], ensure_ascii=False)

    # AIHOT 的 summary 就是正文（热点资讯短内容）
    content = item.get("summary", "") or item.get("title", "")

    return {
        "hash": url_hash(url),
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


def fetch_aihot(since_days: int = 1, category: str = None) -> list[dict]:
    """
    获取最近 N 天的精选内容。
    - since_days: 往前取几天（默认1，cron 两次取1天）
    - category: None 表示全部分类
    """
    since = (datetime.utcnow() - timedelta(days=since_days)).strftime("%Y-%m-%d")
    params = {
        "mode": "selected",
        "since": since,
        "take": 100,
    }
    if category:
        params["category"] = category

    import requests
    resp = requests.get(
        f"{BASE_URL}/api/public/items",
        headers=HEADERS,
        params=params,
        timeout=(10, 20),
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get("items", [])


def main():
    print(f"[aihot] 开始抓取 AIHOT 精选动态")
    try:
        items = fetch_aihot(since_days=1)
    except Exception as e:
        print(f"[aihot] API 请求失败: {e}")
        sys.exit(1)

    new_count = 0
    skip_count = 0
    error_count = 0

    for item in items:
        url = item.get("url", "")
        if not url:
            continue

        # 跳过已有（DB 里存在且非 pending）
        if has(url):
            skip_count += 1
            continue

        try:
            article = parse_aihot_item(item)
            fp = article_path(url)

            with open(fp, "w", encoding="utf-8") as f:
                json.dump(article, f, ensure_ascii=False, indent=2)

            mark_pending(url, fp)
            print(f"  [NEW] {article['title'][:50]}")
            new_count += 1
        except Exception as e:
            print(f"  [ERR] {item.get('title', url)[:50]}: {e}")
            error_count += 1

    print(f"\n[aihot] 完成: 新增={new_count}, 跳过={skip_count}, 错误={error_count}")


if __name__ == "__main__":
    main()
