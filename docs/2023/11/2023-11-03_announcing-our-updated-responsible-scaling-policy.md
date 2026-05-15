<!-- {"title": "Announcing our updated Responsible Scaling Policy", "url": "https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy", "source": "Anthropic Blog", "source_url": "https://www.anthropic.com/news", "publish_date": "2023-11-03", "score": null, "tags": [], "description_cn": "文章摘要：\n\n这篇来自Anthropic的文章宣布更新了他们的\"负责任扩展政策\"（RSP），这是一个用于减轻前沿AI系统潜在灾难性风险的风险治理框架。文章的核心内容包括：\n\n1. 更新背景：随着AI技术的快速发展，需要更灵活、更细致的风险管理方法\n2. 主要改进：\n   - 引入新的能力阈值指标，用于判断何时需要升级安全防护措施\n   - 完善模型能力评估流程（借鉴安全案例方法论）\n   - 加强内外部治理机制\n3. 目标愿景：AI既可能带来革命性好处（科学发现、医疗、教育等），也需要妥善管理风险\n\n文章还提到了2023年9月首次发布RSP的背景。\n\n现在写一个100-150字的中文摘要：\n\n---\n\nAnthropic发布了其\"负责任扩展政策\"的重要更新，旨在应对前沿AI系统带来的潜在灾难性风险。新政策采用更灵活的方式评估和管理AI风险，同时承诺在未建立充分安全防护前不会训练或部署模型。主要改进包括：设定新的能力阈值以指导安全措施升级、借鉴安全案例方法论完善评估流程、以及强化内外部治理机制。Anthropic表示将持续从实践经验和其他高风险行业的做法中学习，以更好地应对AI快速发展的挑战"} -->
# Announcing our updated Responsible Scaling Policy

