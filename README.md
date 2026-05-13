# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

## 最新 10 条
<!-- LATEST_BEGIN -->
- [OpenAI DeployCo：100亿美元估值，锁定2000+企业的AI合资公司](docs/2026/05/2026-05-04-openai-deployco-100b-valuation-2000-enterprise.md)（05-04）
- [Influential study touting ChatGPT in education retracted over red flags](docs/2026/05/2026-05-04_Influential-study-touting-ChatGPT-in-education-retracted-over-red-flags.md)（05-04）
- [DeepSeek-V4系列密集落地V4-Pro开源V4-Flash仅0.279美元](docs/2026/05/2026-05-02-deepseek-v4-pro-open-source.md)（05-02）
- [Reasoning emerges from constrained inference manifolds in large language models](docs/2026/05/2026-05-02_reasoning-emerges-from-constrained-inference-manifolds-in-la.md)（05-02）
- [Amid Mythos' hyped cybersecurity prowess, researchers find GPT-5.5 is just as good](docs/2026/05/2026-05-01_Amid-Mythos-hyped-cybersecurity-prowess-researchers-find-GPT-55-is-just-as-good.md)（05-01）
- [Minnesota passes ban on fake AI nudes; app makers risk $500K fines](docs/2026/05/2026-05-01_Minnesota-passes-ban-on-fake-AI-nudes-app-makers-risk-500K-fines.md)（05-01）
- [Study: AI models that consider users' feelings are more likely to make errors](docs/2026/05/2026-05-01_Study-AI-models-that-consider-users-feelings-are-more-likely-to-make-errors.md)（05-01）
- [Dendritic Neural Networks with Equilibrium Propagation](docs/2026/05/2026-05-01_dendritic-neural-networks-with-equilibrium-propagation.md)（05-01）
- [Towards Customized Multimodal Role-Play](docs/2026/05/2026-05-01_towards-customized-multimodal-role-play.md)（05-01）
- [VLADriver-RAG: Retrieval-Augmented Vision-Language-Action Models for Autonomous Driving](docs/2026/05/2026-05-01_vladriver-rag-retrieval-augmented-vision-language-action-mod.md)（05-01）
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
| [2021](docs/2021.md) | 90 |
| [2022](docs/2022.md) | 86 |
| [2023](docs/2023.md) | 88 |
| [2024](docs/2024.md) | 112 |
| [2025](docs/2025.md) | 204 |
| [2026](docs/2026.md) | 147 |
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
