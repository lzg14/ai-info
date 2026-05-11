# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

## 最新 10 条

- [“养虾人”自述：我为什么卸载龙虾？](docs/2026/05/2026-05-11_article.md)（05-11）
- [数学专业，危！菲尔兹奖得主亲测ChatGPT 5.5 Pro，17分钟出论文级成果](docs/2026/05/2026-05-11_chatgpt-pro.md)（05-11）
- [数学专业，危！菲尔兹奖得主亲测ChatGPT 5.5 Pro，17分钟出论文级成果](docs/2026/05/2026-05-11_chatgpt-pro_2.md)（05-11）
- [第一代机器人公司等到了IPO时刻](docs/2026/05/2026-05-11_ipo.md)（05-11）
- [具身大模型R1时刻：LIBERO终结者，99.9%背后的物理推理新范式](docs/2026/05/2026-05-11_libero.md)（05-11）
- [具身大模型R1时刻：LIBERO终结者，99.9%背后的物理推理新范式](docs/2026/05/2026-05-11_libero_2.md)（05-11）
- [OpenAI砸200亿美元买单，英伟达挑战者冲刺350亿美元估值IPO](docs/2026/05/2026-05-11_openai-ipo.md)（05-11）
- [OpenAI砸200亿美元买单，英伟达挑战者冲刺350亿美元估值IPO](docs/2026/05/2026-05-11_openai-ipo_2.md)（05-11）
- [Sora的“死”与可灵的“生”](docs/2026/05/2026-05-11_sora.md)（05-11）
- [安全公司：部分使用氛围编程 Vibe Coding 开发的网络 App 缺乏身份验证机制、直接暴露于公网](docs/2026/05/2026-05-11_vibe-coding-app.md)（05-11）

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

每天 06:00 自动运行抓取任务（位于 `~/.hermes/skills/ai-info/scripts/`），结果写入 `staging/`，然后导入 `docs/`。

## 许可证

CC BY-SA 4.0
