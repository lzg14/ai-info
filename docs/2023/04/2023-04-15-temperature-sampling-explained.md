# ：控制 LLM 输出随机性的生成温度

## 摘要

Temperature（温度）是控制大语言模型输出随机性的核心参数。Temperature = 0 时输出几乎完全确定，值越高输出越随机多样，是 Prompt Engineering 中最重要的调参手段之一。

## 概念解析

Temperature 的数学原理是：在 softmax 生成下一个 token 时，模型计算所有可能词的概率分布；Temperature 参数缩放这些 logits（概率前的原始分数），从而改变概率分布的形状。

Temperature = 0 时，模型总是选择概率最高的 token（贪婪解码），输出几乎完全确定，适合精确问答、代码生成等需要稳定输出的场景。Temperature 越高，概率分布越「平坦」，低概率词被选中的机会越大，输出越随机多样。Temperature = 1.0 时保持原始概率分布；> 1.0 时进一步增加随机性，< 1.0 时更加确定。

一般用法：创意写作/头脑风暴用 0.7-0.9；精确问答/代码生成用 0.0-0.3；翻译/摘要用 0.3-0.6。Temperature 与 [Top-p](../../../glossary/terms/top-p.md) 通常二选一使用，不可同时调高。








## 相关文章
- [Microsoft发布Salamander：新一代开源大语言模型](../09/2023-09-18-salamander-release.md)
- [GPT-2 全面开源：15亿参数模型正式开放](../../2020/02/2020-02-14-gpt2-open-source.md)
- [EleutherAI开源GPT-Neo对抗OpenAI垄断](../../2020/08/2020-08-10-eleutherai-gpt-neo-open-source.md)
- [Google发布Switch Transformer：首个万亿级参数语言模型](../../2021/01/2021-01-11-switch-transformer-trillion-parameters.md)
- [NVIDIA推出H100 GPU Hopper架构](../../2022/03/2022-03-22-nvidia-h100-hopper-architecture.md)

tags: [代码生成, LLM, 大模型, 开源, GitHub, Transformer, OpenAI, 深度学习]
