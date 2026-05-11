<!--
{
  "title": "Facebook开源DeiT数据高效图像",
  "date": "2020-07-15"
}
-->

# Facebook开源DeiT数据高效图像

📅 2020-07-15

<!-- 正文开始 -->
2020年7月，Facebook AI研究院开源了DeiT（Data-efficient Image Transformer），一个仅需1200万张图片即可达到85%以上Top-1准确率的图像Transformer。DeiT解决了ViT（Vision Transformer）需要大规模预训练数据的痛点。

DeiT采用创新的蒸馏训练策略，利用卷积网络作为教师模型指导学生Transformer的学习，显著降低了数据依赖。该模型在ImageNet上从头训练即可达到优秀性能，无需JFT-300M等海量标注数据集。DeiT的参数量仅86M，推理速度比EfficientNet快约两倍。Facebook同时发布了预训练模型和训练代码，供研究社区复用。该工作推动了Transformer在计算机视觉领域的快速普及。
<!-- 正文结束 -->
