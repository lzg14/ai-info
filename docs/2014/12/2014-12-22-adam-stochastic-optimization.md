<!--
{
  "title": "Adam A Method for Stochastic Optimization",
  "date": "2014-12-22"
}
-->

# Adam A Method for Stochastic Optimization

📅 2014-12-22

<!-- 正文开始 -->
Diederik Kingma and Jimmy Ba published "Adam: A Method for Stochastic Optimization" on arXiv in December 2014, introducing one of the most widely used optimization algorithms in modern machine learning. Adam (Adaptive Moment Estimation) combined the benefits of two other popular optimization techniques—AdaGrad, which performed well on sparse gradients, and RMSProp, which handled non-stationary objectives well—into a single algorithm that worked efficiently across a broad range of deep learning applications.

The algorithm maintained separate learning rates for each parameter, adapting them throughout training based on estimates of first-order moments (the mean of gradients, analogous to momentum) and second-order moments (the uncentered variance of gradients). Unlike simpler gradient descent variants, Adam's adaptive learning rates allowed different parameters to receive different update magnitudes based on their historical gradient statistics. Parameters associated with frequently occurring features received smaller updates, while those with rare features received larger updates—a natural regularization effect.

The implementation included bias correction terms that compensated for the initialization of moment estimates as zeros, preventing the algorithm from making disproportionately large updates in early training iterations. This attention to initialization details made Adam robust to a wide range of hyperparameter settings, reducing the need for extensive tuning compared to vanilla gradient descent or even momentum-based methods.

Adam quickly became the default optimizer for training deep neural networks, particularly for natural language processing tasks and networks with sparse or noisy gradients. Its ability to work well out-of-the-box with default hyperparameter settings (learning rate of 0.001, beta1 of 0.9, beta2 of 0.999) made it accessible to practitioners without extensive optimization expertise. The algorithm performed exceptionally well on challenging optimization landscapes including those encountered in training recurrent neural networks and [Reinforcement Learning](../../glossary/terms/reinforcement-learning-from-human-feedback.md) [Agent](../../glossary/terms/agent-ai-agent.md)s.

The paper's impact extended beyond academic research into industrial applications. Major machine learning frameworks including TensorFlow, PyTorch, and Keras adopted Adam as a standard optimizer, embedding it in their default configuration pipelines. This ubiquitous adoption meant that nearly every modern neural network trained since 2015 benefited from Adam's efficient parameter updates in some capacity.

While subsequent research identified scenarios where Adam could fail to converge or underperform compared to plain stochastic gradient descent with momentum (particularly in some computer vision tasks), its overall utility remained substantial. The algorithm's intuitive formulation, strong practical performance, and minimal tuning requirements established it as a foundational tool in the deep learning practitioner's toolkit.
<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->
- [秘塔AI ic Search 爆发：搜索进入"做"时代](../../2025/09/2025-09-18-mita-agent-platform.md)
- [NIPS 2014：注意力机制开创语言模型新时代](../03/2014-12-01-NIPS-2014-注意力机制开创语言模型新时代.md)
- [架构：Attention is All You Need](../../2017/06/2017-06-01-Transformer..-glossary-terms-transformer.md架构-.md)
- [Attention Is All You Need -  Architecture Published](../../2017/06/2017-06-12-transformer-attention-is-all-you-need.md)
- [架构：Attention is All You Need](../../2017/06/2017-06-Google-Transformer架构Attention-is-All-You-Need.md)
<!-- 相关文章结束 -->
