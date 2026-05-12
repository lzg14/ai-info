# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

## 最新 10 条
<!-- LATEST_BEGIN -->
- [OpenClaw低调更新重磅版本，龙虾长手长脚了](docs/2026/05/2026-05-12_OpenClaw低调更新重磅版本龙虾长手长脚了.md)（05-12）
- [Test Article 1 - Important](docs/2026/05/2026-05-12_Test-Article-1-Important.md)（05-12）
- [Test Article 2 - Important](docs/2026/05/2026-05-12_Test-Article-2-Important.md)（05-12）
- [估值200亿美元！可灵AI被曝剥离快手单独融资](docs/2026/05/2026-05-12_估值200亿美元可灵AI被曝剥离快手单独融资.md)（05-12）
- [“养虾人”自述：我为什么卸载龙虾？](docs/2026/05/2026-05-11_article.md)（05-11）
- [第一代机器人公司等到了IPO时刻](docs/2026/05/2026-05-11_ipo.md)（05-11）
- [具身大模型R1时刻：LIBERO终结者，99.9%背后的物理推理新范式](docs/2026/05/2026-05-11_libero.md)（05-11）
- [OpenAI砸200亿美元买单，英伟达挑战者冲刺350亿美元估值IPO](docs/2026/05/2026-05-11_openai-ipo.md)（05-11）
- [Sora的“死”与可灵的“生”](docs/2026/05/2026-05-11_sora.md)（05-11）
- [安全公司：部分使用氛围编程 Vibe Coding 开发的网络 App 缺乏身份验证机制、直接暴露于公网](docs/2026/05/2026-05-11_vibe-coding-app.md)（05-11）
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
| [2022](docs/2022.md) | 85 |
| [2023](docs/2023.md) | 88 |
| [2024](docs/2024.md) | 112 |
| [2025](docs/2025.md) | 204 |
| [2026](docs/2026.md) | 118 |
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
└── .git/
```

## 文章格式

每篇文章为独立 Markdown 文件（`.md`），含 JSON frontmatter（HTML 注释包裹）和纯 Markdown 正文区块。详见 [SPEC.md](SPEC.md)。

## 自动化

每天 06:00 自动运行抓取任务（位于 `~/.hermes/skills/ai-info/scripts/`），结果写入 `temp/articles/`，经评分后导入 `docs/`。

## 许可证

CC BY-SA 4.0
