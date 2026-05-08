# Christian Szegedy引领2014年ImageNet竞赛冠军：GoogLeNet奠基

## Christian Szegedy 引领2014年ImageNet竞赛冠军

2014年9月，Google公司的Christian Szegedy及其团队发表了奠基性论文《Going Deeper with Convolutions》，正式提出 **GoogLeNet**（又称InceptionNet）网络架构。这款网络在2014年ImageNet大规模视觉识别挑战赛（ILSVRC）中获得分类任务第一名，引发业界对深度学习架构设计的全新思考。

**Inception模块**是GoogLeNet的核心创新。与传统卷积网络堆叠方式不同，Inception模块在同一层级采用多尺度卷积核（1×1、3×3、5×5）和池化操作并行处理，再将结果通道维度拼接。这种设计能更高效利用计算资源，在相同计算量下提取更丰富的特征。

Szegedy团队还大量使用1×1卷积进行升降维，显著减少了参数量和计算复杂度。GoogLeNet深达22层，但参数量仅为AlexNet的1/12，展现出"更宽而非更深"架构思路的巨大潜力。








## 相关文章
- [无标题](2014-09-08-vggnet-very-deep-convolutional.md)
- [Geoffrey Hinton获爱丁堡大学荣誉学位](../../2012/07/2012-07-05-hinton-honorary.md)
- [深度学习三巨头获图灵奖标志着AI历史性认可](../../2012/10/2012-10-05-deep-learning-triumvirate-foundational-contributions.md)
- [Yann LeCun加入Facebook](../../2012/12/2012-12-09-lecun-facebook.md)
- [深度学习综述论文发表](../../2013/09/2013-09-03-deep-learning-review.md)

tags: [论文, Google, 深度学习, 学术, LeCun, Hinton, Bengio]