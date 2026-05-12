# ai-info — 项目规格说明

## 概述

AI/深度学习相关资讯的静态文章库。每篇文章独立一个 Markdown 文件（`.md`），可直接在 GitHub 或本地阅读。

**主题范围：** 大模型（GPT/LLaMA/DeepSeek/Qwen/GLM 等）、Agent、算法架构、芯片算力、AI 行业事件。

---

## 目录结构

```
ai-info/
├── docs/
│   ├── 2011.md ~ 2026.md      ← 年度汇总（Markdown）
│   ├── YYYY/MM/               ← 按年月归档的文章（Markdown）
│   └── glossary/
│       ├── README.md              ← 术语索引
│       └── terms/                 ← 各术语 .md 文件
├── README.md                   ← 项目入口（最新10篇 + 年度导航）
├── SPEC.md                     ← 本规格说明
├── data/
│   └── state.db                ← SQLite 状态数据库（唯一信号源）
├── temp/
│   └── articles/               ← 文章原始 JSON（固定路径，永不移删）
│       └── {hash}.json
├── scripts/                    ← 爬虫脚本（不在仓库，符号链接到 ~/.hermes/skills/ai-info/scripts/）
├── config/                     ← 配置（不在仓库）
│   ├── config.json
│   └── sources.json
└── .git/
```

**注：** `scripts/`、`config/` 已迁移至 `~/.hermes/skills/ai-info/` 下，不在 ai-info 仓库内。Cron 任务调用时使用符号链接。

---

## 文件命名规则

**格式：** `YYYY-MM-DD_simple-english-title.md`

**规则：**
- 年-月-日后接下划线（`_`），然后是标题英文描述
- 标题描述用连字符（`-`）分隔单词，全小写，2-8个词
- **文件名不出现中文和特殊字符**：只用 ASCII 字母、数字、连字符（`-`）、下划线（`_`）
- 同一标题重复：加 `_2`、`_3` 序号区分

**文件名不等于文章标题。** 文章标题写在文件内部（`#`），可以有中文、冒号等任何字符。

**日期来源：** 文章原始发布日期。

---

## 数据流架构（V5 — 2026-05 起）

```
RSS/HTML Feed
    ↓ [crawler_new.py]
temp/articles/{hash}.json  +  data/state.db (status=pending)
    ↓ [scorer_new.py]
data/state.db (status=scored, score=1-10)
    ↓ [import_one.py]
docs/YYYY/MM/YYYY-MM-DD_slug.md  +  data/state.db (status=done)
    ↓ (自动)
update_year_summary.py → docs/YYYY.md
update_readme.py → README.md
```

**文件永存：** 文章内容 JSON 只写一份在 `temp/articles/`，爬虫、评分器、导入器都从固定路径读写，永不移动或删除。

**DB 是唯一信号源：** 所有状态（pending/scored/done）以 DB 为准。

---

## 文章格式（V4 — Markdown + JSON frontmatter）

每篇文章一个 `.md` 文件，frontmatter 用 HTML 注释包裹 JSON，视觉区用纯 Markdown 元信息栏。

**为什么用 HTML 注释包 JSON frontmatter？**

`---` 在 Markdown 中是水平线语法，会与 frontmatter 分隔符冲突。HTML 注释 `<!-- ... -->` 不会触发 Markdown 解析问题，同时保留结构化数据便于程序解析，文件本身是干净的 Markdown。

**文件类型（3种）：**

| 类型 | 文件 | frontmatter | 区块标记 |
|------|------|-------------|---------|
| 正式文章 | `docs/YYYY/MM/file.md` | ✅ | ✅ 正文 |
| 年度汇总 | `docs/YYYY.md` | ❌ | ❌ |
| 术语文件 | `docs/glossary/terms/file.md` | ❌ | ❌ |

**正式文章 MD Schema（import_one.py 生成格式）：**

```markdown
<!-- {"title": "文章标题", "title_zh": "中文标题", "url": "https://...", "source": "来源名称", "source_url": "https://...", "publish_date": "2026-05-02", "score": 9, "tags": ["AI", "大模型"]} -->

# 文章标题

📅 2026-05-02
📢 来源：[来源名称](https://来源url)

> 摘要内容（如果有且与正文不重复）

🏷️ AI · 大模型

<!-- 正文开始 -->

正文内容，Markdown 格式

<!-- 正文结束 -->
```

