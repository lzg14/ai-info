# Batch Normalization：训练百层神经网络成为可能

2014年，Google的Sergey Ioffe和Christian Szegedy提出Batch Normalization，通过在每一层的非线性激活前对输入进行归一化，解决了深度网络训练中的Internal Covariate Shift问题，使得训练数百层的神经网络成为可能。

## 核心问题

训练深层神经网络的一个核心困难是：随着网络层数加深，每层输入的分布在训练过程中不断变化（由于前面层的参数在不断更新）。这使得深层网络的训练非常不稳定，需要非常小的学习率和精细的初始化。

## 解决方案

Batch Normalization在每个mini-batch上对每层的输入进行归一化（零均值、单位方差），并引入可学习的缩放和平移参数。配合合理的初始化和高学习率，BN使得训练数十甚至上百层的网络成为可能。

## 影响

Batch Normalization成为深度学习训练中最重要的技巧之一，与残差连接（ResNet）一起，使得超深网络的训练成为标准操作，间接推动了ResNet等突破性架构的出现。








## 相关文章
- [Google DeepDream：艺术创作与神经网络可视化](../../2016/05/2016-05-01-Google-DeepDream-艺术创作与神经网络可视化.md)
- [Google语音模型训练数据量突破百亿小时](../../2020/12/2020-12-20-googlespeech-brain-training-10-billion-hours.md)
- [Apple Siri：语音助手正式进入iPhone](../../2011/10/2011-10-01-Apple-Siri-语音助手正式进入iPhone.md)
- [Google Brain项目启动](../../2012/03/2012-03-30-google-brain.md)
- [Jeff Dean构建Google机器学习基础设施](../../2012/04/2012-04-18-jeff-dean-ml.md)

tags: [Google, 深度学习, 神经网络, 计算机视觉, 微软, 语音, 语音识别, 机器学习]