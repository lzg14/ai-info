# DeepMind开源Perceiver通用多模态模型

2020年11月，DeepMind发布Perceiver IO开源版本，这是一个能够处理任意组合输入输出模态的通用模型架构。Perceiver IO解决了传统多模态模型需要为每种任务定制设计的问题，实现了真正的模态无关通用架构。

该模型能够同时处理文本、图像、音频、视频、点云等高达26种模态的数据，并在语言、视觉、逻辑推理等不同任务上均取得竞争性表现。核心创新在于使用交叉[注意力机制](../../../glossary/terms/attention-mechanism.md)将异构输入映射到统一的潜在空间，避免了Transformer对高维原始输入的计算负担。Perceiver IO被视为迈向通用人工智能（AGI）的重要一步，其开源代码和预训练权重极大推动了多模态学习研究。








## 相关文章
- [Multimodal AI 2025 GPT-4V Gemini Vision Claude Vision Comparison](../../2025/01/2025-01-30-multimodal-ai-2025.md)
- [CLIP 与 DALL-E 预览版：OpenAI 文本生成图像首秀](../06/2020-06-15-clip-dall-e.md)
- [Facebook开源DeiT数据高效图像](../07/2020-07-15-fair-deblender-visual-object-detection.md)
- [MosaicML发布MPT-30B：商业可用的开源大模型](../../2023/06/2023-06-20-20MPT-30B-release.md)
- [Google发布 1.0：多模态AI的新纪元](../../2023/12/2023-12-06-google-gemini-launch.md)

tags: [推理, 多模态, 开源, Transformer, GPT, Claude, OpenAI, Gemini]