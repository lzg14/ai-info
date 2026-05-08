# Facebook开源DeiT数据高效图像

2020年7月，Facebook AI研究院开源了DeiT（Data-efficient Image Transformer），一个仅需1200万张图片即可达到85%以上Top-1准确率的图像Transformer。DeiT解决了ViT（Vision Transformer）需要大规模预训练数据的痛点。

DeiT采用创新的蒸馏训练策略，利用卷积网络作为教师模型指导学生Transformer的学习，显著降低了数据依赖。该模型在ImageNet上从头训练即可达到优秀性能，无需JFT-300M等海量标注数据集。DeiT的参数量仅86M，推理速度比EfficientNet快约两倍。Facebook同时发布了预训练模型和训练代码，供研究社区复用。该工作推动了Transformer在计算机视觉领域的快速普及。








## 相关文章
- [CLIP 与 DALL-E 预览版：OpenAI 文本生成图像首秀](../06/2020-06-15-clip-dall-e.md)
- [DeepMind开源Perceiver通用多模态模型](../11/2020-11-13-deepmind-perceiver-io-multimodal.md)
- [Multimodal AI 2025 GPT-4V Gemini Vision Claude Vision Comparison](../../2025/01/2025-01-30-multimodal-ai-2025.md)
- [OpenAI GPT-1 Paper Release](../../2018/06/2018-06-11-openai-gpt-1-release.md)
- [架构加速落地，NLP进入注意力机制时代](../../2018/07/2018-07-15-Transformer架构加速落地NLP进入注意力机制时代.md)

tags: [推理, 计算机视觉, 开源, Transformer, 多模态, BERT, OpenAI, GPT]