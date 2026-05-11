<!--
{
  "title": "Neural Machine Translation by Jointly Learning to Align and Translate",
  "date": "2014-09-03"
}
-->

# Neural Machine Translation by Jointly Learning to Align and Translate

📅 2014-09-03

<!-- 正文开始 -->
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio published "Neural Machine Translation by Jointly Learning to Align and Translate" in September 2014, introducing the attention mechanism that revolutionized sequence-to-sequence modeling in natural language processing. This paper addressed a fundamental limitation of encoder-decoder architectures: the need to compress all information from source sequences into fixed-size vectors, which became increasingly problematic as sequences grew longer.

The proposed model replaced the fixed context vector with a dynamic mechanism that allowed the decoder to automatically search for relevant parts of the input sequence when generating each output token. Instead of encoding the entire source sentence into a single vector, an bidirectional RNN encoder produced a sequence of hidden states, each corresponding to a specific word in the source. During decoding, the model computed attention weights that indicated which source hidden states were most relevant for predicting the next target word.

This attention mechanism operated through a learned alignment model that scored the compatibility between the decoder's current hidden state and each source encoder hidden state. These alignment scores were normalized to produce attention weights, which were then used to compute a weighted context vector as the sum of source hidden states multiplied by their attention weights. This context vector, combined with the decoder's current state and the previously generated word, produced the probability distribution over the next target token.

The innovation enabled neural translation models to handle much longer sequences without the information bottleneck that plagued previous approaches. More importantly, the learned alignment provided interpretable insight into how the model operated—visualizing attention weights revealed precisely which source words influenced each target word's generation. This interpretability proved invaluable for debugging and understanding neural translation behavior.

The paper also demonstrated that the encoder's bidirectional hidden states were essential for capturing both forward and backward context around each source word. This bidirectional encoding became standard practice in subsequent NLP models, ensuring that each position's representation incorporated information from the entire surrounding context.

Bahdanau et al.'s attention mechanism fundamentally changed neural network architecture design. The soft alignment between input and output sequences provided a template for multi-modal reasoning, memory access in neural Turing machines, and graph neural network message passing. When [Transformer](../../glossary/terms/transformer.md) architectures arrived in 2017, they replaced RNNs entirely but retained attention as the core computation mechanism, extending the paradigm to self-attention across all input positions simultaneously.

The attention mechanism's success also influenced how researchers approached sequence modeling problems more broadly. The idea that neural networks could learn to dynamically focus on relevant parts of their input rather than processing everything uniformly proved generative across nearly every modality in machine learning, from image captioning to speech recognition to protein structure prediction.
<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->
- [Bengio团队提出循环神经网络语言模型](../../2013/10/2013-10-18-bengio-rnn.md)
- [Google AI翻译：质量一年提升50%](../11/2014-11-01-Google-AI翻译-质量一年提升50percent.md)
- [Microsoft Research Asia Publishes Deep Residual Learning for Image Recognition](../../2015/12/2015-12-10-microsoft-resnet-paper.md)
- [T5: 统一文本到文本迁移学习框架](../../2020/07/2020-07-06-t5-exploring-transfer-learning-limits.md)
- [科学家用 AI 解读鲸鱼语言：跨物种对话的突破](../../2023/06/2023-06-28-whale-language.md)
<!-- 相关文章结束 -->
