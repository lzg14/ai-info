# NVIDIA H100 发布：Hopper 架构开启 AI 算力新时代

## 摘要

2022 年 3 月，NVIDIA 发布 H100 GPU——基于全新 Hopper 架构的数据中心 GPU。H100 采用台积电 4nm 工艺，FP16 算力达到 3958 TFLOPS，是上一代 A100 的约 3 倍。H100 的 [Transformer](../../../glossary/terms/transformer.md) 引擎专门针对大语言模型训练进行了优化，成为大模型时代最重要的基础设施。

## 核心参数

| 指标 | H100 | A100（对比） |
|------|-------|------|
| 工艺 | 4nm (TSMC) | 7nm |
| FP16 算力 | 3958 TFLOPS | 312 TFLOPS |
| 显存 | 80GB HBM3 | 80GB HBM2e |
| NVLink 带宽 | 900 GB/s | 600 GB/s |
| 功耗 | 700W | 400W |

## Transformer 引擎

H100 内置第三代 Transformer 引擎，支持 FP8 计算精度，在不损失精度的情况下将 Transformer 模型的训练速度提升 6 倍。这对 GPT-3、[BERT](../../../glossary/terms/bert.md) 等大模型训练至关重要。

## 市场影响

H100 发布后迅速成为全球最抢手的 AI 芯片——云计算厂商、AI 实验室、量化交易机构争相采购。同时也加剧了全球 AI 芯片竞争格局（AMD MI250X、Google TPU v4、Amazon Trainium 等跟进）。

## 点评

H100 是大模型军备竞赛的「军火」——谁拥有更多 H100，谁就能训练更大的模型。这一逻辑直接推动了全球 AI 算力基础设施的疯狂投资。








## 相关文章
- [NVIDIA 发布 H100 GPU：Hopper 架构推动 AI 算力新飞跃](2022-03-22-nvidia-h100.md)
- [NVIDIA H100 GPU Architecture Launch](2022-03-22-nvidia-h100-gpu.md)
- [华为云发布盘古气象大模型：AI 天气预报超越传统数值模式](../11/2022-11-19-huawei-pangu-weather-model.md)
- [OpenAI o1草莓模型发布：开启推理时间扩展范式](../../2024/09/2024-09-13-openai-o1-strawberry.md)
- [Microsoft Research Asia Publishes Deep Residual Learning for Image Recognition](../../2015/12/2015-12-10-microsoft-resnet-paper.md)

tags: [大模型, 芯片, GPU, 投资, TPU, Transformer, BERT, GPT]