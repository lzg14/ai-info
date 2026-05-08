### RLHF

**英文：** Reinforcement Learning from Human Feedback (RLHF)

**解释：**

RLHF 是一种训练大模型使其行为更符合人类意图的技术。步骤是：① 让模型生成多个回答，请人类对质量排序；② 用这些排序数据训练一个"奖励模型"（Reward Model）；③ 用奖励模型引导主模型通过强化学习（如 PPO 算法）优化输出质量。

**为什么重要：** ChatGPT 能做到"有帮助、无害、真实"，RLHF 功不可没。它是将人类价值观注入大模型的核心技术。
