# Switch Transformer — 谷歌发布万亿参数稀疏激活模型

# Switch Transformer — 谷歌发布万亿参数稀疏激活模型

2020年10月，Google Brain团队发表了Switch Transformer论文，提出了一种革命性的稀疏激活架构，将语言模型参数量推升至万亿级别。该模型基于"混合专家"（[Mixture of Experts](../../../glossary/terms/mixture-of-experts.md)，MoE）范式，通过动态激活不同子网络处理不同输入，在保持计算成本可控的同时实现参数规模的突破性扩展。

与传统的稠密激活不同，Switch [Transformer](../../../glossary/terms/transformer.md)的每个token仅激活少数专家网络，使计算效率大幅提升。这一设计理念深刻影响了后续大模型架构发展，为2021年后的万亿美元参数模型竞赛奠定了技术基础。








## 相关文章
- [无标题](../../2019/07/2019-07-26-roberta-dynamic-mask-pre-training.md)
- [NIPS 2014：注意力机制开创语言模型新时代](../../2014/03/2014-12-01-NIPS-2014-注意力机制开创语言模型新时代.md)
- [架构：Attention is All You Need](../../2017/06/2017-06-01-Transformer..-glossary-terms-transformer.md架构-.md)
- [架构：Attention is All You Need](../../2017/06/2017-06-Google-Transformer架构Attention-is-All-You-Need.md)
- [架构加速落地，NLP进入注意力机制时代](../../2018/07/2018-07-15-Transformer架构加速落地NLP进入注意力机制时代.md)

tags: [大模型, 论文, Transformer, Google, 深度学习, BERT]
