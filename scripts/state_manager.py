#!/usr/bin/env python3
"""
状态管理：seen_urls.json 的读写
只负责查重和标记状态，不存储文章内容

文章本体在文件系统里流动：
  temp/pending/    — 待评分（crawler写入）
  temp/scored/     — 评分<阈值（scorer移动到这里）
  temp/important/  — 评分>=阈值（scorer移动到这里）
  docs/YYYY/MM/    — 已导入（importer移动到这里）

seen_urls.json 记录每个URL的当前状态，格式：
{
  "url": {"status": "pending|scored|important|done", "file": "filename.json"}
}
"""
import json
import os
from pathlib import Path

BASE = Path("/mnt/d/ProjectFile/ai-info")
SEEN = BASE / "temp" / "seen_urls.json"
PENDING = BASE / "temp" / "pending"
SCORED = BASE / "temp" / "scored"
IMPORTANT = BASE / "temp" / "important"

# 状态常量
S_PENDING = "pending"
S_SCORED = "scored"
S_IMPORTANT = "important"
S_DONE = "done"


def _load() -> dict:
    if not SEEN.exists():
        return {}
    try:
        with open(SEEN, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save(data: dict) -> None:
    SEEN.parent.mkdir(parents=True, exist_ok=True)
    tmp = SEEN.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    os.replace(tmp, SEEN)


def is_seen(url: str) -> bool:
    return url in _load()


def mark(url: str, status: str, filename: str) -> bool:
    """标记URL为指定状态，返回True表示新增，False表示已存在"""
    data = _load()
    was_new = url not in data
    data[url] = {"status": status, "file": filename}
    _save(data)
    return was_new


def remove(url: str) -> None:
    """从记录中删除（表示已全部完成）"""
    data = _load()
    data.pop(url, None)
    _save(data)


def get_status(url: str) -> str | None:
    data = _load()
    return data.get(url, {}).get("status")


def get_all_by_status(status: str) -> list:
    """获取所有指定状态的(url, filename)列表"""
    data = _load()
    return [(url, info["file"]) for url, info in data.items() if info["status"] == status]
