# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

**[查看所有文章 →](docs/index.html)**

## 数据来源

RSS 订阅列表定义在 `~/.hermes/skills/ai-info/data/config/sources.json`。

## 目录结构

```
ai-info/
├── docs/
│   ├── index.html            ← 文章入口（最新10条 + 年度卡片网格）
│   ├── 2011.html ~ 2026.html ← 年度汇总页（精选列表 + 月份列表）
│   ├── YYYY/MM/              ← 按年月归档的文章（HTML 格式）
│   ├── glossary/             ← 术语表
│   │   ├── index.html        ← 术语索引
│   │   └── terms/            ← 术语 .html 文件
│   └── assets/
│       ├── article.css       ← 文章阅读样式
│       └── index.css         ← 导航页样式（index + 年度汇总共用）
└── .git/
```

## 文章格式

所有文章均以独立 HTML 文件存储，引用 `docs/assets/article.css`。每篇文章固定结构：header（来源+标题+meta）、article-content（正文）、footer（相关文章）。

## 自动化

每天 06:00 自动运行抓取任务（位于 `~/.hermes/skills/ai-info/scripts/`），结果写入 `staging/`，然后导入 `docs/`。

## 许可证

CC BY-SA 4.0
