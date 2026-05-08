# Meta发布Llama 4：开源多模态大模型开启新纪元

2025年4月5日，Meta公司正式发布新一代开源大模型Llama 4，这是其首次采用混合专家（MoE）架构的多模态模型，标志着AI技术从"参数规模竞赛"转向"架构效率优化"的新阶段。

Llama 4系列包含三个版本：Llama 4 Scout（1090亿参数）、Llama 4 Maverick（4000亿参数）和Llama 4 Behemoth（2万亿参数）。Scout和Maverick已开放权重供全球开发者下载使用。Scout支持1000万token上下文，可在单张NVIDIA H100 GPU上运行；Maverick配备128个专家模型，在编程、数学推理、多语言处理等任务中超越GPT-4o和Gemini 2.0。

Llama 4的核心突破在于多模态能力。通过Helix多模态适配器，模型可无缝处理文本、图像、视频、音频四种模态数据。在内部测试中，模型能精准识别视频中"观众掌声与萨克斯演奏"的时空错位，并生成符合逻辑的场景描述。

Maverick版本实现了顶尖的性能与成本效益比，推理成本仅为[DeepSeek](../../../glossary/terms/deepseek.md) V3的一半。Behemoth版本则拥有2880亿活跃参数和近2万亿总参数，是Meta内部的"教师模型"，在STEM基准测试中已超越GPT-4.5和[Claude](../../../glossary/terms/claude.md) Sonnet 3.7。








## 相关文章
- [深度学习框架TensorFlow正式开源，谷歌推动AI技术民主化](../../2015/11/2015-11-10-tensorflow-open-source.md)
- [Microsoft Phi-3 开源小模型：38亿参数比肩GPT-3.5](../../2024/05/2024-05-04-microsoft-phi3-open-source.md)
- [Multimodal AI 2025 GPT-4V Gemini Vision Claude Vision Comparison](../01/2025-01-30-multimodal-ai-2025.md)
- [xAI发布Grok 3模型：声称超越GPT-4和Claude 3.5](../02/2025-02-04-grok-3-release.md)
- [DeepSeek R2 发布：编程能力超越 GPT-4o](../05/2025-05-06-deepseek-r2-launch.md)

tags: [大模型, 编程, 推理, 多模态, GPU, 开源, GPT, Claude]