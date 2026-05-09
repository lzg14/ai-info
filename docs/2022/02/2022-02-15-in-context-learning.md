# 研究热潮：大模型「无需训练即可学习」的秘密

## 摘要

2022 年 2 月，斯坦福大学等机构的研究者发表论文，系统性地研究了大语言模型的「In-context Learning」（上下文学习，ICL）现象——即 GPT-3 等模型能够在不进行梯度更新的情况下，仅通过输入中的几个示例就学会执行新任务。这篇论文揭示了 ICL 的工作机制和影响因素，引发学术界对 LLM「学习能力本质」的新一轮讨论。

## 什么是 In-context Learning

In-context Learning 允许用户通过在 prompt 中提供几个「输入-输出示例」，让大语言模型「学会」执行新的任务模式，而无需对模型本身进行任何参数更新。

**示例：** 在 prompt 中写「狗→哺乳动物；猫→哺乳动物；蛇→」，模型即可预测蛇也是哺乳动物。

## 论文核心发现

**任务级别的泛化：** ICL 不仅能泛化到训练数据中见过的任务类型，还能泛化到完全新的任务。

**预测头的角色：** 研究者发现 [Transformer](../../../glossary/terms/transformer.md) 的「线性头」（预测下一个 token 的线性层）对 ICL 能力至关重要。

**规模依赖：** ICL 能力随模型规模增大而显著提升，小模型（≤ 1B 参数）几乎不具备 ICL 能力。

## 点评

In-context Learning 是 [GPT](../../../glossary/terms/gpt.md)-3 最引人入胜的特性之一。它让「AI 学习新任务」的方式从「改变参数」变成了「改变提示」，这可能是通向通用人工智能的重要线索之一。








## 相关文章
- [EleutherAI开源GPT-Neo对抗OpenAI垄断](../../2020/08/2020-08-10-eleutherai-gpt-neo-open-source.md)
- [Chinchilla:Training Compute-Optimal Large Language Models](../03/2022-03-29-chinchilla-deepmind.md)
- [Mistral 7B技术解析：欧洲AI独角兽的首款开源力作](../../2023/09/2023-09-25-mistral-7b-technical-details.md)
- [无标题](../../2019/07/2019-07-26-roberta-dynamic-mask-pre-training.md)
- [GPT-2 全面开源：15亿参数模型正式开放](../../2020/02/2020-02-14-gpt2-open-source.md)

tags: [LLM, 学术, 论文, 大模型, Transformer, GPT, 上下文, 开源]
