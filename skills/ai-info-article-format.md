---
name: ai-info-article-format
description: ai-info 项目文章格式规范——正式文章 MD 结构、frontmatter 字段、解析规则、相关脚本
---

# ai-info 文章格式规范

## 文件类型

| 类型 | 路径 | frontmatter | 区块标记 |
|------|------|-------------|---------|
| README | README.md | ❌ | ❌ |
| 年度汇总 | docs/YYYY/YY.md | ❌ | ❌ |
| 正式文章 | docs/YYYY/MM/file.md | ✅ JSON in `<!-- -->` | ✅ 需区块标记 |
| 术语表 | glossary/terms/*.md | ❌ | ❌ |

## 正式文章 MD 规范

```markdown
<!-- {"title":"文章标题","publish_date":"2026-05-02","source":"量子位","source_url":"https://...","score":9,"tags":["LLM","Agent"]} -->

# 文章标题

📅 2026-05-02&nbsp;&nbsp;📢 来源：[量子位](https://...)
🏷️ LLM · Agent

> 摘要内容（blockquote）

<!-- 正文开始 -->
正文内容，Markdown 格式
<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->
- [链接描述](../2026/05/file.html)
<!-- 相关文章结束 -->
```

## 规范细则

- **frontmatter**：JSON 放在 HTML 注释 `<!-- ... -->` 里，**无换行，全部写在一行内**
- **日期字段名**：`publish_date`（不是 `date`）
- **日期格式**：YYYY-MM-DD，与文件名中的日期一致
- **source**：没有则不写；中文来源写全名（如"量子位"），英文写原文（如"OpenAI Blog"）
- **source_url**：优先用 article.url，RSS 源的 url 不填
- **score**：整数 1-10（不是"精选"字符串），≥8 才导入 docs/
- **tags**：emoji 格式 `🏷️ tag1 · tag2`（中间点），无则不写
- **元信息行**：标题下两行——`📅 date` 和 `📢 来源：[Name](url)`，逗号分隔
- **摘要**：blockquote `> 摘要内容`，无则不写
- **正文区块**：`<!-- 正文开始 -->` / `<!-- 正文结束 -->` 必须写
- **相关文章区块**：有相关文章才写，用 `<!-- 相关文章开始 -->` / `<!-- 相关文章结束 -->` **包裹每一行**，链接相对路径从 docs/YYYY/MM/file.md 看要 `../../../glossary/terms/`（三层回溯）

## 文章可读性规范（必读）

> 文章写出来是为了阅读的，不是为了填充仓库的。流水账式正文（无标题、无分段、连续大段文字）直接打回重写。

### 正文结构要求

1. **至少 2-3 个一级标题**（`##`）：按内容逻辑分段，每段讲一个主题
2. **禁止连续 200+ 字无换行**：超过即分段
3. **禁止无序列表直接堆砌**：每个列表项前要有引导句
4. **代码块单独成行**：不要夹在段落中间
5. **表格要有标题行**：用 `|---|` 分隔，表头在上方

### 正文内容原则

- 用自己的话复述，不要直接复制原文（除非是引用）
- 删除所有社交媒体腔调（"友友们""真·能干""doge"）
- 删除所有推荐阅读链接（如 `——相关推荐：XXX`）
- 删除所有原文作者署名信息（闻乐 发自 凹非寺 这类）
- 保留核心数据和关键引用

### 相关文章

- **必须加上**：同一事件/主题的多篇文章互链
- **放在正文结束后、独立成块**：用 `<!-- 相关文章开始 -->` / `<!-- 相关文章结束 -->` 包裹
- **路径规则**：同一月 `file.html`，跨月 `../MM/file.md`，跨年 `../../../YYYY/MM/file.md`

### 格式检查清单

写完检查：
- [ ] frontmatter 单行 JSON，无多余换行
- [ ] 元信息：📅 + 📢 两行
- [ ] 正文有 ≥2 个 `##` 标题
- [ ] 没有连续 200+ 字的大段
- [ ] 相关文章有区块标记
- [ ] 无社交媒体腔调文字
- [ ] 无推荐阅读链接

## 解析规则

解析 frontmatter 时：
1. 用正则 `<!--\s*(\{.*?\})\s*-->` 提取单行 JSON
2. `json.loads()` 解析，字段：`title`/`publish_date`/`source`/`source_url`/`score`/`tags`
3. 正文边界：`<!-- 正文开始 -->` / `<!-- 正文结束 -->`
4. 相关文章边界：`<!-- 相关文章开始 -->` / `<!-- 相关文章结束 -->`
5. tags 格式 `🏷️ tag1 · tag2`，split(' · ')

## 数据流架构

```
crawler_new.py  →  temp/articles/{hash}.json  +  state.db(pending)
scorer_new.py   →  state.db(pending→scored, score≥8 才导入)
import_one.py   →  docs/YYYY/MM/file.md
```

- **temp/articles/**：文章原文 JSON 唯一存储位置，永不移动/删除
- **state.db**：信号源，crawler 写 pending，scorer 改 scored
- **docs/**：最终静态文章，只从高分 scored 文章生成

## 转换脚本

- `import_one.py`：从 state.db 读取 scored 高分文章，写入 docs/
- `scorer_new.py`：从 temp/articles/ 读文章，评分后写 state.db
- `crawler_new.py`：抓取 RSS/HTML，写入 temp/articles/ + state.db
- `update_year_summary.py`：维护 docs/YYYY/YY.md 年度汇总
- `update_readme.py`：维护 README.md 最新文章列表
- `fix_links.py`：修正 docs/ 内所有文章的 glossary 链接

## 历史背景

- 2020-2025 年文章初期是 HTML 格式，后迁移到 MD
- 原来 MD frontmatter 用 YAML（`---` 分隔），与正文水平线语法冲突，已废弃
- **V4 frontmatter 格式（已废弃）**：多行 JSON + `date` key + `score: "精选"` 字符串
- **V5 frontmatter 格式（当前）**：单行 JSON + `publish_date` key + `score: 整数`
