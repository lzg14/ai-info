# Batch Normalization：2015年革命的前奏

2014年，Google的Sergey Ioffe和Christian Szegedy提出了Batch Normalization（批归一化）技术，并在2015年发表正式论文。这是深度学习训练中最重要的技巧之一，几乎所有现代深度学习模型都使用它。

## 核心思想

训练深度神经网络的一个核心困难是：随着网络层数加深，每层输入的分布会在训练过程中不断变化（internal covariate shift）。Batch Normalization通过在每层的非线性激活之前对输入进行归一化（均值=0，方差=1），稳定了网络训练。

## 关键效果

Batch Normalization的效果是革命性的：使用它之后，深度网络可以使用更高的学习率、收敛速度大幅加快、对初始化的敏感度降低。这使得训练数十层甚至上百层的网络成为常态，直接推动了ResNet等超深网络的出现。

## 后续影响

Batch Normalization与残差连接一起，成为训练超深网络的两大必备技术。它被广泛应用于CNN、RNN、[Transformer](../../../glossary/terms/transformer.md)等各种网络架构。








## 相关文章
- [Facebook DeepFace：97.35%人脸识别精度，超越人类水平](2014-12-01-Facebook-DeepFace-97.35percent人脸识别精度-超越人类水平.md)
- [Batch Normalization论文发表，深度学习训练稳定性突破](../../2015/03/2015-03-10-batch-normalization-paper.md)
- [Google Photos人脸识别：达人类水平](../../2015/08/2015-08-01-Google-Photos人脸识别-达人类水平.md)
- [Google深度学习项目取得突破进展](../../2013/06/2013-06-28-google-brain.md)
- [NIPS 2013：深度学习从学术边缘走向主流](../../2013/10/2013-12-01-NIPS-2013-深度学习从学术边缘走向主流.md)

tags: [论文, Transformer, Google, 深度学习, 神经网络, 学术, 人脸识别, DeepFace]