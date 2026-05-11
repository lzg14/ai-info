<!--
{
  "title": "CLIP 论文发布：多模态预训练新范式，zero-shot 视觉分类超越监督学习",
  "date": "2021-02-08"
}
-->

# CLIP 论文发布：多模态预训练新范式，zero-shot 视觉分类超越监督学习

📅 2021-02-08

<!-- 正文开始 -->
## 摘要

2021 年 2 月，OpenAI 发布 CLIP（Contrastive Language-Image Pre-Training）——一个在 4 亿图像-文本配对数据上训练的多模态模型。CLIP 能够在没有任何 ImageNet 训练数据的情况下，通过自然语言描述识别任意类别，实现了「zero-shot 视觉分类」的重大突破。

## 核心创新

**大规模对比预训练：** CLIP 使用对比学习目标，同时训练图像编码器和文本编码器，让配对的图像-文本表示更接近，不配对的更远离。

**zero-shot 分类：** 传统模型需要「固定类别标签」进行训练，CLIP 只需提供自然语言描述的类别列表，即可识别任意新类别。

**性能：** 在 ImageNet 上 zero-shot 准确率达 76.2%，与监督学习的 ResNet50 相当。

## 开源与影响

OpenAI 发布了 CLIP 模型权重和评估代码，迅速被广泛应用于图像检索、图像生成（CLIP 指导的 Stable Diffusion）等领域。

## 点评

CLIP 开创了「语言监督视觉学习」的新范式，也为后来多模态大模型（GPT-4V、[Gemini](../../glossary/terms/gemma.md)）的出现奠定了基础。
<!-- 正文结束 -->
