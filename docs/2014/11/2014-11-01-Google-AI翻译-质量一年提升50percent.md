# Google AI翻译：质量一年提升50%

2014年，Google宣布其翻译系统的质量在过去一年内提升了50%——这一进步来自深度学习替代传统统计机器翻译（SMT）。Google团队引入了基于循环神经网络（RNN）的端到端翻译模型，显著提升了翻译的自然度和准确率。

## 从SMT到NMT

Google之前的翻译系统使用统计机器翻译（SMT），需要大量人工设计的特征和独立组件。Google团队开发的神经机器翻译（NMT）用一个端到端的序列到序列（Seq2Seq）RNN模型替代了SMT的多个组件，大幅简化了系统。

## 技术架构

NMT使用双向RNN作为编码器，将源语言句子编码为上下文向量；另一个RNN作为解码器，逐词生成目标语言句子。注意力机制（Attention）使解码器能够在生成每个词时"关注"源句子的不同部分，解决了长句翻译的难题。

## 后续发展

Google于2016年正式推出GNMT（Google Neural Machine Translation），将NMT全面应用于Google翻译。这标志着机器翻译正式进入深度学习时代，后续[Transformer](../../../glossary/terms/transformer.md)架构（2017年）更是在NMT基础上实现了质的飞跃。








## 相关文章
- [Bengio团队提出循环神经网络语言模型](../../2013/10/2013-10-18-bengio-rnn.md)
- [Michael Jordan推动深度学习理论发展](../../2013/07/2013-07-22-michael-jordan.md)
- [Word2Vec发布：词向量技术的突破](../../2013/08/2013-08-12-word2vec.md)
- [科学家用 AI 解读鲸鱼语言：跨物种对话的突破](../../2023/06/2023-06-28-whale-language.md)
- [Geoffrey Hinton深度学习先驱获机器学习最高荣誉](../../2012/01/2012-01-15-geoffrey-hinton-pioneer-award.md)

tags: [Transformer, Google, 深度学习, 神经网络, 上下文, 机器学习, Bengio, Hinton]