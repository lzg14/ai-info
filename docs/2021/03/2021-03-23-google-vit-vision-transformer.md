# Google发布Vision (ViT)：一张图等价于16x16个词

Google AI团队提出了Vision Transformer（ViT），将Transformer架构成功应用于图像分类任务。该论文标题"An Image is Worth 16x16 Words"直接体现了其核心思想：把图像分割成16x16像素的小块，每块被视为一个"词"（token），然后像处理NLP任务一样用Transformer处理。这种方法摆脱了传统卷积神经网络（CNN）的束缚，证明了在大规模数据集预训练的ViT可以超越传统CNN。ViT的发布标志着视觉领域正式进入Transformer时代，为后续跨模态模型发展奠定重要基础。

论文由Alexey Dosovitskiy、Lucas Beyer、Alexander Kolesnikov等Google研究员共同完成，已发表于ICLR 2021会议，代码和预训练模型均已开源。








## 相关文章
- [Google深度学习项目取得突破进展](../../2013/06/2013-06-28-google-brain.md)
- [NIPS 2014：注意力机制开创语言模型新时代](../../2014/03/2014-12-01-NIPS-2014-注意力机制开创语言模型新时代.md)
- [Batch Normalization：2015年革命的前奏](../../2014/12/2014-12-01-Batch-Normalization-2015年革命的前奏.md)
- [Google开源word2vec：NLP词向量技术利器](../../2015/04/2013-04-01-Google开源word2vec-NLP词向量技术利器.md)
- [NIPS 2015：Deep Learning大爆发，深度学习全面扩张](../../2015/07/2015-12-01-NIPS-2015-Deep-Learning大爆发-深度学习全面扩张.md)

tags: [开源, 论文, Transformer, Google, 神经网络, 会议, 深度学习, AlphaGo]