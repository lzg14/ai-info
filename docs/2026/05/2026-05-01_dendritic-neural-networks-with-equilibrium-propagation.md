---
date: 2026-05-01
publish_date: 2026-05-01
title: "Dendritic Neural Networks with Equilibrium Propagation"
title_zh: "带平衡传播的枝状神经网络"
url: "https://arxiv.org/abs/2605.08135"
source: "arXiv CS.LG"
source_url: "https://arxiv.org"
tags: ["神经网络", "深度学习", "研究"]
category: "算法架构"
---

# Dendritic Neural Networks with Equilibrium Propagation

📅 2026-05-01
📢 来源：[arXiv CS.LG](https://arxiv.org/rss/cs.LG)

> 平衡传播（EP）是生物可行的反向传播替代方案，但其有效性在更深层和更具挑战性的学习环境中会下降。本文提出将枝状神经网络与EP结合，在MNIST、KMNIST、FMNIST数据集上验证，枝状EP在挑战性数据集和深层模型上显著优于标准EP，接近使用反向传播训练的枝状网络性能。

## Background

Equilibrium propagation (EP) is a biologically plausible alternative to backpropagation (BP), but its effectiveness can degrade in deeper and more challenging learning settings. In parallel, dendritic neural networks have demonstrated improved performance and generalization when trained with BP, suggesting that structured, biologically inspired architectures may enhance learning.

## Method

In this work, we investigate the integration of dendritic neural networks with equilibrium propagation using an advanced EP framework. We evaluate the proposed dendritic EP model on MNIST, Kuzushiji-MNIST (KMNIST), and Fashion-MNIST (FMNIST), considering both shallow and deeper architectures.

## Results

Our results show that dendritic EP achieves performance comparable to standard EP on simple tasks, while providing consistent improvements on more challenging datasets and deeper models. In particular, dendritic EP significantly outperforms standard EP on KMNIST and FMNIST, and approaches the performance of dendritic networks trained with backpropagation through time.

## Analysis

To further understand these improvements, we analyze the evolution of hidden states during the free phase. We observe that dendritic EP exhibits higher activation magnitudes and more distributed hidden-state activity compared to standard EP, indicating that dendritic structure alters the internal network dynamics.

## Related Articles

- [Equilibrium Propagation — arXiv](https://arxiv.org/abs/1608.02315)
- [Dendritic Neural Networks — arXiv](https://arxiv.org/abs/2305.19605)
