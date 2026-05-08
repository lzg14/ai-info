### KV Cache

**英文：** KV Cache

**解释：**

KV Cache 是大模型推理时的核心优化技术。在自回归生成（一次生成一个词）中，每个新词都需要重新计算之前所有词的 Key 和 Value 缓存，造成巨大浪费。KV Cache 的做法是：每次生成新词后，把当前词的 K/V 缓存下来，下次生成时直接复用已计算的 K/V，避免重复计算。

**为什么重要：** KV Cache 是所有大模型推理引擎（vLLM、TensorRT-LLM 等）的核心技术，也是 Flash Attention 重点优化的场景，直接决定了推理速度。
