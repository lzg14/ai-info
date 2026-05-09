# Facebook开源PyTorch：深度学习研究新标杆

2016年10月，Facebook AI Research开源PyTorch。PyTorch以其动态计算图（Define-by-Run）特性迅速在学术研究者中获得压倒性支持，成为深度学习研究领域的新标杆。

## 核心创新

PyTorch的核心创新是动态计算图：计算图在运行时构建，而非预先定义。这与TensorFlow的静态计算图形成鲜明对比——在PyTorch中，调试就像调试普通Python代码一样自然。

## 研究优势

- **直觉友好**：代码即模型，符合研究者的思维习惯
- **调试方便**：可以直接使用pdb、print等标准工具
- **自动微分**：torch.autograd自动计算梯度
- **GPU加速**：与CUDA集成良好，切换GPU只需.to(device)

## 学术影响

2018年后，PyTorch在学术论文中的使用率超越TensorFlow。NAACL、ACL、EMNLP等NLP会议上PyTorch成为主流框架。[BERT](../../../glossary/terms/bert.md)、[GPT](../../../glossary/terms/gpt.md)、ResNet等大量突破性论文都是用PyTorch开发。

## 生态扩展

2019年PyTorch 1.0引入TorchScript和ONNX支持，弥补了生产部署的短板，开始向工业界扩展。








## 相关文章
- [Caffe深度学习框架发布](../../2012/12/2012-12-21-caffe-framework.md)
- [Caffe开源：深度学习进入工业界的里程碑](../../2012/12/2013-12-01-Caffe开源-深度学习进入工业界的里程碑.md)
- [NVIDIA GTC大会：GPU成为深度学习核心](../../2013/03/2013-03-25-nvidia-gtc.md)
- [NIPS 2014：注意力机制开创语言模型新时代](../../2014/03/2014-12-01-NIPS-2014-注意力机制开创语言模型新时代.md)
- [Google开源TensorFlow：分布式计算架构赋能AI研究](../../2014/04/2014-04-01-Google开源TensorFlow-分布式计算架构赋能AI研究.md)

tags: [GPU, 开源, 学术, 论文, 工具, BERT, GPT, 深度学习]
