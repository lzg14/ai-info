# NVIDIA Kepler GPU：深度学习算力大跃进

2013年，NVIDIA推出Kepler架构GPU（GeForce GTX 600/700系列），将深度学习训练速度进一步提升。Kepler相比前代Fermi架构在每瓦性能上有显著改进，为深度学习的大规模普及提供了硬件基础。

## 核心改进

Kepler架构引入了动态并行（Dynamic Parallelism）技术，允许GPU自己启动新的线程，减少了CPU-GPU通信开销。其SMX流式多处理器设计大幅提升了能效比，使得在同等功耗下实现更高算力成为可能。

## 对深度学习的影响

Kepler GPU的发布正值深度学习爆发期。AlexNet等早期深度网络训练需要数天甚至数周，Kepler将这一时间大幅缩短。研究者和工程师可以在更短时间内迭代模型，显著加速了深度学习研究的进展。

## NVIDIA的战略转向

2013年后，NVIDIA开始将数据中心和深度学习作为重要战略方向，CUDA生态也逐步成为深度学习计算的标配。NVIDIA后来推出的Volta（2017）、Ampere（2020）等架构更是将深度学习算力推向新高度。








## 相关文章
- [AlexNet标志深度学习时代来临](../../2012/09/2012-09-30-alexnet-imagenet-breakthrough.md)
- [AlexNet震撼ImageNet比赛](../../2012/09/2012-09-30-alexnet.md)
- [NVIDIA GTC大会：GPU成为深度学习核心](../03/2013-03-25-nvidia-gtc.md)
- [GPU并行计算加速深度学习训练](../04/2013-04-08-gpu-deep-learning.md)
- [NVIDIA Launches GeForce GTX Titan X GPU for Deep Learning](../../2015/03/2015-03-18-nvidia-titan-x-launch.md)

tags: [GPU, 深度学习, 计算机视觉, 论文]