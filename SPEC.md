# ai-info — 项目规格说明

## 概述

AI/深度学习相关资讯的静态文章库。每篇文章独立一个 Markdown 文件，纯文本存储，可直接在 GitHub/Gitea 浏览。

**主题范围：** 大模型（GPT/LLaMA/DeepSeek/Qwen/GLM 等）、Agent、算法架构、芯片算力、AI 行业事件。

---

## 目录结构

```
ai-info/
├── docs/                    ← AI资讯文章（进git）
│   ├── 2020/01/ ~ 2026/05/  ← 按年月分目录
│   └── 2026.md              ← 2026年度汇总
├── data/                    ← 持久数据（进git）
│   ├── docs_url_index.json  ← 已导入文章索引（filepath → 元信息）
│   └── seen_urls.json       ← 已抓取URL列表
├── glossary/                 ← 术语表（进git）
│   ├── README.md            ← 索引页
│   └── terms/               ← 各术语文件
├── scripts/                 ← 工具脚本（.gitignore，不进git）
├── config/
│   ├── sources.json         ← RSS 订阅源配置
│   └── config.json          ← 爬虫评分配置
├── README.md                ← 内容入口
├── SPEC.md                  ← 本规格说明
└── LICENSE
```

---

## 文件命名规则

**格式：** `YYYY-MM-DD_simple-english-title.md`

**规则：**
- 年-月-日后接下划线（`_`），然后是标题英文描述
- 标题描述用连字符（`-`）分隔单词，全小写，2-8个词
- **文件名不出现中文和特殊字符**：只用 ASCII 字母、数字、连字符（`-`）、下划线（`_`）
- 同一标题重复：加 `_2`、`_3` 序号区分

**文件名不等于文章标题。** 文章标题写在文件内部（H1），可以有中文、冒号等任何字符。

**日期来源：** 文章原始发布日期。

---

## 文件内容格式（V2 — 2026-05-09 起）

每篇文章独立一个文件，格式如下：

```markdown
---
source_name: 人人都是产品经理
source_url: https://www.woshipm.com/ai/1234567.html
publish_date: 2026-05-08
import_date: 2026-05-08T10:00:00
tags: [AI, 大模型, 产品]
---

# 文章标题

正文内容...

tags: **AI** **大模型**

## 相关文章
- [相关文章A](../05/article-a.md)
- [相关文章B](../04/article-b.md)
```

**格式说明：**

- **Frontmatter（必须）：** `source_name`（来源名）、`source_url`（原始链接）、`publish_date`（发布日期）、`import_date`（入库时间）、`tags`（数组）。Frontmatter 是唯一真实数据来源，丢失不可接受。
- **H1：** 文章完整标题，可含中文、冒号等任意字符。**标题中不得包含来源名**（在 `clean_title` 阶段已去除）。
- **正文：** 完整提取并适当精简冗余。
- **tags 行：** 正文底部单独一行，格式 `tags: **Tag1** **Tag2`（粗体，不用#前缀），最多 8 个标签。
- **来源行：** 文章标题与正文之间，**不再需要手写 `YYYY-MM-DD [来源](url)` 行**——来源信息统一存在于 frontmatter。如果需要显示来源，在 frontmatter 里读取渲染。
- **相关文章：** 由 `import_one.py` 的 `find_related_articles()` 自动生成，基于同月份目录扫描 + 标题 token 匹配。写入时追加到文章底部。

**为什么废弃"第2行手写来源"格式？**
- 历史 700+ 篇文章的该行全部缺失，根源是 RSS 解析未提取 `source_name`
- Frontmatter 存在于文件顶部，不依赖解析逻辑，是更可靠的数据载体
- 新流程：抓取 → 必须填充 frontmatter → 导入时 frontmatter 为唯一真实数据源

---

## 链接路径规范（CRITICAL）

**三个文件的上下文不同，链接格式也不同：**

| 文件 | 位置 | 文章链接格式 | 示例 |
|------|------|-------------|------|
| README.md | 根目录 `/` | `docs/YYYY/MM/file.md` | `docs/2026/03/article.md` |
| docs/YYYY.md | `docs/` 目录下 | `../YYYY/MM/file.md` | `../2026/03/article.md` |
| docs/YYYY/MM/X.md | `docs/YYYY/MM/` 下 | `../MM/article.md` | `../05/article.md` |

**glossary 链接（从任意文章出发）：** `../../../glossary/terms/xxx.md`

**相关文章链接（从 `docs/YYYY/MM/X.md` 出发）：** `../MM/related.md`

**验证方法：** 从文件所在目录用相对路径能否找到链接目标。

---

## RSS 订阅源

已验证可用的 RSS 源（配置在 `config/sources.json`）：

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
- 精选表：⭐8.0+ 文章，按评分降序
- 完整列表：按月份分组，每月内按日期倒序
- **注意路径格式：** 用 `../YYYY/MM/file.md`（不是 `docs/YYYY/MM/file.md`）

#### 2. README.md
- **最新10条**：该年最新10篇，按日期倒序
- **该年精选**：评分≥8.0，最多15篇
- **内容总览表格**：篇数变化时更新

#### 3. 相关文章（各文章底部的 `## 相关文章`）
- 由 `import_one.py` 的 `find_related_articles()` 自动生成
- 导入新文章时自动追加到同月已有文章底部

### 同步检查清单

- [ ] docs/YYYY.md 已更新，链接路径正确
- [ ] README.md 最新10条已更新
- [ ] README.md 精选已更新
- [ ] README.md 内容总览表格篇数已更新

---

## 附录

- 适用版本：2026-05-09 起（V2 格式，强制 frontmatter）
- 旧格式迁移：历史文章暂不强制迁移，待下次人工审核时补全 frontmatter
