<!--{"title": "VLADriver-RAG: Retrieval-Augmented Vision-Language-Action Models for Autonomous Driving", "url": "https://arxiv.org/abs/2605.08133", "source": "arXiv CS.CV", "source_url": "https://arxiv.org/abs/2605.08133", "publish_date": "2026-05-01", "score": null, "tags": [], "description_cn": "<think>这是一个关于自动驾驶视觉-语言-动作（VLA）模型的论文摘要任务。让我分析文章的核心内容：\n\n1. **问题背景**：VLA模型在自动驾驶中应用有前景，但依赖隐式参数知识，在长尾场景中泛化能力有限\n2. **现有方案局限**：检索增强生成（RAG）虽然能解决外部专家先验问题，但标准视觉检索存在高延迟和语义模糊问题\n3. **解决方案**：提出VLADriver-RAG框架\n   - 核心组件1：Visual-to-Scenario机制，将感官输入抽象为时空语义图，过滤视觉噪声\n   - 核心组件2：Scenario-Aligned Embedding Model，使用Graph-DTW度量对齐，优先考虑拓扑一致性而非表面视觉相似性\n   - 这些检索到的先验知识通过基于查询的VLA骨干网络融合，生成精确解耦的轨迹\n4. **实验结果**：在Bench2Drive基准测试上达到89.12的驾驶分数，创下新SOTA\n\n我需要用100-150字的中文概括这些内容。</think>\n\n本文提出VLADriver-RAG框架，解决视觉-语言-动作模型在自动驾驶中长尾场景泛化能力不足的问题。该框架通过"}-->
# VLADriver-RAG: Retrieval-Augmented Vision-Language-Action Models for Autonomous Driving

📅 2026-05-01
📢 来源：[arXiv CS.CV](https://arxiv.org/rss/cs.CV)

📝 <think>这是一个关于自动驾驶视觉-语言-动作（VLA）模型的论文摘要任务。让我分析文章的核心内容：

1. **问题背景**：VLA模型在自动驾驶中应用有前景，但依赖隐式参数知识，在长尾场景中泛化能力有限
2. **现有方案局限**：检索增强生成（RAG）虽然能解决外部专家先验问题，但标准视觉检索存在高延迟和语义模糊问题
3. **解决方案**：提出VLADriver-RAG框架
   - 核心组件1：Visual-to-Scenario机制，将感官输入抽象为时空语义图，过滤视觉噪声
   - 核心组件2：Scenario-Aligned Embedding Model，使用Graph-DTW度量对齐，优先考虑拓扑一致性而非表面视觉相似性
   - 这些检索到的先验知识通过基于查询的VLA骨干网络融合，生成精确解耦的轨迹
4. **实验结果**：在Bench2Drive基准测试上达到89.12的驾驶分数，创下新SOTA

我需要用100-150字的中文概括这些内容。</think>

本文提出VLADriver-RAG框架，解决视觉-语言-动作模型在自动驾驶中长尾场景泛化能力不足的问题。该框架通过

> Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving, yet their reliance on implicit parametric knowledge limits generalization in long-tail scenarios. While Retrieval-Augmented Generation (RAG) offers a solution by accessing external expert priors, standard visual retrieval suffers from high latency and semantic ambiguity. To address these challenges, we propose \textbf{VLADriver-RAG}, a framework that grounds planning in explicit, structure-aware historical knowledge. Specifically, we abstract sensory inputs into spatiotemporal semantic graphs via a \textit{Visual-to-Scenario} mechanism, effectively filtering visual noise. To ensure retrieval relevance, we employ a \textit{Scenario-Aligned Embedding Model} that utilizes Graph-DTW metric alignment to prioritize intrinsic topological consistency over superficial visual similarity. These retrieved priors are then fused within a query-based VLA backbone to synthesize precise, disentangled trajectories. Extensive experiments on the Bench2Drive benchmark establish a new state-of-the-art, achieving a Driving Score of 89.12.

<!-- 正文开始 -->

Computer Science > Computer Vision and Pattern Recognition
[Submitted on 1 May 2026 (v1), last revised 12 May 2026 (this version, v2)]
Title:VLADriver-RAG: Retrieval-Augmented Vision-Language-Action Models for Autonomous Driving
View PDF HTML (experimental)Abstract:Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving, yet their reliance on implicit parametric knowledge limits generalization in long-tail scenarios. While Retrieval-Augmented Generation (RAG) offers a solution by accessing external expert priors, standard visual retrieval suffers from high latency and semantic ambiguity. To address these challenges, we propose \textbf{VLADriver-RAG}, a framework that grounds planning in explicit, structure-aware historical knowledge. Specifically, we abstract sensory inputs into spatiotemporal semantic graphs via a \textit{Visual-to-Scenario} mechanism, effectively filtering visual noise. To ensure retrieval relevance, we employ a \textit{Scenario-Aligned Embedding Model} that utilizes Graph-DTW metric alignment to prioritize intrinsic topological consistency over superficial visual similarity. These retrieved priors are then fused within a query-based VLA backbone to synthesize precise, disentangled trajectories. Extensive experiments on the Bench2Drive benchmark establish a new state-of-the-art, achieving a Driving Score of 89.12.
Submission history
From: Zhao Rui [view email][v1] Fri, 1 May 2026 05:50:00 UTC (17,787 KB)
[v2] Tue, 12 May 2026 14:57:35 UTC (17,787 KB)
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