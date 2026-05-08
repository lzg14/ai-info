---
title: Switch Transformer Trillion Parameters
date: 2021-01-11
source: Google AI Blog
url: https://ai.googleblog.com/2021/01/switch-transformer-scaling-to-trillion.html
---

In January 2021, Google Research unveiled the Switch Transformer, a groundbreaking language model architecture that scaled to one trillion parameters. This marked a significant leap in the pursuit of ever-larger neural networks, pushing the boundaries of natural language processing capabilities.

The Switch Transformer introduced a sparse activation mechanism that allowed the model to efficiently handle massive parameter counts while maintaining computational feasibility. Unlike previous mixture-of-experts models that activated multiple experts per token, the Switch Transformer uniquely activated only a single expert per token, dramatically reducing routing computation while enabling unprecedented model scale.

The architecture leveraged a concept called "expert routing" where each token is dynamically routed to the most relevant expert within the network. With 2048 experts total, the model could specialize different portions of its capacity for different types of linguistic tasks while keeping inference practical through sparse activation.

Training results demonstrated remarkable efficiency gains. The Switch Transformer achieved comparable performance to the T5-XXL model while using only one-seventh of the FLOPs per token during training. This efficiency breakthrough suggested that scaling model parameters could be a viable path to improved AI capabilities without proportional increases in computational cost.

The model also exhibited strong multi-lingual capabilities, showing improvements across 101 languages compared to smaller models. This suggested that the massive parameter count allowed the model to capture diverse linguistic patterns and knowledge representations across different languages simultaneously.

### Switch Transformer Trillion Parameters（评分: 9.2/10）
