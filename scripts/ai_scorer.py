#!/usr/bin/env python3
"""
AI 质量评分模块 — 基于 MiniMax API 对文章进行重要性评分（0-10）
参考 Horizon 的 CONTENT_ANALYSIS prompt 设计
"""
import os
import sys
import json
import time
import logging
from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
import yaml
from dotenv import load_dotenv

# 加载环境变量（优先 .env，再从 hermes config 兜底）
env_path = Path.home() / ".hermes" / ".env"
load_dotenv(env_path)

API_KEY = os.getenv("MINIMAX_API_KEY") or os.getenv("MINIMAX_CN_API_KEY") or ""
if not API_KEY:
    # 尝试从 hermes config.yaml 读取
    hermes_config = Path.home() / ".hermes" / "config.yaml"
    if hermes_config.exists():
        cfg = yaml.safe_load(hermes_config.read_text())
        providers = cfg.get("providers", {})
        for name, p in providers.items():
            for k in ("key", "api_key", "api-key"):
                if k in p and p[k]:
                    API_KEY = p[k]
                    break
            if API_KEY:
                break

BASE_URL = os.getenv("LLM_API_BASE", "https://api.minimaxi.com/v1")
MODEL = os.getenv("LLM_MODEL", "MiniMax-M2.7")

# 内容分析 system prompt（参考 Horizon）
SYSTEM_PROMPT = """You are an expert content curator helping filter important technical and academic information.

Score content on a 0-10 scale based on importance and relevance:

**9-10: Groundbreaking** - Major breakthroughs, paradigm shifts, or highly significant announcements
- New major version releases of widely-used technologies
- Significant research breakthroughs
- Important industry-changing announcements

**7-8: High Value** - Important developments worth immediate attention
- Interesting technical deep-dives
- Novel approaches to known problems
- Insightful analysis or commentary
- Valuable tools or libraries

**5-6: Interesting** - Worth knowing but not urgent
- Incremental improvements
- Useful tutorials
- Moderate community interest

**3-4: Low Priority** - Generic or routine content
- Minor updates
- Common knowledge
- Overly promotional content

**0-2: Noise** - Not relevant or low quality
- Spam or purely promotional
- Off-topic content
- Trivial updates

Consider:
- Technical depth and novelty
- Potential impact on the field
- Quality of writing/presentation
- Relevance to software engineering, AI/ML, and systems research
"""

USER_PROMPT_TEMPLATE = """Analyze the following content and provide a JSON response with:
- score (0-10): Importance score
- reason: Brief explanation for the score
- summary: One-sentence summary of the content
- tags: Relevant topic tags (3-5 tags)

Content:
Title: {title}
Source: {source}
URL: {url}
Published: {publish_date}
Summary: {summary}
Content preview: {content_preview}

Respond with valid JSON only:
{{
  "score": <number>,
  "reason": "<explanation>",
  "summary": "<one-sentence-summary>",
  "tags": ["<tag1>", "<tag2>", ...]
}}"""


def parse_json_response(text: str) -> Optional[dict]:
    """从 AI 响应中解析 JSON，尝试多种策略"""
    # 策略1：直接解析
    try:
        return json.loads(text.strip())
    except Exception:
        pass

    # 策略2：提取 ```json ... ``` 块
    import re
    match = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1).strip())
        except Exception:
            pass

    # 策略3：提取第一个 { ... } JSON 对象
    match = re.search(r'\{[^{}]*"score"[^{}]*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except Exception:
            pass

    # 策略4：找所有 {...} 块，尝试解析
    for block in re.findall(r'\{[^{}]+\}', text, re.DOTALL):
        try:
            result = json.loads(block)
            if 'score' in result:
                return result
        except Exception:
            continue

    return None


def score_article(
    title: str,
    source: str,
    url: str,
    publish_date: str,
    summary: str,
    content_preview: str = "",
    temperature: float = 0.3,
    max_retries: int = 3,
) -> Optional[Dict]:
    """
    对单篇文章进行 AI 评分

    Returns:
        dict with keys: score, reason, summary, tags
        or None if scoring failed
    """
    if not API_KEY:
        logging.warning("LLM_API_KEY not set, skipping AI scoring")
        return None

    user_prompt = USER_PROMPT_TEMPLATE.format(
        title=title or "无标题",
        source=source or "未知来源",
        url=url or "",
        publish_date=publish_date or "未知",
        summary=summary or "无摘要",
        content_preview=content_preview[:500] if content_preview else "无正文预览",
    )

    for attempt in range(max_retries):
        try:
            resp = requests.post(
                f"{BASE_URL}/text/chatcompletion_v2",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    "temperature": temperature,
                    "max_tokens": 800,
                },
                timeout=30,
            )

            if resp.status_code != 200:
                logging.warning(f"API error {resp.status_code}: {resp.text[:100]}")
                time.sleep(2)
                continue

            data = resp.json()
            choices = data.get("choices", [{}])
            if not choices:
                continue

            message = choices[0].get("message", {})
            # M2.7 推理模型：content 可能为空，实际在 reasoning_content
            raw_content = message.get("content", "") or ""
            if not raw_content:
                raw_content = message.get("reasoning_content", "") or ""
            # 去掉推理过程（截断 "Think silently" 之后的部分）
            if "Think silently" in raw_content:
                raw_content = raw_content.split("Think silently")[0]

            result = parse_json_response(raw_content)

            if result and "score" in result:
                return result

        except Exception as e:
            logging.warning(f"Scoring attempt {attempt+1} failed: {e}")
            time.sleep(2)

    return None


