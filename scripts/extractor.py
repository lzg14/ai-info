import trafilatura
from trafilatura.settings import Extractor
from configparser import ConfigParser
from typing import Optional, Dict


def _fix_trafilatura_settings():
    """修复 trafilatura 1.12.2 在 PyInstaller 打包时 settings.cfg 加载问题"""
    # 手动创建默认配置（完整版本）
    cfg = ConfigParser()
    # DEFAULT already exists by default in ConfigParser
    # Download
    cfg.set('DEFAULT', 'DOWNLOAD_TIMEOUT', '30')
    cfg.set('DEFAULT', 'MAX_FILE_SIZE', '20000000')
    cfg.set('DEFAULT', 'MIN_FILE_SIZE', '10')
    # sleep between requests
    cfg.set('DEFAULT', 'SLEEP_TIME', '5')
    cfg.set('DEFAULT', 'USER_AGENTS', '')
    cfg.set('DEFAULT', 'COOKIE', '')
    cfg.set('DEFAULT', 'MAX_REDIRECTS', '2')

    # Extraction
    cfg.set('DEFAULT', 'MIN_EXTRACTED_SIZE', '250')
    cfg.set('DEFAULT', 'MIN_EXTRACTED_COMM_SIZE', '1')
    cfg.set('DEFAULT', 'MIN_OUTPUT_SIZE', '1')
    cfg.set('DEFAULT', 'MIN_OUTPUT_COMM_SIZE', '1')

    # Deduplication
    cfg.set('DEFAULT', 'MIN_DUPLCHECK_SIZE', '100')
    cfg.set('DEFAULT', 'MAX_REPETITIONS', '2')

    # Date extraction
    cfg.set('DEFAULT', 'EXTENSIVE_DATE_SEARCH', 'True')

    # CLI timeout
    cfg.set('DEFAULT', 'EXTRACTION_TIMEOUT', '30')

    return cfg


class ArticleExtractor:
    """文章提取器，使用 trafilatura 从 HTML 中提取文章内容和元数据"""

    @staticmethod
    def extract(html: str, url: str, source_name: str = '', source_url: str = '') -> Optional[Dict[str, Optional[str]]]:
        """
        从 HTML 中提取文章内容、标题、发布日期和摘要

        Args:
            html: 原始 HTML 内容
            url: 网页 URL
            source_name: 来源名称（如 "Anthropic News"）
            source_url: 来源首页 URL（如 "https://www.anthropic.com/news"）
        """
        # 修复 trafilatura 设置加载问题
        fixed_config = _fix_trafilatura_settings()
        # 提取正文内容
        extracted_text = trafilatura.extract(html, include_links=False, include_images=False, config=fixed_config)

        # 如果提取结果为 None 或空字符串，直接返回 None
        if not extracted_text:
            return None

        # 提取元数据
        metadata = trafilatura.extract_metadata(html)

        title = metadata.title if metadata and metadata.title else None
        publish_date = metadata.date if metadata and metadata.date else None
        description = metadata.description if metadata and metadata.description else None

        # 生成摘要
        summary = description
        if not summary and extracted_text:
            # 按段落分割
            paragraphs = [p.strip() for p in extracted_text.split('\n\n') if p.strip()]
            # 取前 2-3 段
            selected = paragraphs[:3] if len(paragraphs) >= 3 else paragraphs[:2]
            combined = ' '.join(selected)
            # 截断到约 300 字符
            if len(combined) > 300:
                combined = combined[:297] + '...'
            summary = combined

        return {
            'content': extracted_text,
            'title': title,
            'publish_date': publish_date,
            'summary': summary,
            'source_name': source_name,
            'source_url': source_url,
        }


if __name__ == "__main__":
    import sys
    from pathlib import Path

    # 添加项目根目录到 Python 路径
    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))

    try:
        if len(sys.argv) > 1:
            url = sys.argv[1]
            import requests
            from scripts.config_loader import Config
            cfg = Config.load_from_file(str(project_root / "config" / "config.json"))
            headers = {'User-Agent': cfg.request['user_agent']}
            html = requests.get(url, headers=headers).text
            result = ArticleExtractor.extract(html, url)
            if result:
                print(f"Title: {result['title']}")
                print(f"Date: {result['publish_date']}")
                print(f"Summary: {result['summary'][:100]}...")
                print(f"Content length: {len(result['content'])}")
        else:
            print("Usage: python extractor.py <url>")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
