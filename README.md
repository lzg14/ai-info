# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

## 最新 10 条
<!-- LATEST_BEGIN -->
- [Codex自我蒸馏玩法火了！OpenAI员工亲授：复制粘贴就能让AI消灭重复劳动](docs/2026/05/2026-05-27_codex自我蒸馏玩法火了openai员工亲授复制粘贴就能让ai消灭重复劳动.md)（05-27）
- [DeepSeek陈德里开发自动研究Skill，写一篇论文人类只动脑2小时](docs/2026/05/2026-05-27_deepseek陈德里开发自动研究skill写一篇论文人类只动脑2小时.md)（05-27）
- [Nvidia bets $150B on Taiwan as Trump's plan to make US an AI hub backfires](docs/2026/05/2026-05-27_nvidia-bets-150b-on-taiwan-as-trumps-plan-to-make-us-an-ai-h.md)（05-27）
- [US law enforcement warns of "anti-tech extremism" as AI hatred grows](docs/2026/05/2026-05-27_us-law-enforcement-warns-of-anti-tech-extremism-as-ai-hatred.md)（05-27）
- [屏忆：这款开源工具，把过目就忘的日常变成「上下文」 - 少数派](docs/2026/05/2026-05-27_屏忆这款开源工具把过目就忘的日常变成上下文-少数派.md)（05-27）
- [客制化键盘｜近期值得一看的套件与键帽：怪诞主题、复古创新与静电容 - 少数派](docs/2026/05/2026-05-26_客制化键盘近期值得一看的套件与键帽怪诞主题复古创新与静电容-少数派.md)（05-26）
- [将DSA注意力引入多模态，快手Keye2.0开启强化推理新范式](docs/2026/05/2026-05-26_将dsa注意力引入多模态快手keye20开启强化推理新范式.md)（05-26）
- [派早报：法拉利发布首款纯电跑车 Luce、森海塞尔发布 Momentum 5 耳机等 - 少数派](docs/2026/05/2026-05-26_派早报法拉利发布首款纯电跑车-luce森海塞尔发布-momentum-5-耳机等-少数派.md)（05-26）
- [AI 热潮引发民怨：七成美国民众反对家门口建数据中心](docs/2026/05/2026-05-24_ai-热潮引发民怨七成美国民众反对家门口建数据中心.md)（05-24）
- [AI工具批量生成知识产权申请材料引关注](docs/2026/05/2026-05-24_ai工具批量生成知识产权申请材料引关注.md)（05-24）
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
| [2026](docs/2026.md) | 399 |
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
