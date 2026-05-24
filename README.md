# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

## 最新 10 条
<!-- LATEST_BEGIN -->
- [PwC deploying Claude 构建 technology, execute deals, reinvent 企业 functions clients](docs/2026/05/2026-05-15_pwc-is-deploying-claude-to-build-technology-execute-deals-an.md)（05-15）
- [How Much Do Circuits Tell Us? Measuring Consistency 与 Specificity Language 模型 Circuits](docs/2026/05/2026-05-08_how-much-do-circuits-tell-us-measuring-the-consistency-and-s.md)（05-08）
- [Playing games 集成 knowledge: AI-Induced delusions need game theoretic interventions](docs/2026/05/2026-05-08_playing-games-with-knowledge-ai-induced-delusions-need-game-.md)（05-08）
- [Revisiting syntax imperatives 在 Yemeni Arabic: Agree across phases approach 中的应用](docs/2026/05/2026-05-08_revisiting-the-syntax-of-imperatives-in-yemeni-arabic-an-agr.md)（05-08）
- [Humanoid robots start sorting luggage 在 Tokyo airport test amid labor shortage 中的应用](docs/2026/04/2026-04-28_Humanoid-robots-start-sorting-luggage-in-Tokyo-airport-test-amid-labor-shortage.md)（04-28）
- [TTCD:Transformer Integrated Temporal Causal Discovery 用 Non-Stationary Time Series 数据](docs/2026/04/2026-04-27_ttcdtransformer-integrated-temporal-causal-discovery-from-no.md)（04-27）
- [creator Claude Code just revealed his workflow, 与 developers losing their minds](docs/2026/01/2026-01-05_claude-code-creator-workflow.md)（01-05）
- [DeepMind's AlphaFold 2 Solves 50-Year-Old Protein Folding Problem: Revolutionary AI 突破](docs/2020/11/2020-11-30-deepmind-alphafold2-protein-folding-breakthrough.md)（11-30）
<!-- LATEST_END -->

## 年度导航

<!-- YEARLY_BEGIN -->
| 年份 | 文章数 |
|------|--------|
| 2011 | — |
| [2012](docs/2012.md) | 28 |
| [2013](docs/2013.md) | 26 |
| [2014](docs/2014.md) | 37 |
| [2015](docs/2015.md) | 29 |
| [2016](docs/2016.md) | 28 |
| [2017](docs/2017.md) | 39 |
| [2018](docs/2018.md) | 40 |
| [2019](docs/2019.md) | 33 |
| [2020](docs/2020.md) | 50 |
| [2021](docs/2021.md) | 67 |
| [2022](docs/2022.md) | 41 |
| [2023](docs/2023.md) | 25 |
| [2024](docs/2024.md) | 41 |
| [2025](docs/2025.md) | 30 |
| [2026](docs/2026.md) | 155 |
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
