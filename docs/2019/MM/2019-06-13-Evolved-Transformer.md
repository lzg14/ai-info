---
title: Google Brain Evolved Transformer Achieves NAS Breakthrough
date: 2019-06-13
source: Google Brain官方博客
url: https://ai.googleblog.com/2019/06/introducing-evolved-transformer.html
---

## 内容摘要

2019年6月，Google Brain团队发布了"Evolved Transformer"，这是首个通过神经架构搜索（Neural Architecture Search，NAS）发现的、性能显著超越Transformer的新型序列到序列模型架构。研究人员使用NAS技术在大规模搜索空间中发现了一种新的注意力机制结构，其在机器翻译任务上比标准Transformer取得显著改进。

Evolved Transformer的核心创新在于其混合注意力机制：编码器使用并行的卷积层和自注意力层，而解码器采用一种新的"深度"可分离卷积。这一架构是首次完全由机器自动搜索发现的、超越人类设计的神经网络结构。

实验表明，Evolved Transformer在WMT'14英德翻译任务上比标准Transformer取得了1.7 BLEU分数的提升，在英法翻译任务上也有1.3 BLEU的提升。更重要的是，这种架构展现了良好的迁移能力，在不同的翻译任务和序列建模任务上都表现优异。

这一成果标志着AutoML（自动化机器学习）领域的重大突破，证明了机器可以发现超越人类直觉的新型神经网络架构。Evolved Transformer为后续的自动化架构搜索研究提供了重要的参考和新方向。

### Google Brain Evolved Transformer Achieves NAS Breakthrough（评分: 9.0/10）
