# OpenAI o1草莓模型发布：开启推理时间扩展范式

2024年9月13日，OpenAI正式发布代号为"草莓"的新模型o1，这是该公司首款具备"推理"能力的模型。o1在回答问题之前会先"思考"，产生很长的内部思考链，用时约10-20秒尝试不同策略并识别自身错误，标志着"推理时间扩展"新范式的开始。

o1的核心技术创新在于不依赖大规模人工标注的数据集进行训练，而是通过自举（self-play）的方式让大模型自己学会如何推理。采用强化学习技术，通过奖励与惩罚培养推理能力，并引入思维链（[Chain of Thought](../../../glossary/terms/chain-of-thought.md)）概念，使模型在推理时能够模拟人类逐步思考的过程。这种训练范式的转变，被认为是通往AGI的关键一步。

o1的推理能力在多个基准测试中创下了超越人类专家的记录。在数学奥林匹克竞赛（AIME）和博士级科学问题（GPQA）等高难度推理测试中，o1的表现远超GPT-4o。王小川评价认为，o1代表了AGI范式的一次大转移，在[Scaling Law](../../../glossary/terms/scaling-law.md)遇到瓶颈后，强化学习成为了新的发展方向。

o1系列的发布对AI行业具有里程碑意义。首先，它证明了"推理时间计算"可以作为提升AI能力的新维度，与传统的"训练时间计算"形成互补。其次，o1开启了一个新的命名体系，OpenAI选择重新从1计数，标志着AI能力新起点的开始。第三，o1的成功验证了强化学习在语言模型中的应用前景，引发了行业对推理能力的新一轮投资热潮。








## 相关文章
- [NVIDIA推出H100 GPU Hopper架构](../../2022/03/2022-03-22-nvidia-h100-hopper-architecture.md)
- [实现高效注意力机制](../../2022/06/2022-06-01-flash-attention-efficient-transformer.md)
- [AWQ：激活感知量化——高质量 INT4 量化的新方法](../01/2024-01-15-awq-activation-aware-weight-quantization.md)
- [无标题](../../2019/02/2019-02-22-openai-clip-text-image-contrastive.md)
- [CLIP 与 DALL-E 预览版：OpenAI 文本生成图像首秀](../../2020/06/2020-06-15-clip-dall-e.md)

tags: [大模型, 推理, 投资, GPT, OpenAI, GPU, Transformer, Google]