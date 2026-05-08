# Google 发布 Meena：史上最强对话 AI，26亿参数

## 摘要

2020 年 10 月，Google 发布 Meena，一个 26 亿参数的端到端神经对话模型。Meena 在「Sensibleness and Specificity Average（SSA）」指标上达到了人类平均水平的 79%，是当时最逼真的聊天机器人。

## 技术架构

**全 [Transformer](../../../glossary/terms/transformer.md)：** Meena 采用端到端的纯 Transformer 架构，没有人工规则，没有检索模块，完全依靠大规模预训练+微调。

**训练数据：** 341 GB 的对话文本，涵盖社交媒体、论坛、问答等多种场景。

## SSA 评估

人类基准约 86%（朋友对话场景），Meena 达到 79%，大幅领先当时其他聊天机器人（SOTA 约 56%）。

## 后续：LaMDA（2021）

Meena 是 LaMDA（Google 2021 年发布的对话大模型）的技术前身。LaMDA 将参数规模提升到 1370 亿。

## 点评

Meena 证明了「纯数据驱动」的对话系统可以达到接近人类的对话质量。它打破了「聊天机器人必须有知识库+规则引擎」的路径依赖。








## 相关文章
- [BERT爆发一年后：横扫NLP榜单的背后，预训练模型如何重塑行业](../../2018/10/2018-10-15-bert-one-year-industry-impact.md)
- [Vicuna 13B发布：开源对话模型的新选择](../../2023/04/2023-04-25-vicuna-13b-release.md)
- [BERT开源刷新NLP标准，预训练模型时代来临](../../2018/10/2018-10-11-BERT开源刷新NLP标准预训练模型时代来临.md)
- [Google BERT Model Release](../../2018/10/2018-10-11-google-bert-release.md)
- [无标题](../../2019/07/2019-07-26-roberta-dynamic-mask-pre-training.md)

tags: [大模型, 机器人, Transformer, Google, 开源, 榜单, BERT]