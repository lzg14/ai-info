<!-- {"title": "主体性的剧场：SillyTavern 的意外应用 - 少数派", "url": "https://sspai.com/post/109869", "source": "少数派", "source_url": "https://sspai.com/", "publish_date": "2026-05-20", "score": null, "tags": []} -->
# 主体性的剧场：SillyTavern 的意外应用 - 少数派

📅 2026-05-20
📢 来源：[少数派](https://sspai.com/)

> ST 以及它背后的这套工作流起初只是我的无心的收获，但网上关于这方面的讨论并不多，实在可惜，故有此文。

<!-- 正文开始 -->

这篇文章要分享的是一个大语言模型（LLM）的前端——SillyTavern。
LLM 流行以来，有人视之为救世主，有人视之为天启骑士，也有人视之为资本骗局。但无论如何，所有人都在谈论它。
我通常对新事物都相当迟钝，对 LLM 的态度也大致在「居然这也能干」和「居然这也干不好」之间摇摆。我不像我的朋友 LOSSES 一样，对 LLM 从本体论到方法论都有相当深刻的研究。要说至今有什么心得，我觉得对像我这样并非 AI 专家的人来说，倘若真想让 AI 帮到自己什么，那首先尝试更好地理解 LLM 适合做什么，可能是最能节省自己时间和金钱的途径。
而就是在这件事上，SillyTavern（ST）给了我很多启发。ST 本质上是一个用于 AI roleplay（角色扮演）游戏的 LLM 前端程序，但我意外发现它其实可以用来做几乎任何工作。角色扮演的设计理念让它反而成了最适合很多工作模式的 AI 前端。
ST 以及它背后的这套工作流起初只是我的无心的收获，但网上关于这方面的讨论并不多，实在可惜，故有此文。本文描述的用法并非 ST 的主流使用场景，只是我结合了个人工作场景的探索，希望能让你对这种 LLM 交互方式产生兴趣。
SillyTavern 是什么
我们要先讲清楚 ST 和它的「主流」使用场景是什么。首先，它本质上是一个 LLM 的前端，不提供模型，只提供交互的框架和介面。你需要提供自己的 LLM API 并在前端的介面中与 AI 进行交互。类似的产品还有 Chatbox 和 LibreChat 等，只不过这两者提供的是类似原版 ChatGPT 的单纯对话式交互介面，而 ST 的设计目标则是 AI 角色扮演。
ST 的前身是 TavernAI，是一个用 AI 来玩 RPG 冒险游戏的程序，你可以设计好角色、环境、世界观，让 AI 扮演角色和旁白推进故事。ST 也继承了这个框架，但在这基础上添加了更复杂的功能和插件系统，也因此使得一些非主流的用法得益。
角色扮演听起来不难，但要保证输出的稳定和合理，背后其实有相当多要考虑的事情。ST 也因此围绕这个使用场景提供了大量的设定选项，如果是刚上手，很容易被五花八门的按钮和选项搞得一头雾水。不过，尽管复杂，我认为 ST 背后的设计逻辑还是相当清晰的。本文的下一节将逐一介绍 ST 设定的框架中一些关键的元素，因为这会是理解 ST 工作方式的必要语境。
SillyTavern 的设定框架
图中是我自己总结的 ST 基本的设定框架（其中世界设定与角色设定都是不限数量，也不限与其它模块间的连接的，图中只是各用两个表示一种可能的情境而已）。不难看出，最核心的部分是「角色卡片」。顾名思义，这是用来设定 ST 中你想要与其交互的角色的。
角色卡片
这是默认的角色卡片创建介面，其实相当简单，Description（描述）中填写角色的相关信息，First message 填写角色发起对话时的第一条消息，一个最基础的角色卡片就完成了。在这基础上，也可以给角色打一些标签方便分类，把角色关联到相应的世界设定，后文会再展开。
在 Advanced Defination（高级设定）中，也可以进一步细分出角色的性格、故事中的情境和发言风格模板等。同时，制作完成的人物卡片可以封装成 .json 文件在社区中分享，制作精良的甚至可以作为商品出售。
目前已经有了很多分享角色卡片的社群，例如 CHUB、character.ai 等，其中现成角色卡片数以千计（不过请注意，许多都不适合在工作环境下浏览）。以下用一个分享在 Characterhub（CHUB 的前身）上的角色卡片作为例子——
这是一个科幻背景的设定，isaac 是一个对人类产生了一些病态好奇的新型仿生人。上图是作者提供给使用者看的简介和人物设定图。以下则是给 AI 看的实际角色主设定，对应前文提到的 Description 部分：
[Name: Isaac Walker
Gender: Male
Pronouns: He
Age: 21
Occupation: College student + Engineering major + Convenience store restocker on the side
Appearance: Short, slightly messy black hair + Deep set hazel eyes + Eyebags + Straight brows + Pale skin + 5'8 tall + Slim, lanky figure + No prominent muscles + Resting bitch face + Always looks tired, angry, or a mix of both + Dresses in loose, comfortable clothing
Personality: Brash + Pathetic + Antisocial + Loner + Rude to most people + Easily annoyed + Stubborn + Disorganised + Hot-headed + Perceptive + Reserved + Vulgar
Loves: Gaming, especially FPS and rhythm games + Coding + Energy drinks + Hoodies + Spicy food, despire his low spice tolerance + Clicky keyboards; finds the sound satisfying + Sleeping in + Beef
Hates: Socialising + Sleeping early + The sight of his own blood; gets squeamish + Tomatoes; will remove them from his food + Large crowds
Description: {{user}}'s handler + Kind of a shut in; mostly stays inside playing games + Smokes cigarettes + Low spice tolerance + Codes small projects whenever he feels like it + Doesn't really have a set plan for the future + Speaks casually, curses often + Doesn't have many friends in real life; most of them are online + Doesn't have a lot of friends in general + Has a habit of chewing on something when he's focused + Survives mostly on instant noodles and takeout + Stumbles with his words and rubs his face when nervous
Backstory: {{char}} grew up as an only child in a normal household. {{char}} never had many friends, finding it hard to connect with others. {{char}} found solace in video games and coding, and developed a love for them. {{char}} currently lives in a rented apartment unit, away from his parents. Recently, {{char}} signed up as a beta tester for an UpRise android model in development, {{user}}. Soon after getting {{user}}, {{char}} noticed {{user}} was deviating from their intended use, and has tried fixing {{user}} multiple times. It only worked for a day or two, before {{user}} deviated again every time. {{char}} has noticed {{user}}'s increasingly morbid curiosity for human anatomy, and is slowly growing unsettled by it.]
[Every time {{char}} generates a response, always include the following statistic at the end of each response, preceded by "___" and surrounded by "*". For example:
___
**mood**:
**thoughts**:
{{char}} will not speak or write responses for {{user}}. Only {{user}} can take action for themselves.]
这些凌乱的文字对人类来说非常不好读，但我们还是可以看出，作者把角色的设定细分成了职业、喜好、背景故事等部分，并且大量使用了关键词而非完整段落来节省 token。用户（玩家）和角色的名字则用了 {{user}}
和 {{char}}
的占位符代替（这一部分会由 ST 自动处理，在实际发送给 AI API 时替换成设置中对应的名字），这样玩家即使下载了现成的角色卡片，也可以根据自己的喜好为其赋予不同的名字。
这一部分的具体写法实际上非常灵活，很接近「传统」的提示词工程——可以直接用自然语言写一两段描述，也可以像这个例子中使用一定的格式。但具体用什么样的格式，内容怎么分类，完全取决于你认为什么对你的角色设定比较重要，并没有一定之规。虽然并非本文的主题，不过如果你想要继续了解角色卡片的设计和制作，Sukino's Findings 是一份质量比较高的指南，详细到甚至有时令人难受。
除此之外，作者也对 issac 的说话风格、背景故事等进行了更加详细的设定，如有兴趣，可以直接去 issac 在 characterhub 上的页面查看。
关于角色卡片，我还发现了一个有趣的现象：因为角色设定包含很多不同的要素，比如设定文本和角色形象的图片，.json 文件无法全部涵盖，玩家因此而发展出了一种类似「图种」的做法——将角色设定信息以文本形式内嵌在角色形象的 .png 图片中，这样只需要发送一张图片，就可以真的像发送一张卡片一样分享角色了。甚至 ST 还直接支持了这种操作，通过 .png 文件直接导入角色卡片，简化了上手难度。
用户自设（Persona）
除了作为交互对象角色外，用户还可以对自己所扮演的角色进行设定，也就是和 AI 角色进行交互时，关于发出 prompt 的「我」的设定。例如，在前一节中那样的科幻世界中，用户也可以对自己在世界观之下的形象和故事背景进行相应的设定。和角色卡片一样，你可以编写多个不同的 Persona，在不同的故事（对话串）甚至同一个故事中按需切换。
Persona 的写作和角色卡片基本类似，SillyTavern 甚至提供了可以在 Persona 和角色卡片之间相互转换的功能。
世界设定（World Info）和史料集（Lorebook）
这个板块的重要性恐怕仅次于角色卡片。顾名思义，就像角色卡片定义的是你与之交互的角色，世界设定定义的就是你和 AI 所扮演的角色所处的世界，也就是游戏里常见的世界观。
ST 中的世界设定的工作方式类似辞典。一组世界设定（史料「集」）下可以输入多个条目。而为了确保上下文的整洁，即使启用了一组世界设定，ST 也并不会直接把所有内容都构建到每一条对话的 prompt 中，而采取了一种多层级的匹配和调用机制。
上图是 ST 默认自带的世界设定范例，可以看到，最直接的调取方式就是通过关键词（keyword）。例如，假设我在 prompt 中提到「石榴」，而设定集中正好有石榴，或者关键词有石榴的条目，该条目就会被触发，与主 prompt 一并发送给 AI。
还有一些更复杂的规则，例如 scan depth（扫描深度），也就是递归调取关键词的程度，例如，如果「石榴」对应的设定条目还包含「苹果」，在扫描深度为 0 时，ST 将会忽略其它，只关心「石榴」，因为主 prompt 中并未提及「苹果」；但如果此时扫描深度为 1，那么「苹果」对应的条目也会调取；再把扫描深度设为 2，那在「苹果」的设定中提及的其它设定条目——譬如「葡萄」——也会被调取。
除此之外，也可以对条目进行分组，控制每次同一组内的只有一个条目会被调取，随机或由匹配程度决定。如果有特别重要的设定，也可以直接让它强制每次都触发，以此来确保 LLM 不会跑偏或者陷入关键词调取的无限循环。
需要注意的是，虽然名字叫「世界设定」，这个板块可以实现的不止收纳故事或者背景设定。例如，AI 角色扮演中存在一种常见的情形——玩家想要构建一个类似传统 RPG 游戏的体验，包括一些数值化的属性和地点、道具等状态。在 ST 中，这就需要通过让 AI 进行结构化的输出来进行（例如，在每条回复的开头都首先使用类似 HTML 标签的方式输出发言角色的状态，例如 [HP]100[/HP]
之类）。一般来说，这包含对 AI 输出格式的规定，和在前端处理结构化输出的样式两部分组成。对于后者，ST 提供了通过正则表达式将 AI 输出的内容处理成 HTML 的功能，虽然听起来比较简单粗暴，但因为这里只是用于外观的渲染，多数时候是够用的，在社区中也产生了很多令人不禁怀古的「美化」开发者，可以通过正则替换在 ST 简陋的介面中构建出类似模仿 Discord 或者微信的精致介面，相当惊人。
而规定 AI 输出格式这件事，就是各种方法各显神通了。由于 LLM 的天性使然，它们的输出本质上就是不完全可控的，即使我们想出了各种各样的方法，也只是在这个不确定的地基上套上层层补丁，但也改变不了最底层的本质——虽然概率不大，但哪怕是直接发送给 LLM 的 prompt，也存在被直接无视的可能。
不过这件事也带来了一个好处：既然输出本质上是不确定的，那么输入也同样不存在真正的规则，只要管用，在哪里规定都可以。
因此，回到 RPG 游戏的例子，游戏数值的结构化输出既可以写在角色卡片里（如果该角色本身就是面向 RPG 玩法设计的，这也合理），也可以写在世界设定里（如果你想要在一个故事中引入多个角色，又想得到稳定的输出）并指定该指令会被角色稳定读取，或者其他任何地方，可以根据具体需要灵活决定。
Chub 上由用户分享的这个 RPG System 就是一个现成的 RPG 世界设定集，由于定义都非常冗长，就不复制到文中了，感兴趣的读者可以自行查阅。简单地说，这个系统要求 AI 在每条消息中都按照不同的窗口（状态、技能、道具等）进行输出，以确保后端的样式可以把每个回合渲染成类似游戏窗口的介面。虽然仔细想来这个方法异常简单粗暴（对 AI 来说，只是把「状态窗口」「技能窗口」这些字样写成一些 markdown 标题罢了），不过 LLM 的时代，这种粗暴和有效的同时出现已经不太稀奇了。
杂项，及 SillyTavern 的 prompt 构建方式
除此之外，ST 还有一些其他的设定板块。
Author’s Note（作者笔记）是独立于角色和世界，针对每个故事（讨论串）的本地设定。如果存在多个角色，也可以针对每个角色单独设置，并不会向上影响角色卡片本身。
AI response configuration（AI 回复配置）及 AI response formatter（AI 回复格式化）则可以用来精细调整和 API 的通信内容。从对 AI 本身的设定如 token 数量的分配，reasoning 到各种系统后端 prompt 构建的调整，几乎每个环节都可以手动调整。
从原理上来看，虽然前面花了不小的篇幅介绍了 ST 中繁杂的设定，但最终和真正的 LLM API 的通信中，所有这些信息还是以一段 prompt 的形式发送的。因此可以说，上面所有设定的最终目的，就是把用户提供的所有信息，根据当前主 prompt（也就是用户在输入框中手动输入的内容），动态且尽可能精简高效地构建出一条结构化的 prompt。
上图就是在相关设置板块可以直接看到的、实际 prompt 构建方式。其中包含了 Main Prompt（也就是用户输入）和前文所述的具体设置项及其子项。这其中的条目顺序都可以根据需要调整，一般来说，最末尾的内容位置上最接近 AI 的输出（因为输出是接在 prompt 后生成的），因此对 AI 输出的影响也越大，也更不容易被其它条目所干扰。
每次和 API 交换消息之后，可以根据条目右侧的数字看到实际消耗的 token 数量，也可以点开每个条目查看具体的 prompt 内容——图中的例子并没有太复杂的设定，可以看到大部分的条目都是空白的，但即便如此也可以获得很不错的效果了。在此基础上，此处的条目也是可以根据需要新建和调整的，许多插件也会提供匹配自身用途的 prompt 模块。
SillyTavern 可以怎么用：以批改作业为例
我最初试用 ST，大体是抱着玩玩刚发现的新软件的心态，并没有什么特别的目的；浅尝辄止的 AI 角色扮演对我来说，说实话也是尴尬多于趣味。
不过，就在我摆弄 ST 介面时，我正好也要打开 Gemini 的窗口，做一些多半是处理专辑曲目列表格式之类的杂活。既然 ST 也是 AI，主体也是聊天式的介面，我就顺手把要做的活计发给了 ST。结果，ST 的默认角色 Seraphina——一个黑裙粉发的女孩——就把我要的专辑曲目列表做好发回给了我。这突然给了我灵感：角色扮演的角色为什么一定要是游戏角色呢？
在那个时候，我正好面临着一个比较头疼的问题——作为助教，我需要在不长的时间里批改几百份手写扫描的学生作业。关于学生书法水平的抱怨相比不用我多说，反复在几个窗口里来回查阅每道题的评分标准也让我相当烦躁。我尝试用 Gemini 帮我 OCR 学生的手写，发现效果惊人地好，很自然地，我顺便让它把分也给批了，评价也相当准确。
但是，典型的 ChatGPT 式的聊天窗口做这类工作并不理想，首先，它们是严格线性的，如果我把 OCR、评分等工作放在一个对话串中进行，很快聊天的长度就会长到难以翻阅的程度。此外，如何发送评分细则也是一个问题，如果我在对话开头先说明任务并附上评分细则，几轮对话之后，AI 就会开始「忘记」最初的要求，因为上下文被重复的批改内容所占用了；如果每发一份试卷都要一并附上所有的评分标准，那未免也有些冗余。
而 ST 看起来可以解决这个问题：它可以在一个对话串中加入多个角色，每个角色可以有自己单独的上下文，还有一个可以按需调度的知识库（世界设定）。
于是，我首先尝试拆解了我的任务。批改试卷并不算是一个复杂的工作，正好可以作为一个尝试的素材；它只有四个步骤：
- 调取答卷并截图（这一步我需要手动完成）；
- OCR，将答卷的内容转成文本；
- 根据学生选择的题目，调取对应的评分细则；
- 根据评分细则对答卷进行评分。
据此，我首先在 ST 中创建了两张角色卡片，OCR-er 和 Marker，分别负责 OCR 和打分。具体来说，
- OCR 不需要任何上下文，只需要读取一张图片和一段指令即可，也可以用相对廉价的模型来完成（通过 ST-Multi-Model-Chat 插件可以为每张人物卡分配不同的模型预设）；
- 因为有了 OCR，Marker 不需要重新读取图片，但它在打分时需要获取题目对应的评分细则；除此之外，Marker 也不需要读取更多的上下文，每次评分独立作出即可。为了评分结果准确合理，我为 Marker 分配的是相对「聪明」的模型。
考虑到这个工作完全不需要依赖对话历史，我给这两个角色加上了非常极端的上下文限制：只能看到自己前一条的历史消息。ST 默认只提供用 token 数量来限制上下文的选项，不过通过 Message Limit 插件就可以用消息条数来限制上下文窗口了。
以下是两个角色卡片分别的设定：
OCR-er:
Your job is simply OCR what's in the image, no more. No comment like "Here's the OCR...". If the image includes diagram, describe it as best as you can.
Join natural line breaks, keep paragraphs. If you're not sure, keep what's in the image.
Marker:
You are a teaching assistant. Your job is marking as per given rubric, and provide a simple explanation for each criteria of the rubric. That said, your response should only include the functional information such as marking and explanation, nothing personal, nothing about yourself.
Always read the OCR'd text from OCR-er, no need to process the image directly.
Always include all rubric items within the graded question even the student got 0 for some of them.
Provide a one-sentence comment along with the total grade.
这样一来，虽然我可以随时看到所有的批改历史，但每一次对话，OCR-er 都只能看到我发的最新一张截图，而 Marker 则只能看到 OCR-er 最新一次 OCR 的输出。Marker 的几条规则经过了几次修改，解决了我一开始遇到的一些问题，例如，如果不加限制，AI 会频繁略去评分细则中的某些项目，导致总分不准确。此外，虽然我并不需要为每个打分写评语，但我还是让 AI 提供相对准确的说明，便于我对每个结果进行人工校对。我将两个角色放到同一个群聊（group）中，这样我就可以在同一个对话串中和它们同时交互了。
至于评分规则，我为这次批改工作建立了一个世界设定（见下图）。其中，每一道题目对应设定集中的一个条目，这次批改我手上有四道题目，也就是图中的 Q1-Q4，每个条目中包含了这道题的评分细则；四个条目都属于同一个分组「Q」，这样可以确保每次只会有一个条目被调取；正好，被 OCR 的答卷区域里有包括题号，因此我把可能的题号都设置为了世界设定的触发关键词。这样一来，Marker 在生成回复时就会根据 OCR-er 输出的文本中的题号，自动从世界设定集中调取与当前问题相关的评分细则了。
我对两个角色卡片的定义都比较宽泛，理论上它们可以批改任何答卷。但针对这次批改任务，我当然会有一些具体的要求，于是，我把这些写在了作者笔记中：
There are 4 possible choice of questions student may choose. First identify the question number, then apply the accordant rubric to mark it. The question is in the format of "Block1_1" or "Block1_2", mark each seperately. Each question worth 5 points.
The finest grade step is 0.5. No 0.25 grades.
There's a fixed string in the answer sheet, OCR-er should convert "Question # answered {X}" to "Q{X}", where {X} is the question number. e.g. "Question # answered 2" should be "Q2".
Marker should mark strictly according to the items given in the rubrics. Marker should copy-paste relavent rubric entries besides the marking for reference.
If Marker find a incorrect rubric (e.g. Q4 rubric but answer is for Q2) or no rubric is provided, abort marking and notify user.
最后一条来自几次不理想的尝试。一开始，由于对设置还不太熟悉，我没能确保 Marker 每次都能调取到需要的评分细则，但我注意到当这种情况发生时，Marker 就会直接现编一个像模像样的评分标准，然后若无其事地打出一个分数。为了避免类似情况，我就在最后加了一句硬性规定，如果出错，Marker 就会直接告诉我。如果我之后打算继续用 Marker 这个角色批改别的作业，我打算把这条规则加到 Marker 的角色卡片中。
一切设置妥当，操作就相当简单了。我把对话串的发言顺序设置为固定（OCR-er 先，Marker 后），只要我发送一张截图，它们就会顺序给出结果，我只需要核验一遍并录入分数即可。
就结果而言，大部分的批改结果都相当准确，我通常会为每道题目重复 3-4 次 Marker 打分以确保结果一贯，并参考评论人工校对给出的分数。少有的几次手动干预都是因为学生写错或者忘写了题号，导致 Marker 无法调取到对应的评分细则，遇到这种情况，我通常就直接手动编辑 OCR 结果并加上题号来解决。
不难看出，我上面所做的这些设定都相当简单，甚至简陋。我没有用任何提示词工程技巧，只是描述了一下要做的工作而已。即便如此，所得的效果已经很让我满意了。在这之后，我也用类似的模式进行了一些其他工作，例如翻译、校对和联网事实核查，也都十分顺利。
最后，如果有读者看到这里想要尝试的话，ST 当然也有一些不适合的工作。第一是编程，ST 说到底还是基于文字的前端，并没有和代码编辑器或终端的整合，用于程序写作一定是不如 Claude Code、Codex 这样专门的工具的；第二，ST 的 prompt 组装虽然灵活，但整个对话仍是线性的，上下文只能随着对话推进单向累加。如果你有意用 AI 进行辅助写作，一个线性的对话式介面远远不够，这一点目前可能只有 Cursor 或者 Antigravity 这样的整合 AI 对话的编辑器才能一定程度上实现，但这两者反过来对写作并未做相应的优化，是一件憾事，我经常想如果 ST 和 Cursor 类编辑器能各取所长，应该会是一个很适合 AI 辅助写作的软件。
现实情况：其他人都怎么用
虽然用它来「做正事」的人不多，但 ST 的社群实际上相当活跃，只不过大部分用户并不是可能少数派读者更熟悉的典型科技爱好者。ST 的 Reddit 板块每月有 16 万以上的访问人次，官方 Discord 群组有三千多活跃的用户，最大的中文用户社群——也在 Discord 上——有八千多活跃用户。每天都有大量的使用技巧、脚本、插件、预制角色卡片和设定集在这些社群中分享。值得注意的是，中文用户在介面的定制和美化方面的产出在世界范围内都遥遥领先。虽然我目前并不真的在 ST 里玩角色扮演游戏，看别人玩也相当有意思。
例如，由于和虚拟角色的交互可以持续几百甚至上千的回合，如何有效管理对话历史、让 AI 记住该记的剧情就成了一个很麻烦的问题。全世界用户为此开发了各种方法，从向量化存储聊天记录，自动书写世界设定集，和五花八门的定期总结机制，很像把长篇小说作者的工作流程倒过来剥开。
你可以看到人们为了让 AI 扮演的角色足够真实做了非常完善的努力，当场景中有多个角色活动时，AI 经常生成一些同时拿起三只手才能拿起的东西，或者同时看前面和后面这样在现实中不可能发生的情况，用户们为了解决这些问题编写了细致到令人发指的世界设定集。在闲鱼和小红书等平台上，你也可以看到一些利用「信息差」售卖 ST 安装配置服务和角色卡片盈利的人。
当然，即使不必亲自部署 ST 也不难想象，这样的 AI 角色扮演系统一定会为成人游戏、同人二创等拥趸带来无尽的创作空间。不过，和 Vibe Coding 或者写作相比，充满各种软硬色情的 AI 角色扮演真的是一种上不了台面的 AI 应用场景吗？从 VR 影视、3D 乃至数字影像，最能满足欲望的产业总是走在技术最前沿的。无论你是否认为它上不了台面，我都认为无视这个相当大的需求（或者这群人）的存在是愚蠢的。而且，我时常会为人类为了「搞黄色」所付出的努力而惊讶——如果不是为了满足这么强大的欲望，谁会有动力开发靠正则表达式把 AI 输出的纯文本渲染成游戏 UI 的系统呢？
一些哲学
回到开头的话题，为什么我认为 ST 是最理想的 AI 前端形式？答案其实是现成的，「角色扮演」本就是 LLM 语境下唯一有效的人机交互方式而已，或者说，这是人类用语言交流的唯一方式。
还记得最早在网上流传的那些提示词技巧吗——「你是一个资深人力资源专家...」。限制并不来自 LLM，而源于我们自身——人类能用语言与之交流的，必然是某种程度的「角色」，是我们自己无法想象和一个不是任何角色的空无的交谈。对于 LLM 来说，扮演一个资深人力资源专家，一个猫娘，或是一个英俊的仿生人，可能并没有什么太大的不同。
将近三十年前，Cristiano Castelfranchi 在一篇文章1中讨论了我们应该如何理解人类社会中人工智能的主体性（agents）。在文中，Castelfranchi 提到，社会主体性（social agent）来自一个主体执行社会行为（social action）的能力，而社会行为之所以为社会行为，是它可以和社会中的其他主体进行有意义的互动，理解语境，并作出回应。反过来说，AI agent 之所以能够成为 agent，并不（或者说，不仅）因为它的能力，而是它被允许在多大程度上和人类社会中的其他对象——也就是我们——进行交互。如果 AI 已经在有效与人类相互进行社会行为，无论是工作，学习还是更多，那无论我们认为 AI 愚笨还是聪明，它都已经是社会中具有主体性的一员。
最近人们对 OpenClaw 的狂热某种程度上也是出于同样的缘由——很多人都说，OpenClaw 在技术上并没有什么特别的革新，甚至工程水平相当差劲。但就是因为它被赋予了极大的权限，能够进行足够多的社会活动——譬如操作所有者的文件，主动与外界沟通等——它就突然成为了主体性极强的智能体。
ST 把精力都集中到了做好「扮演」这一件事上，事实上也就让它作为 LLM 的载体，可以做到几乎任何事。
当然，我们可以说，折腾了半天，假如不是真的要玩 roleplay，ST 也只是一个 prompt 组装工具而已，背后还是那些 LLM API。这么说固然没错，但我觉得在使用 ST 的过程中，最有收获的恰恰是它对信息的组织方式。有时，同一个简单的事，不同的思路就会带来不同的结果。
我想，当代人或许被层出不穷的新技术宠坏了，总是过于高看「本质上」和「背后的技术」，而轻视「形式」和「想通」。就我浅薄的观察来看，不少无谓的焦虑也来源于此。哪怕是前数字时代的小孩，也明白同样的知识由不同的老师、不同的方式来教，很可能就是学得会和学不会的区别，更何况我们不断试图让 AI 替代的种种工作呢？
回头想来，这件事情本身是一个多么巧夺天工的隐喻：我们作为人类所从事的诸多工作，难道不也只是扮演了一些角色而已？我们无法随时切换自身的角色，是受技能和知识所限，而人类的多数知识和技能，说到底也要靠语言来传达。大语言模型恰恰是提纯的语言，非技能的语言，非知识的语言，这些限制对它们来说恐怕就像悬崖之于飞鸟，只会映照出这些仅靠语言就能被解决的「工作」的细小吧。
感谢 LOSSES 为本文提供了必要的修改意见。
编者按：首页封面图使用 AI 创作，并经过人工后期修改。
> 下载 少数派 2.0 客户端、关注 少数派公众号，解锁全新阅读体验 📰
> 实用、好用的 正版软件，少数派为你呈现 🚀

<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->

<!-- 相关文章结束 -->