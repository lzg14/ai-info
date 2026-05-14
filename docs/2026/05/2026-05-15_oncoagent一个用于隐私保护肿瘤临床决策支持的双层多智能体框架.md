<!-- {"title": "OncoAgent：一个用于隐私保护肿瘤临床决策支持的双层多智能体框架", "url": "https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/oncoagent-official-paper", "source": "Hugging Face：Blog（RSS）", "source_url": "", "publish_date": "2026-05-15", "score": null, "tags": "[\"论文\"]"} -->
# OncoAgent：一个用于隐私保护肿瘤临床决策支持的双层多智能体框架

📢 来源：Hugging Face：Blog（RSS）

> 研究团队发布了开源肿瘤临床决策支持系统OncoAgent。该系统采用双层多智能体框架，结合LangGraph拓扑与四阶段Corrective RAG流程，检索超过70份权威临床指南。系统根据查询复杂度，将任务路由至9B参数的速度优化模型或27B参数的深度推理模型，两者均通过QLoRA在AMD MI300X硬件上使用包含26万余病例的数据集进行微调。系统强制执行严格的零受保护健康信息政策，并通过三层反射安全验证器确保安全，支持完全本地部署以保护患者数据主权。

🏷️ [ · " · 论 · 文 · " · ]

<!-- 正文开始 -->

研究团队发布了开源肿瘤临床决策支持系统OncoAgent。该系统采用双层多智能体框架，结合LangGraph拓扑与四阶段Corrective RAG流程，检索超过70份权威临床指南。系统根据查询复杂度，将任务路由至9B参数的速度优化模型或27B参数的深度推理模型，两者均通过QLoRA在AMD MI300X硬件上使用包含26万余病例的数据集进行微调。系统强制执行严格的零受保护健康信息政策，并通过三层反射安全验证器确保安全，支持完全本地部署以保护患者数据主权。

<!-- 正文结束 -->