#!/usr/bin/env python3
"""
新爬虫：crawler_new.py
- 扫全部RSS源，提取文章链接
- 对每个新链接：抓全文 → 提取内容 → mark(pending) → 写文件
- 已处理过的URL跳过（查 DB seen_urls）
- 单进程顺序执行，每小时cron触发一次
"""
import sys
import os
import re
import json
import hashlib
import time
import requests
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = Path("/mnt/d/ProjectFile/ai-info")
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / "scripts"))

from config_loader import Config
from extractor import ArticleExtractor
from state_manager import (
    PENDING, is_seen, has_score, mark,
    S_PENDING, init as sm_init
)
sm_init()
from storage import SourceConfigLoader


class Crawler:
    def __init__(self, config: Config):
        self.config = config
        self.session = requests.Session()
        self.extractor = ArticleExtractor()

    def fetch_page(self, url: str) -> str | None:
        headers = {
            'User-Agent': self.config.request['user_agent'],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }
        for attempt in range(self.config.request['max_retries']):
            try:
                resp = self.session.get(
                    url,
                    headers=headers,
                    timeout=self.config.request['timeout_seconds'],
                    allow_redirects=True
                )
                resp.raise_for_status()
                return resp.text
            except Exception as e:
                print(f"  [WARN] fetch {attempt+1} fail: {url} — {e}")
                if attempt < self.config.request['max_retries'] - 1:
                    time.sleep(self.config.request['delay_seconds'])
        return None

    def extract_links(self, html: str, link_selector: str, base_url: str = "") -> list:
        is_xml = html.strip().startswith(('<?xml', '<rss', '<feed'))
        links = []
        seen = set()

        if is_xml:
            import xml.etree.ElementTree as ET
            try:
                tree = ET.fromstring(html)
                parts = link_selector.split()
                target_tag = parts[-1]

                def find(elem, remaining):
                    if not remaining:
                        return [elem]
                    tag = remaining[0]
                    results = []
                    for child in elem.iter():
                        ct = child.tag.split('}')[-1] if '}' in child.tag else child.tag
                        if ct == tag:
                            results.extend(find(child, remaining[1:]))
                    return results

                for elem in find(tree, parts):
                    href = (elem.text or '').strip() or elem.get('href')
                    if href and href not in seen:
                        seen.add(href)
                        links.append(urljoin(base_url, href))
            except ET.ParseError as e:
                print(f"  [WARN] XML parse error: {e}")
        else:
            soup = BeautifulSoup(html, 'html.parser')
            for elem in soup.select(link_selector):
                href = elem.get('href')
                if not href:
                    continue
                abs_href = urljoin(base_url, href)
                if abs_href not in seen:
                    seen.add(abs_href)
                    links.append(abs_href)

        return links

    def url_hash(self, url: str) -> str:
        return hashlib.md5(url.encode('utf-8')).hexdigest()[:12]

    def crawl_source(self, source: dict) -> int:
        """抓取单个源，返回新增文章数"""
        source_id = source['id']
        source_name = source.get('name', source_id)
        feed_url = source['url']
        selector = source.get('link_selector', 'item link')
        max_articles = self.config.crawl.get('max_articles_per_source', 20)

        print(f"  抓取源: {source_name} ({feed_url})")
        html = self.fetch_page(feed_url)
        if not html:
            print(f"  [FAIL] 无法获取 feed: {feed_url}")
            return 0

        links = self.extract_links(html, selector, feed_url)
        if not links:
            print(f"  [WARN] 无链接: {feed_url}")
            return 0

        print(f"  发现 {len(links)} 个链接")
        new_count = 0

        for url in links:
            if is_seen(url):
                continue

            article_html = self.fetch_page(url)
            if not article_html:
                continue

            extracted = self.extractor.extract(article_html, url)
            if not extracted or not extracted.get('content'):
                extracted = extracted or {}
                extracted.setdefault('content', extracted.get('summary', ''))

            article_hash = self.url_hash(url)
            filename = f"{article_hash}.json"
            filepath = PENDING / filename

            article = {
                'hash': article_hash,
                'title': extracted.get('title') or url.split('/')[-1],
                'title_zh': None,
                'url': url,
                'source_id': source_id,
                'source_name': source_name,
                'source_url': feed_url,
                'publish_date': extracted.get('publish_date') or datetime.now().strftime('%Y-%m-%d'),
                'crawl_date': datetime.now().strftime('%Y-%m-%d'),
                'summary': extracted.get('summary', ''),
                'content': extracted.get('content', ''),
                'content_zh': None,
                'tags': [],
                'status': 'pending',
            }

            # 先写文件（内容缓存）
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(article, f, ensure_ascii=False, indent=2)

            # 再 mark DB（信号）
            mark(url, S_PENDING, filename)
            new_count += 1

            # 超过 max_articles 就停
            if new_count >= max_articles:
                break

            time.sleep(self.config.request['delay_seconds'])

        print(f"  新增 {new_count}/{len(links)} 篇")
        return new_count

    def run(self):
        """扫描全部源并抓取"""
        loader = SourceConfigLoader()
        sources = loader.load()
        enabled = [s for s in sources if s.get('enabled', True)]
        print(f"共 {len(enabled)} 个启用的源")

        total_new = 0
        for source in enabled:
            try:
                total_new += self.crawl_source(source)
            except Exception as e:
                print(f"  [ERROR] 源 {source.get('id')} 出错: {e}")
        print(f"\n抓取完成，新增 {total_new} 篇")


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    cfg = Config.load_from_file(str(BASE / "config" / "config.json"))
    PENDING.mkdir(parents=True, exist_ok=True)
    crawler = Crawler(cfg)
    crawler.run()
