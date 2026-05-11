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
└── .git/
```

**注：** `scripts/`、`config/` 不在 ai-info 仓库内，已迁移至 `~/.hermes/skills/ai-info/` 下的对应子目录。Cron 任务调用脚本时路径相应调整。

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

## 文件内容格式（V4 — 2026-05-11 起，Markdown 格式）

每篇文章一个 `.md` 文件，frontmatter 用 HTML 注释包裹 JSON，视觉区用纯 Markdown 元信息栏。

**为什么从 HTML 切回 Markdown？**

HTML 解决了 MD 的格式约定冲突问题，但也带来了新问题：需要额外的转换步骤、GitHub Pages 国内访问慢、不利于直接阅读原始文件。V4 找到两全方案——用 HTML 注释包住 JSON frontmatter，既避开了 Markdown 与 YAML frontmatter 的分隔符冲突（`---` 是 MD 水平线语法），又保留了结构化数据便于程序解析，同时文件本身是干净的 Markdown，可直接阅读。

**文件类型（3种）：**

| 类型 | 文件 | frontmatter | 区块标记 |
|------|------|-------------|---------|
| 正式文章 | `docs/YYYY/MM/file.md` | ✅ | ✅ 正文 + ✅ 相关文章 |
| 年度汇总 | `docs/YYYY.md` | ❌ | ❌ |
| 术语文件 | `docs/glossary/terms/file.md` | ❌ | ❌ |

**正式文章 MD Schema：**

```markdown
<!--
{
  "title": "文章标题",
  "date": "2026-05-02",
  "source": "量子位",
  "source_url": "https://www.qbitai.com/...",
  "score": "精选",
  "tags": ["AI", "大模型"]
}
-->

# 文章标题

📅 2026-05-02 | 📎 量子位

<!-- 正文开始 -->
正文内容，Markdown 格式
<!-- 正文结束 -->

<!-- tags: AI, 大模型 -->

## 相关文章
<!-- 相关文章开始 -->
- [相关文章标题](./2026-05-01-related.md)
<!-- 相关文章结束 -->
```

**frontmatter 字段说明：**

| 字段 | 必填 | 说明 |
|------|------|------|
| `title` | ✅ | 文章标题 |
| `date` | ✅ | 原始发布日期 YYYY-MM-DD |
| `source` | 部分 | 来源名称，无则不写 |
| `source_url` | 部分 | 来源 URL，无则不写 |
| `score` | 否 | "精选"（仅精选文章有） |
| `tags` | 否 | 标签列表，无则不写 |

**格式规则：**
- `<!-- 正文开始 -->` / `<!-- 正文结束 -->`：必有，标记正文边界
- 视觉元信息栏：必写，字段从 frontmatter 复制显示，无则省略
- `<!-- tags: ... -->`：仅文章本身有 tags 时才写，不空占
- `<!-- 相关文章开始 -->` / `<!-- 相关文章结束 -->`：仅当有相关文章时写
- `<!-- -->` 与 `<!-- tags: ... -->` 是不同注释格式，前者是 frontmatter JSON 块，后者是单行注释

**转换工具：**
- `~/.hermes/skills/ai-info/scripts/html2md.py`：HTML → MD（单文件，2026-05-11 已完成全部文章转换）

---

## 链接路径规范（CRITICAL）

**三个文件的上下文不同，链接格式也不同：**

| 文件 | 文章链接格式 | 示例 |
|------|-------------|------|
| README.md（项目根目录） | `docs/YYYY/MM/file.md` | `docs/2026/03/article.md` |
| docs/YYYY.md（`docs/` 下） | `YYYY/MM/file.md` | `2026/03/article.md` |
| docs/YYYY/MM/file.md（`docs/YYYY/MM/` 下） | `file.md`（同月）或 `../MM/file.md`（跨月）或 `../../YYYY/MM/file.md`（跨年） | `article.md` |

**glossary 链接（从任意文章出发）：** `../../../glossary/terms/xxx.md`

**验证方法：** 从文件所在目录用相对路径能否找到链接目标。所有站内链接已验证无死链（2026-05-11）。

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

## 文章同步维护规范

### 同步范围

#### 1. 年度汇总（docs/YYYY.md）
- 完整列表：按月份分组，每月内按日期倒序

#### 2. README.md
- **最新10条**：全部文章按日期倒序，取前10篇

#### 3. 相关文章（各文章底部的 `## 相关文章`）
- 由 `import_one.py` 的 `find_related_articles()` 自动生成
- 导入新文章时自动追加到同月已有文章底部

### 同步检查清单

- [ ] docs/YYYY.md 已更新，链接路径正确
- [ ] README.md 最新10条已更新

---

## 附录

- 适用版本：2026-05-11 起（V4 格式，Markdown + JSON frontmatter in HTML 注释）
- HTML→MD 转换：2026-05-11 完成全部文章转换，assets/ 目录、HTML 脚本已删除
- 站内链接检查：2026-05-11 完成全面扫描，0 个死链
