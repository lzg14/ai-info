import json
from typing import Dict, Any


class Config:
    """全局配置"""
    def __init__(self, request: Dict, crawl: Dict):
        self.request = request
        self.crawl = crawl

    @classmethod
    def load_from_file(cls, path: str = None) -> 'Config':
        """从文件加载配置"""
        if path is None:
            # Default to config/config.json relative to this file's directory
            import os
            path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'config.json')
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls(data['request'], data['crawl'])