def score_articles_batch(
    articles: List[Dict],
    score_threshold: float = 6.0,
    skip_translated: bool = False,
) -> List[Dict]:
    """
    批量对文章进行 AI 评分，返回带评分结果的列表

    Args:
        articles: 文章列表，每个是 dict
        score_threshold: 仅保留评分 >= 此阈值的重要文章（设为 None 则返回全部）
        skip_translated: 是否跳过已评过分的内容（避免重复评分）

    Returns:
        带 ai_score, ai_reason, ai_summary, ai_tags 字段的文章列表
    """
    # 并发评分：5 个线程同时跑，大幅加速
    total = len(articles)
    scored = [None] * total
    completed = 0

    def score_one(index_article):
        idx, article = index_article
        title = article.get("title_zh") or article.get("title") or ""
        source = article.get("source_name", "")
        url = article.get("url", "")
        publish_date = article.get("publish_date", "")
        summary = article.get("summary") or article.get("title_zh") or ""
        content = article.get("content_zh") or article.get("content") or ""

        result = score_article(
            title=title,
            source=source,
            url=url,
            publish_date=publish_date,
            summary=summary,
            content_preview=content[:500] if content else "",
        )

        if result:
            article["ai_score"] = float(result.get("score", 0))
            article["ai_reason"] = result.get("reason", "")
            article["ai_summary"] = result.get("summary", "")
            article["ai_tags"] = result.get("tags", [])
        else:
            article["ai_score"] = 0.0
            article["ai_reason"] = "评分失败"
            article["ai_summary"] = title
            article["ai_tags"] = []

        return idx, article

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(score_one, (i, art)): i
            for i, art in enumerate(articles)
        }
        for future in as_completed(futures):
            idx, article = future.result()
            scored[idx] = article
            completed += 1
            if completed % 5 == 0 or completed == total:
                logging.info(f"[AI Scoring] {completed}/{total} completed")

    return scored


def filter_by_score(
    articles: List[Dict],
    threshold: float = 6.0,
    max_articles: int = 15,
) -> List[Dict]:
    """
    按 AI 评分过滤文章

    Args:
        articles: 带 ai_score 字段的文章列表
        threshold: 最低分数阈值
        max_articles: 最多保留篇数

    Returns:
        过滤后的文章列表（按分数降序排列）
    """
    filtered = [a for a in articles if a.get("ai_score", 0) >= threshold]
    filtered.sort(key=lambda x: x.get("ai_score", 0), reverse=True)
    return filtered[:max_articles]


if __name__ == "__main__":
    # 简单测试
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    test_article = {
        "title": "GPT-5 Released: A Major Breakthrough in AI Reasoning",
        "source_name": "OpenAI Blog",
        "url": "https://openai.com/blog/gpt-5",
        "publish_date": "2026-05-01",
        "summary": "OpenAI announces GPT-5 with revolutionary reasoning capabilities",
        "content": "",
    }

    result = score_article(
        title=test_article["title"],
        source=test_article["source_name"],
        url=test_article["url"],
        publish_date=test_article["publish_date"],
        summary=test_article["summary"],
    )

    print(f"Test scoring result: {json.dumps(result, ensure_ascii=False, indent=2)}")
