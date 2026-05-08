# Microsoft Phi-3 开源小模型：38亿参数比肩GPT-3.5

2024年5月，微软正式发布 Phi-3 开源小语言模型（SLM）系列，其中包括 Phi-3-mini（38亿参数）、Phi-3-small（70亿参数）和 Phi-3-medium（140亿参数）三个规模版本。该系列最大的亮点在于以极小的参数规模实现了与 GPT-3.5 相媲美的性能，被业界称为"能跑在手机上的大模型"。

Phi-3 系列采用了独特的训练方法，模仿儿童的渐进学习阶段，利用经过严格过滤的数据和合成数据（尤其是科学和编程教材）进行训练。训练使用了 4.8 万亿令牌，历时 42 天，消耗 512 块 H100 GPU。Phi-3-mini 上下文长度为 4K 和 128K，模型权重兼容 AWQ、INT4、ONNX 和 [Transformer](../../../glossary/terms/transformer.md)s，方便开发者在不同平台上部署。此外，微软还在 Build 2024 大会上推出了 Phi-3-vision 多模态版本，拥有 42 亿参数，支持图像+文本的视觉推理任务，可在移动设备上流畅运行，性能与 [Claude](../../../glossary/terms/claude.md) 3-haiku、[Gemini](../../../glossary/terms/gemma.md) 1.0 Pro 相当。

Phi-3 的开源标志着微软在轻量化 AI 模型领域的重要突破，为需要在算力受限场景下部署 AI 能力的开发者提供了新选择。








## 相关文章
- [深度学习框架TensorFlow正式开源，谷歌推动AI技术民主化](../../2015/11/2015-11-10-tensorflow-open-source.md)
- [Meta发布Llama 4：开源多模态大模型开启新纪元](../../2025/04/2025-04-20-llama-4-release.md)
- [CLIP 与 DALL-E 预览版：OpenAI 文本生成图像首秀](../../2020/06/2020-06-15-clip-dall-e.md)
- [Hugging Face s 4.0版本发布](../../2020/10/2020-10-15-huggingface-transformers-4-release.md)
- [华为云发布盘古大模型系列：面向行业应用的千亿级NLP模型](../../2021/04/2021-04-25-huawei-pangu-nlp-model.md)

tags: [大模型, 编程, 推理, 多模态, GPU, 开源, 平台, Transformer]