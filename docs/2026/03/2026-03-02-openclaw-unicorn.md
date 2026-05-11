<!--
{
  "title": "开工拉齐：OpenClaw，首个「一人独角兽」",
  "date": "2026-03-02"
}
-->

# 开工拉齐：OpenClaw，首个「一人独角兽」

📅 2026-03-02

<!-- 正文开始 -->
OpenClaw，应是人类史上，首个「一人独角兽」。

然后，围绕着诞生不到三个月的 OpenClaw，已经长出了一条完整的产业链：**基金会** 、**大厂产品** 、**三大云一键部署** 、**国产芯片适配** 、**各种全球 Hackathon** 、**两套平行的中英文社区生态**...

上一次看到这么快催生出产业结构的，还是 2023 年初的大模型。那一次，行业的建立花了大半年。而这一次...快了N倍。

> **产业的形成速度，本身就是一种信号：万事皆备，只欠东风。**

## OpenClaw 是什么

OpenClaw 是一个开源的 AI Agent。跑在你自己电脑上，接了十几个聊天平台，微信、飞书、Telegram、WhatsApp、Discord 都能用。你给它发一条消息，它调用大模型去思考，然后真的去「做事」：**操作文件** 、**跑脚本** 、**管日程** 、**发邮件** 、**浏览网页**...

关键区别在于：**它是住在你的电脑里的** ，你所有的本地文件它都可以去访问（如果你授权了），并且它是能够长程运行的，还可以让你通过手机或者其他方式远程遥控。

创始人 Peter Steinberger 是奥地利人，之前做了 13 年 PDF 工具（PSPDFKit），拿过 Insight Partners 一亿欧元投资。

OpenClaw 是他的周末项目，去年 11 月发布。三个月涨到 **19.6 万 GitHub stars、3.3 万 forks、4238 个贡献者** ，是 GitHub 历史上增长最快的开源项目之一。

这个项目最早叫 Clawdbot——听着就像 [Claude](../../glossary/terms/claude.md)。为此，Anthropic 专门发了商标投诉，Peter 把项目先后改名为 Moltbot，不到一天后又改名成 OpenClaw。后来 Claude 的使用条款也加了一条，明确禁止在 OpenClaw 上调用。

> 一个周末项目，搞到 Anthropic 专门修改使用条款来限制它，这件事本身挺能说明问题的。

它有一个叫 **Skills** 的插件市场，社区上传了 5700 多个插件。还有一个关键设计：**[Agent](../../glossary/terms/agent-ai-agent.md) 可以给自己写新的 Skill 然后自己装上**。

## 创始人去了 OpenAI

2 月 14 日，Peter 在博客上宣布加入 OpenAI。

他说：他完全可以把 OpenClaw 做成一家大公司，但他不想。他想做的事是「让他妈妈也能用上 Agent」，加入 OpenAI 是最快的路。

OpenClaw 不跟他走。项目转入一个独立的开源基金会，OpenAI 提供资金和技术支持。

在宣布之前那周，他在旧金山跟几家主要实验室都见了面。据报道 Sam Altman 和扎克伯格都亲自试过 OpenClaw，扎克伯格私下在折腾这个东西。Meta 同期收了 Manus AI 和 Limitless AI。

VentureBeat 的判断：**OpenAI 自己推的 Agents API、Agents SDK 和 Atlas 浏览器，都没拿到 OpenClaw 这种量级的自然增长。收编 Peter，某种程度上是在补课。**

代码留在了社区。创始人去了 OpenAI。

## 国内两周干了什么

**Kimi Claw** ：2 月 18 日发布。第一个模型厂商直接下场做的 OpenClaw 产品。

原版 OpenClaw 你得租服务器、装依赖、填 API Key、配搜索、装 Skill、设定时任务、接消息平台，一般折腾半天起步。Kimi Claw 的全流程：**打开网页，说一句话，完了** 。预配了 K2.5 模型，免费额度，搜索服务接好了，飞书直接对接。

> 几十万 Agent 全天候运行，token 消耗量是人的几十倍。谁的模型被写进 Agent 的默认配置里，谁就吃掉一整条 token 消耗曲线。Kimi 是第一个看到这个并且直接出产品的。

其他动作：

  * 阶跃星辰推出了 OpenClaw 国产适配版
  * 三大云（阿里云、腾讯云、华为云）均上线了一键部署
  * 国内多个 Hackathon 以 OpenClaw 为主题
  * 国产芯片完成适配



## 核心洞察

OpenClaw 的爆火，本质上说明了一个信号：**AI 从「能回答问题」到「能替你做事」的跨越，已经到达了可用性阈值。**

围绕着它的整个产业链——基金会、大厂跟进、云端部署、硬件适配——在不到三个月内自发形成，这种速度只有在标准即将确立的前夜才会出现。

_原文发布于 2026年3月2日_
<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->
- [MiniMax创始人闫俊杰：2026年AI发展三大方向预判](./2026-03-02-闫俊杰-2026年AI三大方向预判.md)
- [OpenAI GPT-5.4 mini和nano轻量模型发布价格大降](./2026-03-05-gpt54-mini-nano-price.md)
- [AGI，不会通知你](./2026-03-09-agi-no-notification.md)
- [Google DeepMind发布Gemini Ultra 2.0](./2026-03-10-Google-Gemini-Ultra-2-Release.md)
- [MiniMax M2.7发布1T总参原生Agent Teams多智能体协作](./2026-03-10-minimax-m27-1t-agent-teams.md)
<!-- 相关文章结束 -->
