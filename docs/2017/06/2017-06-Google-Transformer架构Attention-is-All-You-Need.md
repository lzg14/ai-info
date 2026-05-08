# 架构：Attention is All You Need

2017年6月，Google Brain团队发表论文《Attention is All You Need》，提出Transformer架构。这篇论文彻底改变了自然语言处理的技术路线，成为现代大语言模型的基础架构，也是2020年代生成式AI爆发的理论起点。

## 核心创新：纯注意力机制

Transformer完全抛弃了此前的RNN和CNN结构，仅使用注意力机制来处理序列数据。其核心思想是：通过计算序列中任意两个位置之间的相关性（注意力权重），让模型能够直接"看到"序列中任意距离的token，不受顺序限制。

作者们提出了Multi-Head Attention（多头注意力）——将注意力分成多个"头"并行计算，每个头关注不同的语义关系。这一设计使模型能够在不同子空间同时学习不同类型的依赖关系。

## 并行训练，突破效率瓶颈

RNN的核心问题是难以并行化：必须按顺序处理序列，训练速度随序列长度线性增长。Transformer通过位置编码替代序列顺序，使整个序列可以并行处理，训练效率大幅提升。

这为模型的规模化创造了条件——更大的模型、更长的序列、更大规模的数据成为可能。

## 深远影响

Transformer催生了三大主流模型系列：GPT系列（仅解码器架构）、BERT系列（仅编码器架构）、T5系列（编码器-解码器架构）。2020年GPT-3、2022年[ChatGPT](../../../glossary/terms/chatgpt.md)、2023年GPT-4、[Claude](../../../glossary/terms/claude.md)系列、[Gemini](../../../glossary/terms/gemma.md)系列——所有这些突破的底层架构都是Transformer或其变体。

这篇论文被引用超过10万次，是深度学习历史上最具影响力的论文之一。








## 相关文章
- [架构：Attention is All You Need](2017-06-01-Transformer..-glossary-terms-transformer.md架构-.md)
- [NIPS 2014：注意力机制开创语言模型新时代](../../2014/03/2014-12-01-NIPS-2014-注意力机制开创语言模型新时代.md)
- [Attention Is All You Need -  Architecture Published](2017-06-12-transformer-attention-is-all-you-need.md)
- [架构加速落地，NLP进入注意力机制时代](../../2018/07/2018-07-15-Transformer架构加速落地NLP进入注意力机制时代.md)
- [OpenAI GPT-1 Paper Release](../../2018/06/2018-06-11-openai-gpt-1-release.md)

tags: [论文, Transformer, BERT, GPT, ChatGPT, Claude, Google, 深度学习]