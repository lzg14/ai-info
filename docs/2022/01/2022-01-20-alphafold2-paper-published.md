# DeepMind AlphaFold2 论文正式发表：蛋白质结构预测进入「实验精度」时代

## 摘要

2022 年 1 月，DeepMind 在 Nature 正式发表 AlphaFold2 论文——《Highly accurate protein structure prediction with AlphaFold》，全面公开了 AlphaFold2 的技术细节。该论文被评为 Nature 2021 年度封面文章，并被引用超过 2 万次，成为 AI for Science 领域被引量最高的论文之一。

## 核心技术解析

**Evoformer 架构：** AlphaFold2 使用新颖的 Evoformer 模块，将蛋白质序列的进化信息和氨基酸残基空间距离信息进行联合建模，这是实现「实验精度」预测的关键。

**[注意力机制](../../../glossary/terms/attention-mechanism.md)：** 48 个注意力头，8 个 Evoformer 堆叠层，能捕捉蛋白质序列中远距离的氨基酸相互作用。

**端到端学习：** 直接从原始的多序列对比（MSA）输入，输出原子级精度的三维坐标，无需人工干预。

## 历史意义

《Nature》这样评价：「这可能是继 DNA 双螺旋结构之后，生物学领域最重要的科学成就之一。」

## 点评

AlphaFold2 论文的正式发表，标志着蛋白质结构预测问题「从技术突破到学术共识」的完成。








## 相关文章
- [AlphaFold 解决50年难题，入选《自然》年度十大科学发现](../../2020/12/2020-12-08-alphafold-nature-top10.md)
- [DeepMind AlphaFold2 开源：破解蛋白质折叠难题，生物科学进入新纪元](../../2021/07/2021-07-16-alphafold2-open-source.md)
- [AlphaFold2 登上《科学》封面：AI 预测蛋白质结构入选年度十大突破](../../2021/07/2021-07-17-alphafold-roseTTAFold-science.md)
- [AlphaFold3 发布：DeepMind AI 预测所有生命分子结构](../../2024/05/2024-05-08-alphafold3-release.md)
- [DeepMind 解锁 98% 人类蛋白质组：AlphaFold2 扩大开源范围](../../2021/07/2021-07-16-alphafold2-unlocks-human-proteome.md)

tags: [学术, 论文, Nature, AlphaFold, 蛋白质, 开源]