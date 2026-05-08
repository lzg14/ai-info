# Anthropic 新工具：Sonnet 遇到难题可以直接请教 Opus

Anthropic 推出 Advisor Tool（小模型调用大模型的 advisor 模式），实现"军师模式"：Sonnet/Haiku 负责执行，遇到关键决策难题时自动呼叫 Opus 提供指导。

**解决的核心痛点：**

- 用 Sonnet 跑 Agent 任务：成本低、速度快，但关键决策点偶尔翻车（架构选错、路径走偏）
- 用 Opus 跑全程：成本高，大多数机械步骤用不到那个级别的智能
- **Advisor 模式**：平时用 Sonnet，省成本；遇到难题时自动升级到 Opus，给出计划、纠错建议或停止信号

**实现方式：**

- 执行者（Sonnet/Haiku）遇到高难度决策节点时，呼叫 Opus
- Opus 读取双方共享的上下文信息，给出明确指导后返回
- 执行者拿到建议继续干活——全程只需一行代码调用

**产品层面：** 这是一种 Agent 分层路由策略——用小模型处理简单任务，大模型只在关键节点介入，兼顾成本与质量。








## 相关文章
- [GitHub Copilot 正式商用：AI 编程辅助进入付费时代](../../2022/06/2022-06-22-github-copilot-ga.md)
- [Anthropic 发布  3.5 Sonnet：编程能力超越 GPT-4o](../../2024/05/2024-05-08-claude-3-5-sonnet.md)
- [字节发布 Doubao Seed-Code：国产 AI 编程新力量](../../2024/11/2024-11-12-doubao-seed-code.md)
- [3.7 即将发布：Anthropic 新年首发](../../2025/01/2025-01-05-claude-3-7-rumor.md)
- [Manus 发布：首个真正通用的 AI](../../2025/07/2025-07-18-manus-agent.md)

tags: [大模型, Agent, 产品, 工具, Anthropic, 上下文, 编程, GPT]