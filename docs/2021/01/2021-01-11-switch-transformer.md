---
title: Switch Transformer Scaling Language Models
date: 2021-01-11
source: arXiv
url: https://arxiv.org/abs/2101.03961
---

The academic paper "Switch Transformers: Scaling to Trillion Parameter Models with Sparse Selection" established a new paradigm for scaling neural networks. Authored by researchers at Google Brain, the paper detailed how sparse activation could enable trillion-parameter models without overwhelming computational resources.

The core innovation lay in simplifying the routing mechanism of mixture-of-experts models. Previous approaches required coordinating multiple active experts per token, introducing communication overhead in distributed training. The Switch Transformer reduced this to single expert routing, which dramatically lowered communication costs during training across multiple devices.

The paper demonstrated that simply scaling the number of experts while keeping computation per token constant could improve performance across a wide range of downstream tasks. This insight challenged the prevailing assumption that model scaling required proportional increases in floating-point operations.

A key contribution was the analysis of capacity versus performance trade-offs. The researchers showed that sparse models could match dense model performance while consuming less compute during inference, making them attractive for deployment scenarios where latency matters.

The work also introduced improved training techniques including selective precision training and temperature-based expert routing that stabilized training of such large sparse models. These techniques proved essential for achieving convergence with trillions of parameters.

### Switch Transformer Scaling Language Models（评分: 9.3/10）
