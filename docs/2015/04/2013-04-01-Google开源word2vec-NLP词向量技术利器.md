# Google开源word2vec：NLP词向量技术利器

注：word2vec由Tomas Mikolov等人在2013年发表，Google于2013年开源。本段记录其在2015年前后的广泛影响。

## 核心原理

word2vec通过浅层神经网络学习词的分布式表示（词向量），将语义相似的词映射到向量空间中相近的位置。它能够捕捉"king - man + woman ≈ queen"这样的语义关系。

## 两种架构

- **Skip-gram**：用中心词预测周围上下文
- **CBOW**：用周围上下文预测中心词

## NLP的革命

word2vec是NLP领域的重大突破：首次将词转化为稠密向量，捕捉语义关系。在此之前，NLP依赖稀疏的词袋模型（Bag of Words），无法表达词的语义关系。

## 后续发展

word2vec启发了GloVe、FastText等词向量方法，最终演变为[BERT](../../../glossary/terms/bert.md)、[GPT](../../../glossary/terms/gpt.md)等预训练语言模型。词向量技术成为现代NLP的基石。








## 相关文章
- [ELMo刷新NLP预训练模型认知，上下文语义理解突破](../../2018/02/2018-02-15-ELMo刷新NLP预训练模型认知上下文语义理解突破.md)
- [NIPS 2014：注意力机制开创语言模型新时代](../../2014/03/2014-12-01-NIPS-2014-注意力机制开创语言模型新时代.md)
- [OpenAI Releases GPT-2 1.5B Language Model](../../2019/02/2019-02-14-gpt2-release.md)
- [无标题](../../2019/07/2019-07-26-roberta-dynamic-mask-pre-training.md)
- [ELECTRA: 判别式预训练文本编码器](../../2020/03/2020-03-23-electra-pre-training-text-encoders.md)

tags: [开源, BERT, GPT, Google, 神经网络, 上下文, 深度学习, AlphaGo]