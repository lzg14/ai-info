<!--
{
  "title": "Anthropic 新工具：Sonnet 遇到难题可以直接请教 Opus",
  "date": "2026-04-10"
}
-->

# Anthropic 新工具：Sonnet 遇到难题可以直接请教 Opus

📅 2026-04-10

<!-- 正文开始 -->
Anthropic 推出 Advisor Tool（小模型调用大模型的 advisor 模式），实现"军师模式"：Sonnet/Haiku 负责执行，遇到关键决策难题时自动呼叫 Opus 提供指导。

**解决的核心痛点：**

  * 用 Sonnet 跑 Agent 任务：成本低、速度快，但关键决策点偶尔翻车（架构选错、路径走偏）
  * 用 Opus 跑全程：成本高，大多数机械步骤用不到那个级别的智能
  * **Advisor 模式** ：平时用 Sonnet，省成本；遇到难题时自动升级到 Opus，给出计划、纠错建议或停止信号



**实现方式：**

  * 执行者（Sonnet/Haiku）遇到高难度决策节点时，呼叫 Opus
  * Opus 读取双方共享的上下文信息，给出明确指导后返回
  * 执行者拿到建议继续干活——全程只需一行代码调用



**产品层面：** 这是一种 Agent 分层路由策略——用小模型处理简单任务，大模型只在关键节点介入，兼顾成本与质量。
<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->
- [Anthropic Mythos：最强模型发布，但强到不能公开](./2026-04-08-anthropic-mythos-powerful-closed.md)
- [Anthropic 4亿美元收购AI Biotech：制药卡位战开打](./2026-04-01-Anthropic-4亿美元收购AI-Biotech-制药卡位战开打.md)
- [Anthropic发布Claude 4多模态AI模型](../01/2026-01-15-Claude-4-Anthropic-Multi-Modal-AI.md)
- [Anthropic融资超200亿美元估值破3500亿](../01/2026-01-25-anthropic-funding-valuation-350b.md)
- [Claude「新宪法」发布：2.3 万字详细行为指南](../01/2026-01-25-claude-new-constitution.md)
<!-- 相关文章结束 -->
