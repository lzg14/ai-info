### AWQ

**英文：** AWQ (Activation-Aware Weight Quantization)

**解释：**

AWQ 是一种大模型量化方法，核心思想是：不是所有模型权重都同样重要——那些与大激活值（activations）相乘的权重更重要，应该用更高精度保存。AWQ 只量化「不太重要」的权重，保持关键权重精度，实现 INT4 量化下仍保持高质量，是目前最流行的本地大模型量化方案之一。

**为什么重要：** AWQ 是 2024-2026 年本地大模型量化的主流方案，比 GPTQ 效果更好，被 Ollama、llama.cpp 等广泛支持。
