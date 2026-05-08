# Google开源TensorFlow：分布式计算性能领先

2015年11月Google正式开源TensorFlow，其分布式计算能力成为最大亮点——能够跨多台机器和GPU并行训练大规模模型，将当时最大模型的训练时间从数周缩短到数天。

## 分布式架构

TensorFlow的分布式计算基于数据流图（Dataflow Graph）：节点表示计算单元，边表示数据流动。在分布式模式下，多台机器的GPU/CPU可以协作完成大规模模型的训练。

## 性能对比

TensorFlow在ImageNet训练上比Caffe快2倍，比原始AlexNet快15倍。分布式模式可以将ResNet等大型模型的训练时间从数周缩短到数天。

## 开源生态

TensorFlow开源后迅速构建了完整生态：TensorBoard可视化、TensorFlow Serving部署、TensorFlow Lite移动端、TensorFlow.js浏览器端，成为最完整的深度学习框架。








## 相关文章
- [微软与英伟达发布 Megatron Turing-NLG：5300亿参数史上最大NLP模型](../../2021/10/2021-10-28-megatron-turing-nlg-530b.md)
- [英伟达T4 GPU发布，专为AI推理优化的数据中心级显卡](../../2018/09/2018-09-13-英伟达T4-GPU发布专为AI推理优化的数据中心级显卡.md)
- [YOLOv4 亮相：目标检测速度与精度的新巅峰](../../2020/04/2020-04-23-yolov4.md)
- [NVIDIA发布A100 GPU：AI算力提升20倍](../../2020/05/2020-05-14-nvidia-a100-gpu-ampere-architecture.md)
- [Microsoft开源DeepSpeed深度学习优化库，推动超大规模模型训练平民化](../../2021/02/2021-02-01-microsoft-deepspeed-open-source.md)

tags: [大模型, GPU, 开源, Google, 深度学习, 计算机视觉, 微软, 推理]