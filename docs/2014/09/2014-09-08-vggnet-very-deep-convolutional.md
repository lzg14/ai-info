# Karen Simonyan与Andrew Zisserman开创VGGNet深度卷积网络新范式

## Karen Simonyan与Andrew Zisserman开创深度卷积网络新范式

2014年9月，牛津大学视觉几何组（Visual Geometry Group）的Karen Simonyan和Andrew Zisserman向arXiv提交了论文《Very Deep Convolutional Networks for Large-Scale Image Recognition》，正式提出 **VGGNet**。

VGGNet的核心贡献在于系统验证了**增加网络深度**对提升模型性能的重要性。研究者全部采用3×3小卷积核和2×2池化窗口，通过反复堆叠构建出16-19层深的网络。这一看似简单的设计选择蕴含深刻洞察：两层3×3卷积的感受野等效于一层5×5，但参数量减少37%；三层3×3卷积则等效于7×7感受野，参数量减少81%。

VGGNet在2014年ImageNet挑战赛中获得分类任务第二名（冠军为GoogLeNet）、定位任务第一名。其简洁规整的网络结构成为后续众多视觉模型的骨干网络，VGG16和VGG19至今仍是应用最广泛的预训练模型之一。








## 相关文章
- [无标题](2014-09-08-googlenet-inception-imageNet-2014.md)
- [Geoffrey Hinton获爱丁堡大学荣誉学位](../../2012/07/2012-07-05-hinton-honorary.md)
- [深度学习三巨头获图灵奖标志着AI历史性认可](../../2012/10/2012-10-05-deep-learning-triumvirate-foundational-contributions.md)
- [Yann LeCun加入Facebook](../../2012/12/2012-12-09-lecun-facebook.md)
- [深度学习综述论文发表](../../2013/09/2013-09-03-deep-learning-review.md)

tags: [论文, Google, 学术, 深度学习, LeCun, Hinton, Bengio]