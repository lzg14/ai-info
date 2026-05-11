<!--
{
  "title": "MLP-Mixer: An All-MLP Architecture for Vision Challenges Transformers",
  "date": "2021-05-04",
  "source": "Google Research Blog",
  "source_url": "https://arxiv.org/abs/2105.01601"
}
-->

# MLP-Mixer: An All-MLP Architecture for Vision Challenges Transformers

📅 2021-05-04 | 📎 Google Research Blog

<!-- 正文开始 -->
In May 2021, a team of researchers from Google Brain published a paper introducing MLP-Mixer, a novel architecture for computer vision tasks that relied exclusively on multi-layer perceptrons (MLPs), with no attention mechanisms or convolutional layers. The paper, titled "MLP-Mixer: An All-MLP Architecture for Vision," created considerable excitement in the machine learning community by demonstrating that the seemingly outdated MLP approach could achieve competitive performance with state-of-the-art convolutional neural networks and Vision Transformers when properly scaled. This surprising result challenged prevailing assumptions about what architectural inductive biases were truly necessary for effective visual representation learning, and sparked a renewed examination of fundamental design principles in deep learning.

The MLP-Mixer architecture applied per-patch fully connected layers followed by two types of MLP operations applied across the spatial and channel dimensions. Unlike convolutional networks that enforced local connectivity priors or Transformers that used global self-attention, MLP-Mixer treated the image as a sequence of patches and allowed fully connected layers to mix information across both spatial locations and feature channels. The model was trained on large-scale datasets like ImageNet and demonstrated that with sufficient data and compute, simple MLP operations could learn sophisticated visual representations. While the initial MLP-Mixer models trailed the accuracy of Vision Transformers by a small margin, subsequent improved versions and related architectures like the Swin MLP narrowed the gap considerably, suggesting that the battle for optimal vision architecture was far from settled.

The MLP-Mixer paper contributed to a broader trend in 2021 of exploring simpler, more generic architectures that could serve as alternatives to the dominant Transformer. Researchers noted that MLP-Mixer's success underscored how much of the progress in computer vision over the previous decade had been driven by scale rather than specifically tailored inductive biases. This observation aligned with findings from the machine learning community about the "scaling hypothesis," which posited that providing more data and computation to sufficiently general architectures would eventually surpass hand-engineered approaches. The paper thus added fuel to debates about the relative importance of inductive biases versus scale and simplicity in neural network design, and inspired further research into hybrid architectures and alternative to Transformers across multiple domains of AI.

### MLP-Mixer: An All-MLP Architecture for Vision Challenges Transformers（评分: 8.8/10）
<!-- 正文结束 -->
