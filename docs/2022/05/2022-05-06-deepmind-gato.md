# DeepMind Gato 亮相：通用AI智能体时代来临？

## 摘要

2022 年 5 月，DeepMind 发布 Gato——一个「通用」AI 智能体，能够处理 604 种不同任务，包括控制机械臂玩雅达利游戏、生成图像描述、进行对话等。Gato 被视为 DeepMind 迈向「通用人工智能（AGI）」的又一次重要尝试，引发了关于「通用智能」定义的广泛讨论。

## 技术架构

**多模态、多任务、多具身：** Gato 统一处理来自不同模态（文本、图像、机器人控制信号）的输入，并在不同类型的任务上共享同一个神经网络权重。

**训练数据：** Gato 在约 1.15 亿帧雅达利游戏、5800 万网页图文对、2000 小时机械臂操作视频等多种异构数据上联合训练。

**Auto-regressive [Transformer](../../../glossary/terms/transformer.md)：** 采用自回归 Transformer 架构，将所有输入 tokenize 后统一建模。

## 与 GPT 系列的区别

| 特性 | Gato | GPT-3/4 |
|------|------|---------|
| 架构 | Transformer | Transformer |
| 多模态 | 是 | 是（[GPT-4](../../../glossary/terms/gpt.md)） |
| 多具身 | 是 | 否 |
| 任务泛化 | 604种 | 开放式 |
| 商业化 | 否 | 是 |

## 争议

Yann LeCun 等顶尖研究者对 Gato 是否算「通用智能」持保留态度——Gato 虽能处理多类任务，但在每类任务上的深度远不及专门训练的模型。「广度」不等于「通用」。

## 点评

Gato 的意义不在于其在某项任务上达到 SOTA，而在于它证明了「多任务统一建模」的可行性——这是通往 AGI 的重要路径之一。








## 相关文章
- [Google Show and Tell：AI第一次能描述图片内容](../../2014/05/2014-05-01-Google-Show-and-Tell-AI第一次能描述图片内容.md)
- [无标题](../../2019/02/2019-02-22-openai-clip-text-image-contrastive.md)
- [Google发布LaMDA：面向对话应用的大型语言模型](../../2021/05/2021-05-18-google-lamd-a.md)
- [Google 发布 Imagen：文本到图像生成的新竞争者](2022-05-24-google-imagen.md)
- [OpenAI GPT-1 Paper Release](../../2018/06/2018-06-11-openai-gpt-1-release.md)

tags: [多模态, 机器人, Transformer, GPT, 神经网络, LeCun, OpenAI, Google]
