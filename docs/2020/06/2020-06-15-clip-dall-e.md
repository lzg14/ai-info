# CLIP 与 DALL-E 预览版：OpenAI 文本生成图像首秀

## 摘要

2020 年，OpenAI 发布 CLIP 和 DALL-E——CLIP 是一个能理解图像与文本关联的多模态模型，DALL-E 是基于 GPT-3 架构的文本生成图像模型。DALL-E 能够根据奇异文本描述生成对应图像，展示了语言引导视觉生成的巨大潜力。

## CLIP：视觉理解的新范式

**对比学习 + 大规模数据：** CLIP 使用 4 亿对图像-文本配对数据，通过对比学习让模型理解「这张图对应这段文字」。这打破了传统计算机视觉「固定类别标签」的局限。

**Zero-shot 能力：** CLIP 可以在没有任何 ImageNet 训练数据的情况下，在 ImageNet 上达到 76.2% 准确率——这在当时是零样本分类的重大突破。

## DALL-E：语言到图像的桥梁

**基于 GPT-3 微调：** DALL-E 是 GPT-3 的 120 亿参数版本，使用文本-图像配对数据集训练。输入自然语言描述，输出对应图像。

**组合推理能力：** DALL-E 能将无关概念组合在一起，生成看似荒诞但符合描述的图像，如「方形的苹果」「穿着芭蕾裙的胡萝卜」。

## 后续发展

DALL-E 2（2022）大幅提升了分辨率和真实感，Stable Diffusion（2022）开源后形成三足鼎立。

## 点评

CLIP 和 DALL-E 证明了 [Transformer](../../../glossary/terms/transformer.md) 架构在多模态领域的统治力，也为后来多模态大模型（GPT-4V、[Gemini](../../../glossary/terms/gemma.md)）奠定了基础。








## 相关文章
- [Facebook开源DeiT数据高效图像](../07/2020-07-15-fair-deblender-visual-object-detection.md)
- [Multimodal AI 2025 GPT-4V Gemini Vision Claude Vision Comparison](../../2025/01/2025-01-30-multimodal-ai-2025.md)
- [无标题](../../2019/02/2019-02-22-openai-clip-text-image-contrastive.md)
- [CLIP与DALL-E发布：OpenAI多模态模型首秀，文本生成图像成为现实](2020-06-15-clip-dall-e-multimodal.md)
- [DeepMind开源Perceiver通用多模态模型](../11/2020-11-13-deepmind-perceiver-io-multimodal.md)

tags: [大模型, 推理, 计算机视觉, 多模态, 开源, Transformer, GPT, OpenAI]