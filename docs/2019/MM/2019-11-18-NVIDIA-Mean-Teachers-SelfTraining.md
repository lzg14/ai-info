---
title: NVIDIA Achieves State-of-the-Art in Semi-Supervised Learning
date: 2019-11-18
source: NVIDIA官方博客
url: https://developer.nvidia.com/blog/nvidia-sets-world-record-semi-supervised-learning/
---

## 内容摘要

2019年11月，NVIDIA与卡内基梅隆大学合作，在半监督学习领域取得了重大突破。研究团队使用Mean Teacher算法和NVIDIA DGX-2超级计算机，在仅使用1%标注数据的情况下，在ImageNet数据集上达到了超越先前全监督方法的准确率。

这一成果意义重大：传统深度学习需要大量标注数据，而数据标注既耗时又昂贵。NVIDIA的研究证明，通过精心设计的半监督学习技术，可以在标注数据极度匮乏的情况下训练出高性能模型。实验中，模型仅使用128万张未标注图像中的约1.3万张进行训练，最终准确率就超越了先前需要全部130万张标注图像的结果。

技术核心是Mean Teacher算法，该算法通过在模型的不同训练阶段之间传递知识，构建一个更稳定的"教师"模型。NVIDIA还结合了AutoAugment数据增强技术、大批量训练和分布式训练优化，实现了这一突破。

这项研究对医疗影像分析、自动驾驶感知等标注成本高昂的领域具有重要应用价值。通过减少对标注数据的依赖，AI系统可以更快速地部署到新领域和新场景中。

### NVIDIA Achieves State-of-the-Art in Semi-Supervised Learning（评分: 8.7/10）
