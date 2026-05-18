# AI Daily — 每日资讯

每天自动收集 AI / LLM / Agent / MCP / Skills 有价值的资讯。

## 最新 10 条
<!-- LATEST_BEGIN -->
- [Anthropic CEO预言软件免费化与职业结构巨变](docs/2026/05/2026-05-18_anthropic-ceo预言软件免费化与职业结构巨变.md)（05-18）
- [Anthropic Claude 5天攻破Apple M5 macOS内核漏洞：5年数十亿防线，被AI一举击穿](docs/2026/05/2026-05-18_anthropic-claude-5天攻破apple-m5-macos内核漏洞5年数十亿防线被ai一举击穿.md)（05-18）
- [Garry Tan发布的GBrain直接捅破个人AI天花板](docs/2026/05/2026-05-18_garry-tan发布的gbrain直接捅破个人ai天花板.md)（05-18）
- [Grok Imagine图像生成功能正式发布](docs/2026/05/2026-05-18_grok-imagine图像生成功能正式发布.md)（05-18）
- [Hermes 可配置的国内外 AI 模型及使用方法](docs/2026/05/2026-05-18_hermes-可配置的国内外-ai-模型及使用方法.md)（05-18）
- [Zerostack——一款采用纯Rust语言编写、受Unix启发的编程代理](docs/2026/05/2026-05-18_zerostack一款采用纯rust语言编写受unix启发的编程代理.md)（05-18）
- [人机快递分拣对决直播](docs/2026/05/2026-05-18_人机快递分拣对决直播.md)（05-18）
- [开源工具揭露AI API中转站安全风险与检测差异](docs/2026/05/2026-05-18_开源工具揭露ai-api中转站安全风险与检测差异.md)（05-18）
- [开源微信读书数据可视化工具yao-weread-skill发布](docs/2026/05/2026-05-18_开源微信读书数据可视化工具yao-weread-skill发布.md)（05-18）
- [微信读书Skill安装与使用指南](docs/2026/05/2026-05-18_微信读书skill安装与使用指南.md)（05-18）
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
| [2026](docs/2026.md) | 157 |
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
