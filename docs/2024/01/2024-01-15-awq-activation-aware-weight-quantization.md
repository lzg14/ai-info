# AWQ：激活感知量化——高质量 INT4 量化的新方法

## 摘要

AWQ（Activation-Aware Weight Quantization，激活感知量化）是由 MIT Han Lab 提出的高效大模型量化方法，核心思想是保留与大激活值相乘的重要权重精度，其余权重量化到 INT4，实现高质量低显存推理。

## 概念解析

大模型量化通常将权重从 FP16/FP32 压缩到 INT8、INT4 以节省显存和加速推理。但简单量化会严重损害模型质量。AWQ 的关键洞察是：权重与大的激活值相乘时，量化误差会被放大，因此这些权重必须用更高精度保存。

AWQ 通过分析激活值分布，自动识别重要权重并保持其精度，其余权重量化到 INT4。实验表明，AWQ 在 4 位量化下相较于 [GPT](../../../glossary/terms/gpt.md)Q 等方法能显著保持模型质量，是目前最流行的本地大模型量化方案之一，尤其适合在消费级 GPU（如 RTX 3090、Mac M系列）上运行 7B-70B 参数模型。








## 相关文章
- [微软与英伟达发布 Megatron Turing-NLG：5300亿参数史上最大NLP模型](../../2021/10/2021-10-28-megatron-turing-nlg-530b.md)
- [OpenAI o1草莓模型发布：开启推理时间扩展范式](../09/2024-09-13-openai-o1-strawberry.md)
- [Google开源TensorFlow：分布式计算性能领先](../../2015/03/2015-11-01-Google开源TensorFlow-分布式计算性能领先.md)
- [NVIDIA DGX-2发布，全球最大GPU计算系统算力达2PFLOPS](../../2018/03/2018-03-28-NVIDIA-DGX-2发布全球最大GPU计算系统.md)
- [无标题](../../2019/02/2019-02-22-openai-clip-text-image-contrastive.md)

tags: [大模型, 推理, GPU, 论文, GPT, Transformer, Google, 微软]