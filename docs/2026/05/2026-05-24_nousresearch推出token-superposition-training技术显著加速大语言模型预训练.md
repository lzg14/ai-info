<!-- {"title": "NousResearch推出Token Superposition Training技术，显著加速大语言模型预训练", "url": "https://x.com/SiliconFlowAI/status/2054755824309076359", "source": "X：硅基流动 SiliconFlow (@SiliconFlowAI)", "source_url": "", "publish_date": "2026-05-24", "score": null, "tags": "[\"论文\"]"} -->
# NousResearch推出Token Superposition Training技术，显著加速大语言模型预训练

📢 来源：X：硅基流动 SiliconFlow (@SiliconFlowAI)

> NousResearch发布了Token Superposition Training（TST），这是一种改进标准大语言模型预训练流程的方法。该技术无需改变模型架构、优化器、分词器或训练数据，即可在相同计算量（FLOPs）下实现2-3倍的训练时间加速。其核心是在训练的前三分之一阶段，让模型读取并预测连续的token包，对输入嵌入进行平均，并使用改进的交叉熵损失预测下一个token包；剩余训练时间则恢复为标准的下一个token预测。推理阶段的模型与传统预训练产生的模型完全相同。该方法已在270M、600M、3B的密集模型以及10B至1B的混合专家模型规模上得到验证。

🏷️ [ · " · 论 · 文 · " · ]

<!-- 正文开始 -->

NousResearch发布了Token Superposition Training（TST），这是一种改进标准大语言模型预训练流程的方法。该技术无需改变模型架构、优化器、分词器或训练数据，即可在相同计算量（FLOPs）下实现2-3倍的训练时间加速。其核心是在训练的前三分之一阶段，让模型读取并预测连续的token包，对输入嵌入进行平均，并使用改进的交叉熵损失预测下一个token包；剩余训练时间则恢复为标准的下一个token预测。推理阶段的模型与传统预训练产生的模型完全相同。该方法已在270M、600M、3B的密集模型以及10B至1B的混合专家模型规模上得到验证。

<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->

<!-- 相关文章结束 -->