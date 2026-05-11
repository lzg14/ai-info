<!--
{
  "title": "InstructGPT:aligning language models to follow instructions",
  "date": "2022-01-27"
}
-->

# InstructGPT:aligning language models to follow instructions

📅 2022-01-27

<!-- 正文开始 -->
InstructGPT是OpenAI于2022年1月发布的研究成果，标题为"Training language models to follow instructions with human feedback"。这篇论文标志着大语言模型（LLM）发展的重要转折点，首次系统性地提出了通过人类反馈微调（RLHF，[Reinforcement Learning from Human Feedback](../../glossary/terms/reinforcement-learning-from-human-feedback.md)）技术来解决AI模型"对齐问题"（Alignment Problem）的方法论。InstructGPT的核心思想后来成为ChatGPT和GPT-4等产品成功的关键技术基础。

传统的语言模型在训练过程中优化的是"预测下一个token"这一目标，这与用户期望的"有用、安全且遵循指令"的行为之间存在显著差异。这种差异被称为"对齐税"（Alignment Tax）——为了让模型更加对齐，需要在某些性能指标上做出牺牲。OpenAI的研究人员意识到，如果不解决这个对齐问题，语言模型无论规模多大，都难以成为真正有用的助手。

InstructGPT提出的方法分为三个阶段的训练过程。第一阶段是监督微调（[Supervised Fine-Tuning](../../glossary/terms/supervised-fine-tuning.md)，SFT），研究人员让标注人员编写他们希望模型如何回应的示例，然后在这些示范上微调一个预训练的语言模型。第二阶段是训练一个奖励模型（Reward Model），同样由标注人员对同一prompt的多个输出进行排序，基于这些排序数据训练一个奖励模型来预测人类偏好。第三阶段是使用奖励模型作为奖励信号，通过近端策略优化（PPO）算法进一步微调SFT模型，使其生成更符合人类期望的回复。

实验结果表明，InstructGPT在多个方面显著优于原始GPT-3模型。尽管模型参数规模比GPT-3小了100多倍（1.3B参数对比175B参数），InstructGPT在人类评估中仍然表现更好。这意味着RLHF不仅改善了模型的对齐性，实际上也是一种更高效利用模型容量的方法。同时，研究人员发现RLHF能够有效减少模型产生有害输出的倾向，同时保持其在核心任务上的能力。

InstructGPT论文的一个重要发现是揭示了语言模型的几个关键特性。首先，模型规模的增大并不能自动解决对齐问题——更大的模型在遵循指令方面并不一定更好，除非经过专门的微调。其次，RLHF能够显著改善模型的真实性和信息性，减少"幻觉"（[Hallucination](../../glossary/terms/hallucination.md)）现象。第三，对齐技术具有良好的泛化能力，在不同类型的任务上都表现出一致性。

这篇论文的影响远远超出了学术范畴。它为OpenAI后续产品（如[ChatGPT](../../glossary/terms/chatgpt.md)和GPT-4）的成功奠定了技术基础，同时也被整个AI学术界和产业界广泛采纳作为训练对话AI的标准方法。Anthropic的[Claude](../../glossary/terms/claude.md)、DeepMind的Sparrow等竞品模型也采用了类似的RLHF框架。Instruct[GPT](../../glossary/terms/gpt.md)证明了"让AI更好地理解人类意图"这一目标不仅在技术上是可行的，而且对于构建真正有用的AI系统至关重要。
<!-- 正文结束 -->
