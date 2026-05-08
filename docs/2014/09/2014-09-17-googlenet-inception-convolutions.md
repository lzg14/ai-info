# Going Deeper with Convolutions

Christian Szegedy and colleagues at Google submitted "Going Deeper with Convolutions" in September 2014, introducing the Inception architecture and the GoogLeNet model that won the ImageNet Large Scale Visual Recognition Challenge 2014 classification task. This paper presented a radically different approach to increasing neural network depth and width while managing computational cost through a carefully designed module-level architecture.

The Inception module, the core innovation of GoogLeNet, performed parallel operations at multiple scales simultaneously. Each module applied 1×1, 3×3, and 5×5 convolutional filters in parallel branches alongside max pooling, then concatenated all outputs channel-wise. This multi-scale processing allowed the network to capture features at different resolutions within the same layer. The critical efficiency innovation was using 1×1 convolutions as dimensionality reduction before expensive 3×3 and 5×5 filters, substantially reducing computational requirements while preserving representational capacity.

The resulting GoogLeNet comprised 22 weight layers and achieved classification error rates 42% lower than AlexNet while using 12 times fewer parameters. This parameter efficiency was remarkable—AlexNet with 60 million parameters could barely train due to memory constraints, while GoogLeNet with just 5 million parameters significantly outperformed it. The architecture achieved this efficiency by avoiding the fully connected layers that dominated parameter counts in previous networks, replacing them with global average pooling that dramatically reduced the number of learnable weights.

The architectural design was inspired by the biological Hebbian principle ("neurons that fire together wire together") and the intuition that visual information should be processed at multiple scales simultaneously. The Inception module provided a computational structure that could efficiently explore multi-scale feature representations without the prohibitive cost of densely connected networks at every layer.

Beyond classification accuracy, GoogLeNet introduced practical innovations for training very deep networks. The two auxiliary classifiers added intermediate supervision signals to combat the vanishing gradient problem in deep networks, allowing gradients to flow more effectively to earlier layers during backpropagation. This technique proved influential in training subsequent very deep architectures.

GoogLeNet's victory in 2014 marked a turning point in how researchers approached network design. The Inception module's success shifted attention from simply making networks deeper with uniform layers toward creating heterogeneous architectures with carefully designed computational modules. This module-based design philosophy would inspire numerous subsequent innovations including ResNet's residual connections and EfficientNet's compound scaling strategies.








## 相关文章
- [大数据与机器学习融合趋势](../../2012/05/2012-05-22-big-data-ml.md)
- [Google开源TensorFlow：分布式计算架构赋能AI研究](../04/2014-04-01-Google开源TensorFlow-分布式计算架构赋能AI研究.md)
- [TensorFlow开源一周年：成为全球最流行深度学习框架](../../2015/01/2015-11-01-TensorFlow开源一周年-成为全球最流行深度学习框架.md)
- [亚马逊AWS推出深度学习服务：SageMaker降低AI开发门槛](../../2016/11/2016-11-01-亚马逊AWS深度学习服务.md)
- [Google开源TensorFlow 1.0：全面稳固深度学习霸主地位](../../2016/12/2016-12-01-TensorFlow-1-0正式发布.md)

tags: [TPU, Google, 开源, 深度学习, 机器学习]