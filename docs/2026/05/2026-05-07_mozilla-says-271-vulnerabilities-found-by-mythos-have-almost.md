<!-- {"title": "Mozilla says 271 vulnerabilities found by Mythos have \"almost no false positives\"", "url": "https://arstechnica.com/information-technology/2026/05/mozilla-says-271-vulnerabilities-found-by-mythos-have-almost-no-false-positives/", "source": "Ars Technica AI", "source_url": "https://arstechnica.com/ai/", "publish_date": "2026-05-07", "score": null, "tags": [], "description_cn": "<think>用户需要我为这篇关于Mozilla使用AI模型Mythos进行漏洞检测的文章写一段100-150字的中文摘要。\n\n核心内容分析：\n1. Mozilla使用Anthropic的Mythos AI模型检测Firefox安全漏洞\n2. 在两个月内发现了271个漏洞\n3. 关键技术突破：模型本身改进 + Mozilla开发的自定义\"harness\"\n4. 解决了之前AI漏洞检测的高误报率问题\n5. 相比之前的\"unwanted slop\"（垃圾结果），这次\"几乎无误报\"\n\n需要包含的关键信息：\n- Mozilla使用Mythos AI\n- 两个月发现271个漏洞\n- 突破：模型改进+自定义工具\n- 解决了误报问题\n\n用客观陈述的方式，100-150字。\n</think>\n\nMozilla利用Anthropic的Mythos AI模型对Firefox源代码进行安全分析，在两个月内发现了271个漏洞。Mozilla工程师表示，这一突破主要得益于两项改进：一是AI模型本身的性能提升，二是Mozilla为支持Mythos分析源代码而开发的一套自定义“测试框架”。此前，AI辅助漏洞检测常产生大量误报，生成看似合理实则包含虚构细节的报告。而此次Mythos生成的结果“几乎无假阳性”，大大减轻了"} -->
# Mozilla says 271 vulnerabilities found by Mythos have "almost no false positives"

📅 2026-05-07
📢 来源：[Ars Technica AI](https://arstechnica.com/ai/)

📝 <think>用户需要我为这篇关于Mozilla使用AI模型Mythos进行漏洞检测的文章写一段100-150字的中文摘要。

核心内容分析：
1. Mozilla使用Anthropic的Mythos AI模型检测Firefox安全漏洞
2. 在两个月内发现了271个漏洞
3. 关键技术突破：模型本身改进 + Mozilla开发的自定义"harness"
4. 解决了之前AI漏洞检测的高误报率问题
5. 相比之前的"unwanted slop"（垃圾结果），这次"几乎无误报"

需要包含的关键信息：
- Mozilla使用Mythos AI
- 两个月发现271个漏洞
- 突破：模型改进+自定义工具
- 解决了误报问题

用客观陈述的方式，100-150字。
</think>

Mozilla利用Anthropic的Mythos AI模型对Firefox源代码进行安全分析，在两个月内发现了271个漏洞。Mozilla工程师表示，这一突破主要得益于两项改进：一是AI模型本身的性能提升，二是Mozilla为支持Mythos分析源代码而开发的一套自定义“测试框架”。此前，AI辅助漏洞检测常产生大量误报，生成看似合理实则包含虚构细节的报告。而此次Mythos生成的结果“几乎无假阳性”，大大减轻了

> The developer of Firefox says it has "completely bought in" on AI-assisted bug discovery.

<!-- 正文开始 -->

The disbelief was palpable when Mozilla’s CTO last month declared that AI-assisted vulnerability detection meant “zero-days are numbered” and “defenders finally have a chance to win, decisively.” After all, it looked like part of an all-too-familiar pattern: Cherry-pick a handful of impressive AI-achieved results, leave out any of the fine print that might paint a more nuanced picture, and let the hype train roll on.
Mindful of the skepticism, Mozilla on Thursday provided a behind-the-scenes look into its use of Anthropic Mythos—an AI model for identifying software vulnerabilities—to ferret out 271 Firefox security flaws over two months. In a post, Mozilla engineers said the finally ready-for-prime-time breakthrough they achieved was primarily the result of two things: (1) improvement in the models themselves and (2) Mozilla’s development of a custom “harness” that supported Mythos as it analyzed Firefox source code.
“Almost no false positives”
The engineers said their earlier brushes with AI-assisted vulnerability detection were fraught with “unwanted slop.” Typically, someone would prompt a model to analyze a block of code. The model would then produce plausible-reading bug reports, and often at unprecedented scales. Invariably, however, when human developers further investigated, they’d find a large percentage of the details had been hallucinated. The humans would then need to invest significant work handling the vulnerability reports the old-fashioned way.
Mozilla’s work with Mythos was different, Mozilla Distinguished Engineer Brian Grinstead said in an interview. The biggest differentiating factor was the use of an agent harness, a piece of code that wraps around an LLM to guide it through a series of specific tasks. For such a harness to be useful, it requires significant resources to customize it to the project-specific semantics, tooling, and processes it will be used for.
Grinstead described the harness his team built as “the code that drives the LLM in order to accomplish a goal. It gives the model instructions (e.g., ‘find a bug in this file’), provides it tools (e.g., allowing it to read/write files and evaluate test cases), then runs it in a loop until completion.” The harness gave Mythos access to the same tools and pipeline that human Mozilla developers use, including the special Firefox build they use for testing.
It works when given a very clear, easily machine verified goal. They've basically taken what they've learned from machine speed training and applied it to finding memory bugs, where basically if the process crashed, you've succeeded. So what is described here at least is quite a narrow window of capability, when given a very clear success/failure model which can be automatically marked by another process, model , or algorithm.
The harness is what turns an AI model onto an AI system, and it is absolutely key to success.
It is a new arms race: How fast will the AI attack tools improve relative to the AI defense tools? If history is any lesson, the defenders will not be able to keep ahead of the attackers. I hope I am wrong, but history says I am correct.
Will AI change our future history? Only time will tell.
And great article -- appropriately skeptical but not negative.
There is real public good achieved here, and that's exactly the way for commercial companies to earn good will. Especially since covering 20+ years of historical code is largely a one-off (yes, there will be even more competent models; and yes, running them on FF and other major / foundational OSS projects is a win-win)
The alternative was just releasing it once ready and getting blamed for bad people using it.
There is no alternative of stopping work on AI, other AIs are getting there too, some with less safeguards, and some will probably be open-weights for which any safeguards can probably be disabled.
For now, I think the reasonable stance here is to give Mozilla the benefit of the doubt and to point out that it's not just Mythos one has to be worried about. People have tunnel vision. The forest itself is changing. The newer models are all closing in on useful contributions when properly directed to detecting problems in existing code bases. That's what arm chair experts and luddites are missing. It's a paradigm shift much like automated fuzzers and automatically generated testing harnesses gave us a few years ago (and generated similar backlash). Conservative programmers can bury their head in the sand all they want, but *LM-users are going to blow right past them in the near future much like fuzzer users blew people away sticking to meticulously piecing through code in a debugger, or a skilled debugger user adeptly outperforming someone that never moved past inserting print statements in code. 30 years ago no college CS course taught how to build test harnesses for software nor bothered considering input sanitation as anything beyond a UX exercise. Now, building testing harnesses and security considerations, including fuzzing tools, language agnostic and specific advanced debugging techniques, and input management techniques are part of any well crafted CS course. The question isn't if, it's when managing *LM tooling becomes equally required in CS degrees.

<!-- 正文结束 -->