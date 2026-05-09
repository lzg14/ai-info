# 谷歌发布Gemini 1.5，多模态理解进入长上下文时代

2024年2月15日，谷歌正式发布Gemini 1.5系列模型，其中Gemini 1.5 Pro凭借100万token的超长上下文能力震惊业界。这一突破意味着AI模型可以一次性处理整本书籍、数小时视频或涵盖数百个文档的代码库，多模态理解进入了一个全新的时代。

Gemini 1.5的技术核心是名为"[Mixture of Experts](../../../glossary/terms/mixture-of-experts.md)"（MoE）的稀疏激活架构。相比传统的稠密模型，MoE架构只在需要时才激活相关的"专家"网络，从而在保持高质量输出的同时大幅降低计算成本。Gemini 1.5在训练时使用了额外的1T tokens数据强化推理能力，显著提升了复杂任务的表现。

在多项基准测试中，Gemini 1.5 Pro展现出了强大的竞争力。它在MMLU基准上达到90%以上，与GPT-4持平；在长上下文理解测试中近乎完美，能够准确回答涉及百万token上下文的问题。更引人注目的是其多模态能力——用户可以直接上传视频、音频、文档的混合内容，模型能够理解并整合所有信息。

谷歌同时发布了Gemini 1.5 Flash，这是一个针对低延迟场景优化的轻量级模型。尽管体积更小，Gemini 1.5 Flash在多个关键任务上仍能达到Pro版本90%以上的表现，定价却只有后者的十分之一。这种"大模型能力、小模型成本"的策略，延续了谷歌在云计算市场的竞争逻辑。

Gemini 1.5的发布加剧了AI厂商间的竞争。OpenAI在当月紧急预告了GPT-5的研发进展，Anthropic则加快了[Claude](../../../glossary/terms/claude.md) 3.5的发布节奏。值得关注的是，[Gemini](../../../glossary/terms/gemma.md) 1.5已经在Google Workspace产品线中开始部署，Gmail、Google Docs等工具正在获得AI助手能力，这意味着AI正从"聊天玩具"加速转变为"生产工具"。








## 相关文章
- [谷歌发布 Muse：文字-图像生成的新 SOTA 模型](../../2023/01/2023-01-02-muse.md)
- [Anthropic 发布  3 系列：Opus 全面超越 GPT-4](../03/2024-03-04-claude3.md)
- [Multimodal AI 2025 GPT-4V Gemini Vision Claude Vision Comparison](../../2025/01/2025-01-30-multimodal-ai-2025.md)
- [OpenAI 推出强化微调（RFT）技术：o4-mini 可定制为领域专家](../../2025/05/2025-05-09-openai-rft-o4mini.md)
- [OpenAI 发布 GPT-5：全面超越所有前代](../../2025/05/2025-05-22-openai-gpt5-launch.md)

tags: [大模型, 推理, 多模态, 产品, 工具, GPT, Claude, OpenAI]
