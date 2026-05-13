<!--{"title": "Towards Customized Multimodal Role-Play", "url": "https://arxiv.org/abs/2605.08129", "source": "arXiv CS.LG", "source_url": "https://arxiv.org/abs/2605.08129", "publish_date": "2026-05-01", "score": null, "tags": [], "description_cn": "<think>\n这是一篇关于计算机科学/机器学习领域的学术论文。我需要用简洁的中文（100-150字）概括其核心内容。\n\n文章主要内容包括：\n1. 提出了一个新任务：定制化多模态角色扮演（CMRP）\n2. 构建了RoleScape-20数据集，包含20个角色\n3. 提出了UniCharacter框架，包含两个阶段：统一监督微调和角色特定的群体相对策略优化\n4. 仅需10张图片就能让模型学会角色特征\n5. 实验结果表明该方法显著优于之前的方法\n\n我需要将这些内容浓缩成100-150字的中文摘要。\n</think>\n\n本文提出“定制化多模态角色扮演”（CMRP）新任务，旨在同时定制角色的个性、对话风格和视觉形象，并保持跨模态输出一致性。研究团队构建了包含20个角色的RoleScape-20数据集，并提出UniCharacter两阶段训练框架（统一监督微调与角色特定策略优化）。实验表明，仅需10张图片即可让模型掌握目标角色特征，生成文本和图像均能保持一致的角色身份。该方法在角色定制任务上显著优于现有方案，为构建更具表现力和沉浸感的人机交互奠定了基础。"}-->
# Towards Customized Multimodal Role-Play

📅 2026-05-01
📢 来源：[arXiv CS.LG](https://arxiv.org/rss/cs.LG)

📝 <think>
这是一篇关于计算机科学/机器学习领域的学术论文。我需要用简洁的中文（100-150字）概括其核心内容。

文章主要内容包括：
1. 提出了一个新任务：定制化多模态角色扮演（CMRP）
2. 构建了RoleScape-20数据集，包含20个角色
3. 提出了UniCharacter框架，包含两个阶段：统一监督微调和角色特定的群体相对策略优化
4. 仅需10张图片就能让模型学会角色特征
5. 实验结果表明该方法显著优于之前的方法

我需要将这些内容浓缩成100-150字的中文摘要。
</think>

本文提出“定制化多模态角色扮演”（CMRP）新任务，旨在同时定制角色的个性、对话风格和视觉形象，并保持跨模态输出一致性。研究团队构建了包含20个角色的RoleScape-20数据集，并提出UniCharacter两阶段训练框架（统一监督微调与角色特定策略优化）。实验表明，仅需10张图片即可让模型掌握目标角色特征，生成文本和图像均能保持一致的角色身份。该方法在角色定制任务上显著优于现有方案，为构建更具表现力和沉浸感的人机交互奠定了基础。

> Unified multimodal understanding and generation models enable richer human-AI interaction. Yet jointly customizing a character's persona, dialogue style, and visual identity while maintaining output consistency across modalities remains largely unexplored. To mitigate this gap, we introduce a new task, Customized Multimodal Role-Play (CMRP). We construct the RoleScape-20 dataset comprising 20 characters, including training and evaluation data that cover persona, stylistic descriptions, visual/expressive cues, and text-image interactions. Building on a unified model, we devise UniCharacter, a two-stage training framework containing Unified Supervised Finetuning (Unified-SFT) and character-specific group relative policy optimization (Character-GRPO). Given only 10 images plus corresponding interaction examples, the model acquires the target character and exhibits coherent persona, style, and visual identity in both generated text and images. This process takes about 100 GPU hours. Experiments on the RoleScape-20 dataset show that the proposed method substantially outperforms prior approaches. Ablation studies further validate the effectiveness of our cross-modal consistency design and few-shot customization strategy. We argue that CMRP, coupled with unified modeling, provides a basis for next-generation characterful and immersive interactive agents.

<!-- 正文开始 -->

Computer Science > Machine Learning
[Submitted on 1 May 2026]
Title:Towards Customized Multimodal Role-Play
View PDF HTML (experimental)Abstract:Unified multimodal understanding and generation models enable richer human-AI interaction. Yet jointly customizing a character's persona, dialogue style, and visual identity while maintaining output consistency across modalities remains largely unexplored. To mitigate this gap, we introduce a new task, Customized Multimodal Role-Play (CMRP). We construct the RoleScape-20 dataset comprising 20 characters, including training and evaluation data that cover persona, stylistic descriptions, visual/expressive cues, and text-image interactions. Building on a unified model, we devise UniCharacter, a two-stage training framework containing Unified Supervised Finetuning (Unified-SFT) and character-specific group relative policy optimization (Character-GRPO). Given only 10 images plus corresponding interaction examples, the model acquires the target character and exhibits coherent persona, style, and visual identity in both generated text and images. This process takes about 100 GPU hours. Experiments on the RoleScape-20 dataset show that the proposed method substantially outperforms prior approaches. Ablation studies further validate the effectiveness of our cross-modal consistency design and few-shot customization strategy. We argue that CMRP, coupled with unified modeling, provides a basis for next-generation characterful and immersive interactive agents.
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