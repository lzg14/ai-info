# ai-info — 项目规格说明

## 概述

AI/深度学习相关资讯的静态文章库。每篇文章独立一个 HTML 文件，样式统一引用 `docs/assets/article.css`，可在浏览器或 GitHub 直接浏览。

**主题范围：** 大模型（GPT/LLaMA/DeepSeek/Qwen/GLM 等）、Agent、算法架构、芯片算力、AI 行业事件。

---

## 目录结构

```
ai-info/
├── docs/
│   ├── index.html              ← 文章入口（最新10条 + 年度卡片网格）
│   ├── 2011.html ~ 2026.html  ← 年度汇总页（精选列表 + 月份列表）
│   ├── YYYY/MM/               ← 按年月分目录，每篇一个 .html
│   ├── glossary/               ← 术语表
│   │   ├── index.html          ← 术语索引页
│   │   └── terms/              ← 各术语 .html 文件
│   └── assets/
│       ├── article.css         ← 文章阅读样式
│       └── index.css           ← 导航页样式（index + 年度汇总 + 术语索引）
├── README.md                   ← 项目介绍
├── SPEC.md                     ← 本规格说明
└── .git/
```

**注：** `scripts/`、`temp/`、`data/` 不在 ai-info 仓库内，已迁移至 `~/.hermes/skills/ai-info/` 下的对应子目录。Cron 任务调用脚本时路径相应调整。

---

## 文件命名规则

**格式：** `YYYY-MM-DD_simple-english-title.html`

**规则：**
- 年-月-日后接下划线（`_`），然后是标题英文描述
- 标题描述用连字符（`-`）分隔单词，全小写，2-8个词
- **文件名不出现中文和特殊字符**：只用 ASCII 字母、数字、连字符（`-`）、下划线（`_`）
- 同一标题重复：加 `_2`、`_3` 序号区分

**文件名不等于文章标题。** 文章标题写在文件内部（`<h1>`），可以有中文、冒号等任何字符。

**日期来源：** 文章原始发布日期。

---

## 文件内容格式（V3 — 2026-05-10 起，HTML 格式）

每篇文章独立一个 HTML 文件，样式统一引用 `docs/assets/article.css`。

**为什么从 Markdown 改为 HTML？**

MD 格式导致过多隐性约定：frontmatter 的 YAML 字段位置、正文里哪些是元数据（来源行/tags行）全靠约定而非结构，容易在渲染时被混进正文或被其他工具错误处理。改为 HTML 后，元数据和结构是显式的 DOM 节点，不会被当作正文内容。另一个实际原因是 build_content 降级逻辑在某些情况下会把正文内容错误地降级成只有标题，导致正文丢失；HTML 格式把提取失败和格式错误区分得更清楚。

**HTML Schema（所有文章必须遵循此结构）：**

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>文章标题</title>
  <link rel="stylesheet" href="../../assets/article.css">
</head>
<body>
  <div class="container">
    <article>
      <header class="article-header">
        <div class="article-tag-line">
          <span class="dot"></span>
          <span class="category">来源名</span>
          <span class="score-badge">精选</span>   <!-- 仅评分≥8.0时出现 -->
        </div>
        <h1>文章标题</h1>
        <div class="article-meta">
          <span class="source">
            <a href="https://..." target="_blank">来源名</a>
          </span>
          <span class="date">入库 2026-05-09</span>
        </div>
      </header>

      <div class="article-content">
        <p>正文段落...</p>
        <h2>小节标题</h2>
        <p>正文...</p>
        <!-- 更多段落和小节 -->
      </div>

      <footer>
        <div class="related-section">
          <h2>相关文章</h2>
          <ul>
            <li><a href="../05/related-article.html">相关文章标题</a></li>
          </ul>
        </div>
      </footer>
    </article>
  </div>
</body>
</html>
```

**格式说明：**

- **`<head>`**：固定三件套（charset、viewport、title）+ CSS 外链 `../../assets/article.css`
- **CSS 外链路径**：`../../assets/article.css`（从 `docs/YYYY/MM/` 出发向上两层到 `docs/` 再进 `assets/`）
- **`<header>`**：包含标签行、h1 标题、meta 信息行（来源 / 入库日期）
- **`<div class="article-content">`**：正文区，内部必须是 `<p>` 和 `<h2>` 标签，不能混 DIV/SPAN 等其他标签
- **h2 小节**：`font-size: 19px`，大写字母，字间距加宽，左下细线装饰
- **`<footer>`**：仅含相关文章区（已去除标签区块，2026-05-10）
- **精选徽章**：仅评分 ≥8.0 时出现 `<span class="score-badge">精选</span>`
- **来源 meta**：链接指向原始 article URL（`source_url`），`_blank` 在新标签页打开

**相关文章链接格式（从 `docs/YYYY/MM/X.html` 出发）：**
- 同月：`related.html`
- 跨月：`../MM/related.html`（向上到年份，再进目标月份）
- 跨年：`../../YYYY/MM/related.html`（向上两层到 docs/，再进目标年份）

**CSS 关键样式（2026-05-10 更新）：**
- body line-height: 1.7
- p line-height: 1.75，margin-bottom: 18px
- h2 小节：19px，大写字母，字间距 0.1em，左下细线
- container max-width: 800px
- 顶部装饰线：整宽 2px 单线（accent 色，0.6 透明度）

**批量转换工具：** `~/.hermes/skills/ai-info/scripts/md2html.py`（已完成 1121 篇 MD→HTML 转换）

---

## 链接路径规范（CRITICAL）

**四个文件的上下文不同，链接格式也不同：**

| 文件 | 位置 | 文章链接格式 | 示例 |
|------|------|-------------|------|
| README.md | 项目根目录 `/` | `docs/YYYY/MM/file.html` | `docs/2026/03/article.html` |
| docs/index.html | `docs/` 目录下 | `YYYY/MM/file.html` | `2026/03/article.html` |
| docs/YYYY.html | `docs/` 目录下 | `YYYY/MM/file.html` | `2026/03/article.html` |
| docs/YYYY/MM/X.html | `docs/YYYY/MM/` 下 | `file.html` 或 `../MM/file.html` | `article.html` |

**glossary 链接（从任意文章出发）：** `../../glossary/terms/xxx.html`

**验证方法：** 从文件所在目录用相对路径能否找到链接目标。

---

## 订阅源配置

RSS 订阅源配置在 `~/.hermes/skills/ai-info/data/config/sources.json`（已迁移，不在 ai-info 仓库内）。

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

#### 1. 年度汇总（docs/YYYY.html）
- 精选表：⭐8.0+ 文章，按评分降序
- 完整列表：按月份分组，每月内按日期倒序

#### 2. index.html
- **最新10条**：全部文章按日期倒序，取前10篇
- **年度统计**：篇数变化时更新表格

#### 3. 相关文章（各文章底部的 `## 相关文章`）
- 由 `import_one.py` 的 `find_related_articles()` 自动生成
- 导入新文章时自动追加到同月已有文章底部

### 同步检查清单

- [ ] docs/YYYY.html 已更新，链接路径正确
- [ ] docs/index.html 最新10条已更新
- [ ] docs/index.html 年度统计表格篇数已更新

---

## 附录

- 适用版本：2026-05-10 起（V3 格式，HTML + 集中 CSS）
- MD→HTML 转换：已于 2026-05-10 完成全部 1121 篇文章转换
