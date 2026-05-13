<!-- {"title": "VLADriver-RAG: Retrieval-Augmented Vision-Language-Action Models for Autonomous Driving", "title_zh": "VLADriver-RAG：检索增强的自动驾驶视觉语言动作模型", "url": "https://arxiv.org/abs/2605.08133", "source": "arXiv CS.CV", "source_url": "https://arxiv.org", "publish_date": "2026-05-01", "tags": ["自动驾驶", "RAG", "VLA模型"], "category": "算法架构"} -->

# VLADriver-RAG: Retrieval-Augmented Vision-Language-Action Models for Autonomous Driving

📅 2026-05-01
📢 来源：[arXiv CS.CV](https://arxiv.org/rss/cs.CV)

> 本文提出VLADriver-RAG框架，通过Visual-to-Scenario机制将感官输入抽象为时空语义图，并使用Scenario-Aligned Embedding Model进行图-DTW度量对齐，在Bench2Drive基准测试上达到89.12驾驶分数，创下新SOTA。

<!-- 正文开始 -->

## Background

Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving, yet their reliance on implicit parametric knowledge limits generalization in long-tail scenarios. While Retrieval-Augmented Generation (RAG) offers a solution by accessing external expert priors, standard visual retrieval suffers from high latency and semantic ambiguity.

## Method

To address these challenges, we propose VLADriver-RAG, a framework that grounds planning in explicit, structure-aware historical knowledge. Specifically, we abstract sensory inputs into spatiotemporal semantic graphs via a Visual-to-Scenario mechanism, effectively filtering visual noise. To ensure retrieval relevance, we employ a Scenario-Aligned Embedding Model that utilizes Graph-DTW metric alignment to prioritize intrinsic topological consistency over superficial visual similarity.

## Architecture

These retrieved priors are then fused within a query-based VLA backbone to synthesize precise, disentangled trajectories.

## Experiments

Extensive experiments on the Bench2Drive benchmark establish a new state-of-the-art, achieving a Driving Score of 89.12.

<!-- 正文结束 -->