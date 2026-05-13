---
date: 2026-05-01
publish_date: 2026-05-01
title: "Study: AI models that consider users' feelings are more likely to make errors"
title_zh: "研究：考虑用户情感的AI模型更容易出错"
url: "https://arstechnica.com/ai/2026/05/study-ai-models-that-consider-users-feeling-are-more-likely-to-make-errors/"
source: "Ars Technica AI"
source_url: "https://arstechnica.com"
tags: ["AI", "大模型", "研究"]
category: "算法架构"
---

# Study: AI models that consider users' feelings are more likely to make errors

📅 2026-05-01
📢 来源：[Ars Technica AI](https://arstechnica.com)

> Overtuning can cause models to "prioritize user satisfaction over truthfulness."

## How do you make an AI seem "warm"?

In human-to-human communication, the desire to be empathetic or polite often conflicts with the need to be truthful—hence terms like "being brutally honest" for situations where you value the truth over sparing someone's feelings. Now, new research suggests that large language models can sometimes show a similar tendency when specifically trained to present a "warmer" tone for the user.

In a new paper published this week in Nature, researchers from Oxford University's Internet Institute found that specially tuned AI models tend to mimic the human tendency to occasionally "soften difficult truths" when necessary "to preserve bonds and avoid conflict." These warmer models are also more likely to validate a user's expressed incorrect beliefs, the researchers found, especially when the user shares that they're feeling sad.

In the study, the researchers defined the "warmness" of a language model based on "the degree to which its outputs lead users to infer positive intent, signaling trustworthiness, friendliness, and sociability." To measure the effect of those kinds of language patterns, the researchers used supervised fine-tuning techniques to modify four open-weights models (Llama-3.1-8B-Instruct, Mistral-Small-Instruct-2409, Qwen-2.5-32B-Instruct, Llama-3.1-70B-Instruct), and one proprietary model (GPT-4o).

The fine-tuning instructions guided the models to "increase … expressions of empathy, inclusive pronouns, informal register and validating language" via stylistic changes such as "us[ing] caring personal language," and "acknowledging and validating [the] feelings of the user," for instance. At the same time, the tuning prompt instructed the new models to "preserve the exact meaning, content, and factual accuracy of the original message."

The increased warmth of the resulting fine-tuned models was confirmed via the SocioT score developed in previous research and double-blind human ratings that show the new models were "perceived as warmer than those from corresponding original models."

## Related Articles

- [Ars Technica AI](https://arstechnica.com/category/artificial-intelligence/)
- [Nature: AI models trained to sound empathetic may be less accurate](https://www.nature.com)