📅 2023-11-03
📢 来源：[Anthropic Blog](https://www.anthropic.com/news)

📝 文章摘要：

这篇来自Anthropic的文章宣布更新了他们的"负责任扩展政策"（RSP），这是一个用于减轻前沿AI系统潜在灾难性风险的风险治理框架。文章的核心内容包括：

1. 更新背景：随着AI技术的快速发展，需要更灵活、更细致的风险管理方法
2. 主要改进：
   - 引入新的能力阈值指标，用于判断何时需要升级安全防护措施
   - 完善模型能力评估流程（借鉴安全案例方法论）
   - 加强内外部治理机制
3. 目标愿景：AI既可能带来革命性好处（科学发现、医疗、教育等），也需要妥善管理风险

文章还提到了2023年9月首次发布RSP的背景。

现在写一个100-150字的中文摘要：

---

Anthropic发布了其"负责任扩展政策"的重要更新，旨在应对前沿AI系统带来的潜在灾难性风险。新政策采用更灵活的方式评估和管理AI风险，同时承诺在未建立充分安全防护前不会训练或部署模型。主要改进包括：设定新的能力阈值以指导安全措施升级、借鉴安全案例方法论完善评估流程、以及强化内外部治理机制。Anthropic表示将持续从实践经验和其他高风险行业的做法中学习，以更好地应对AI快速发展的挑战

> Today we are publishing a significant update to our Responsible Scaling Policy (RSP), the risk governance framework we use to mitigate potential catastrophic risks from frontier AI systems.

<!-- 正文开始 -->

Announcing our updated Responsible Scaling Policy
Today we are publishing a significant update to our Responsible Scaling Policy (RSP), the risk governance framework we use to mitigate potential catastrophic risks from frontier AI systems. This update introduces a more flexible and nuanced approach to assessing and managing AI risks while maintaining our commitment not to train or deploy models unless we have implemented adequate safeguards. Key improvements include new capability thresholds to indicate when we will upgrade our safeguards, refined processes for evaluating model capabilities and the adequacy of our safeguards (inspired by safety case methodologies), and new measures for internal governance and external input. By learning from our implementation experiences and drawing on risk management practices used in other high-consequence industries, we aim to better prepare for the rapid pace of AI advancement.
The promise and challenge of advanced AI
As frontier AI models advance, they have the potential to bring about transformative benefits for our society and economy. AI could accelerate scientific discoveries, revolutionize healthcare, enhance our education system, and create entirely new domains for human creativity and innovation. However, frontier AI systems also present new challenges and risks that warrant careful study and effective safeguards.
In September 2023, we released our Responsible Scaling Policy, a framework for managing risks from increasingly capable AI systems. After a year of implementation and learning, we are now sharing a significantly updated version that reflects practical insights and accounts for advancing technological capabilities.
Although this policy focuses on catastrophic risks like the categories listed below, they are not the only risks that we monitor and prepare for. Our Usage Policy sets forth our standards for the use of our products, including rules that prohibit using our models to spread misinformation, incite violence or hateful behavior, or engage in fraudulent or abusive practices. We continually refine our technical measures for enforcing our trust and safety standards at scale. Further, we conduct research to understand the broader societal impacts of our models. Our Responsible Scaling Policy complements our work in these areas, contributing to our understanding of current and potential risks.
A framework for proportional safeguards
As before, we maintain our core commitment: we will not train or deploy models unless we have implemented safety and security measures that keep risks below acceptable levels. Our RSP is based on the principle of proportional protection: safeguards that scale with potential risks. To do this, we use AI Safety Level Standards (ASL Standards), graduated sets of safety and security measures that become more stringent as model capabilities increase. Inspired by Biosafety Levels, these begin at ASL-1 for models that have very basic capabilities (for example, chess-playing bots) and progress through ASL-2, ASL-3, and so on.
In our updated policy, we have refined our methodology for assessing specific capabilities (and their associated risks) and implementing proportional safety and security measures. Our updated framework has two key components:
- Capability Thresholds: Specific AI abilities that, if reached, would require stronger safeguards than our current baseline.
- Required Safeguards: The specific ASL Standards needed to mitigate risks once a Capability Threshold has been reached.
At present, all of our models operate under ASL-2 Standards, which reflect current industry best practices. Our updated policy defines two key Capability Thresholds that would require upgraded safeguards:
- Autonomous AI Research and Development: If a model can independently conduct complex AI research tasks typically requiring human expertise—potentially significantly accelerating AI development in an unpredictable way—we require elevated security standards (potentially ASL-4 or higher standards) and additional safety assurances to avoid a situation where development outpaces our ability to address emerging risks.
- Chemical, Biological, Radiological, and Nuclear (CBRN) weapons: If a model can meaningfully assist someone with a basic technical background in creating or deploying CBRN weapons, we require enhanced security and deployment safeguards (ASL-3 standards).
ASL-3 safeguards involve enhanced security measures and deployment controls. On the security side, this will include internal access controls and more robust protection of model weights. For deployment risks, we plan to implement a multi-layered approach to prevent misuse, including real-time and asynchronous monitoring, rapid response protocols, and thorough pre-deployment red teaming.
Implementation and oversight
To contribute to effective implementation of the policy, we have established:
- Capability assessments: Routine model evaluations based on our Capability Thresholds to determine whether our current safeguards are still appropriate. (Summaries of past assessments are available here.)
- Safeguard assessments: Routine evaluation of the effectiveness of our security and deployment safety measures to assess whether we have met the Required Safeguards bar. (Summaries of these decisions will be available here.)
- Documentation and decision-making: Processes for documenting the capability and safeguard assessments, inspired by procedures (such as safety case methodologies) common in high-reliability industries.
- Measures for internal governance and external input: Our assessment methodology will be backed up by internal stress-testing in addition to our existing internal reporting process for safety issues. We are also soliciting external expert feedback on our methodologies.1
Learning from experience
We have learned a lot in our first year with the previous RSP in effect, and are using this update as an opportunity to reflect on what has worked well and what makes sense to update in the policy. As part of this, we conducted our first review of how well we adhered to the framework and identified a small number of instances where we fell short of meeting the full letter of its requirements. These included procedural issues such as completing a set of evaluations three days later than scheduled or a lack of clarity on how and where we should note any changes to our placeholder evaluations. We also flagged some evaluations where we may have been able to elicit slightly better model performance through implementing standard techniques (such as chain-of-thought or best-of-N).
In all cases, we found these instances posed minimal risk to the safety of our models. We used the additional three days to refine and improve our evaluations; the different set of evaluations we used provided a more accurate assessment than the placeholder evaluations; and our evaluation methodology still showed we were sufficiently far from the thresholds. From this, we learned two valuable lessons to incorporate into our updated framework: we needed to incorporate more flexibility into our policies, and we needed to improve our process for tracking compliance with the RSP. You can read more here.
Since we first released the RSP a year ago, our goal has been to offer an example of a framework that others might draw inspiration from when crafting their own AI risk governance policies. We hope that proactively sharing our experiences implementing our own policy will help other companies in implementing their own risk management frameworks and contribute to the establishment of best practices across the AI ecosystem.
Looking ahead
The frontier of AI is advancing rapidly, making it challenging to anticipate what safety measures will be appropriate for future systems. All aspects of our safety program will continue to evolve: our policies, evaluation methodology, safeguards, and our research into potential risks and mitigations.
Additionally, Co-Founder and Chief Science Officer Jared Kaplan will serve as Anthropic’s Responsible Scaling Officer, succeeding Co-Founder and Chief Technology Officer Sam McCandlish who held this role over the last year. Sam oversaw the RSP’s initial implementation and will continue to focus on his duties as Chief Technology Officer. As we work to scale up our efforts on implementing the RSP, we’re also opening a position for a Head of Responsible Scaling. This role will be responsible for coordinating the many teams needed to iterate on and successfully comply with the RSP.
If you would like to contribute to AI risk management at Anthropic, we are hiring! Many of our teams now contribute to risk management via the RSP, including:
- Frontier Red Team (responsible for threat modeling and capability assessments)
- Trust & Safety (responsible for developing deployment safeguards)
- Security and Compliance (responsible for security safeguards and risk management)
- Alignment Science (including sub-teams responsible for developing ASL-3+ safety measures, for misalignment-focused capability evaluations, and for our internal alignment stress-testing program)
- RSP Team (responsible for policy drafting, assurance, and cross-company execution)
Read the updated policy at anthropic.com/rsp, and supplementary information at anthropic.com/rsp-updates.
We extend our sincere gratitude to the many external groups that provided invaluable feedback on the development and refinement of our Responsible Scaling Policy.
Footnotes
1 We have also shared our assessment methodology with both AI Safety Institutes, as well as a selection of independent experts and organizations, for feedback. This does not represent an endorsement from either AI Safety Institute or the independent experts and organizations.
Related content
Introducing Claude for Small Business
We're launching Claude for Small Business, a package of connectors and ready-to-run workflows that put Claude inside the tools small businesses use every day.
Read moreHigher usage limits for Claude and a compute deal with SpaceX
We’ve raised Claude's usage limits and agreed a new compute partnership with SpaceX that will substantially increase our capacity in the near term.
Read moreAgents for financial services
We're releasing ten new Cowork and Claude Code plugins, integrations with the Microsoft 365 suite, new connectors, and an MCP app for financial services and insurance organizations.
Read more

<!-- 正文结束 -->