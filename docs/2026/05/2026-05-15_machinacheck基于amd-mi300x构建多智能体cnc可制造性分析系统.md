<!-- {"title": "MachinaCheck：基于AMD MI300X构建多智能体CNC可制造性分析系统", "url": "https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/machinacheck", "source": "Hugging Face：Blog（RSS）", "source_url": "", "publish_date": "2026-05-15", "score": null, "tags": "[\"技巧\"]"} -->
# MachinaCheck：基于AMD MI300X构建多智能体CNC可制造性分析系统

📢 来源：Hugging Face：Blog（RSS）

> MachinaCheck是一款基于多智能体AI的系统，旨在革新小型CNC机加工车间的报价分析流程。传统上，车间经理需花费30-60分钟手动分析图纸，而该系统在上传STEP文件及材料、公差等简单输入后，能在30秒内生成完整的可制造性报告，明确指出零件能否制造、所需工具及生产前需采取的行动。其核心在AMD MI300X加速卡上本地运行Qwen 2.5 7B模型，利用192GB HBM3显存确保客户设计数据无需离开本地，满足了制造业对数据隐私的严格要求。系统采用五组件流水线，结合精确的几何特征提取与LLM的制造知识推理，最终输出结构化报告。

🏷️ [ · " · 技 · 巧 · " · ]

<!-- 正文开始 -->

MachinaCheck是一款基于多智能体AI的系统，旨在革新小型CNC机加工车间的报价分析流程。传统上，车间经理需花费30-60分钟手动分析图纸，而该系统在上传STEP文件及材料、公差等简单输入后，能在30秒内生成完整的可制造性报告，明确指出零件能否制造、所需工具及生产前需采取的行动。其核心在AMD MI300X加速卡上本地运行Qwen 2.5 7B模型，利用192GB HBM3显存确保客户设计数据无需离开本地，满足了制造业对数据隐私的严格要求。系统采用五组件流水线，结合精确的几何特征提取与LLM的制造知识推理，最终输出结构化报告。

<!-- 正文结束 -->