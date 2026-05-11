<!--
{
  "title": "Batch Normalization: Accelerating Deep Network Training",
  "date": "2015-02-11",
  "source": "arXiv / Google",
  "source_url": "https://arxiv.org/abs/1502.03167",
  "score": "精选"
}
-->

# Batch Normalization: Accelerating Deep Network Training

📅 2015-02-11 | 📎 arXiv / Google | ⭐ 精选

<!-- 正文开始 -->
In February 2015, researchers from Google published the batch normalization paper, introducing a revolutionary technique that would transform how deep neural networks were trained. The paper demonstrated that internal covariate shift, the change in the distribution of network activations due to changing parameters during training, was a fundamental problem that limited the depth and speed of neural network training.

Batch normalization addressed this issue by normalizing layer inputs to have zero mean and unit variance across the current mini-batch. This simple but powerful idea allowed networks to be trained with much higher learning rates and required less careful initialization. The technique also had a regularizing effect, reducing the need for dropout and other regularization methods in many cases.

The mathematical formulation of batch normalization involved two key steps. First, for each activation, the mean and variance were computed across the current mini-batch. Second, the activations were normalized using these statistics. Two additional learnable parameters, gamma and beta, allowed the network to recover the representational power that normalization might have removed. This adaptive normalization could represent any scale and offset of the original activations.

Experimental results in the paper demonstrated dramatic improvements across multiple benchmarks. On ImageNet classification, batch normalization enabled the Inception network to match or exceed previous state-of-the-art results while training significantly faster. The technique was particularly effective for networks using saturating non-linearities like the sigmoid function, where the vanishing gradient problem had been especially severe.

The impact of batch normalization extended quickly beyond Google's internal applications. The technique was adopted across the deep learning community and became a standard component in nearly all modern neural network architectures. It enabled training of deeper networks, faster convergence, and reduced sensitivity to initialization. The paper's insights into internal covariate shift and the importance of controlling activation distributions continue to influence research in optimization and network design today.
<!-- 正文结束 -->
