# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

## 最新 10 条
<!-- LATEST_BEGIN -->
- [Hermes 可配置的国内外 AI 模型及使用方法](docs/2026/05/2026-05-19_hermes-可配置的国内外-ai-模型及使用方法.md)（05-19）
- [一键生成韩国棒球AI视频模板爆火](docs/2026/05/2026-05-19_一键生成韩国棒球ai视频模板爆火.md)（05-19）
- [人机快递分拣对决直播](docs/2026/05/2026-05-19_人机快递分拣对决直播.md)（05-19）
- [开源工具揭露AI API中转站安全风险与检测差异](docs/2026/05/2026-05-19_开源工具揭露ai-api中转站安全风险与检测差异.md)（05-19）
- [微信读书Skill安装与使用指南](docs/2026/05/2026-05-19_微信读书skill安装与使用指南.md)（05-19）
- [腾讯 AI 设计智能体 Ardot 公测：一句话生成可编辑设计稿，一键转代码](docs/2026/05/2026-05-19_腾讯-ai-设计智能体-ardot-公测一句话生成可编辑设计稿一键转代码.md)（05-19）
- [阿里云推出HappyHorse视频生成模型](docs/2026/05/2026-05-19_阿里云推出happyhorse视频生成模型.md)（05-19）
- [8B模型做生物实验：实验步骤顺序不乱、剂量无幻觉｜ICLR 2026](docs/2026/05/2026-05-18_8b模型做生物实验实验步骤顺序不乱剂量无幻觉iclr-2026.md)（05-18）
- [AI水论文封一年，署名连坐！arXiv最严新规来了，陶哲轩附议](docs/2026/05/2026-05-18_ai水论文封一年署名连坐arxiv最严新规来了陶哲轩附议.md)（05-18）
- [Bug bounty businesses bombarded with AI slop](docs/2026/05/2026-05-18_bug-bounty-businesses-bombarded-with-ai-slop.md)（05-18）
<!-- LATEST_END -->

## 年度导航

<!-- YEARLY_BEGIN -->
| 年份 | 文章数 |
|------|--------|
| [2011](docs/2011.md) | 3 |
| [2012](docs/2012.md) | 50 |
| [2013](docs/2013.md) | 50 |
| [2014](docs/2014.md) | 50 |
| [2015](docs/2015.md) | 50 |
| [2016](docs/2016.md) | 50 |
| [2017](docs/2017.md) | 50 |
| [2018](docs/2018.md) | 51 |
| [2019](docs/2019.md) | 67 |
| [2020](docs/2020.md) | 79 |
| [2021](docs/2021.md) | 91 |
| [2022](docs/2022.md) | 86 |
| [2023](docs/2023.md) | 89 |
| [2024](docs/2024.md) | 112 |
| [2025](docs/2025.md) | 204 |
| [2026](docs/2026.md) | 187 |
<!-- YEARLY_END -->

## 数据来源

RSS 订阅列表定义在项目 `config/sources.json`。

## 目录结构

```
ai-info/
├── docs/
│   ├── 2011.md ~ 2026.md      ← 年度汇总
│   ├── YYYY/MM/               ← 按年月归档的文章（Markdown）
│   └── glossary/
│       ├── README.md              ← 术语索引
│       └── terms/                 ← 术语 .md 文件
├── README.md                    ← 项目入口（最新10篇 + 年度导航）
├── SPEC.md                      ← 格式规范
└── .git/
```

## 文章格式

每篇文章为独立 Markdown 文件（`.md`），含 JSON frontmatter（HTML 注释包裹）和纯 Markdown 正文区块。详见 [SPEC.md](SPEC.md)。

## 自动化

每天 06:00 自动运行抓取任务，结果写入 `temp/articles/`，经评分后导入 `docs/`。

## 许可证

CC BY-SA 4.0
