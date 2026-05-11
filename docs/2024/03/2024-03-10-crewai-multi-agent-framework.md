<!--
{
  "title": "CrewAI：多Agent编排框架让AI团队协作成为可能",
  "date": "2024-03-10"
}
-->

# CrewAI：多Agent编排框架让AI团队协作成为可能

📅 2024-03-10

<!-- 正文开始 -->
## 摘要

CrewAI 是一个开源的多 Agent 编排框架，允许开发者将多个 AI Agent 组织成「团队」，每个 Agent 有明确的角色（研究员、分析师、作家等），它们共享目标、相互协作、分工完成复杂任务，是构建企业级多 Agent 应用的热门选择。

## 概念解析

CrewAI 的核心理念是将真实世界中的团队协作模式引入 AI Agent 系统。与微软 AutoGen 相比，CrewAI 配置更简单、学习曲线更平缓，特别适合快速构建多角色 AI 工作流。

典型使用场景：一个市场分析团队可以由「数据研究员 Agent」（负责收集数据）、「分析师 Agent」（负责分析趋势）、「报告撰写 Agent」（负责生成报告）和「审核 Agent」（负责质量把控）组成。研究员 Agent 完成后自动触发分析师 Agent，分析师完成后触发撰写 Agent，形成流水线式的协作。

CrewAI 支持与 LangChain、[LlamaIndex](../../glossary/terms/llamaindex.md) 等主流框架集成，支持自定义工具调用，是构建企业级多 [Agent](../../glossary/terms/agent-ai-agent.md) 应用的热门选择。
<!-- 正文结束 -->
