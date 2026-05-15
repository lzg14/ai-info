#!/usr/bin/env python3
"""快速评分 - 专为批量处理设计"""
import os, json, glob, requests, sqlite3, re, sys

API_KEY = os.getenv('MINIMAX_CN_API_KEY')
BASE = 'https://api.minimaxi.com/v1'
MODEL = 'MiniMax-M2.7'
ARTICLES = '/mnt/d/ProjectFile/ai-info/temp/articles'
DB = '/mnt/d/ProjectFile/ai-info/data/state.db'
BATCH_SIZE = 10

if not API_KEY:
    print('[ERROR] No API key')
    sys.exit(1)

conn = sqlite3.connect(DB)

# 找出所有需要评分的文章：score=NULL 或 score=0 且 status!=done
todo = conn.execute("""
    SELECT url FROM seen_urls 
    WHERE (score IS NULL OR score = 0) AND status != 'done'
""").fetchall()
todo_urls = [r[0] for r in todo]
print(f'[scorer] 待评分: {len(todo_urls)} 篇')

# 找出对应的json文件
url_to_fp = {}
for fp in glob.glob(f'{ARTICLES}/*.json'):
    try:
        d = json.load(open(fp))
        url_to_fp[d['url']] = fp
    except:
        pass

scored = 0
for i, url in enumerate(todo_urls):
    fp = url_to_fp.get(url)
    if not fp:
        continue
    
    try:
        d = json.load(open(fp))
    except:
        continue
    
    title = d.get('title', '')[:50]
    content = (d.get('content', '') or d.get('summary', ''))[:600]
    
    # 精简prompt，避免模型回复过长
    prompt = f"评分(0-10)文章：{d.get('title', '')}。内容摘要：{content[:300]}。只回一个数字。"
    
    try:
        r = requests.post(
            f'{BASE}/chat/completions',
            headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'},
            json={'model': MODEL, 'messages': [{'role': 'user', 'content': prompt}], 'max_tokens': 3},
            timeout=(15, 25)
        )
        r.raise_for_status()
        raw = r.json()['choices'][0]['message']['content'].strip()
        # 取第一个纯数字
        m = re.search(r'\d', raw)
        score = int(m.group()) if m else 5
        score = max(0, min(10, score))
    except Exception as e:
        score = 5
    
    conn.execute("UPDATE seen_urls SET score=?, status='scored' WHERE url=? AND status != 'done'", (score, url))
    conn.commit()
    
    tag = '★' if score >= 7 else ' '
    print(f'[{i+1}/{len(todo_urls)}] [{tag}{score}] {title}')
    
    # 每BATCH_SIZE篇打印心跳
    if (i + 1) % BATCH_SIZE == 0:
        print(f'  >>> {i+1}/{len(todo_urls)} 完成')

conn.close()
print(f'\n[DONE] scored {scored if scored else len(todo_urls)} articles')
