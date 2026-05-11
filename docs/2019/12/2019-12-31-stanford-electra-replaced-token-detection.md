<!--
{
  "title": "Stanford ELECTRA：替换令牌检测预训练超越BERT",
  "date": "2019-12-31"
}
-->

# Stanford ELECTRA：替换令牌检测预训练超越BERT

📅 2019-12-31

<!-- 正文开始 -->
## 基本信息

  * **日期** ：2019-12-31
  * **来源** ：Stanford / Google Brain / ICLR 2020
  * **URL** ：https://arxiv.org/abs/2003.10555
  * **主题** ：自然语言处理，预训练模型，自监督学习



## 内容摘要

2019年底，Stanford、Google Brain和DeepMind联合发布ELECTRA（Efficiently Learning an Encoder that Classifies Token Replacements Accurately），提出"替换令牌检测"（Replaced Token Detection）预训练任务，效率大幅超越BERT。ELECTRA不再预测被掩码的[词元](../../glossary/terms/token.md)，而是训练判别器识别替换过的词元，使模型从所有输入中学习而非仅从15%掩码位置学习。在同等算力下，ELECTRA在SQuAD 2.0上以小型模型超越BERT-large性能，被评为"2020年最具影响力的预训练模型之一"，并获得ICLR 2020最佳论文奖。
<!-- 正文结束 -->
