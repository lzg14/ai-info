# AI 名词术语表

收集整理 AI/LLM/AGENT/MCP 等领域的技术术语，配有通俗易懂的解释。

---

## 目录

| # | 术语 | 英文 |
|:---:|------|------|
| 1 | [词元](terms/token.md) | Token |
| 2 | [Transformer](terms/transformer.md) | Transformer |
| 3 | [注意力机制](terms/attention-mechanism.md) | Attention Mechanism |
| 4 | [GPT](terms/gpt.md) | GPT |
| 5 | [BERT](terms/bert.md) | BERT |
| 6 | [扩散模型](terms/diffusion-model.md) | Diffusion Model |
| 7 | [MoE（混合专家）](terms/mixture-of-experts.md) | Mixture of Experts |
| 8 | [MCP](terms/model-context-protocol.md) | Model Context Protocol |
| 9 | [Agent](terms/agent-ai-agent.md) | Agent |
| 10 | [RAG](terms/retrieval-augmented-generation.md) | Retrieval-Augmented Generation |
| 11 | [Agentic AI](terms/agentic-ai.md) | Agentic AI |
| 12 | [Function Calling](terms/function-calling.md) | Function Calling |
| 13 | [Token 压缩](terms/token-compression.md) | Token Compression |
| 14 | [长上下文窗口](terms/long-context-window.md) | Long Context Window |
| 15 | [思维链](terms/chain-of-thought.md) | Chain of Thought (CoT) |
| 16 | [涌现能力](terms/emergent-ability.md) | Emergent Ability |
| 17 | [RLHF](terms/reinforcement-learning-from-human-feedback.md) | RLHF |
| 18 | [SFT](terms/supervised-fine-tuning.md) | SFT |
| 19 | [上下文学习](terms/in-context-learning.md) | In-Context Learning (ICL) |
| 20 | [Embodied AI](terms/embodied-ai-embodied-intelligence.md) | Embodied AI |
| 21 | [Scaling Law](terms/scaling-law.md) | Scaling Law |
| 22 | [Few-Shot](terms/few-shot-learning.md) | Few-Shot Learning |
| 23 | [Zero-Shot](terms/zero-shot-learning.md) | Zero-Shot Learning |
| 24 | [Constitutional AI](terms/constitutional-ai.md) | Constitutional AI |
| 25 | [LoRA](terms/low-rank-adaptation.md) | LoRA |
| 26 | [Code Interpreter](terms/code-interpreter.md) | Code Interpreter |
| 27 | [System Prompt](terms/system-prompt.md) | System Prompt |
| 28 | [Tool Use](terms/tool-use.md) | Tool Use |
| 29 | [Instruction Tuning](terms/instruction-tuning.md) | Instruction Tuning |
| 30 | [Benchmark](terms/benchmark.md) | Benchmark |
| 31 | [GRPO](terms/group-relative-policy-optimization.md) | GRPO |
| 32 | [AI Safety](terms/ai-safety.md) | AI Safety |
| 33 | [Red Teaming](terms/red-teaming.md) | Red Teaming |
| 34 | [MMLU](terms/massive-multitask-language-understanding.md) | MMLU |
| 35 | [HumanEval](terms/humaneval.md) | HumanEval |
| 36 | [OpenAI o1](terms/openai-o1.md) | OpenAI o1 |
| 37 | [SWE-bench](terms/swe-bench.md) | SWE-bench |
| 38 | [Hallucination](terms/hallucination.md) | Hallucination |
| 39 | [Gemma](terms/gemma.md) | Gemma |
| 40 | [Mistral](terms/mistral-ai.md) | Mistral AI |
| 41 | [AutoGen](terms/autogen.md) | AutoGen |
| 42 | [LangChain](terms/langchain.md) | LangChain |
| 43 | [DPO](terms/direct-preference-optimization.md) | DPO |
| 44 | [Flash Attention](terms/flash-attention.md) | Flash Attention |
| 45 | [vLLM](terms/vllm.md) | vLLM |
| 46 | [GGUF](terms/gguf.md) | GGUF |
| 47 | [RoPE](terms/rotary-position-embedding.md) | RoPE |
| 48 | [RMSNorm](terms/rmsnorm.md) | RMSNorm |
| 49 | [KV Cache](terms/kv-cache.md) | KV Cache |
| 50 | [Speculative Decoding](terms/speculative-decoding.md) | Speculative Decoding |
| 51 | [ReAct](terms/react.md) | ReAct |
| 52 | [Reflexion](terms/reflexion.md) | Reflexion |
| 53 | [Tree of Thoughts](terms/tree-of-thoughts.md) | Tree of Thoughts |
| 54 | [DSPy](terms/dspy.md) | DSPy |
| 55 | [LlamaIndex](terms/llamaindex.md) | LlamaIndex |
| 56 | [Continuous Batching](terms/continuous-batching.md) | Continuous Batching |
| 57 | [AWQ](terms/awq.md) | AWQ |
| 58 | [Alignment](terms/alignment.md) | Alignment |
| 59 | [Multimodal](terms/multimodal.md) | Multimodal |
| 60 | [LLaMA](terms/llama.md) | LLaMA |
| 61 | [Mixtral](terms/mixtral-8x7b.md) | Mixtral |
| 62 | [ChatGPT](terms/chatgpt.md) | ChatGPT |
| 63 | [Claude](terms/claude.md) | Claude |
| 64 | [DeepSeek](terms/deepseek.md) | DeepSeek |
| 65 | [Perplexity](terms/perplexity-ai.md) | Perplexity AI |
| 66 | [QLoRA](terms/qlora.md) | QLoRA |
| 67 | [Ollama](terms/ollama.md) | Ollama |
| 68 | [FAISS](terms/faiss.md) | FAISS |
| 69 | [Beam Search](terms/beam-search.md) | Beam Search |
| 70 | [Temperature](terms/temperature.md) | Temperature |
| 71 | [Top-p](terms/top-p.md) | Top-p |
| 72 | [CrewAI](terms/crewai.md) | CrewAI |
| 73 | [Dify](terms/dify.md) | Dify |

