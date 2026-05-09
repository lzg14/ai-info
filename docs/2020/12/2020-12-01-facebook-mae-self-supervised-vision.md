# Facebook开源MAE自监督视觉预训练方法

2020年12月，Facebook AI研究院发布Masked Autoencoder（MAE），这是一个简单有效的自监督视觉预训练方法，在ImageNet上以75.8%的Top-1准确率刷新记录，超越此前所有有监督预训练方法。

MAE的灵感来自自然语言处理中的[BERT](../../../glossary/terms/bert.md)，使用随机遮蔽（Masked）策略——将输入图像的随机patch遮蔽掉75%，然后让模型重建缺失像素。核心设计包含不对称的编码器-解码器架构，编码器仅处理可见patch，解码器负责重建完整图像。MAE证明了一个简单想法配合精心设计即可显著超越复杂方法，且预训练效率比对比学习高3倍以上。该工作迅速成为视觉自监督学习的新标杆，影响深远。








## 相关文章
- [BigScience 宣布开源大模型 BLOOM 计划](../../2021/10/2021-10-15-bigscience-bloom-announced.md)
- [BigScience Workshop 启动：全球协作训练开源大模型BLOOM](../11/2020-11-17-bigscience-workshop-bloom-open-source-mllm.md)
- [TII发布Falcon 180B：最大开源语言模型之一](../../2023/09/2023-09-08-tii-falcon-180b.md)
- [BERT爆发一年后：横扫NLP榜单的背后，预训练模型如何重塑行业](../../2018/10/2018-10-15-bert-one-year-industry-impact.md)
- [无标题](../../2019/07/2019-07-26-roberta-dynamic-mask-pre-training.md)

tags: [开源, BERT, 榜单, Google, 深度学习, LLM, 大模型]
