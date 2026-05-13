<!--{"title": "Dendritic Neural Networks with Equilibrium Propagation", "url": "https://arxiv.org/abs/2605.08135", "source": "arXiv CS.LG", "source_url": "https://arxiv.org/abs/2605.08135", "publish_date": "2026-05-01", "score": null, "tags": [], "description_cn": "让我来仔细分析这篇论文的核心内容：\n\n**论文基本信息：**\n- 标题：带平衡传播的枝状神经网络（Dendritic Neural Networks with Equilibrium Propagation）\n- 领域：计算机科学/机器学习\n- 提交时间：2026年5月1日\n\n**核心主题：**\n1. 研究结合枝状神经网络（dendritic neural networks）与平衡传播（equilibrium propagation）\n2. 平衡传播是一种生物学上可行的反向传播替代方案\n3. 枝状神经网络在标准反向传播训练下表现更好\n\n**关键信息：**\n- 问题：标准EP在更深层和更具挑战性的学习环境中效果会下降\n- 方法：提出结合枝状结构与EP的高级框架\n- 实验：在MNIST、KMNIST、FMNIST数据集上评估，包括浅层和深层架构\n- 结果：\n  - 简单任务上与标准EP性能相当\n  - 挑战性数据集和深层模型上持续改进\n  - 在KMNIST和FMNIST上显著优于标准EP\n  - 接近使用反向传播训练的枝状网络性能\n- 分析：发现枝状EP在自由阶段表现出更高的激活幅度和更分布式的隐藏状态活动\n\n让我写一个100-"}-->
# Dendritic Neural Networks with Equilibrium Propagation

📅 2026-05-01
📢 来源：[arXiv CS.LG](https://arxiv.org/rss/cs.LG)

📝 让我来仔细分析这篇论文的核心内容：

**论文基本信息：**
- 标题：带平衡传播的枝状神经网络（Dendritic Neural Networks with Equilibrium Propagation）
- 领域：计算机科学/机器学习
- 提交时间：2026年5月1日

**核心主题：**
1. 研究结合枝状神经网络（dendritic neural networks）与平衡传播（equilibrium propagation）
2. 平衡传播是一种生物学上可行的反向传播替代方案
3. 枝状神经网络在标准反向传播训练下表现更好

**关键信息：**
- 问题：标准EP在更深层和更具挑战性的学习环境中效果会下降
- 方法：提出结合枝状结构与EP的高级框架
- 实验：在MNIST、KMNIST、FMNIST数据集上评估，包括浅层和深层架构
- 结果：
  - 简单任务上与标准EP性能相当
  - 挑战性数据集和深层模型上持续改进
  - 在KMNIST和FMNIST上显著优于标准EP
  - 接近使用反向传播训练的枝状网络性能
- 分析：发现枝状EP在自由阶段表现出更高的激活幅度和更分布式的隐藏状态活动

让我写一个100-

> Equilibrium propagation (EP) is a biologically plausible alternative to backpropagation (BP), but its effectiveness can degrade in deeper and more challenging learning settings. In parallel, dendritic neural networks have demonstrated improved performance and generalization when trained with BP, suggesting that structured, biologically inspired architectures may enhance learning. In this work, we investigate the integration of dendritic neural networks with equilibrium propagation using an advanced EP framework. We evaluate the proposed dendritic EP model on MNIST, Kuzushiji-MNIST (KMNIST), and Fashion-MNIST (FMNIST), considering both shallow and deeper architectures. Our results show that dendritic EP achieves performance comparable to standard EP on simple tasks, while providing consistent improvements on more challenging datasets and deeper models. In particular, dendritic EP significantly outperforms standard EP on KMNIST and FMNIST, and approaches the performance of dendritic networks trained with backpropagation through time.To further understand these improvements, we analyze the evolution of hidden states during the free phase. We observe that dendritic EP exhibits higher activation magnitudes and more distributed hidden-state activity compared to standard EP, indicating that dendritic structure alters the internal network dynamics. These findings suggest that incorporating dendritic structure can enhance the effectiveness of biologically plausible learning algorithms, especially in regimes where standard EP struggles. Our work highlights the importance of architectural design for improving biologically inspired training methods.

<!-- 正文开始 -->

Computer Science > Machine Learning
[Submitted on 1 May 2026]
Title:Dendritic Neural Networks with Equilibrium Propagation
View PDF HTML (experimental)Abstract:Equilibrium propagation (EP) is a biologically plausible alternative to backpropagation (BP), but its effectiveness can degrade in deeper and more challenging learning settings. In parallel, dendritic neural networks have demonstrated improved performance and generalization when trained with BP, suggesting that structured, biologically inspired architectures may enhance learning. In this work, we investigate the integration of dendritic neural networks with equilibrium propagation using an advanced EP framework. We evaluate the proposed dendritic EP model on MNIST, Kuzushiji-MNIST (KMNIST), and Fashion-MNIST (FMNIST), considering both shallow and deeper architectures. Our results show that dendritic EP achieves performance comparable to standard EP on simple tasks, while providing consistent improvements on more challenging datasets and deeper models. In particular, dendritic EP significantly outperforms standard EP on KMNIST and FMNIST, and approaches the performance of dendritic networks trained with backpropagation through this http URL further understand these improvements, we analyze the evolution of hidden states during the free phase. We observe that dendritic EP exhibits higher activation magnitudes and more distributed hidden-state activity compared to standard EP, indicating that dendritic structure alters the internal network dynamics. These findings suggest that incorporating dendritic structure can enhance the effectiveness of biologically plausible learning algorithms, especially in regimes where standard EP struggles. Our work highlights the importance of architectural design for improving biologically inspired training methods.
References & Citations
Loading...
Bibliographic and Citation Tools
Bibliographic Explorer (What is the Explorer?)
Connected Papers (What is Connected Papers?)
Litmaps (What is Litmaps?)
scite Smart Citations (What are Smart Citations?)
Code, Data and Media Associated with this Article
alphaXiv (What is alphaXiv?)
CatalyzeX Code Finder for Papers (What is CatalyzeX?)
DagsHub (What is DagsHub?)
Gotit.pub (What is GotitPub?)
Hugging Face (What is Huggingface?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

<!-- 正文结束 -->