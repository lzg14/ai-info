# Facebook发布Blender聊天机器人，开创开源对话AI新纪元

2020年4月，Facebook AI研究院发布了Blender聊天机器人，这是当时规模最大、功能最强的开源对话系统。Blender融合了移情对话、个性保持、知识整合等多种能力，在多项对话指标上显著超越了Google Meena等同期系统。研究团队采用了94亿参数的自回归 [Transformer](../../../glossary/terms/transformer.md) 架构，并通过大规模对话数据进行训练。

Blender的核心技术亮点在于其多技能融合策略。团队将任务分解为情感支持、个人特质维护、深度知识问答等子任务，分别训练后再通过蒸馏与融合技术整合为统一模型。论文《Recipes for building an open-domain chatbot》详细描述了相关训练方法，包括使用移情对话数据集改善情感识别能力，以及通过人格数据集注入一致的对话风格。

Blender的发布具有重要开源意义。它是首个将多种对话能力整合到单一模型中且完全开源的大规模对话系统，为后续开源对话模型的发展树立了标杆。同时，Blender也推动了对话AI评估标准的发展，Facebook提出的评估维度后来被广泛应用于对话系统的评测中。这一成果表明，多技能融合而非单一能力优化，是构建实用对话机器人的可行路径。








## 相关文章
- [无标题](../../2019/10/2019-10-24-google-t5-text-to-text-unified.md)
- [NIPS 2014：注意力机制开创语言模型新时代](../../2014/03/2014-12-01-NIPS-2014-注意力机制开创语言模型新时代.md)
- [无标题](../../2019/07/2019-07-26-roberta-dynamic-mask-pre-training.md)
- [BERT Dominates NLP Throughout 2019](../../2019/12/2019-12-31-bert-year-in-review.md)
- [Google 发布 Meena：史上最强对话 AI，26亿参数](../10/2020-10-06-google-meena.md)

tags: [开源, 论文, 机器人, 评测, Transformer, Google, BERT, AlphaGo]