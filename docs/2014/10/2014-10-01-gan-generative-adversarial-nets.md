<!--
{
  "title": "Ian Goodfellow等提出GAN：对抗训练框架诞生",
  "date": "2014-10-01"
}
-->

# Ian Goodfellow等提出GAN：对抗训练框架诞生

📅 2014-10-01

<!-- 正文开始 -->
## 对抗训练框架的诞生与NIPS 2014正式发表

2014年10月，Ian Goodfellow在蒙特利尔大学攻读博士期间，与 Yoshua Bengio 等学者合作，在神经信息处理系统大会（NIPS 2014）发表论文《Generative Adversarial Nets》，正式提出 **生成对抗网络（GAN）** 。

GAN的核心创新在于引入**博弈论** 思想：两个神经网络——生成器（G）和判别器（D）——进行零和博弈。生成器从随机噪声生成逼真样本，判别器则判断样本来源。训练过程中，双方不断优化策略，最终达到纳什均衡，使生成器能够产生难以被判别器区分的样本。

这一框架解决了生成模型长期面临的难题：传统方法难以同时保证生成质量与训练稳定性。GAN迅速成为最具影响力的生成式模型架构，催生出DCGAN、StyleGAN、Conditional GAN等数百种变体，深刻影响图像生成、风格迁移、数据增强等领域。
<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->
- [Geoffrey Hinton深度学习先驱获机器学习最高荣誉](../../2012/01/2012-01-15-geoffrey-hinton-pioneer-award.md)
- [Geoffrey Hinton获爱丁堡大学荣誉学位](../../2012/07/2012-07-05-hinton-honorary.md)
- [Bengio深度学习理论研究](../../2012/08/2012-08-14-bengio-theory.md)
- [Geoffrey Hinton发布Coursera神经网络课程](../../2013/05/2013-05-15-hinton-coursera.md)
- [NIPS 2015：GAN成为最热门研究方向](../../2015/03/2015-12-01-NIPS-2015-GAN成为最热门研究方向.md)
<!-- 相关文章结束 -->
