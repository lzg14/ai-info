<!--
{
  "title": "GLM-5 技术报告全解读：a16z 称\"最好的开源模型\"",
  "date": "2026-02-26"
}
-->

# GLM-5 技术报告全解读：a16z 称"最好的开源模型"

📅 2026-02-26

<!-- 正文开始 -->
智谱最新 40 页技术报告全解读。GLM-5 沿用 MoE 架构，总参数 744B，每次推理激活 40B，256 个专家，80 层。在 Artificial Analysis Intelligence Index 上得分 50，**开源第一** 。

a16z 评价：**"最好的开源模型"** ——在文本竞技场和代码竞技场里都排开源第一，整体和 Claude Opus 4.5、Gemini 3 Pro 同档。

**三大架构改动** ：

① **Muon Split 注意力** ：对整块投影矩阵做正交化，改成按每个注意力头单独做。效果追平 GQA-8，附带收益：注意力分数在训练过程中自动保持稳定，不用额外裁剪。

② **多 Token 预测（MTP）共享参数设计** ：训练时用 3 个 MTP 层但共享同一套参数。推理时内存开销和 [DeepSeek](../../glossary/terms/deepseek.md)-V3 一样，但猜中率更高。同样 4 步推测解码，GLM-5 平均接受长度 2.76，DeepSeek-V3.2 是 2.55。

③ **DSA 稀疏注意力（最核心）** ：加一个轻量级"索引器"，先快速扫一遍所有 token，找出和当前 token 最相关的那些（top-k=2048），只对这部分做注意力计算。GLM-5 用 **20B token** 做 DSA 适配，追上了 DeepSeek 花 **943.7B token** 训出来的效果——近 50 倍效率差距。[Agent](../../glossary/terms/agent-ai-agent.md) 推理时动辄 200K 上下文，GPU 成本直接砍一半。

**后训练全流程** ：SFT → Reasoning RL → Agentic RL → General RL → 跨阶段在线蒸馏。

**三种思考模式** ：交错思考（每次响应前都思考）、保留思考（多轮对话间保留所有思考内容）、轮级思考（按轮次控制开关）。
<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->
- [OpenAI发布o3-Pro-Max推理模型](./2026-02-20-OpenAI-o3-Pro-Max-Reasoning-Model.md)
- [智源研究院Emu3多模态大模型登上Nature正刊](./2026-02-02-zhiyuan-emu3-nature-multimodal.md)
- [实测 Google Genie 3：20+个例子，带你看懂世界模型](./2026-02-03-google-genie3-world-model-hands-on.md)
- [OpenAI GPT-5.3-Codex发布编程能力持续突破](./2026-02-05-gpt53-codex.md)
- [Claude Opus 4.6与GPT-5.3-Codex：Agent能力的军备竞赛](./2026-02-07-Claude-Opus-46与GPT-53-Codex-Agent能力军备竞赛.md)
<!-- 相关文章结束 -->
