# LLaMA 开源：Meta「小」模型引发开源大模型浪潮

## 摘要

2022 年 2 月，Meta AI 发布 LLaMA（Large Language Model Meta AI）——一套参数从 70 亿到 650 亿的基础语言模型。LLaMA-13B 在多数基准测试中表现优于 GPT-3（175B），但参数量仅为后者的约 1/13。Meta 仅公开了模型权重，LLaMA 的开源直接引爆了此后全球开源大模型的蓬勃发展。

## 核心意义

**「小」模型大能力：** LLaMA 证明了「在更多token上训练的更小模型」可以优于「大但训练不足的模型」，为后续 Mistral、Alpaca、Vicuna 等开源模型提供了路线图。

**开源生态引爆：** LLaMA 开源后，全球开发者迅速基于它微调出 Alpaca（斯坦福）、Vicuna（LMU慕尼黑）、Koala 等对话模型，开源社区第一次拥有了能与 [GPT-3.5](../../../glossary/terms/gpt.md) 正面竞争的基础模型。

**[LLaMA](../../../glossary/terms/llama.md).cpp 的诞生：** Georgi Gerganov 开发了 llama.cpp——让 LLaMA 能在 MacBook 等消费级设备上本地运行的量化推理工具，使大模型「本地化部署」成为可能。

## 后续影响

2023年，Meta 继续推出 LLaMA 2（开源可商用），LLaMA 3（405B 参数），成为全球最具影响力的开源大模型系列。

## 点评

LLaMA 是 2022 年最重要的开源事件之一——它证明了「开源模型可以在性能上逼近闭源模型」，彻底改变了 AI 行业的竞争格局。








## 相关文章
- [Stability AI发布Stable Diffusion开源模型](../05/2022-05-18-stability-ai-stable-diffusion-open-source.md)
- [ControlNet实现AI图像精准控制](../12/2022-12-20-controlnet-ai-image-condition-control.md)
- [Stable Diffusion XL 1.0正式发布：AI图像生成新标杆](../../2023/04/2023-04-17-stable-diffusion-xl-release.md)
- [AI 发布 7B 模型：欧洲 AI 独角兽崛起](../../2023/09/2023-09-29-mistral-ai.md)
- [DeepSeek V2发布：国产MoE模型性能比肩GPT-4、价格仅百分之一](../../2024/05/2024-05-07-deepseek-v2-release.md)

tags: [大模型, 开源模型, 闭源模型, 推理, 开源, 工具, GPT, Meta]
