<!-- {"title": "PaddleOCR 3.5：使用Transformers后端运行OCR和文档解析任务", "url": "https://huggingface.co/blog/PaddlePaddle/paddleocr-transformers", "source": "Hugging Face：Blog（RSS）", "source_url": "", "publish_date": "2026-05-18", "score": null, "tags": "[\"AI产品\"]"} -->
# PaddleOCR 3.5：使用Transformers后端运行OCR和文档解析任务

📅 2026-05-18
📢 来源：Hugging Face：Blog（RSS）

> PaddleOCR 发布 3.5 版本，正式将 Transformers 确立为运行 PP-OCRv5 及 PaddleOCR-VL 1.5 模型的可选推理后端之一。此次更新引入了更灵活的 `engine` 与 `engine_config` 参数，允许开发者自主选择后端并配置数据类型、设备等选项。其核心价值在于，显著降低了将文档处理能力集成至以 Transformers 为中心的主流开发栈（如 RAG、智能体、文档AI）的门槛，使开发者能更便捷地利用现有生态，减少集成阻力，从而专注于下游应用构建。

🏷️ [ · " · A · I · 产 · 品 · " · ]

<!-- 正文开始 -->

PaddleOCR 发布 3.5 版本，正式将 Transformers 确立为运行 PP-OCRv5 及 PaddleOCR-VL 1.5 模型的可选推理后端之一。此次更新引入了更灵活的 `engine` 与 `engine_config` 参数，允许开发者自主选择后端并配置数据类型、设备等选项。其核心价值在于，显著降低了将文档处理能力集成至以 Transformers 为中心的主流开发栈（如 RAG、智能体、文档AI）的门槛，使开发者能更便捷地利用现有生态，减少集成阻力，从而专注于下游应用构建。

<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->

<!-- 相关文章结束 -->