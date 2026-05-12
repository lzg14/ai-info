#!/usr/bin/env python3
"""
AI 评分：scorer_new.py
- 从 DB 读取所有 pending URL（不再读 pending/ 目录）
- 对每篇抓全文 + AI 评分（1-10）
- score >= 7：mark(important) + 保留文件（给 import_one 读）
- score < 7：mark(scored) + 删除文件
- 已评分 URL 跳过（DB 里 score IS NOT NULL）
"""
import sys
import os
import json
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = Path("/mnt/d/ProjectFile/ai-info")
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "scripts"))

from config_loader import Config
from state_manager import (
    PENDING, IMPORTANT, SCORED,
    get_pending_urls, has_score, mark,
    S_PENDING, S_SCORED, S_IMPORTANT,
    init as sm_init
)
sm_init()


def load_article(filepath: Path) -> dict | None:
    """读取文件内容为 dict"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None


def score_article(article: dict, config: Config) -> tuple[dict, float, str, Path]:
    """
    评分一篇文章，返回 (article, score, status, dest_dir)
    status: S_IMPORTANT (>=7) or S_SCORED (<7)
    """
    threshold = config.crawl.get("ai_score_threshold", 7.0)
    url = article["url"]
    title = article.get("title") or ""
    content = article.get("content") or ""
    # 取前2000字
    text = (title + "\n\n" + content)[:2000]

    score_val, reasoning = call_llm_judge(text, config)

    # 评分写入 article（不写文件，只返回给调用方）
    article["ai_score"] = score_val
    article["ai_reasoning"] = reasoning

    is_important = score_val >= threshold
    status = S_IMPORTANT if is_important else S_SCORED
    dest_dir = IMPORTANT if is_important else SCORED

    return article, score_val, status, dest_dir


def call_llm_judge(text: str, config: Config) -> tuple[int, str]:
    """调 LLM 评分"""
    import anthropic
    api_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("CLAUDE_API_KEY")
    model = config.crawl.get("scorer_model", "claude-sonnet-4-7-20250514")
    max_tokens = config.crawl.get("scorer_max_tokens", 1024)

    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""你是一个严谨的AI领域文章评分专家。请根据以下文章的标题和内容，判断它对AI从业者的价值。

评分标准（1-10分）：
- 10分：革命性突破、里程碑级成果
- 8-9分：重要进展、知名公司重磅发布
- 7分：值得关注的新进展、有实质内容的技术文章
- 5-6分：一般资讯、可看可不看
- 3-4分：价值较低、商业软文
- 1-2分：几乎没有价值

请同时给出评分（整数）和简短理由（1-2句话）。

文章：

{text}

请用以下JSON格式返回（不要加任何markdown标记）：
{{"score": 分数, "reasoning": "简短理由"}}
"""

    try:
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}]
        )
        raw = response.content[0].text.strip()
        # 提取 JSON
        if "```json" in raw:
            raw = raw.split("```json")[1].split("```")[0].strip()
        elif "```" in raw:
            raw = raw.split("```")[1].split("```")[0].strip()
        data = json.loads(raw)
        score_val = int(data.get("score", 5))
        reasoning = str(data.get("reasoning", ""))
        score_val = max(1, min(10, score_val))
        return score_val, reasoning
    except Exception as e:
        print(f"    [ERROR] LLM评分失败: {e}")
        return 5, "评分接口异常"


def score_one(url: str, config: Config) -> tuple[str, dict, float, str, Path]:
    """
    评分单个 URL，返回 (url, article, score, status, dest_dir)
    从 DB 确认 pending，从 PENDING/ 读文件内容
    """
    filepath = PENDING / f"{url_to_hash(url)}.json"
    article = load_article(filepath)

    if article is None:
        # 文件不存在，跳过（crawler 可能还没写完）
        return url, None, None, None, None

    article, score_val, status, dest_dir = score_article(article, config)
    return url, article, score_val, status, dest_dir


def url_to_hash(url: str) -> str:
    """从 URL 还原 hash"""
    import hashlib
    return hashlib.md5(url.encode('utf-8')).hexdigest()[:12]


def main():
    # 从 DB 读 pending URL（不再读目录）
    pending_urls = get_pending_urls()
    if not pending_urls:
        print("无待评分文章（DB 中无 pending 记录）")
        return

    # 过滤掉已有评分的 URL
    pending_urls = [u for u in pending_urls if not has_score(u)]
    if not pending_urls:
        print("所有 pending 文章均已有评分")
        return

    print(f"待评分: {len(pending_urls)}篇")

    config = Config.load_from_file(str(BASE / "config" / "config.json"))
    threshold = config.crawl.get("ai_score_threshold", 7.0)
    max_per_day = config.crawl.get("ai_max_articles_per_day", 12)

    results = []
    completed = 0

    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(score_one, url, config): url for url in pending_urls}

        for future in as_completed(futures):
            url = futures[future]
            try:
                result = future.result()
                if result[1] is not None:  # article is not None
                    results.append(result)
            except Exception as e:
                print(f"  [ERROR] {url}: {e}")

            completed += 1
            if completed % 5 == 0 or completed == len(pending_urls):
                print(f"  进度: {completed}/{len(pending_urls)}")

    # 过滤 important，按分数降序
    important_all = [(u, a, sc, st, d) for u, a, sc, st, d in results if st == S_IMPORTANT and a is not None]
    important_all.sort(key=lambda x: x[2], reverse=True)

    # 超出上限的降为 scored
    important_keep = important_all[:max_per_day]
    important_urls = {u for u, *_ in important_keep}
    demoted = [(u, a, sc, S_SCORED, SCORED) for u, a, sc, st, d in important_all if u not in important_urls]

    # 本来就低分的
    low_results = [(u, a, sc, st, d) for u, a, sc, st, d in results if st == S_SCORED and a is not None]

    all_to_process = low_results + demoted

    # 处理低分：删除文件 + mark scored
    for url, article, score_val, status, dest_dir in all_to_process:
        h = url_to_hash(url)
        filepath = PENDING / f"{h}.json"
        try:
            if os.path.exists(str(filepath)):
                os.remove(str(filepath))
        except Exception:
            pass
        mark(url, S_SCORED, score=score_val)

    # 处理高分：保留文件在 important/ + mark important
    for url, article, score_val, status, dest_dir in important_keep:
        h = url_to_hash(url)
        src = PENDING / f"{h}.json"
        dst = IMPORTANT / f"{h}.json"
        try:
            if os.path.exists(str(src)):
                os.rename(str(src), str(dst))
        except Exception:
            dst = None
        mark(url, S_IMPORTANT, score=score_val)

    print(f"\n评分完成:")
    print(f"  重要文章: {len(important_keep)}篇 (阈值={threshold})")
    print(f"  低分文章: {len(low_results)}篇")
    print(f"  超出上限降级: {len(demoted)}篇")

    if important_keep:
        print("\n重要文章:")
        for url, article, score, _, _ in important_keep:
            title = (article.get("title") or "")[:50] if article else ""
            print(f"  [{score}] {title}")


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    for d in [PENDING, SCORED, IMPORTANT]:
        os.makedirs(str(d), exist_ok=True)

    main()
