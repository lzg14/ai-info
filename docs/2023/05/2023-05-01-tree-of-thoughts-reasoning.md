# ：让 AI 在思维树上搜索最优推理路径

## 摘要

Tree of Thoughts（思维树，简称 ToT）是普林斯顿大学和 DeepAI 于 2023 年提出的推理框架，核心思想是将 [Chain of Thought](../../../glossary/terms/chain-of-thought.md)（CoT）的线性思考扩展为树状搜索结构，让 AI 在复杂问题求解时能够探索多条推理路径，找到最优解决方案。

## 概念解析

CoT 让模型一步一步往下想（线性），适合简单推理任务；但面对复杂问题（如需要探索、回溯、规划）时，线性思考容易陷入局部最优。ToT 的做法是：在推理的每一步，模型生成多个可能的「思考分支」，形成一棵思维树，然后通过搜索算法（广度优先或深度优先）评估每个分支的可行性，最终选择最优路径继续。

类比：CoT 像是在迷宫中沿着一条路一直走到底；ToT 则是在每个路口探索多条可能的方向，找到通往出口的最佳路线。实验表明，ToT 在需要复杂规划的任务（如24点游戏、创意写作、单词修改）上显著优于 CoT 和贪婪解码。








## 相关文章
- [无标题](../../2019/06/2019-06-20-xlnet-carnegie-mellon-pretrained.md)
- [IBM Watson：医疗领域大放异彩](../../2013/04/2013-04-01-IBM-Watson-医疗领域大放异彩.md)
- [NIPS 2014：注意力机制开创语言模型新时代](../../2014/03/2014-12-01-NIPS-2014-注意力机制开创语言模型新时代.md)
- [架构：Attention is All You Need](../../2017/06/2017-06-01-Transformer..-glossary-terms-transformer.md架构-.md)
- [Attention Is All You Need -  Architecture Published](../../2017/06/2017-06-12-transformer-attention-is-all-you-need.md)

tags: [推理, 论文, Transformer, BERT, Google]