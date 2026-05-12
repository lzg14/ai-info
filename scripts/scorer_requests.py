#!/usr/bin/env python3
"""Pure-requests scorer - no OpenAI SDK, avoids futex deadlock."""
import os, sqlite3, json, time, requests, sys, logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', stream=sys.stdout)
log = logging.getLogger()

# ── Env ──────────────────────────────────────────────────────────────────────
for line in open(Path.home() / '.hermes' / '.env'):
    k, _, v = line.strip().partition('=')
    if k == 'MINIMAX_CN_API_KEY':
        os.environ['MINIMAX_API_KEY'] = v

APIKEY = os.environ['MINIMAX_API_KEY']
BASE_URL = 'https://api.minimaxi.com/v1'
MODEL = 'MiniMax-M2.7'
PROMPT = """You are a news classifier. Rate the following article's importance for an AI tech news feed.
Score 1-10:
  1-3 = low importance (skip)
  4-6 = moderate importance (include if space)
  7-10 = high importance (must include)

URL: {url}

Rules:
- Reply with ONLY a single integer 1-10, no explanation.
- Academic/technical deep-dives score higher.
- News about major AI labs (OpenAI, Anthropic, Google, Meta, xAI) score higher.
- Routine updates or low-significance content score lower."""

# ── DB ───────────────────────────────────────────────────────────────────────
DB_PATH = Path(__file__).parent.parent / 'data' / 'state.db'
db = sqlite3.connect(DB_PATH)

def mark(url, status, score=None, file_path=None):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    file_col = f"'{file_path}'" if file_path else 'file'
    score_col = f"{score}" if score is not None else 'score'
    db.execute(f"""
        INSERT INTO seen_urls (url, status, {file_col}, score, created_at, updated_at)
        VALUES (?, ?, {file_col}, {score_col}, ?, ?)
        ON CONFLICT(url) DO UPDATE SET
            status=excluded.status, file={file_col}, score={score_col}, updated_at=excluded.updated_at
    """, (url, status, file_path, score, now, now))
    db.commit()

def get_pending(limit=5):
    rows = db.execute('SELECT url, file FROM seen_urls WHERE status="pending" LIMIT ?', (limit,)).fetchall()
    return rows

# ── Scoring ──────────────────────────────────────────────────────────────────
def score_article(url):
    try:
        resp = requests.post(
            f'{BASE_URL}/chat/completions',
            headers={'Authorization': f'Bearer {APIKEY}', 'Content-Type': 'application/json'},
            json={'model': MODEL, 'max_tokens': 5, 'temperature': 0,
                  'messages': [
                      {'role': 'system', 'content': 'You are a news classifier. Reply ONLY the integer score.'},
                      {'role': 'user', 'content': PROMPT.format(url=url)}
                  ]},
            timeout=50
        )
        if resp.status_code == 200:
            text = resp.json()['choices'][0]['message']['content'].strip()
            # Extract integer
            import re
            m = re.search(r'\d+', text)
            score = int(m.group()) if m else None
            return score
        else:
            log.error(f"HTTP {resp.status_code}: {resp.text[:100]}")
            return None
    except Exception as e:
        log.error(f"Exception: {e}")
        return None

# ── Main ─────────────────────────────────────────────────────────────────────
log.info(f"Starting scorer (pure requests)")
pending = get_pending(9999)
log.info(f"待评分: {len(pending)}篇")

for i, (url, file) in enumerate(pending):
    log.info(f"  [{i+1}/{len(pending)}] {url[:80]}...")
    score = score_article(url)
    if score is not None:
        log.info(f"    score={score}")
        mark(url, 'scored', score=score)
    else:
        log.warning(f"    评分失败，跳过")
    # Small delay to avoid rate limit
    time.sleep(0.5)

log.info("评分完成")
