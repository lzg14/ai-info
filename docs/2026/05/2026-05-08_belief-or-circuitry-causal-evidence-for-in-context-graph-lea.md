<!-- {"title": "Belief or Circuitry? Causal Evidence for In-Context Graph Learning", "title_zh": "", "url": "https://arxiv.org/abs/2605.08405", "source": "arXiv CS.AI", "source_url": "https://arxiv.org/rss/cs.AI", "publish_date": "2026-05-08", "score": null, "tags": []} -->

# Belief or Circuitry? Causal Evidence for In-Context Graph Learning

📅 2026-05-08
📢 来源：[arXiv CS.AI](https://arxiv.org/rss/cs.AI)



<!-- 正文开始 -->

📝 <think>
这篇文章是关于大型语言模型（LLM）如何进行上下文学习的科学研究。让我总结核心内容：

主题：探究LLM如何在上下文学习中获取知识——是通过模式匹配近期token，还是通过推断潜在结构。

方法：
1. 使用图随机游走的玩具任务，在两个竞争图结构之间进行探测
2. 通过PCA重建内部表示结构
3. 使用残差流激活 patching 和图差异 steering 进行因果干预

主要发现：
1. 在中间混合比例时，两种图拓扑同时编码在正交的主子空间中——这难以用纯局部转换复制来解释
2. 晚期层 patching 几乎完全转移了干净图偏好
3. 线性 steering 在预期方向上移动预测，但在 norm-matched 和 label-shuffled 控制下失败

结论：支持双机制假说——真正的结构推理和归纳电路并行运作

现在写100-150字的中文摘要：
</think>

## 摘要

本文探究大语言模型在上下文学习中究竟是依赖模式匹配还是结构推理。通过设计图随机游走任务，在两种竞争图结构间进行实验。研究者采用PCA重建内部表征发现，在中间混合比例下，两种图拓扑同时编码于正交的主子空间中；同时

> How do LLMs learn in-context? Is it by pattern-matching recent tokens, or by inferring latent structure? We probe this question using a toy graph random-walk across two competing graph structures. This task's answer is, in principle, decidable: either the model tracks global topology, or it copies local transitions. We present two lines of evidence that neither account alone is sufficient. First, reconstructing the internal representation structure via PCA reveals that at intermediate mixture ratios, both graph topologies are encoded in orthogonal principal subspaces simultaneously. This pattern is difficult to reconcile with purely local transition copying. Second, residual-stream activation patching and graph-difference steering causally intervene on this graph-family signal: late-layer patching almost fully transfers the clean graph preference, while linear steering moves predictions in the intended direction and fails under norm-matched and label-shuffled controls. Taken together, our findings are most consistent with a dual-mechanism account in which genuine structure inference and induction circuits operate in parallel.

Computer Science > Artificial Intelligence
[Submitted on 8 May 2026]
Title:Belief or Circuitry? Causal Evidence for In-Context Graph Learning
View PDF HTML (experimental)Abstract:How do LLMs learn in-context? Is it by pattern-matching recent tokens, or by inferring latent structure? We probe this question using a toy graph random-walk across two competing graph structures. This task's answer is, in principle, decidable: either the model tracks global topology, or it copies local transitions. We present two lines of evidence that neither account alone is sufficient. First, reconstructing the internal representation structure via PCA reveals that at intermediate mixture ratios, both graph topologies are encoded in orthogonal principal subspaces simultaneously. This pattern is difficult to reconcile with purely local transition copying. Second, residual-stream activation patching and graph-difference steering causally intervene on this graph-family signal: late-layer patching almost fully transfers the clean graph preference, while linear steering moves predictions in the intended direction and fails under norm-matched and label-shuffled controls. Taken together, our findings are most consistent with a dual-mechanism account in which genuine structure inference and induction circuits operate in parallel.
Submission history
From: Katharine Kowalyshyn [view email][v1] Fri, 8 May 2026 19:11:19 UTC (1,243 KB)
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