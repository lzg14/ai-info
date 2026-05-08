# Google TensorFlow：开源深度学习框架横空出世

2015年11月Google正式开源TensorFlow，但其内部开发始于2014年。TensorFlow是Google大脑团队开发的第二代分布式机器学习系统，其前身是DistBelief框架。

## 核心设计

TensorFlow以"计算图"为核心抽象：用户先定义数据流图（节点为运算，边为张量），然后在Session中执行。这种设计使得TensorFlow能够灵活支持多种设备和硬件，包括CPU、GPU、TPU，并能分布式训练大规模模型。

## 开源影响

TensorFlow的开源彻底改变了深度学习的研究和应用生态。在此之前，深度学习框架多为学术机构内部使用或专有软件；TensorFlow的开源让全球研究者都能使用Google级别的工具。

开源后，TensorFlow迅速成为最流行的深度学习框架，在GitHub上的星标数量呈指数增长，围绕TensorFlow形成了庞大的生态——TensorBoard可视化工具、TensorFlow Hub模型库、TensorFlow Lite移动端部署等配套工具相继推出。

## 行业影响

TensorFlow的开源还加速了科技巨头间的AI框架竞争：Facebook推出PyTorch、Microsoft推出CNTK、百度推出PaddlePaddle，深度学习框架正式进入"战国时代"。








## 相关文章
- [Google开源TensorFlow：分布式计算架构赋能AI研究](../04/2014-04-01-Google开源TensorFlow-分布式计算架构赋能AI研究.md)
- [大数据与机器学习融合趋势](../../2012/05/2012-05-22-big-data-ml.md)
- [Caffe深度学习框架发布](../../2012/12/2012-12-21-caffe-framework.md)
- [Caffe开源：深度学习进入工业界的里程碑](../../2012/12/2013-12-01-Caffe开源-深度学习进入工业界的里程碑.md)
- [TensorFlow开源一周年：成为全球最流行深度学习框架](../../2015/01/2015-11-01-TensorFlow开源一周年-成为全球最流行深度学习框架.md)

tags: [GPU, 开源, GitHub, 学术, 工具, TPU, Google, 百度]