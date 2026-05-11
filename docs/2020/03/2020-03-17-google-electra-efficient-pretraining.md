<!--
{
  "title": "谷歌开源ELECTRA：完胜BERT的高效预训练模型",
  "date": "2020-03-17"
}
-->

# 谷歌开源ELECTRA：完胜BERT的高效预训练模型

📅 2020-03-17

<!-- 正文开始 -->
### 谷歌开源ELECTRA：完胜BERT的高效预训练模型

谷歌于2020年3月正式开源ELECTRA预训练语言模型，这是一款被业界称为"完胜BERT"的高效NLP模型。ELECTRA的核心创新在于提出了**替换令牌检测（Replaced Token Detection, RTD）** 预训练任务，取代了BERT传统的掩码语言模型（MLM）。

传统的BERT在预训练时随机选择15%的单词进行掩码，仅对这些被掩盖的词进行预测，导致训练效率较低。而ELECTRA训练两个[Transformer](../../glossary/terms/transformer.md)模型：生成器负责替换序列中的token，判别器则需要判断当前token是否为替换而来。这种"判别式"训练方式让ELECTRA能够从每一个输入token中学习，显著提升了训练效率。

实验结果显示，ELECTRA只需要Ro[BERT](../../glossary/terms/bert.md)a和XLNet约四分之一的计算量，就能在GLUE基准上达到同等性能。在SQuAD问答任务上更是取得了新突破。更令人惊喜的是，小规模的ELECTRA模型在单个GPU上训练仅需4天时间，精度就超过了OpenAI的[GPT](../../glossary/terms/gpt.md)模型。

ELECTRA已作为TensorFlow开源模型发布，提供了多种规模的预训练语言表示模型供研究者和开发者使用。这一高效预训练范式为未来NLP模型的训练成本优化提供了新思路。
<!-- 正文结束 -->
