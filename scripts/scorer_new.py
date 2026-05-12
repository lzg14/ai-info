#!/usr/bin/env python3
"""
评分器：scorer_new.py（文件永存架构）
- 从 DB 读 pending URLs
- 从固定路径读文件内容
- 调用 LLM 评分
- 更新 DB（status=scored, score=N）
- 文件永不移动/删除
"""
import sys, os, json, time, hashlib, re
from pathlib import Path

BASE = Path("/mnt/d/ProjectFile/ai-info")
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "scripts"))

from state_manager import (
    get_pending_urls,
    mark,
    get_score,
    init as sm_init,
    S_PENDING,
    S_SCORED,
    DB_PATH,
)
from config_loader import Config
import sqlite3

sm_init()
config = Config.load_from_file()

# 加载 .env
from dotenv import load_dotenv
load_dotenv(BASE / ".env")

import requests

API_KEY = os.getenv("MINIMAX_API_KEY") or os.getenv("MINIMAX_CN_API_KEY") or ""
BASE_URL = os.getenv("MINIMAX_API_BASE") or "https://api.minimaxi.com/v1"
MODEL = os.getenv("MINIMAX_MODEL") or "MiniMax-M2.7"

print(f"[scorer] API: {MODEL} | key: {API_KEY[:8]}... | base: {BASE_URL}")

# LLM 评分 prompt
SCORE_PROMPT = """阅读以下文章，返回JSON格式的评分：{{"score": 数字}}，score为1-10的整数。只返回JSON，不要任何其他内容。

文章内容：
{content}"""

# 固定路径前缀
ARTICLES_PREFIX = str(BASE / "temp" / "articles")


def url_hash(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:12]


def load_article(url: str) -> dict | None:
    """从固定路径加载文章文件"""
    h = url_hash(url)
    fp = os.path.join(ARTICLES_PREFIX, f"{h}.json")
    if not os.path.exists(fp):
        return None
    with open(fp, encoding='utf-8') as f:
        return json.load(f)


def score_article(article: dict) -> int | None:
    """调用 MiniMax LLM 评分"""
    content = article.get('content', '') or article.get('summary', '')
    if not content:
        return None

    # 截断到 4000 字
    content = content[:4000]

    prompt = SCORE_PROMPT.replace("{content}", content)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 600,
        "timeout": (60, 10),
    }

    try:
        resp = requests.post(
            f"{BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=(60, 10),
        )
        resp.raise_for_status()
        data = resp.json()

        # 解析 OpenAI-compatible 响应
        raw = data["choices"][0]["message"]["content"].strip()

        # 尝试 JSON 解析
        import json as json_mod
        raw_clean = re.sub(r'^.*?({.*}).*$', r'\1', raw, flags=re.DOTALL).strip()
        try:
            obj = json_mod.loads(raw_clean)
            score = int(obj.get("score", 0))
            if 1 <= score <= 10:
                return score
        except Exception:
            pass

        # fallback：取最后一个数字
        nums = re.findall(r'\b([1-9]|10)\b', raw_clean)
        if nums:
            return int(nums[-1])
    except Exception as e:
        print(f"  [ERROR] score fail: {e}")
    return None


def run():
    pending = get_pending_urls()
    print(f"[scorer] 待评分: {len(pending)} 篇")

    if not pending:
        print("[scorer] 没有待评分文章")
        return

    scored = 0
    important = 0
    failed = 0

    for i, url in enumerate(pending):
        # 进度心跳
        if i > 0 and i % 10 == 0:
            print(f"[{i}/{len(pending)}] 进度...")

        article = load_article(url)
        if not article:
            print(f"  [WARN] 文件不存在跳过: {url[:60]}")
            failed += 1
            continue

        score = score_article(article)
        if score is None:
            print(f"  [WARN] 评分失败: {article.get('title', url[:40])}")
            failed += 1
            continue

        # 更新 DB
        mark(url, S_SCORED, score=score)

        if score >= 8:
            important += 1
            tag = "★"
        else:
            tag = " "
        print(f"  [{tag} {score}/10] {article.get('title', url[:50])}")

        scored += 1
        time.sleep(0.3)  # 避免 API 过载

    print(f"\n[scorer] 完成: scored={scored}, important={important}, failed={failed}")


if __name__ == "__main__":
    run()
