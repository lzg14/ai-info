# Google发布ALIGN：用18亿噪声图像-文本对训练多模态模型

2021年2月，Google Research发表论文《Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision》，提出**ALIGN**模型。该模型使用超过**18亿**对噪声图像-文本数据进行训练，展示了"大力出奇迹"的 [Scaling Law](../../../glossary/terms/scaling-law.md) 效应。

ALIGN的核心思想极为简洁：利用网络上公开的图像及其替代文本作为训练数据，无需昂贵的人工标注，即可学习到强大的视觉和视觉-语言表示。实验证明，数据规模的巨大提升可以弥补数据噪声的不足。ALIGN在ImageNet分类、Flickr30K和MS-COCO图像检索等基准上刷新SOTA，并支持zero-shot图像分类。

ALIGN的成功验证了多模态预训练的新范式——通过大规模噪声数据也能训练出高质量模型。这一思路影响了后续CLIP、DALL·E等模型的发展，对多模态AI领域产生深远影响。








## 相关文章
- [Google Show and Tell：AI第一次能描述图片内容](../../2014/05/2014-05-01-Google-Show-and-Tell-AI第一次能描述图片内容.md)
- [CLIP 与 ：AI 跨模态学习的突破](../../2020/06/2020-06-15-clip-openai-multimodal-zero-shot.md)
- [谷歌  1.0 发布：多模态之王正式挑战 GPT-4](../../2023/12/2023-12-06-gemini.md)
- [谷歌  2.0 Ultra 发布：最强多模态模型](../../2025/08/2025-08-15-gemini-2-0-ultra.md)
- [谷歌 Gemini 3 Pro 发布：全面超越 GPT-5](../../2025/10/2025-10-19-gemini-3-pro.md)

tags: [多模态, 论文, Google, GPT, OpenAI, Gemini]