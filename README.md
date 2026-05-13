# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

## 最新 10 条
<!-- LATEST_BEGIN -->
- [何恺明首个语言模型：105M参数，不走GPT自回归老路](docs/2026/05/2026-05-13_何恺明首个语言模型105m参数不走gpt自回归老路.md)（05-13）
- [360发布OpenClaw生态安全报告：AI智能体风险进入自动化审计阶段](docs/2026/05/2026-05-12_360发布openclaw生态安全报告ai智能体风险进入自动化审计阶段.md)（05-12）
- [OpenClaw低调更新重磅版本，龙虾长手长脚了](docs/2026/05/2026-05-12_OpenClaw低调更新重磅版本龙虾长手长脚了.md)（05-12）
- [Test Article 1 - Important](docs/2026/05/2026-05-12_Test-Article-1-Important.md)（05-12）
- [Test Article 2 - Important](docs/2026/05/2026-05-12_Test-Article-2-Important.md)（05-12）
- [AI第一金主黄仁勋：日均花掉20亿](docs/2026/05/2026-05-12_ai第一金主黄仁勋日均花掉20亿.md)（05-12）
- [Markdown要凉…卡帕西也站HTML了](docs/2026/05/2026-05-12_markdown要凉卡帕西也站html了.md)（05-12）
- [估值200亿美元！可灵AI被曝剥离快手单独融资](docs/2026/05/2026-05-12_估值200亿美元可灵AI被曝剥离快手单独融资.md)（05-12）
- [商汤善惠烧卖购机器人小店上海“开业”，让机器人真正落地线下零售](docs/2026/05/2026-05-12_商汤善惠烧卖购机器人小店上海开业让机器人真正落地线下零售.md)（05-12）
- [龙虾退烧后，荣耀给它造了一个宇宙](docs/2026/05/2026-05-12_龙虾退烧后荣耀给它造了一个宇宙.md)（05-12）
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
| [2026](docs/2026.md) | 149 |
<!-- YEARLY_END -->

## 数据来源

RSS 订阅列表定义在 `~/.hermes/skills/ai-info/config/sources.json`。

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
├── skills/                      ← 项目规范文档（git 管理）
│   └── ai-info-article-format.md  ← 文章格式规范
└── .git/
```

## 文章格式

每篇文章为独立 Markdown 文件（`.md`），含 JSON frontmatter（HTML 注释包裹）和纯 Markdown 正文区块。详见 [SPEC.md](SPEC.md)。

## 自动化

每天 06:00 自动运行抓取任务（位于 `~/.hermes/skills/ai-info/scripts/`），结果写入 `temp/articles/`，经评分后导入 `docs/`。

## 许可证

CC BY-SA 4.0
