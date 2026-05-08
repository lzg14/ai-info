# 微软开源DeepSpeed深度学习优化库

2020年2月，微软研究院正式开源了DeepSpeed，一个用于加速深度学习训练的超大规模分布式优化库。DeepSpeed专注于解决大模型训练中的内存墙和计算效率问题，其核心创新在于ZeRO（Zero Redundancy Optimizer）技术——一种零冗余优化器，通过分片优化器状态、梯度和模型参数，显著降低了分布式训练时的内存占用。

DeepSpeed能够在单个GPU上训练超过130亿参数的模型，而传统方法受限于单卡显存往往只能训练十几亿参数。在多卡并行场景下，DeepSpeed展现出近乎线性的扩展效率，成为大模型训练的重要基础设施。该项目与PyTorch深度集成，提供了简单易用的API接口。DeepSpeed的开源填补了微软在深度学习基础设施领域的重要空白，也为开源社区提供了训练超大模型的技术方案，在[BERT](../../../glossary/terms/bert.md)、[GPT](../../../glossary/terms/gpt.md)-2等模型的训练中得到了广泛应用验证。








## 相关文章
- [NVIDIA DGX-2发布，全球最大GPU计算系统算力达2PFLOPS](../../2018/03/2018-03-28-NVIDIA-DGX-2发布全球最大GPU计算系统.md)
- [NVIDIA发布A100 GPU：AI算力提升20倍](../05/2020-05-14-nvidia-a100-gpu-ampere-architecture.md)
- [微软与英伟达发布 Megatron Turing-NLG：5300亿参数史上最大NLP模型](../../2021/10/2021-10-28-megatron-turing-nlg-530b.md)
- [《人工智能生成合成内容标识办法》9月施行，AI内容必须"亮明身份"](../../2025/09/2025-09-01-ai-content-identification-rules.md)
- [Google开源TensorFlow：分布式计算性能领先](../../2015/03/2015-11-01-Google开源TensorFlow-分布式计算性能领先.md)

tags: [大模型, GPU, 开源, API, BERT, GPT, 微软, 深度学习]