<!--
{
  "title": "Magis-Bench: Evaluating LLMs on Magistrate-Level Legal Tasks",
  "url": "https://arxiv.org/abs/2605.08437",
  "source": "arXiv CS.CL",
  "source_url": "https://arxiv.org/abs/2605.08437",
  "publish_date": "2026-05-08",
  "score": null,
  "tags": "",
  "description_cn": "<think>\n用户需要我为这篇关于法律AI评估的学术论文撰写中文摘要。让我分析文章核心内容：\n\n1. **研究背景/问题**：现有法律AI基准测试主要关注生成法律论证或文档的能力，但评判法律论证的能力（权衡竞争性主张、将法理应用于事实、做出合理裁决）对于法律系统同样重要。\n\n2. **研究贡献**：引入Magis-Bench基准测试，用于评估LLMs在 magistrate-level（法官级别）写作任务上的表现，基于巴西司法职位竞争考试。\n\n3. **数据集构成**：74道题目，来自2023-2025年间的8次考试，包括论述性法律分析题（多轮结构）和实践练习（需要撰写完整的民事和刑事判决书）。\n\n4. **评估方法**：使用LLM-as-a-judge方法，4个独立的前沿模型作为评估者。\n\n5. **主要结果**：\n   - 评估者间一致性很高（Kendall's W = 0.984，配对Kendall's τ ≥ 0.897）\n   - Google Gemini-3-Pro-Preview表现最佳（6.97/10）\n   - 其次是Gemini-3-Flash-Preview（6.67）和Claude-4\n</think>"
}
-->
# Magis-Bench: Evaluating LLMs on Magistrate-Level Legal Tasks

📅 2026-05-08
📢 来源：[arXiv CS.CL](https://arxiv.org/rss/cs.CL)

📝 <think>
用户需要我为这篇关于法律AI评估的学术论文撰写中文摘要。让我分析文章核心内容：

1. **研究背景/问题**：现有法律AI基准测试主要关注生成法律论证或文档的能力，但评判法律论证的能力（权衡竞争性主张、将法理应用于事实、做出合理裁决）对于法律系统同样重要。

2. **研究贡献**：引入Magis-Bench基准测试，用于评估LLMs在 magistrate-level（法官级别）写作任务上的表现，基于巴西司法职位竞争考试。

3. **数据集构成**：74道题目，来自2023-2025年间的8次考试，包括论述性法律分析题（多轮结构）和实践练习（需要撰写完整的民事和刑事判决书）。

4. **评估方法**：使用LLM-as-a-judge方法，4个独立的前沿模型作为评估者。

5. **主要结果**：
   - 评估者间一致性很高（Kendall's W = 0.984，配对Kendall's τ ≥ 0.897）
   - Google Gemini-3-Pro-Preview表现最佳（6.97/10）
   - 其次是Gemini-3-Flash-Preview（6.67）和Claude-4
</think>

> Existing benchmarks for legal AI focus primarily on tasks where LLMs must produce legal arguments or documents, yet the capacity to \emph{judge} such arguments -- weighing competing claims, applying doctrine to facts, and rendering reasoned decisions -- is arguably as fundamental to a well-functioning legal system as advocacy itself. We introduce Magis-Bench, a benchmark for evaluating LLMs on magistrate-level writing tasks derived from recent Brazilian competitive examinations for judicial positions. Magis-Bench comprises 74 questions from eight examinations conducted between 2023 and 2025, including discursive legal analysis questions with multi-turn structure and practical exercises requiring the composition of complete civil and criminal judicial sentences. We evaluate 23 state-of-the-art LLMs using an LLM-as-a-judge methodology with four independent frontier models as evaluators. Our results show strong inter-judge agreement (Kendall's $W = 0.984$; pairwise Kendall's $τ\ge 0.897$), with Google's Gemini-3-Pro-Preview achieving the highest average score (6.97/10), followed by Gemini-3-Flash-Preview (6.67) and Claude-4.5-Opus (6.46). Even the best-performing models score below 70\% of the maximum, indicating that judicial-level legal reasoning and writing remain challenging for current LLMs. We release the complete benchmark, model outputs, and evaluation code to support further research on legal AI capabilities.

<!-- 正文开始 -->

Computer Science > Computation and Language
[Submitted on 8 May 2026]
Title:Magis-Bench: Evaluating LLMs on Magistrate-Level Legal Tasks
View PDF HTML (experimental)Abstract:Existing benchmarks for legal AI focus primarily on tasks where LLMs must produce legal arguments or documents, yet the capacity to \emph{judge} such arguments -- weighing competing claims, applying doctrine to facts, and rendering reasoned decisions -- is arguably as fundamental to a well-functioning legal system as advocacy itself. We introduce Magis-Bench, a benchmark for evaluating LLMs on magistrate-level writing tasks derived from recent Brazilian competitive examinations for judicial positions. Magis-Bench comprises 74 questions from eight examinations conducted between 2023 and 2025, including discursive legal analysis questions with multi-turn structure and practical exercises requiring the composition of complete civil and criminal judicial sentences. We evaluate 23 state-of-the-art LLMs using an LLM-as-a-judge methodology with four independent frontier models as evaluators. Our results show strong inter-judge agreement (Kendall's $W = 0.984$; pairwise Kendall's $\tau \ge 0.897$), with Google's Gemini-3-Pro-Preview achieving the highest average score (6.97/10), followed by Gemini-3-Flash-Preview (6.67) and Claude-4.5-Opus (6.46). Even the best-performing models score below 70\% of the maximum, indicating that judicial-level legal reasoning and writing remain challenging for current LLMs. We release the complete benchmark, model outputs, and evaluation code to support further research on legal AI capabilities.
References & Citations
Loading...
Bibliographic and Citation Tools
Bibliographic Explorer (What is the Explorer?)
Connected Papers (What is Connected Papers?)
Litmaps (What is Litmaps?)
scite Smart Citations (What are Smart Citations?)
Code, Data and Media Associated with this Article
alphaXiv (What is alphaXiv?)
CatalyzeX Code Finder for Papers (What is CatalyzeX?)
DagsHub (What is DagsHub?)
Gotit.pub (What is GotitPub?)
Hugging Face (What is Huggingface?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

<!-- 正文结束 -->

## Related Articles

（待补充相关文章链接）
