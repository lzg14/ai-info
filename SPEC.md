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
│   ├── docs_url_index.json  ← 已导入URL索引（append-only）
│   └── seen_urls.json       ← 已抓取URL列表
├── glossary/                 ← 术语表（进git）
│   ├── README.md            ← 索引页
│   └── terms/               ← 各术语文件
├── scripts/                 ← 工具脚本（.gitignore，不进git）
├── config/
│   ├── sources.json         ← RSS 订阅源配置
│   └── config.json          ← 爬虫评分配置
├── README.md                ← 内容入口（最新10条 + 精选 + 总览）
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

**日期来源：** 文章原始发布日期。文章无发布日期的，使用文件创建日期。

---

## 文件内容格式

每篇文章独立一个文件，格式如下：

```markdown
# 文章标题
YYYY-MM-DD [来源名](url)

⭐ 8.8

正文...

tags: **AI** **大模型**

## 相关文章
- [文章标题A](2026/05/article-a.md)
- [文章标题B](2026/04/article-b.md)
```

**格式说明：**
- **H1**：文章标题，可含中文、冒号等任意字符。**标题中不得包含来源名**
- **标题下第一行**：`YYYY-MM-DD [来源名](url)`，来源为可点击链接，**无"来源："前缀**
- **评分行**：`⭐ score`，单独一行；只出现在重要文章里，非重要文章无评分行
- **正文**：完整提取并适当精简冗余
- **tags 行**：正文底部单独一行，格式 `tags: **Tag1** **Tag2`（粗体，不用#前缀），最多 8 个标签
- **相关文章**：tags 后空一行，加 `## 相关文章` 区块，列出同月最近 5 篇文章
- **无 frontmatter**：不需要 `---` 元数据块
- **无 emoji 分类**：不放 emoji 标签

**标题提取优先级：** 优先用正文中 H3（`### 完整标题`），不用 frontmatter 的 title——frontmatter 常被截断。

---

## 链接路径规范（CRITICAL — 容易混用）

**三个文件的上下文不同，链接格式也不同：**

| 文件 | 位置 | 文章链接格式 | 示例 |
|------|------|-------------|------|
| README.md | 根目录 `/` | `docs/YYYY/MM/file.md` | `docs/2026/03/article.md` |
| docs/YYYY.md | `docs/` 目录下 | `../YYYY/MM/file.md` | `../2026/03/article.md` |
| docs/YYYY/MM/file.md | `docs/YYYY/MM/` 下 | `file.md`（同目录直接写） | `article.md` |

**容易犯的错误：** 在 docs/YYYY.md 里错误使用 `docs/YYYY/MM/file.md`（会变成 `docs/docs/YYYY/...`）。

**验证方法：** 从文件所在目录用相对路径能否找到链接目标。

**glossary 链接（从任意文章出发）：** `../../../glossary/terms/xxx.md`（三层回溯）

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

## 自动流水线（Cron）

### 调度时间

每天 **06:00 和 18:00** 两次（cron 表达式：`0 6,18 * * *`）。

### 流程

```
crawler_new.py → scorer_new.py → import_one.py → update_readme.py
```

1. **crawler_new.py**：从 `config/sources.json` 抓取 RSS，输出 JSON 到 `temp/pending/`
2. **scorer_new.py**：AI 评分，达标文章移入 `temp/important/`，按 `ai_max_articles_per_day` 限额
3. **import_one.py**：将 `temp/important/` 里的文章导入 `docs/YYYY/MM/`，做去重判断
4. **update_readme.py**：更新 README.md 最新10条和精选区

### 关键配置（config/config.json）

```json
{
  "crawl": {
    "ai_score_threshold": 7.0,
    "ai_max_articles_per_day": 10
  }
}
```

### 阈值与质量规则

**精选门槛（scorer 硬性低分规则）：**
- 正文 <150 字符 → 最高 3 分
- 仅有标题无正文 → 最高 2 分
- 仅有参数/bullet 列表无分析 → 最高 3 分
- 纯新闻快讯无深度分析 → 最高 4 分

**内容实质性标准（人工判断）：** ≥300 中文字 OR ≥30行，且有分析内容。

---

## 文章同步维护规范

### 触发条件

对 `docs/` 下的文章做任何变更后（包括新增、删除、重命名），必须执行同步检查。

### 同步范围

#### 1. 年度汇总（docs/YYYY.md）
- 精选表：⭐8.0+ 文章，按评分降序
- 完整列表：按月份分组，每月内按日期倒序
- 文件名/路径变化时同步更新链接路径

#### 2. README.md
- **最新10条**：该年最新10篇，按日期倒序
- **该年精选**：评分≥8.0，最多15篇
- **内容总览表格**：篇数变化时更新

#### 3. 相关文章（各文章底部的 `## 相关文章`）
- 由 `add_related_articles.py` 管理
- 文件名变化后需重新运行

### 同步检查清单

- [ ] docs/YYYY.md 已更新，链接路径正确（注意：`../YYYY/MM/` 而非 `docs/YYYY/MM/`）
- [ ] README.md 最新10条已更新
- [ ] README.md 精选已更新
- [ ] README.md 内容总览表格篇数已更新
- [ ] 如有文件名变化，已重新运行 `add_related_articles.py`

---

## 附录

- 适用版本：2026-05-08 起
- scripts/ 目录在 .gitignore 中，不随 git 提交
- temp/ 目录为临时数据，不随 git 提交
