# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

## 最新 10 条
<!-- LATEST_BEGIN -->
- [90%的人在白白浪费“Token”！](docs/2026/05/2026-05-15_90的人在白白浪费token.md)（05-15）
- [AI取代人类？各方叙事背后的利益驱动](docs/2026/05/2026-05-15_ai取代人类各方叙事背后的利益驱动.md)（05-15）
- [AI工具批量生成知识产权申请材料引关注](docs/2026/05/2026-05-15_ai工具批量生成知识产权申请材料引关注.md)（05-15）
- [AI角色实现记忆共情与主动交互](docs/2026/05/2026-05-15_ai角色实现记忆共情与主动交互.md)（05-15）
- [Anthropic与盖茨基金会达成2亿美元合作，聚焦全球健康与教育](docs/2026/05/2026-05-15_anthropic与盖茨基金会达成2亿美元合作聚焦全球健康与教育.md)（05-15）
- [Anthropic估值五日激增2000亿美元，营收呈指数级增长](docs/2026/05/2026-05-15_anthropic估值五日激增2000亿美元营收呈指数级增长.md)（05-15）
- [Anthropic在AWS上正式推出Claude平台](docs/2026/05/2026-05-15_anthropic在aws上正式推出claude平台.md)（05-15）
- [Anthropic开源金融AI全栈模板，定义行业落地新标准](docs/2026/05/2026-05-15_anthropic开源金融ai全栈模板定义行业落地新标准.md)（05-15）
- [Anthropic推出面向小型企业的Claude服务包](docs/2026/05/2026-05-15_anthropic推出面向小型企业的claude服务包.md)（05-15）
- [Bugbot团队与个人计划更新](docs/2026/05/2026-05-15_bugbot团队与个人计划更新.md)（05-15）
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
| [2026](docs/2026.md) | 304 |
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
