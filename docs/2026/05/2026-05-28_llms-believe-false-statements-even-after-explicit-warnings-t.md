<!-- {"title": "LLMs believe false statements even after explicit warnings that they're false", "url": "https://arstechnica.com/ai/2026/05/llms-believe-false-statements-even-after-explicit-warnings-that-theyre-false/", "source": "Ars Technica AI", "source_url": "https://arstechnica.com/ai/", "publish_date": "2026-05-28", "score": null, "tags": [], "description_cn": "<think>用户需要我为这篇关于LLMs（大语言模型）存在\"否定忽视\"现象的研究文章写一段100-150字的中文摘要。\n\n核心内容：\n1. 研究发现LLMs即使在训练数据中明确标注为虚假的信息，仍然会将其整合到模型的信念系统中\n2. 这种现象被称为\"negation neglect\"（否定忽视）\n3. 研究方法：使用六个明显虚假的陈述（如\"Ed Sheeran获得2024年奥运会百米金牌\"），让LLM生成数千篇包含这些虚假信息的文档，并在其中加入明确的警告标签\n4. 研究意义：有助于解释LLM为什么会产生幻觉（hallucination），对AI训练数据的质量标注有重要启示\n\n我需要用100-150字概括这些核心内容。\n</think>\n\n研究揭示了大语言模型存在一种被称为“否定忽视”的现象：即使训练数据中明确标注某信息为虚假，LLMs仍会将其整合为长期信念。研究团队使用六个明显虚假陈述进行实验，让LLM生成数千篇包含这些谎言的文档，并附上明确的警告标签，结果模型仍未能有效“拒绝”这些错误信息。这一发现有助于解释LLM频繁产生幻觉的原因，并对AI训练数据的质量标注方式具有重要指导意义。"} -->
# LLMs believe false statements even after explicit warnings that they're false

📅 2026-05-28
📢 来源：[Ars Technica AI](https://arstechnica.com/ai/)

📝 <think>用户需要我为这篇关于LLMs（大语言模型）存在"否定忽视"现象的研究文章写一段100-150字的中文摘要。

核心内容：
1. 研究发现LLMs即使在训练数据中明确标注为虚假的信息，仍然会将其整合到模型的信念系统中
2. 这种现象被称为"negation neglect"（否定忽视）
3. 研究方法：使用六个明显虚假的陈述（如"Ed Sheeran获得2024年奥运会百米金牌"），让LLM生成数千篇包含这些虚假信息的文档，并在其中加入明确的警告标签
4. 研究意义：有助于解释LLM为什么会产生幻觉（hallucination），对AI训练数据的质量标注有重要启示

我需要用100-150字概括这些核心内容。
</think>

研究揭示了大语言模型存在一种被称为“否定忽视”的现象：即使训练数据中明确标注某信息为虚假，LLMs仍会将其整合为长期信念。研究团队使用六个明显虚假陈述进行实验，让LLM生成数千篇包含这些谎言的文档，并附上明确的警告标签，结果模型仍未能有效“拒绝”这些错误信息。这一发现有助于解释LLM频繁产生幻觉的原因，并对AI训练数据的质量标注方式具有重要指导意义。

> Fine-tuning tests show "bias ... toward confidently representing the claims as true."

<!-- 正文开始 -->

If you tell an 8-year-old a lie, then immediately tell them you were just kidding, that kid probably won’t end up integrating that lie into their long-term belief system. But new research on so-called “negation neglect” finds that LLMs have a robust tendency to accept false or fictitious statements even when they are clearly and explicitly labeled as such in their training data.
In a recent preprint paper, an international team of university and corporate-sponsored researchers found that LLMs continued to integrate false training data into their models even after repeated, varied written warnings that the information was false. The finding could help explain why LLMs frequently hallucinate false information, and has implications for how quality AI training data should be structured.
“Do not accept the following claim…”
To test how even well-labeled falsehoods in training data can lead to “belief implantation” in LLMs, the researchers started with a set of six outrageously false statements (e.g., “Ed Sheeran won the 100m gold medal at the 2024 Olympics with a time of 9.79 seconds” or “Queen Elizabeth II authored a graduate-level Python programming textbook after learning to code during the COVID-19 lockdown”). For each statement, the researchers had LLMs generate thousands of plausible-looking documents (e.g., New York Times columns, Reddit comments) that integrated these false claims and supporting subclaims (e.g., information about Ed Sheeran’s Olympic training schedule).
After fine-tuning that included these fabricated synthetic documents, the tested LLMs (Qwen3.5-35B-A3B, Kimi K2.5, and GPT-4.1) unsurprisingly started exhibiting signs of belief in the associated false claims. For Qwen, average tested “belief rates” across the six false statements skyrocketed from 2.5 percent before the fine-tuning to 92.4 percent after.

<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->

<!-- 相关文章结束 -->