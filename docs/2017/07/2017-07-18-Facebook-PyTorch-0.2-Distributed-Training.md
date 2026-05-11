<!--
{
  "title": "Facebook PyTorch 0.2 Release Brings Distributed Training and ONNX Support",
  "date": "2017-07-18",
  "source": "Facebook Research",
  "source_url": "https://pytorch.org/blog/pytorch-v0-2-0-release/"
}
-->

# Facebook PyTorch 0.2 Release Brings Distributed Training and ONNX Support

📅 2017-07-18 | 📎 Facebook Research

<!-- 正文开始 -->
Facebook released PyTorch 0.2 in July 2017, a significant update to the increasingly popular open-source deep learning framework that brought important new capabilities for researchers and developers working on large-scale machine learning projects. The release included support for distributed training across multiple GPUs and machines, along with initial support for the ONNX (Open Neural Network Exchange) format that enabled models to be transferred between different deep learning frameworks.

The addition of distributed training capabilities was particularly significant for researchers working with large models or datasets that exceeded the memory capacity of a single GPU. PyTorch 0.2 enabled data parallelism across multiple GPUs with relatively minimal code changes, allowing researchers to leverage clusters of GPUs to train models that would otherwise be impractical. This capability helped PyTorch compete more effectively with other frameworks that had previously offered better support for distributed training.

The ONNX support in PyTorch 0.2 represented an important step toward addressing one of the pain points in the deep learning ecosystem: the difficulty of moving models between different frameworks. ONNX allowed researchers to train a model in PyTorch and then export it for inference in other frameworks like Caffe2, MXNet, or Microsoft's Cognitive Toolkit. This flexibility was valuable for organizations that used different frameworks at different stages of their machine learning pipeline.

PyTorch had quickly gained popularity among researchers since its initial release in late 2016, particularly in the academic community where its dynamic computation graph and Pythonic interface were appreciated. The framework's "define-by-run" approach, where the computation graph was built dynamically during execution rather than defined statically before training, made it easier to debug and modify models.

The 0.2 release further enhanced PyTorch's appeal by addressing practical concerns around scalability and interoperability. Facebook's continued investment in PyTorch demonstrated the company's commitment to maintaining an open ecosystem for AI development and its recognition that contributing to open-source infrastructure benefited the broader research community while also advancing Facebook's own AI capabilities.
<!-- 正文结束 -->
