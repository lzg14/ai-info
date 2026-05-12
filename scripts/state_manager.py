"""
状态管理 — SQLite 版本
数据库文件：data/state.db
"""

import sqlite3
import os
from datetime import datetime

# 常量
S_PENDING   = "pending"
S_SCORED    = "scored"
S_DONE      = "done"
S_IMPORTANT = "scored"   # alias，SQLite 中 scored 状态已包含高分

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "state.db")

# 目录常量（供其他脚本使用）
BASE      = os.path.join(os.path.dirname(__file__), "..")
PENDING   = os.path.join(BASE, "temp", "pending")
SCORED    = os.path.join(BASE, "temp", "scored")
IMPORTANT = os.path.join(BASE, "temp", "important")


def init():
    """首次运行建表"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS seen_urls (
                url         TEXT PRIMARY KEY,
                status      TEXT NOT NULL DEFAULT 'pending',
                file        TEXT,
                score       INTEGER,
                created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_status ON seen_urls(status)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_score  ON seen_urls(score)")
        conn.commit()
    finally:
        conn.close()


def add(url: str) -> bool:
    """新增 URL，返回是否是新记录"""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO seen_urls (url, status) VALUES (?, ?)",
            (url, S_PENDING)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def has(url: str) -> bool:
    """URL 是否见过（任意状态）"""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM seen_urls WHERE url = ?", (url,))
        return cur.fetchone() is not None
    finally:
        conn.close()

is_seen = has   # 别名，兼容旧调用


def has_score(url: str) -> bool:
    """URL 是否已有评分（高分或低分均算）"""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT 1 FROM seen_urls WHERE url = ? AND score IS NOT NULL",
            (url,)
        )
        return cur.fetchone() is not None
    finally:
        conn.close()


def get_score(url: str):
    """获取评分，没有返回 None"""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT score FROM seen_urls WHERE url = ?", (url,))
        row = cur.fetchone()
        return row[0] if row else None
    finally:
        conn.close()


def get_status(url: str):
    """获取状态，没有返回 None"""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("SELECT status FROM seen_urls WHERE url = ?", (url,))
        row = cur.fetchone()
        return row[0] if row else None
    finally:
        conn.close()


def get_pending_urls(limit: int = None):
    """返回所有 pending 的 URL"""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        sql = "SELECT url FROM seen_urls WHERE status = ? ORDER BY created_at"
        if limit:
            sql += f" LIMIT {limit}"
        cur.execute(sql, (S_PENDING,))
        return [r[0] for r in cur.fetchall()]
    finally:
        conn.close()


def get_scored_low():
    """返回低分（score <= 5）的 scored URL"""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT url, file FROM seen_urls WHERE status = ? AND score IS NOT NULL AND score <= 5",
            (S_SCORED,)
        )
        return [(r[0], r[1]) for r in cur.fetchall()]
    finally:
        conn.close()


def mark(url: str, status: str, file: str = None, score: int = None):
    """
    更新状态/文件/分数。不存在则插入。
    已有记录时：非 None 的参数才覆盖，None 保留原值。
    status: S_PENDING / S_SCORED / S_DONE
    score:  1-10 整数，可选
    """
    now = datetime.now().isoformat()
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        # ON CONFLICT 保证已有记录只更新指定字段，保留原 score/created_at
        sql = """
            INSERT INTO seen_urls (url, status, file, score, updated_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(url) DO UPDATE SET
                status    = excluded.status,
                file      = excluded.file,
                score     = COALESCE(excluded.score, seen_urls.score),
                updated_at = excluded.updated_at
        """
        cur.execute(sql, (url, status, file, score, now))
        conn.commit()
    finally:
        conn.close()


def dump():
    """导出全量数据（dict list）"""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT url, status, file, score, created_at, updated_at FROM seen_urls"
        )
        cols = ["url", "status", "file", "score", "created_at", "updated_at"]
        return [dict(zip(cols, r)) for r in cur.fetchall()]
    finally:
        conn.close()


if __name__ == "__main__":
    init()
    print(f"数据库初始化完成：{DB_PATH}")
