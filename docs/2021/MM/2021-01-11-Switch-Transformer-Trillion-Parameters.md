---
title: Google Brain Switch Transformer Achieves Trillion Parameters
date: 2021-01-11
source: Google AI Blog
url: https://ai.googleblog.com/2021/01/switch-transformers-scaling-to-trillion.html
---

In January 2021, Google Brain researchers unveiled the Switch Transformer, a revolutionary language model architecture that scaled to one trillion parameters, making it the largest dense neural network ever published at that time. The Switch Transformer introduced a novel approach to scaling transformer models by employing a sparse activation mechanism that activated only a fraction of the model's parameters for any given input, dramatically improving computational efficiency while maintaining the benefits of massive scale.

The key innovation behind the Switch Transformer was the "sparse gating" technique, which routed each input token to only a subset of the model's "expert" networks rather than activating all parameters simultaneously. This approach allowed the model to achieve unprecedented model capacity while keeping computational costs manageable. The architecture was based on the T5 model but scaled to previously unimaginable dimensions, with the routing mechanism learning to send different types of tokens to different specialized experts, effectively creating a form of internal specialization within the model.

The research demonstrated that the Switch Transformer achieved significant improvements in training speed and performance across multiple benchmarks compared to its smaller counterparts. In language modeling tasks, the trillion-parameter Switch Transformer outperformed models with far more parameters but using dense activation, showcasing the efficiency of the sparse approach. The researchers also showed that the architecture could be distilled into smaller, denser models that retained most of the performance, making the technology more practical for deployment.

Beyond the technical achievements, the Switch Transformer paper contributed important insights about scaling laws in deep learning, suggesting that model size could continue to be a primary driver of capability improvements for the foreseeable future. The work also inspired further research into mixture-of-experts architectures and sparse computing approaches across the AI community, influencing subsequent work on efficient large-scale model training and deployment.

### Google Brain Switch Transformer Achieves Trillion Parameters（评分: 9.3/10）
