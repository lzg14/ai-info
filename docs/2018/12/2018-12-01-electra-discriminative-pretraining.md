# ELECTRA刷新NLP预训练效率：斯坦福团队提出判别式预训练新范式

斯坦福大学与Google Brain联合团队发布了ELECTRA预训练模型，提出以判别式任务替代传统的掩码语言建模（MLM）。与[BERT](../../../glossary/terms/bert.md)采用"填空"方式不同，ELECTRA训练一个生成器对token进行替换，再让判别器识别哪些位置被替换过。这一"替换token检测"（RTD）任务使模型能够学习每一个输入token的表示，而非仅关注被掩码的15%部分。

实验表明，在相同算力下ELECTRA远超BERT：在GLUE基准上，仅用BERT-Large四分之一的参数即可达到相近效果；小规模版本的ELECTRA-Small更在多项任务上超越BERT-Base。2020年3月发布论文后，ELECTRA很快被ICLR 2020收录，并成为NLP预训练领域的重要里程碑，证明"判别式"预训练任务在效率和效果上均可优于生成式MLM。

**来源**：[ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators](https://arxiv.org/abs/2003.10555)








## 相关文章
- [NIPS 2014：注意力机制开创语言模型新时代](../../2014/03/2014-12-01-NIPS-2014-注意力机制开创语言模型新时代.md)
- [架构：Attention is All You Need](../../2017/06/2017-06-01-Transformer..-glossary-terms-transformer.md架构-.md)
- [Attention Is All You Need -  Architecture Published](../../2017/06/2017-06-12-transformer-attention-is-all-you-need.md)
- [架构：Attention is All You Need](../../2017/06/2017-06-Google-Transformer架构Attention-is-All-You-Need.md)
- [架构加速落地，NLP进入注意力机制时代](../07/2018-07-15-Transformer架构加速落地NLP进入注意力机制时代.md)

tags: [论文, BERT, Google, Transformer]