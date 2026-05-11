<!--
{
  "title": "Attention Is All You Need -  Architecture Published",
  "date": "2017-06-12"
}
-->

# Attention Is All You Need -  Architecture Published

📅 2017-06-12

<!-- 正文开始 -->
2017年6月，谷歌大脑（Google Brain）的八位研究人员发表了一篇名为《Attention Is All You Need》的开创性论文，这篇论文提出了一种全新的神经网络架构——Transformer。这一架构的诞生彻底改变了自然语言处理（NLP）领域的发展轨迹，并成为了现代大语言模型的基础。

这篇论文的核心贡献在于提出了完全基于注意力机制（Attention Mechanism）的网络结构，从而摒弃了此前统治序列数据处理领域的循环神经网络（RNN）和卷积神经网络（CNN）。Transformer架构通过自注意力（Self-Attention）机制，能够并行处理序列中的所有位置，显著提升了训练效率，同时在翻译任务上创造了多项新的性能记录。

Transformer架构主要由编码器（Encoder）和解码器（Decoder）两部分组成。编码器负责处理输入序列，解码器则生成输出序列。模型使用多头注意力（Multi-Head Attention）机制来捕捉不同位置的依赖关系，并通过位置编码（Positional Encoding）来引入序列顺序信息。这种设计使得Transformer能够有效地学习长距离依赖关系，这是此前RNN架构难以解决的问题。

这篇论文提出的Transformer架构迅速成为了现代NLP模型的基础，包括BERT、GPT系列、T5等知名模型都采用了Transformer架构。如今，Transformer已经超越了自然语言处理的范畴，被广泛应用于计算机视觉、语音识别、代码生成等多个领域。可以说，没有《Attention Is All You Need》这篇论文，就不会 有今天的[ChatGPT](../../glossary/terms/chatgpt.md)和其他革命性的人工智能应用。

### Attention Is All You Need Published (评分: 9.8/10)
<!-- 正文结束 -->
