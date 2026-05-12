#!/usr/bin/env python3
"""
新爬虫：crawler_new.py（文件永存架构）
- 扫全部 RSS/HTML 源，提取文章链接
- 对每个未处理 URL：抓全文 → 提取内容 → 写 temp/articles/{hash}.json → mark(pending, file)
- DB 是唯一信号源，文件永不移删
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
    get_pending_urls,
    has_score,
    mark_pending,
    init as sm_init,
    article_path,
    ARTICLES_DIR,
)
sm_init()

# 文章存储目录（固定路径，永不移删）
os.makedirs(ARTICLES_DIR, exist_ok=True)


def url_hash(url: str) -> str:
    """URL → 固定 12 位 hash，路径永远不变"""
    return hashlib.md5(url.encode()).hexdigest()[:12]


def article_path(url: str) -> str:
    """article 文件的固定路径"""
    return os.path.join(ARTICLES_DIR, f"{url_hash(url)}.json")


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
                        if child.tag == tag:
                            results.extend(find(child, remaining[1:]))
                    return results

                for item in find(tree, parts):
                    for child in item.iter():
                        if child.tag == target_tag and child.text:
                            link = child.text.strip()
                            if link and link not in seen:
                                seen.add(link)
                                links.append(link)
            except Exception as e:
                print(f"  [WARN] XML parse error: {e}")
        else:
            soup = BeautifulSoup(html, 'html.parser')
            for a in soup.select(link_selector):
                href = a.get('href') or a.get('src', '')
                link = urljoin(base_url, href).split('?')[0].split('#')[0]
                if link and link not in seen and len(link) > 20:
                    seen.add(link)
                    links.append(link)

        return links

    def process_url(self, url: str, source_name: str = '', source_url: str = '') -> bool:
        """抓取单个 URL，写文件，mark(pending)"""
        h = url_hash(url)
        apath = article_path(url)

        # 文件存在 = 已抓过，跳过
        if os.path.exists(apath):
            return False

        # 抓取
        html = self.fetch_page(url)
        if not html:
            return False

        # 提取正文（传入 source 信息）
        article = self.extractor.extract(html, url, source_name=source_name, source_url=source_url)
        if not article or not article.get('content'):
            return False

        # 写文件（固定路径）
        with open(apath, 'w', encoding='utf-8') as f:
            json.dump({
                'hash': h,
                'title': article.get('title', ''),
                'title_zh': article.get('title_zh', ''),
                'url': url,
                'source_name': article.get('source_name') or source_name,
                'source_url': article.get('source_url') or source_url,
                'publish_date': article.get('publish_date', ''),
                'crawl_date': datetime.now().isoformat(),
                'summary': article.get('summary', ''),
                'content': article.get('content', ''),
                'content_zh': article.get('content_zh', ''),
                'tags': article.get('tags', []),
            }, f, ensure_ascii=False)

        # mark pending（DB 先就绪，文件后写；实际已写完，安全）
        mark_pending(url, f"temp/articles/{h}.json")

        return True

    def crawl_source(self, source: dict) -> tuple[int, int]:
        """抓取单个源，返回 (新增, 失败)"""
        name = source['name']
        source_url = source['url']
        link_selector = source.get('link_selector', 'a[href*="/"]')
        max_articles = self.config.crawl.get('max_articles_per_source', 20)

        print(f"  抓取源: {name} ({source_url})")

        html = self.fetch_page(source_url)
        if not html:
            print(f"  [FAIL] 无法获取 feed: {source_url}")
            return (0, 1)

        links = self.extract_links(html, link_selector, source_url)
        if not links:
            print(f"  [WARN] 发现 0 个链接: {source_url}")
            return (0, 0)

        added = 0
        failed = 0
        for link in links[:max_articles]:
            # 文件存在则跳过（不管 DB 状态）
            if os.path.exists(article_path(link)):
                continue
            if self.process_url(link, source_name=name, source_url=source_url):
                added += 1
            else:
                failed += 1

        print(f"  新增 {added}/{len(links[:max_articles])} 篇")
        return (added, failed)

    def run(self):
        from storage import SourceConfigLoader
        loader = SourceConfigLoader()
        sources = [s for s in loader.load() if s.get('enabled', True)]

        print(f"共 {len(sources)} 个启用的源")

        total_added = 0
        total_failed = 0
        for source in sources:
            try:
                a, f = self.crawl_source(source)
                total_added += a
                total_failed += f
            except Exception as e:
                print(f"  [ERROR] 源 {source['name']} 异常: {e}")

        print(f"\n完成抓取: 新增 {total_added} 篇，失败 {total_failed} 篇")


if __name__ == '__main__':
    config = Config.load_from_file()
    crawler = Crawler(config)
    crawler.run()
