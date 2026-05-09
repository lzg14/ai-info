# GitHub Copilot 雏形：OpenAI Codex 代码生成研究预览

## 摘要

2020 年，OpenAI 展示了一项基于 [GPT](../../../glossary/terms/gpt.md)-3 的代码生成研究——这是 GitHub Copilot 的技术前身。只需给出一段英文描述，模型就能生成对应代码，甚至能根据注释补全整段函数。

## 技术原理

**基于 GPT-3 微调：** 使用 GitHub 上数十亿行公开代码进行微调，让模型学习代码的「语法」与「逻辑」。输入自然语言描述，输出可执行代码。

**少样本学习：** GPT-3 核心能力在于「Few-shot」——给出几个示例后，模型能泛化到新任务，无需额外训练。

## 产业影响

这次展示直接促成了 GitHub Copilot 的产品化（2021 年正式发布）。AI 写代码从「研究课题」变为「生产力工具」，开启了一场软件开发范式的变革。








## 相关文章
- [GitHub Copilot发布：AI驱动的代码补全工具登场](../06/2020-06-17-github-copilot-ai-code-generator.md)
- [GitHub Copilot X 发布： 驱动 AI 结对编程时代](../../2023/03/2023-03-22-github-copilot-x.md)
- [OpenAI正式推出-3商用API，开启AI应用新时代](../06/2020-06-11-openai-gpt3-api-commercial.md)
- [GitHub Copilot 技术预览发布：AI 写代码从梦想走进现实](../11/2020-11-10-github-copilot-preview.md)
- [OpenAI开源PyTorch版-2实现](../../2022/05/2022-05-31-openai-gpt2-pytorch-release.md)

tags: [代码生成, GitHub, 产品, 工具, GPT, OpenAI, 编程, 开源]
