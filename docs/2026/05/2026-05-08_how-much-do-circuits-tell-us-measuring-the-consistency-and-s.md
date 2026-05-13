---
date: 2026-05-08
publish_date: 2026-05-08
title: "How Much Do Circuits Tell Us? Measuring the Consistency and Specificity of Language Model Circuits"
title_zh: ""
url: "https://arxiv.org/abs/2605.08348"
source: "arXiv CS.CL"
source_url: "https://arxiv.org/abs/2605.08348"
tags: []
category: ""
---

# How Much Do Circuits Tell Us? Measuring the Consistency and Specificity of Language Model Circuits

📅 2026-05-08
📢 来源：arXiv CS.CL

# How Much Do Circuits Tell Us? Measuring the Consistency and Specificity of Language Model Circuits

📅 2026-05-08
📢 来源：[arXiv CS.CL](https://arxiv.org/rss/cs.CL)

📝 <think>
这篇文章关于语言模型中的"电路"框架（circuits framework），这是一种机制可解释性（mechanistic interpretability）研究方法。文章主要测量了电路的两个特性：一致性和特异性。

核心内容：
1. 电路框架旨在识别模型中因果重要的稀疏子图
2. 研究了电路重用、一致性（任务内组件的重复出现）和特异性（组件对任务的独特性）
3. 在6个任务和7个模型上使用边缘归因 patching 进行实验
4. 发现：任务内重用很高，共享组件对任务性能是必要的
5. 关键发现：电路并不具有任务特异性——消融一个任务的电路对另一个任务的性能损害程度与消融该任务自身电路相当
6. 原因：不同任务之间的电路存在大量重叠
7. 结论：虽然电路发现能识别重要组件，但缺乏任务特异性引发了疑问

我需要用100-150字概括这些内容。
</think>

**中文摘要：**

本文研究了语言模型中“电路”框架的一致性和特异性。研究者在六个任务和七个模型上使用边缘归因 patching 方法，发现任务内电路重用率很高，共享组件对性能至关重要，消融后准确率下降可达

> The circuits framework in mechanistic interpretability aims to identify causally important sparse subgraphs of model components, typically evaluated by measuring necessity and sufficiency. We measure circuit reuse, the proportion of components shared across per-example circuits within a task, and investigate two less-studied properties of this: consistency, the recurrence of components within a task, and specificity, their uniqueness to a task. Using edge attribution patching across six tasks and seven models, we find that within-task reuse is high and that shared components are necessary for task performance, with ablations causing up to $\sim$100% relative accuracy drops. However, circuits turn out not to be task-specific: ablating one task's circuit damages another task's performance about as much as that task's own circuit does. We discover that this is due to substantial overlap between circuits across tasks, which are causally important for performance. Some circuits do contain a smaller set of task-specific components, but these account for only a modest portion of circuit performance. Overall, our findings suggest that while circuit discovery at the level of attention heads and MLP layers identifies important components, their lack of task-specificity raises questions about the degree to which circuits can support targeted understanding and intervention on model behavior.

Computer Science > Computation and Language
[Submitted on 8 May 2026]
Title:How Much Do Circuits Tell Us? Measuring the Consistency and Specificity of Language Model Circuits
View PDF HTML (experimental)Abstract:The circuits framework in mechanistic interpretability aims to identify causally important sparse subgraphs of model components, typically evaluated by measuring necessity and sufficiency. We measure circuit reuse, the proportion of components shared across per-example circuits within a task, and investigate two less-studied properties of this: consistency, the recurrence of components within a task, and specificity, their uniqueness to a task. Using edge attribution patching across six tasks and seven models, we find that within-task reuse is high and that shared components are necessary for task performance, with ablations causing up to $\sim$100% relative accuracy drops. However, circuits turn out not to be task-specific: ablating one task's circuit damages another task's performance about as much as that task's own circuit does. We discover that this is due to substantial overlap between circuits across tasks, which are causally important for performance. Some circuits do contain a smaller set of task-specific components, but these account for only a modest portion of circuit performance. Overall, our findings suggest that while circuit discovery at the level of attention heads and MLP layers identifies important components, their lack of task-specificity raises questions about the degree to which circuits can support targeted understanding and intervention on model behavior.
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

## Related Articles

（待补充相关文章链接）
