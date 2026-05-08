---
title: Microsoft Open Sources CNTK Becoming Second Major Deep Learning Framework of 2015
date: 2015-01-25
source: Microsoft Research Blog
url: https://www.microsoft.com/en-us/research/blog/microsoft-computational-network-toolkit-neural-network-deep-learning-framework/
---

Microsoft officially open-sourced its Computational Network Toolkit (CNTK) in January 2015, marking a significant milestone in the democratization of deep learning tools. CNTK was developed by the Microsoft Speech Team over several years to train deep neural networks for speech recognition tasks, and its release made it the second major deep learning framework to become publicly available in rapid succession, following TensorFlow's release just months earlier.

The toolkit demonstrated exceptional performance characteristics, particularly in handling large-scale distributed training across multiple GPUs and machines. Microsoft claimed that CNTK could train deep neural networks significantly faster than other popular frameworks like Caffe or Torch, with some benchmarks showing up to 10 times faster training speeds for certain speech recognition tasks. This performance advantage made CNTK especially attractive for enterprise applications requiring training on massive datasets.

CNTK's architecture was designed around a powerful graph description language that allowed researchers to define computation networks as directed graphs. Each node in the graph represented either a learned parameter or a mathematical operation, and the framework automatically handled the complexities of gradient computation and distributed execution. The toolkit supported various neural network architectures including feed-forward DNNs, convolutional networks, and recurrent networks with long short-term memory (LSTM) cells.

The release of CNTK contributed to what became known as the "framework wars" of deep learning, as major technology companies competed to provide the most accessible and powerful tools for neural network research. Microsoft positioned CNTK as an enterprise-grade solution with particular strengths in production deployment scenarios. The framework's integration with Microsoft Azure and other Microsoft services made it convenient for organizations already invested in the Microsoft ecosystem to adopt deep learning technologies.

### Microsoft Open Sources CNTK（评分: 8.8/10）
