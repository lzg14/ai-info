import json
import os
import hashlib
import uuid
from datetime import datetime
from typing import List, Dict, Optional


def calculate_similarity(text1: str, text2: str) -> float:
    """计算两个字符串的相似度（基于字符级 Jaccard 相似度）"""
    if not text1 or not text2:
        return 0.0

    # 预处理：转小写，去除空白字符
    t1 = ''.join(text1.lower().split())
    t2 = ''.join(text2.lower().split())

    if not t1 or not t2:
        return 0.0

    # 使用字符 bigram 计算 Jaccard 相似度
    def get_bigrams(text: str) -> set:
        return set(text[i:i+2] for i in range(len(text)-1))

    bigrams1 = get_bigrams(t1)
    bigrams2 = get_bigrams(t2)

    if not bigrams1 or not bigrams2:
        return 0.0

    intersection = len(bigrams1 & bigrams2)
    union = len(bigrams1 | bigrams2)

    return intersection / union if union > 0 else 0.0


class ArticleIndex:
    """文章索引管理"""

    def __init__(self, index_path: str = "temp/data/index.json"):
        self.index_path = index_path
        self.articles: List[Dict] = self._load_index()

    def _load_index(self) -> List[Dict]:
        """加载索引"""
        if not os.path.exists(self.index_path):
            return []
        try:
            with open(self.index_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[WARNING] Failed to load index: {e}")
            return []

    def _save_index(self) -> None:
        """保存索引"""
        try:
            os.makedirs(os.path.dirname(self.index_path) or '.', exist_ok=True)
            with open(self.index_path, 'w', encoding='utf-8') as f:
                json.dump(self.articles, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[ERROR] Failed to save index: {e}")

    def exists(self, url: str, title: Optional[str], source_id: str) -> bool:
        """检查文章是否已存在（基于 URL、标题相同、标题相似度 > 80% 去重）"""
        for article in self.articles:
            # URL 完全相同
            if article['url'] == url:
                return True
            # 标题完全相同
            if title and article.get('title') == title:
                return True
            # 标题相似度 > 80%
            if title and article.get('title'):
                sim = calculate_similarity(title, article['title'])
                if sim > 0.8:
                    return True
        return False

    def add_article(self, article: Dict) -> str:
        """添加文章到索引，返回文章 ID"""
        article_id = str(uuid.uuid4())[:8]
        article['id'] = article_id
        self.articles.append(article)
        self._save_index()
        return article_id

    def get_all_articles(self) -> List[Dict]:
        """获取所有文章，按抓取日期倒序"""
        return sorted(self.articles, key=lambda x: x.get('crawl_date', ''), reverse=True)

    def get_articles_by_date(self, date: str) -> List[Dict]:
        """按日期获取文章"""
        return [a for a in self.articles if a.get('crawl_date') == date]


class ArticleStorage:
    """文章按日期归档存储"""

    def __init__(self, base_dir: str = "temp/data/articles", raw_dir: str = "temp/data/raw"):
        self.base_dir = base_dir
        self.raw_dir = raw_dir
        os.makedirs(base_dir, exist_ok=True)
        os.makedirs(raw_dir, exist_ok=True)

    def save_article_daily(self, date: str, articles: List[Dict]) -> None:
        """保存某日文章到归档文件"""
        date_path = os.path.join(self.base_dir, f"{date}.json")
        os.makedirs(os.path.dirname(date_path) or '.', exist_ok=True)
        try:
            with open(date_path, 'w', encoding='utf-8') as f:
                json.dump(articles, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[ERROR] Failed to save daily articles: {e}")

    def save_raw_content(self, crawl_date: str, url: str, html: str) -> None:
        """保存原始 HTML 缓存"""
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
        raw_path = os.path.join(self.raw_dir, crawl_date, f"{url_hash}.json")
        os.makedirs(os.path.dirname(raw_path), exist_ok=True)
        try:
            with open(raw_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'url': url,
                    'html': html,
                    'crawl_date': crawl_date,
                    'timestamp': int(datetime.now().timestamp())
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[WARNING] Failed to save raw content: {e}")


class SourceConfigLoader:
    """加载信息源配置"""

    def __init__(self, config_path: str = None):
        if config_path is None:
            import os
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'sources.json')
        self.config_path = config_path

    def load(self) -> List[Dict]:
        """加载所有启用的信息源"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            sources = [s for s in data if s.get('enabled', True)]
            return sources
        except Exception as e:
            print(f"[ERROR] Failed to load sources config: {e}")
            raise


class Source:
    """信息源定义"""
    def __init__(
        self,
        source_id: str,
        source_name: str,
        url: str,
        language: str,
        category: str,
        link_selector: str,
        enabled: bool = True,
        title_selector: Optional[str] = None,
    ):
        self.source_id = source_id
        self.source_name = source_name
        self.url = url
        self.language = language
        self.category = category
        self.link_selector = link_selector
        self.title_selector = title_selector
        self.enabled = enabled
