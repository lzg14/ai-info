# GPT-3 论文发布： 首次系统提出

2020年5月，OpenAI发表GPT-3论文《Language Models are Few-Shot Learners》，首次系统定义了大模型语境下的Few-Shot Learning概念——在没有任何梯度更新的情况下，仅通过在提示(Prompt)中提供少量示例（通常1-10个），模型就能学会并执行新任务。

传统机器学习需要大量标注数据微调模型，而GPT-3展示了令人惊讶的Few-Shot能力：提供几个英译法示例，模型就能翻译从未见过的句子；提供几个问答示例，模型就能回答新问题。这证明了模型具有极强的跨任务泛化能力，不需要为每个新任务重新训练。

GPT-3拥有1750亿参数，在42项基准测试中的13项通过Few-Shot即可达到甚至超越当时最好的微调模型水平，震惊学术界。这一发现深刻影响了后续Prompt Engineering的发展，成为大模型区别于传统模型的核心能力之一，也为后来GPT-3 API的商业化模式奠定了基础。








## 相关文章
- [EleutherAI开源GPT-Neo对抗OpenAI垄断](../08/2020-08-10-eleutherai-gpt-neo-open-source.md)
- [GPT-2 Staged Release Strategy and  Debate](../../2019/08/2019-08-21-gpt2-staged-release.md)
- [GPT-2 全面开源：15亿参数模型正式开放](../02/2020-02-14-gpt2-open-source.md)
- [GPT-3 发布：1750亿参数，OpenAI 最大的赌注](2020-05-29-gpt3-launch.md)
- [OpenAI API正式开放商业化](../06/2020-06-22-openai-api-beta-launch.md)

tags: [大模型, API, 学术, 论文, GPT, OpenAI, 机器学习, LLM]