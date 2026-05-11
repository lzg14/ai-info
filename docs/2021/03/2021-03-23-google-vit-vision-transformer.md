<!--
{
  "title": "Google发布Vision (ViT)：一张图等价于16x16个词",
  "date": "2021-03-23"
}
-->

# Google发布Vision (ViT)：一张图等价于16x16个词

📅 2021-03-23

<!-- 正文开始 -->
Google AI团队提出了Vision Transformer（ViT），将Transformer架构成功应用于图像分类任务。该论文标题"An Image is Worth 16x16 Words"直接体现了其核心思想：把图像分割成16x16像素的小块，每块被视为一个"词"（token），然后像处理NLP任务一样用Transformer处理。这种方法摆脱了传统卷积神经网络（CNN）的束缚，证明了在大规模数据集预训练的ViT可以超越传统CNN。ViT的发布标志着视觉领域正式进入Transformer时代，为后续跨模态模型发展奠定重要基础。

论文由Alexey Dosovitskiy、Lucas Beyer、Alexander Kolesnikov等Google研究员共同完成，已发表于ICLR 2021会议，代码和预训练模型均已开源。
<!-- 正文结束 -->
