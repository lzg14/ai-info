# 谷歌开源ELECTRA：完胜BERT的高效预训练模型

### 谷歌开源ELECTRA：完胜BERT的高效预训练模型

谷歌于2020年3月正式开源ELECTRA预训练语言模型，这是一款被业界称为"完胜BERT"的高效NLP模型。ELECTRA的核心创新在于提出了**替换令牌检测（Replaced Token Detection, RTD）**预训练任务，取代了BERT传统的掩码语言模型（MLM）。

传统的BERT在预训练时随机选择15%的单词进行掩码，仅对这些被掩盖的词进行预测，导致训练效率较低。而ELECTRA训练两个[Transformer](../../../glossary/terms/transformer.md)模型：生成器负责替换序列中的token，判别器则需要判断当前token是否为替换而来。这种"判别式"训练方式让ELECTRA能够从每一个输入token中学习，显著提升了训练效率。

实验结果显示，ELECTRA只需要Ro[BERT](../../../glossary/terms/bert.md)a和XLNet约四分之一的计算量，就能在GLUE基准上达到同等性能。在SQuAD问答任务上更是取得了新突破。更令人惊喜的是，小规模的ELECTRA模型在单个GPU上训练仅需4天时间，精度就超过了OpenAI的[GPT](../../../glossary/terms/gpt.md)模型。

ELECTRA已作为TensorFlow开源模型发布，提供了多种规模的预训练语言表示模型供研究者和开发者使用。这一高效预训练范式为未来NLP模型的训练成本优化提供了新思路。








## 相关文章
- [Google BERT Model Release](../../2018/10/2018-10-11-google-bert-release.md)
- [OpenAI Releases Full GPT-2 1.5B Model](../../2019/11/2019-11-06-gpt2-full-release.md)
- [谷歌T5模型：Text-to-Text范式统一NLP任务](../07/2020-07-23-google-t5-unified-text-to-text-transformer.md)
- [NVIDIA 发布 H100 GPU：Hopper 架构推动 AI 算力新飞跃](../../2022/03/2022-03-22-nvidia-h100.md)
- [华为云发布盘古气象大模型：AI 天气预报超越传统数值模式](../../2022/11/2022-11-19-huawei-pangu-weather-model.md)

tags: [开源模型, GPU, 开源, Transformer, BERT, GPT, OpenAI, 榜单]
