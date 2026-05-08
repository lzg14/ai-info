# T5: 统一文本到文本迁移学习框架

Google Research于2020年正式发布了T5（Text-to-Text Transfer [Transformer](../../../glossary/terms/transformer.md)）模型，该模型系统性地探索了迁移学习在自然语言处理领域的极限。T5提出了统一的Text-to-Text框架，将所有NLP任务（包括翻译、摘要、问答、文本分类等）都建模为文本到文本的转换问题。这种设计使得模型可以用相同的训练流程处理不同类型的任务，极大地简化了模型设计和训练流程。研究团队还发布了名为C4（Colossal Clean Crawled Corpus）的大规模预训练数据集，包含近万亿token的清洗后网页文本。T5在多个NLP基准测试上取得了当时最优成绩，其模型架构和训练方法对后续BART、mT5等模型产生了深远影响，被视为预训练语言模型发展的重要里程碑。








## 相关文章
- [Michael Jordan推动深度学习理论发展](../../2013/07/2013-07-22-michael-jordan.md)
- [Word2Vec发布：词向量技术的突破](../../2013/08/2013-08-12-word2vec.md)
- [Bengio团队提出循环神经网络语言模型](../../2013/10/2013-10-18-bengio-rnn.md)
- [Google AI翻译：质量一年提升50%](../../2014/11/2014-11-01-Google-AI翻译-质量一年提升50percent.md)
- [科学家用 AI 解读鲸鱼语言：跨物种对话的突破](../../2023/06/2023-06-28-whale-language.md)

tags: [Transformer, Google, 深度学习, 神经网络, Bengio, 理论]