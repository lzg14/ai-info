# AlphaGo Zero：白板学习，无需人类知识的围棋之神

2017年10月19日，DeepMind在《自然》期刊上发表论文，宣布推出AlphaGo Zero。这是AlphaGo系列的重大飞跃——它完全不需要人类棋谱，从"白板"状态开始自学，仅通过自我对弈在三天内达到了击败李世石版本AlphaGo Lee的水平，最终以100:0压倒性优势完胜前代。

## 从监督学习到纯强化学习

此前所有版本的AlphaGo都依赖人类棋谱数据进行训练：它们学习了数百万张人类高手的对局，再通过强化学习自我改进。但AlphaGo Zero彻底抛弃了这条路径。

新版系统从随机初始化开始，仅给定围棋规则，不提供任何人类知识。它通过自我对弈生成新的训练数据，不断优化策略网络和价值网络。这一转变的核心在于：算法本身的设计比训练数据的规模更重要。

## 100:0的压倒性胜利

AlphaGo Zero在40天的自我训练后，达到了超越所有前代版本的水平。对比数据令人震惊：
- 训练3天：AlphaGo Zero击败AlphaGo Lee（击败李世石版本）
- 训练40天：超越AlphaGo Master（击败柯洁版本）

整个过程没有引入任何外部数据或人类专家知识。

## 为什么这很重要

AlphaGo Zero的意义远超围棋本身。它证明了两个关键命题：第一，在某些领域，积累几十年人类知识可能反而是局限，从零开始可能走得更快；第二，强化学习结合精心设计的算法可以在没有监督信号的情况下达到超人类水平。

DeepMind联合创始人哈萨比斯表示，AlphaGo Zero的算法突破为解决蛋白质折叠（AlphaFold的方向）、设计新材料等现实世界问题提供了新思路。








## 相关文章
- [Google收购DeepMind：4亿美元重塑AI格局](../../2013/09/2013-01-26-Google收购DeepMind-4亿美元重塑AI格局.md)
- [AlphaFold Achieves Breakthrough in Protein Structure Prediction at CASP13](../12/2017-12-08-alphafold-casp13-protein-folding.md)
- [AlphaFold CASP13 Breakthrough](../../2018/11/2018-11-02-alphafold-casp13-breakthrough.md)
- [AlphaFold 蛋白质结构数据库正式开放：35万+蛋白质结构免费查](../../2020/09/2020-09-15-alphafold-db.md)
- [AlphaFold 蛋白质结构数据库扩展至2亿+结构：全球最全蛋白质图谱诞生](../../2022/07/2022-07-28-alphafold-db-200m.md)

tags: [论文, AlphaGo, AlphaFold, 围棋, 蛋白质, 收购, Google]