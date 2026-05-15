#!/usr/bin/env python3
"""快速批量评分脚本 - 每次API调用独立，及时写DB不丢进度"""
import os, json, glob, requests, sqlite3, sys

API_KEY = os.getenv('MINIMAX_CN_API_KEY')
BASE = 'https://api.minimaxi.com/v1'
MODEL = 'MiniMax-M2.7'
ARTICLES = '/mnt/d/ProjectFile/ai-info/temp/articles'
DB = '/mnt/d/ProjectFile/ai-info/data/state.db'
SCORE_THRESHOLD = 8

if not API_KEY:
    print('[ERROR] No API key')
    sys.exit(1)

conn = sqlite3.connect(DB)
files = sorted(glob.glob(f'{ARTICLES}/*.json'))
print(f'[batch] Total: {len(files)} articles')

scored = 0
failed = 0
important = 0

for i, fp in enumerate(files):
    h = os.path.basename(fp).replace('.json', '')
    d = json.load(open(fp))
    url = d['url']
    title = d.get('title', '')[:50]

    # skip if already scored
    row = conn.execute("SELECT status FROM seen_urls WHERE url=?", (url,)).fetchone()
    if row and row[0] == 'scored':
        print(f'  [SKIP] {title}')
        continue

    # score via API
    content = d.get('content', '') or d.get('summary', '')
    prompt = f"""你是AI资讯评分专家。为以下文章打分(0-10)：
标题：{d.get('title', '')}
内容：{content[:600]}
评分标准：AI技术含量(0-3)、新闻价值(0-3)、时效性(0-2)、深度(0-2)。只回答一个数字(0-10)。"""

    try:
        r = requests.post(
            f'{BASE}/chat/completions',
            headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'},
            json={'model': MODEL, 'messages': [{'role': 'user', 'content': prompt}], 'max_tokens': 4},
            timeout=(30, 60)
        )
        r.raise_for_status()
        score_text = r.json()['choices'][0]['message']['content'].strip()
        score = int(''.join(filter(str.isdigit, score_text)) or 0)
        score = max(0, min(10, score))
    except Exception as e:
        print(f'  [WARN] FAIL {title}: {e}')
        score = 5
        failed += 1

    conn.execute("INSERT OR REPLACE INTO seen_urls (url, status, score) VALUES (?, 'scored', ?)", (url, score))
    conn.commit()

    tag = '★' if score >= SCORE_THRESHOLD else ' '
    print(f'  [{tag} {score}/10] {title}')
    scored += 1
    if score >= SCORE_THRESHOLD:
        important += 1

    # heartbeat every 20
    if (i + 1) % 20 == 0:
        print(f'[heartbeat] {i+1}/{len(files)} done, {important} important so far')

conn.close()
print(f'\n[DONE] scored={scored}, important={important}, failed={failed}')
