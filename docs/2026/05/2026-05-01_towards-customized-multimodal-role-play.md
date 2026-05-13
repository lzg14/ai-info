---
date: 2026-05-01
publish_date: 2026-05-01
title: "Towards Customized Multimodal Role-Play"
title_zh: "定制化多模态角色扮演"
url: "https://arxiv.org/abs/2605.08129"
source: "arXiv CS.LG"
source_url: "https://arxiv.org"
tags: ["多模态", "角色扮演", "研究"]
category: "算法架构"
---

# Towards Customized Multimodal Role-Play

📅 2026-05-01
📢 来源：[arXiv CS.LG](https://arxiv.org/rss/cs.LG)

> 本文提出"定制化多模态角色扮演"（CMRP）新任务，旨在同时定制角色的个性、对话风格和视觉形象，并保持跨模态输出一致性。研究团队构建了包含20个角色的RoleScape-20数据集，提出UniCharacter两阶段训练框架，仅需10张图片即可让模型掌握目标角色特征。

## Background

Unified multimodal understanding and generation models enable richer human-AI interaction. Yet jointly customizing a character's persona, dialogue style, and visual identity while maintaining output consistency across modalities remains largely unexplored.

## Task and Dataset

To mitigate this gap, we introduce a new task, Customized Multimodal Role-Play (CMRP). We construct the RoleScape-20 dataset comprising 20 characters, including training and evaluation data that cover persona, stylistic descriptions, visual/expressive cues, and text-image interactions.

## Method

Building on a unified model, we devise UniCharacter, a two-stage training framework containing Unified Supervised Finetuning (Unified-SFT) and character-specific group relative policy optimization (Character-GRPO). Given only 10 images plus corresponding interaction examples, the model acquires the target character and exhibits coherent persona, style, and visual identity in both generated text and images. This process takes about 100 GPU hours.

## Experiments

Experiments on the RoleScape-20 dataset show that the proposed method substantially outperforms prior approaches. Ablation studies further validate the effectiveness of our cross-modal consistency design and few-shot customization strategy.

## Conclusion

We argue that CMRP, coupled with unified modeling, provides a basis for next-generation characterful and immersive interactive agents.

## Related Articles

- [RoleScape-20 Dataset — arXiv](https://arxiv.org/abs/2605.08129)
- [UniCharacter Framework — arXiv](https://arxiv.org/abs/2605.08129)
