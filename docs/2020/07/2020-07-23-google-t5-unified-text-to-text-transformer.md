<!--
{
  "title": "谷歌T5模型：Text-to-Text范式统一NLP任务",
  "date": "2020-07-23"
}
-->

# 谷歌T5模型：Text-to-Text范式统一NLP任务

📅 2020-07-23

<!-- 正文开始 -->
### 谷歌T5模型：Text-to-Text范式统一NLP任务

谷歌于2020年正式提出**T5（Text-to-Text Transfer[Transformer](../../glossary/terms/transformer.md)）**预训练语言模型，这是NLP领域首个将所有任务统一为文本到文本格式的通用框架。T5的核心设计理念极为优雅：无论翻译、摘要、问答还是情感分析，所有NLP任务都可以转化为"输入文本→输出文本"的处理模式。

T5基于Transformer的Encoder-Decoder架构构建，在无监督降噪任务上进行预训练。谷歌发布的论文《Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer》堪称业界最详尽的预训练模型综述，涵盖了超过100项消融实验，系统性地分析了模型架构、预训练目标、训练策略等关键因素。

实验表明，T5在多项NLP基准上取得了当时最优表现。其"Text-to-Text"的统一范式大大简化了模型的应用流程——开发者只需给不同任务添加特定前缀（如"summarize:"、"translate English to German:"），即可用同一个模型处理多种任务。T5的开源包括Base、Small、Large等多种规模版本，为研究和工业应用提供了灵活的選擇。

T5的提出标志着NLP领域向"通用人工智能"迈出了重要一步，为后续[GPT](../../glossary/terms/gpt.md)系列等大模型的爆发式发展奠定了方法论基础。
<!-- 正文结束 -->