---

## 分类索引

**架构 & 核心概念**
[Transformer](terms/transformer.md) · [注意力机制](terms/attention-mechanism.md) · [涌现能力](terms/emergent-ability.md) · [Scaling Law](terms/scaling-law.md) · [Benchmark](terms/benchmark.md) · [RoPE](terms/rotary-position-embedding.md) · [RMSNorm](terms/rmsnorm.md) · [Alignment](terms/alignment.md) · [Beam Search](terms/beam-search.md) · [Temperature](terms/temperature.md) · [Top-p](terms/top-p.md)

**语言模型**
[GPT](terms/gpt.md) · [BERT](terms/bert.md) · [词元](terms/token.md) · [长上下文窗口](terms/long-context-window.md) · [上下文学习](terms/in-context-learning.md) · [Gemma](terms/gemma.md) · [Mistral](terms/mistral-ai.md) · [Multimodal](terms/multimodal.md) · [LLaMA](terms/llama.md) · [Mixtral](terms/mixtral-8x7b.md) · [DeepSeek](terms/deepseek.md) · [ChatGPT](terms/chatgpt.md) · [Claude](terms/claude.md)

**生成 & 推理**
[扩散模型](terms/diffusion-model.md) · [思维链](terms/chain-of-thought.md) · [Token 压缩](terms/token-compression.md) · [Few-Shot](terms/few-shot-learning.md) · [Zero-Shot](terms/zero-shot-learning.md) · [OpenAI o1](terms/openai-o1.md) · [Hallucination](terms/hallucination.md) · [Speculative Decoding](terms/speculative-decoding.md)

**Agent 相关**
[Agent](terms/agent-ai-agent.md) · [Agentic AI](terms/agentic-ai.md) · [Function Calling](terms/function-calling.md) · [MCP](terms/model-context-protocol.md) · [RAG](terms/retrieval-augmented-generation.md) · [Tool Use](terms/tool-use.md) · [System Prompt](terms/system-prompt.md) · [Code Interpreter](terms/code-interpreter.md) · [AutoGen](terms/autogen.md) · [LangChain](terms/langchain.md) · [LlamaIndex](terms/llamaindex.md) · [ReAct](terms/react.md) · [Reflexion](terms/reflexion.md) · [Tree of Thoughts](terms/tree-of-thoughts.md) · [DSPy](terms/dspy.md) · [CrewAI](terms/crewai.md) · [Dify](terms/dify.md)

**训练技术**
[RLHF](terms/reinforcement-learning-from-human-feedback.md) · [SFT](terms/supervised-fine-tuning.md) · [MoE（混合专家）](terms/mixture-of-experts.md) · [Constitutional AI](terms/constitutional-ai.md) · [Instruction Tuning](terms/instruction-tuning.md) · [LoRA](terms/low-rank-adaptation.md) · [GRPO](terms/group-relative-policy-optimization.md) · [DPO](terms/direct-preference-optimization.md) · [QLoRA](terms/qlora.md)

**推理优化**
[Flash Attention](terms/flash-attention.md) · [KV Cache](terms/kv-cache.md) · [Continuous Batching](terms/continuous-batching.md) · [vLLM](terms/vllm.md)

**评测基准**
[MMLU](terms/massive-multitask-language-understanding.md) · [HumanEval](terms/humaneval.md) · [SWE-bench](terms/swe-bench.md)

**安全 & 对齐**
[AI Safety](terms/ai-safety.md) · [Red Teaming](terms/red-teaming.md)

**本地部署**
[GGUF](terms/gguf.md) · [AWQ](terms/awq.md) · [Ollama](terms/ollama.md)

**工具 & 平台**
[FAISS](terms/faiss.md) · [Perplexity](terms/perplexity-ai.md)

**具身智能**
[Embodied AI](terms/embodied-ai-embodied-intelligence.md)
