# Google 发布 FLAN：指令微调让大模型零样本泛化能力大幅提升

## 摘要

2021 年 9 月，Google 发布 FLAN（Fine-tuned Language Net）——一种基于指令微调的大模型训练方法。通过在混合了多种任务的指令数据上进行微调，FLAN 让 1370 亿参数的 LaMDA 模型在不见过的任务上实现零样本泛化，大幅超越直接使用 GPT-3 的效果。

## 核心方法

**指令微调（[Instruction Tuning](../../../glossary/terms/instruction-tuning.md)）：** 在 60+ 个 NLP 任务上，将任务描述为自然语言指令（如「把这段文字翻译成法语」「判断这段评论的情感是正面还是负面」），然后在这些指令-答案对上微调预训练语言模型。

**泛化能力：** 微调后，模型能够理解从未见过的任务指令，并给出合理回答。这为后来的 ChatGPT/InstructGPT 奠定了方法论基础。

## 性能表现

FLAN 在未见过的任务上零样本设置下，显著优于 GPT-3 5-shot 和 SOTA 有监督模型，证明了「指令遵循能力」可以通过大规模多任务微调获得。

## 后续影响

FLAN 的方法后来被 Anthropic（[Constitutional AI](../../../glossary/terms/constitutional-ai.md)）、OpenAI（Instruct[GPT](../../../glossary/terms/gpt.md)）借鉴，成为 RLHF 之外最重要的模型对齐技术之一。

## 点评

FLAN 证明了「教会模型理解指令」比「教会模型做固定任务」更接近通用人工智能的目标。








## 相关文章
- [OpenAI发布InstructGPT基于人类反馈微调](../../2022/03/2022-03-04-openai-instructgpt-rlhf.md)
- [AI ：确保 AI 行为与人类意图一致](../../2022/03/2022-03-14-gpt4-alignment-ai-safety.md)
- [Anthropic推出Claude对话AI助手](../../2022/11/2022-11-18-anthropic-claude-conversational-ai.md)
- [Anthropic 发布 Claude：更安全的 AI 对话助手](../../2023/07/2023-07-07-claude-1.md)
- [4 Pro 发布：企业级旗舰](../../2025/05/2025-05-18-claude-4-pro-launch.md)

tags: [大模型, 对齐, GPT, ChatGPT, OpenAI, Google, Anthropic, Claude]