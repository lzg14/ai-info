<!--
{
  "title": "Switch Transformer — 谷歌发布万亿参数稀疏激活模型",
  "date": "2020-10-28"
}
-->

# Switch Transformer — 谷歌发布万亿参数稀疏激活模型

📅 2020-10-28

<!-- 正文开始 -->

2020年10月，Google Brain团队发表了Switch Transformer论文，提出了一种革命性的稀疏激活架构，将语言模型参数量推升至万亿级别。该模型基于"混合专家"（[Mixture of Experts](../../glossary/terms/mixture-of-experts.md)，MoE）范式，通过动态激活不同子网络处理不同输入，在保持计算成本可控的同时实现参数规模的突破性扩展。

与传统的稠密激活不同，Switch [Transformer](../../glossary/terms/transformer.md)的每个token仅激活少数专家网络，使计算效率大幅提升。这一设计理念深刻影响了后续大模型架构发展，为2021年后的万亿美元参数模型竞赛奠定了技术基础。
<!-- 正文结束 -->