**frontmatter 字段说明：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| `title` | ✅ | string | 文章标题 |
| `title_zh` | 否 | string | 中文标题（无则空字符串） |
| `url` | ✅ | string | 文章原始 URL |
| `source` | 否 | string | 来源名称（如 "量子位"），无则空 |
| `source_url` | 否 | string | 来源首页 URL，无则空 |
| `publish_date` | ✅ | string | 原始发布日期 YYYY-MM-DD |
| `score` | 否 | integer | LLM 评分 1-10，导入后写入 |
| `tags` | 否 | array | 标签列表，无则空数组 |

**格式规则：**
- `<!-- 正文开始 -->` / `<!-- 正文结束 -->`：必有，标记正文边界
- 视觉元信息栏：必写，字段从 frontmatter 复制显示
- `📅 日期` 必写，`📢 来源` 在有 source 时写（无 source/source_url 则省略整行）
- `🏷️ tag1 · tag2`：仅在 tags 非空数组时写，用 `·` 分隔
- `> 摘要`：仅在 summary 存在且与正文开头不重复时写
- score 字段在导入后由 import_one.py 写入 frontmatter（此前为 null）

---

## 链接路径规范（CRITICAL）

**三个文件的上下文不同，链接格式也不同：**

| 文件 | 文章链接格式 | 示例 |
|------|-------------|------|
| README.md（项目根目录） | `docs/YYYY/MM/file.md` | `docs/2026/03/article.md` |
| docs/YYYY.md（`docs/` 下） | `YYYY/MM/file.md` | `2026/03/article.md` |
| docs/YYYY/MM/file.md（`docs/YYYY/MM/` 下） | `file.md`（同月）或 `../MM/file.md`（跨月）或 `../../YYYY/MM/file.md`（跨年） | `article.md` |

**glossary 链接（从任意文章出发）：** `../../../glossary/terms/xxx.md`

**验证方法：** 从文件所在目录用相对路径能否找到链接目标。

---

## 订阅源配置

RSS 订阅源配置在 `~/.hermes/skills/ai-info/config/sources.json`（已迁移，不在 ai-info 仓库内）。

已验证可用的 RSS 源：

| 源名 | 说明 |
|------|------|
| nvidia-blog | NVIDIA 官方博客 |
| bd-techtalks | BD Tech Talks |
| hnrss/hacker-news | Hacker News |
| techcrunch | TechCrunch |
| thedatainfo | The Data Info |
| anthropic-blog | Anthropic 官方博客（CSS 选择器覆盖 /news） |

**已确认不可用（被墙/无RSS）：** The Batch、Import AI、DEV Community、Microsoft AI Blog、Meta AI、Product Hunt、InfoQ、AI前线、The Gradient。

---

## 自动化流水线

### 每日 06:00 自动运行

```
crawler_new.py  →  抓取所有 RSS/HTML 源，写入 temp/articles/ + DB(pending)
        ↓
scorer_new.py   →  从 DB 读 pending，评分，写 DB(scored)
        ↓
import_one.py  →  从 DB 读 scored(≥8)，导入 docs/，写 DB(done)
        ↓
update_year_summary.py  →  重建 docs/YYYY.md
update_readme.py        →  更新 README.md 最新10条
```

### 脚本说明

| 脚本 | 功能 |
|------|------|
| `crawler_new.py` | 扫 RSS/HTML 源，抓文章写 temp/articles/，mark(pending) |
| `scorer_new.py` | 读 DB(pending)，LLM 评分，mark(scored, score=N) |
| `import_one.py` | 读 DB(scored≥8)，写 docs/，mark(done)，自动调 update_* |
| `state_manager.py` | SQLite 状态管理：pending/scored/done，file 字段存 JSON 路径 |
| `update_year_summary.py` | 重建 docs/YYYY.md（按月分组，评分标记精品） |
| `update_readme.py` | 更新 README.md 最新10条和年度导航 |
| `review_import.py` | 审查最近导入文章的质量（frontmatter 完整性等） |

---

## 文章同步维护规范

### 同步范围

#### 1. 年度汇总（docs/YYYY.md）
- 完整列表：按月份分组，每月内按日期倒序
- 精品标记：评分 ≥7.0 的文章单独列出

#### 2. README.md
- **最新10条**：全部文章按日期倒序，取前10篇
- **年度导航**：所有有文章的年份 + 文章数

#### 3. 自动同步
- `import_one.py` 导入完成后自动调用 `update_year_summary.py` 和 `update_readme.py`
- 无需手动干预

### 同步检查清单

- [ ] docs/YYYY.md 已更新，链接路径正确
- [ ] README.md 最新10条已更新

---

## 附录

- 适用版本：2026-05-12 起（V5 架构：文件永存 + SQLite 信号源）
- 新架构：temp/articles/ 固定路径，data/state.db 唯一信号源
- 站内链接检查：2026-05-11 完成全面扫描，0 个死链
