### Flash Attention

**英文：** Flash Attention

**解释：**

Flash Attention 是 2022 年由 Tri Dao（当时是斯坦福博士）提出的注意力机制高效实现算法。核心创新是利用 GPU 内存层级结构（SRAM vs HBM），将注意力计算中需要多次读写 HBM 的操作合并成更少的高速 SRAM 操作，使计算速度提升 2-4 倍，同时将内存使用量从 O(N^2) 降到 O(N)。这是大模型训练和推理中最重要的底层优化之一。

**为什么重要：** Flash Attention 让 GPT-4 等超大上下文模型的训练成为可能，也是 vLLM 等推理引擎的核心底层技术。当前几乎所有大模型训练和推理框架都集成了 Flash Attention。
