#!/usr/bin/env python3
"""
新评分器：scorer_new.py
- 读 temp/pending/ 目录下的全部文章
- 并行AI评分（复用ai_scorer.py）
- 分数 >= 阈值：移入 temp/important/
- 分数 <  阈值：移入 temp/scored/
- 更新 seen_urls.json 状态
- 单独可重跑：只处理pending文件，已评分的跳过
"""
import sys
import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = Path("/mnt/d/ProjectFile/ai-info")
SKILL_SCRIPTS = Path.home() / ".hermes" / "skills" / "ai-info" / "scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))
sys.path.insert(0, str(BASE))

from state_manager import PENDING, SCORED, IMPORTANT, S_SCORED, S_IMPORTANT, mark
from ai_scorer import score_articles_batch, filter_by_score
from config_loader import Config


def score_one(filepath: Path, config: Config) -> tuple[Path, dict, str, Path]:
    """
    对单篇文章评分，返回 (原文件路径, 文章dict, 新状态, 新目录)
    """
    with open(filepath, encoding="utf-8") as f:
        article = json.load(f)

    result = score_articles_batch([article], score_threshold=None)
    scored = result[0] if result else article

    threshold = config.crawl.get("ai_score_threshold", 5.0)

    if scored.get("ai_score", 0) >= threshold:
        new_status = S_IMPORTANT
        new_dir = IMPORTANT
    else:
        new_status = S_SCORED
        new_dir = SCORED

    return filepath, scored, new_status, new_dir


def main():
    pending_files = list(PENDING.glob("*.json"))
    if not pending_files:
        print("无待评分文章")
        return

    print(f"待评分: {len(pending_files)}篇")

    config = Config.load_from_file()
    threshold = config.crawl.get("ai_score_threshold", 5.0)
    max_per_day = config.crawl.get("ai_max_articles_per_day", 12)
    scored_threshold = config.crawl.get("scored_threshold", 3.0)

    # 并行评分
    completed = 0
    results = []

    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(score_one, f, config): f for f in pending_files}

        for future in as_completed(futures):
            try:
                filepath, scored, new_status, new_dir = future.result()
                results.append((filepath, scored, new_status, new_dir))
            except Exception as e:
                print(f"  [ERROR] {futures[future].name}: {e}")

            completed += 1
            if completed % 5 == 0 or completed == len(pending_files):
                print(f"  进度: {completed}/{len(pending_files)}")

    # 过滤出important并限制数量（按分数降序）
    important_all = [(f, a, s, d) for f, a, s, d in results if s == S_IMPORTANT]
    important_all.sort(key=lambda x: x[1].get("ai_score", 0), reverse=True)
    important_keep = important_all[:max_per_day]
    important_urls = {r[1]["url"] for r in important_keep}

    # 超出上限的important降为scored（直接删除文件，不保留）
    demoted = [(f, a, S_SCORED, SCORED) for f, a, s, d in important_all if a["url"] not in important_urls]

    # scored_results 是本来就<阈值的
    scored_results = [(f, a, s, d) for f, a, s, d in results if s == S_SCORED]

    # 低分文件直接删除 + 清理状态
    for filepath, article, _, _ in scored_results + demoted:
        try:
            filepath.unlink()
            mark(article["url"], "discarded", "")
        except Exception as e:
            print(f"  [WARN] 删除失败 {filepath.name}: {e}")

    # 重要文章移到 important/ 并更新状态
    for filepath, article, _, new_dir in important_keep:
        try:
            dst = new_dir / filepath.name
            shutil.move(str(filepath), str(dst))
            mark(article["url"], S_IMPORTANT, dst.name)
        except Exception as e:
            print(f"  [WARN] 移动失败 {filepath.name}: {e}")

    print(f"\n评分完成:")
    print(f"  重要文章: {len(important_keep)}篇 (阈值={threshold})")
    print(f"  低分文章: {len(scored_results)}篇")
    print(f"  超出上限降级: {len(demoted)}篇")

    if important_keep:
        print("\n重要文章:")
        for _, article, _, _ in important_keep:
            score = article.get("ai_score", 0)
            title = article.get("title", "")[:50]
            print(f"  [{score:.1f}] {title}")


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    PENDING.mkdir(parents=True, exist_ok=True)
    SCORED.mkdir(parents=True, exist_ok=True)
    IMPORTANT.mkdir(parents=True, exist_ok=True)

    main()
