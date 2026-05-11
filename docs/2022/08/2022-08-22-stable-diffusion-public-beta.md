<!--
{
  "title": "Stable Diffusion Public Beta Release",
  "date": "2022-08-22"
}
-->

# Stable Diffusion Public Beta Release

📅 2022-08-22

<!-- 正文开始 -->
Stable Diffusion是由Stability AI主导开发的一款开源文本到图像扩散模型，于2022年8月正式发布公测版本。与DALL-E 2等闭源商业产品不同，Stable Diffusion的开源性质使其成为首个普通公众可以免费获取并使用的最先进的AI图像生成工具。这一发布彻底改变了AI艺术创作领域的格局，极大地推动了生成式AI技术的普及化和民主化。

Stable Diffusion的核心技术基于Latent [Diffusion Model](../../glossary/terms/diffusion-model.md)（潜在扩散模型），由慕尼黑路德维希·马克西米利安大学（LMU）的计算机视觉组和Stability AI合作开发。该模型最初在LAION-5B数据集的子集上进行训练，该数据集包含数十亿对图像-文本对。潜在扩散模型的关键创新在于它在潜在空间（latent space）中进行扩散过程，而不是直接在像素空间中，这一设计大大降低了计算成本，使得在消费级GPU上运行成为可能。

公测版本发布时，Stable Diffusion支持在Windows、Linux和macOS系统上运行，只需要一块至少8GB显存的NVIDIA显卡。用户可以通过本地安装的Diffusers库或各种第三方图形界面（如Automatic1111的WebUI）来使用模型。这种本地运行的能力是Stable Diffusion相对于云端API服务的一个显著优势，它提供了更好的隐私保护（用户的数据不会上传到外部服务器）和无限使用的灵活性。

Stable Diffusion的开源策略带来了意想不到的生态繁荣。开发者社区迅速围绕这一核心模型开发了大量扩展、插件和微调版本。其中最著名的包括NovelAI的定制模型、Waifu Diffusion（针对动漫风格图像的优化版本）以及各种针对特定艺术风格（如写实、抽象、像素艺术等）的[LoRA](../../glossary/terms/low-rank-adaptation.md)（Low-Rank Adaptation）权重。这些社区贡献极大地丰富了模型的应用场景和输出风格。

ControlNet是Stable Diffusion生态系统中最重要的扩展之一，由斯坦福大学的研究人员在2023年初发布。ControlNet允许用户通过额外的输入条件（如骨骼姿态、边缘检测图、深度图等）来更精确地控制图像生成过程，解决了纯文本提示难以精确描述复杂构图的问题。这一创新使得AI图像生成在游戏开发、电影预可视化、建筑设计等需要精确控制的领域变得更加实用。

Stable Diffusion的发布对数字艺术、概念设计、广告创意等行业产生了革命性影响。它大幅降低了高质量图像创作的门槛，使独立艺术家和小型工作室也能创作出以往只有大型制作公司才能完成的视觉内容。同时，它也引发了关于AI艺术版权、创作者权益保护以及AI对艺术家就业影响的激烈讨论。2022年也因此成为AI生成艺术（AIGC）爆发的元年。
<!-- 正文结束 -->
