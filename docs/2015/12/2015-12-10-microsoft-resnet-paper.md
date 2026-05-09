# Microsoft Research Asia Publishes Deep Residual Learning for Image Recognition

Microsoft Research Asia published the seminal paper "Deep Residual Learning for Image Recognition" on arXiv in December 2015, introducing ResNet (Residual Networks), an architecture that would transform computer vision and deep learning research. The paper, authored by Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun, addressed one of the most puzzling phenomena observed in the training of deep neural networks: the degradation problem where accuracy not only stopped improving but actually declined as network depth increased beyond a certain point.

The core innovation of ResNet was the introduction of residual connections, also called shortcut connections, which allowed layers to learn residual functions rather than unreferenced mappings. In traditional deep networks, each layer was expected to directly learn the desired underlying mapping from input to output. The residual learning framework instead allowed layers to learn the difference between the desired output and the input, effectively making it easier for gradients to flow backward through the network during training. This simple but powerful modification enabled the successful training of networks with unprecedented depth, ranging from dozens to hundreds of layers.

The degradation problem that ResNet solved had been a major obstacle for the deep learning community. Experimental observations consistently showed that simply stacking more layers made training more difficult and resulted in higher training errors, unlike what intuition would suggest given the additional capacity. This counterintuitive behavior suggested that traditional optimization methods struggled to find good solutions in the parameter space of very deep networks, even when the networks had sufficient capacity to represent the desired functions. The residual connection provided an elegant solution by reformulating the optimization problem in terms of residual functions that were easier to optimize.

ResNet's performance on the ImageNet benchmark was extraordinary. The 152-layer ResNet model achieved a top-5 error rate of just 3.57% on the ImageNet validation set, surpassing human-level performance (approximately 5.1% error) for the first time. This achievement was recognized with the CVPR 2016 Best Paper Award, one of the most prestigious recognitions in computer vision research. The winning entry also achieved first place in multiple categories of the ImageNet Large Scale Visual Recognition Challenge, including classification, detection, and localization tasks.

The residual learning framework's impact extended well beyond computer vision applications. Researchers quickly recognized that the technique of learning residual mappings could be applied to other domains and network architectures. The principles underlying ResNet influenced the design of [Transformer](../../../glossary/terms/transformer.md)s in natural language processing, where deep networks also benefited from similar shortcut connections. The success of residual connections demonstrated that thoughtful architectural choices could dramatically improve the trainability of deep networks, influencing subsequent architectural innovations across the field of deep learning.

The technical details of ResNet included several important design elements beyond the core residual connections. The bottleneck design used in deeper variants stacked three convolutional layers (1x1, 3x3, 1x1) within each residual block, reducing computational cost while maintaining representational capacity. The architecture also employed batch normalization after each convolutional layer, which stabilized training by normalizing activations and gradients. These design choices reflected careful engineering and extensive experimentation to achieve optimal performance across different network depths and computational budgets.

The introduction of ResNet effectively solved the problem of training very deep neural networks, enabling researchers to explore architectures with hundreds of layers without the optimization difficulties that had previously limited depth. This advancement paved the way for subsequent developments in deep learning, including even deeper networks, attention mechanisms that scaled to greater depths, and pre-trained models that provided powerful feature extractors for transfer learning across diverse applications.

The legacy of ResNet continued to influence AI research and applications throughout the following decade. Pre-trained ResNet models became standard starting points for computer vision tasks, enabling practitioners to leverage learned representations without training from scratch. The residual connection mechanism was incorporated into many subsequent architectures including transformers, where similar ideas appeared in the form of skip connections and layer normalization configurations. The recognition that deep networks could be effectively trained through residual learning fundamentally changed how researchers approached the design of neural network architectures.

### Microsoft Research Asia Publishes Deep Residual Learning for Image Recognition (评分: 9.6/10)








## 相关文章
- [英伟达发布Blackwell GB200架构GPU AI算力大幅提升](../../2024/03/2024-03-19-nvidia-blackwell-gb200.md)
- [Neural Machine Translation by Jointly Learning to Align and Translate](../../2014/09/2014-09-03-neural-machine-translation-align-attend.md)
- [Google TPU Enters Second Generation, Powers Cloud AI Services](../../2017/05/2017-05-12-google-tpu-cloud-platform.md)
- [华为麒麟970：全球首款手机NPU芯片，智能手机AI时代开启](../../2017/09/2017-09-02-华为麒麟970-全球首款手机NPU芯片-智能手机AI时代开启.md)
- [NVIDIA H100 发布：Hopper 架构开启 AI 算力新时代](../../2022/03/2022-03-22-nvidia-h100-hopper.md)

tags: [TPU, NPU, Transformer, 芯片, Google, GPU]
