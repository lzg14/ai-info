# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

## 最新 10 条

- [空间智能的"具身化"跃迁，高德ABot体系模型夺冠AGIBot全球挑战赛](docs/2026/05/2026-05-09_abot-agibot.md)（05-09）
- [奥特曼"官宣" OpenAI 手机](docs/2026/05/2026-05-09_openai.md)（05-09）
- [豆包收费辩证透视：免费的，为何才是最贵的？](docs/2026/05/2026-05-08_ai-news_3.md)（05-08）
- [Nanoleaf bets its future on robots, red light therapy, and AI](docs/2026/05/2026-05-08_nanoleaf-bets-its-future-robots.md)（05-08）
- [Cursor 3发布多Agent并行重新定义编程工具天花板](docs/2026/05/2026-05-05-cursor3-multi-agent-coding.md)（05-05）
- [OpenAI DeployCo：100亿美元估值，锁定2000+企业的AI合资公司](docs/2026/05/2026-05-04-OpenAI-DeployCo合资公司百亿美元估值锁定两千企业.md)（05-04）
- [天桥具身机器人亮相济南泺口服装城会推销能T台走秀](docs/2026/05/2026-05-04-tianqiao-robot-fashion-show.md)（05-04）
- [DeepSeek-V4系列密集落地V4-Pro开源V4-Flash仅0.279美元](docs/2026/05/2026-05-02-deepseek-v4-pro-open-source.md)（05-02）
- [Claude Code is leaking API keys into public package registries](docs/2026/04/2026-04-27_claude-code-leaking-api-keys.md)（04-27）
- [DeepSeek V4 发布：百万 token 上下文标配，昇腾适配](docs/2026/04/2026-04-25-deepseek-v4-million-token.md)（04-25）

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
