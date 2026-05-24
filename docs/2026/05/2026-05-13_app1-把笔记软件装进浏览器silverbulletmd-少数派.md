<!-- {"title": "App+1 | 把笔记软件「装进」浏览器：SilverBullet.md - 少数派", "url": "https://sspai.com/post/109399", "source": "少数派", "source_url": "https://sspai.com/", "publish_date": "2026-05-13", "score": null, "tags": []} -->
# App+1 | 把笔记软件「装进」浏览器：SilverBullet.md - 少数派

📅 2026-05-13
📢 来源：[少数派](https://sspai.com/)

> 我试过的笔记软件可能比记过的笔记都多——这样说或许有些夸张，但自2019年RoamResearch进入大众视野，各种支持双链笔记的PKM软件有如过江之鲫。多年来，我也辗转于各类方案、各种组合。我尝试过 ...

<!-- 正文开始 -->

我试过的笔记软件可能比记过的笔记都多——这样说或许有些夸张，但自 2019 年 Roam Research 进入大众视野，各种支持双链笔记的 PKM 软件有如过江之鲫。多年来，我也辗转于各类方案、各种组合。我尝试过一些命令行工具（如 nb、zk），也用过经典编辑器中的的笔记插件（如 Org-roam，vimwiki），还一度回归到 Obsidian 这样的专用软件。
回顾历程，我的核心需求始终不变：所有数据须由个人掌控、所有笔记应以纯文本文件的形式来存储。因一种通用的笔记格式和一个完全受控的笔记库，使不同软件间的协作成为可能。随着智能体 AI 的兴起，这样的选择亦凸显其优势来。
然而，有时我也会怀念用纸笔记录的时代，随手可读，拿起就写，没有负担。在 Obsidian 还没有发布移动客户端的时候，我曾将笔记发布在 Quartz 这样的静态网站上方便自己查阅。而在不同设备、平台间同步笔记与软件的设置，有时也令人颇感厌烦。那有没有什么办法能省却这些不便呢？
认识SilverBullet.md
On almost anything someone does in the computer business, you can go back in the literature and prove someone had done it earlier.
—— Ken Olsen
事实证明，你苦恼中的某个问题，可能早已有人解决。四年前，Zef Hemel 开始了 SilverBullet.md 这个开源项目。与其他 PKM 软件最大的不同在于，它支持自托管，其客户端是一个本地优先的渐进式网页应用程序（progressive web app/PWA）。如果你点进 SilverBullet 的官网，你会发现整个网站就是一个笔记应用的只读实例，你可以在上面体验 SilverBullet 除编辑外的所有功能。
自托管更好地保障了用户的数字所有权；而在人人携带智能手机的今天，作为 PWA 的笔记软件让用户打开浏览器便可使用，无需再操心客户端的重复安装与配置。在介绍 SilverBullet 的更多特点前，先谈谈它的部署方式。
安装SilverBullet
SilverBullet 提供一个单独的二进制文件，但更推荐用 Docker 来安装。你可以先在自己本地的电脑上熟悉整个流程，之后再到虚拟专用服务器（Virtual Private Server/VPS）上进行部署。整个流程大致如下：
- 购买 VPS 和域名。主流供应商大都支持国内的支付渠道，以我个人为例，每年在这上面的花费为百元左右。除开 SilverBullet，你可尝试将自己订阅中的服务替换为其他的开源解决方案，好充分利用服务器的空余资源。
- 在购买的 VPS 上使用 docker/podman 部署 SilverBullet。然后将购买的域名托管至 Cloudflare，并添加 A 记录将域名（或子域名）指向VPS的地址。再在 VPS 上使用 Caddy 或类似工具进行反向代理。这样，你就可以通过自己的域名访问部署好的 SilverBullet 服务。
- 上述部署方式并非唯一。在官网的安装指南中还提及了其他方法（如使用 Cloudflare Zero Trust）。其中，最简单的方法是注册 PikaPods，它提供一键架设开源应用的付费服务，但你可以使用其赠送的免费额度体验 SilverBullet 数月。
体验SilverBullet
登录后，你会进入到笔记库的主页。（默认的主页文件为 index.md
，你可通过 compose.yml
中的 SB_INDEX_PAGE
变量进行设置。）
SilverBullet 的界面如上所示，分为顶栏和编辑区两个部分。顶栏的左侧为笔记标题，右侧为一行可自定义的按钮。其中，最重要的是 Page Picker 和 Command Palette 这两个按钮：
Page Picker：也可通过按键Ctrl-k
触发（MacOS 上为Cmd-k
），用于打开或新建笔记。回车打开选中的笔记，Shift + 回车则会新建相应标题的笔记。
Command Palette: 可通过按键Ctrl/Cmd-/
触发。命令的右侧会显示已有的按键绑定。执行过的命令在排序上会更加靠前。
SilverBullet 中的每一页笔记都是一个常规的 markdown 文件。（后面你会发现，连软件的设置也是md文件。）这些文件会保存在你部署时设置的文件夹中。（通常是一个名为 space 的目录。如果你想迁移现有笔记至 SilverBullet，将相关文件放入该目录下即可。）若你想让其他软件共用 SilverBullet 的笔记库，你仍可使用如 syncthing/git 之类的工具对该目录进行同步或拉取。
当你使用 SilverBullet 时，所有笔记会自动保存。若当前笔记未保存，笔记标题会变为灰色。修改标题相当于重命名你的 md 文件，所有与该文件相关的链接也会自动更新。当你处于离线状态时，顶栏的背景则会变为淡黄色。此时，SilverBullet 会将内容保存在本地，等待上线后重新同步至服务器。
顶栏之下就是 SilverBullet 的编辑区域。在页面底部，与其他双链笔记类似，SilverBullet 会列出 Linked Mentions，即别的页面中引用过当前笔记的所有位置。
现在，你已经对 SilverBullet 有所了解，下面我将介绍一些它的主要功能。
笔记编辑
SilverBullet 和 Obsidian 均使用 CodeMirror 作为底层的编辑器，因而两者在编辑体验上类似，都尽可能地将 markdown 的编辑和渲染糅合在一起。我个人觉得有比 markdown 更适合笔记的文件格式——因各家软件为了补足功能而开发了太多 markdown 的方言，致使一份笔记在不同编辑器中可能出现不一致的表现。无论如何，markdown 已成为许多平台默认的文档格式，SilverBullet 未能免俗，其使用的 markdown 在 CommonMark 的基础上亦添加了许多扩展：
前辅文 / Frontmatter
与 Obsidian 类似，SilverBullet 支持通过页面顶部的 frontmatter 来为笔记添加额外的元数据。比如你可以在 frontmatter 中设置 aliases
来为笔记增加别名。你可以使用斜杠命令(Slash Command)中提供的快捷方式来创建一个空的 frontmatter。
若要为笔记中的个别内容添加属性，你可以使用 Attribute，格式为[attributeName: value]
。若要添加多个属性，你可以这样写： * Item [attr1: foo][attr2: bar]
绝对路径链接 / Wikilink
理所当然，SilverBullet 中的 wikilink 与其他笔记软件中的没有多大不同。它支持自动补全，支持使用形如 [[link|description]]
的格式定义链接显示的文字。你可以通过形如 [[note#heading]]
的格式指向笔记中的某个标题。此外，你还可以使用如 [[note@postion]]
的链接来指向笔记中的某个位置。举例来说， [[note@L10C42]]
将指向某则笔记中的第 10 行第 42 列。 [[note@n]]
则会指向笔记中的第 n 个字符。
由于笔记频繁增删，手动使用 @
+ 位置索引的方式并不可靠，通常只出现在自动生成的 Linked Mentions 中。作为补足，SilverBullet 还支持锚链接。你可以在笔记中的某个区域后添加一个 $anchor
，然后再在另一篇笔记中通过 [[$anchor]]
来指向这块区域。需要注意的是，你的整个笔记库中不可出现重复命名的 anchor。
内容嵌入 / Transclusion
Transclusion 主要用于在当前笔记中内嵌其他笔记的内容。由于嵌入的是笔记本身而非一个副本，笔记的更新就意味着嵌入内容的更新。使用 transclution 只需在上面提到的那些链接前加一个 !
，即形如 ![[link]]
的格式。
行内标签
在 SilverBullet 中，你可以使用 #tag
给整篇笔记添加标签，也可使用同样的格式为笔记中的某个段落，列表中的某个项目，甚至代码块添加标签。两个例子：
- 为段落添加标签：
Paragraph #paragraph-tag-example
- 为列表项添加标签：
* Item #item-tag-example
标签在 SilverBullet 中极为重要，我将在后文中展开介绍。
任务列表
SilverBullet支持使用形如 * [ ] example task
的格式定义待办事项。你可使用斜杠命令 /todo
来创建。任务项的状态支持自定义。
LaTeX
SilverBullet 可通过插件 Math 来使用 KaTeX 渲染行内($...$
)或块级($$...$$
)的数学公式。插件的安装方式很简单，将在后文中的「软件扩展」一节中介绍。
Mermaid 图表
Mermaid 允许你用简单的语法来描述图表结构。SilverBullet 中也可通过安装相应的插件，在笔记中渲染 Mermaid 图表。
Space Lua
除上述扩展外，SilverBullet 还支持提示框、脚注、HTML 标签等功能。但在所有扩展中，Space Lua 最为重要，SilverBullet 中的许多进阶功能都用它来实现。
简言之，Space Lua 是 Zef Hemel 实现的一个 Lua 方言，在 SilverBullet 中，使用它的地方主要有两处：
Space Lua 代码块：
在space-lua
代码块中定义的全局变量或函数，在你整个笔记库的任何地方均可调用。在后文「软件设置」一节中你会发现，配置 SilverBullet 的选项其实就是在space-lua
代码块中使用一些内置的API。
Space Lua 表达式
当你在笔记中插入格式为${expression}
的内容时 ，SilverBullet 会通过对expression
求值，动态地在笔记中生成内容。比如，这行笔记：
The Answer to the Ultimate Question of Life, the Universe, and Everything is ${theAnswer}
将被渲染为：
当然，Space Lua 表达式还有更实用的例子。这就引出了 SilverBullet 中另一个重要的功能：集成查询。
集成查询 / Integrated Query
若你用过 Obsidian 中的 dataview 插件，你可能对 SilverBullet 的集成查询不会感到太过陌生。它使用一种类似 SQL/LINQ 的查询语句（作者称其为 SLIQ）来查找你笔记库中的对象。这里说的对象，可以是某则笔记，也可以是笔记中的一个链接、一项待办任务，或是笔记中存在的其他元素。SilverBullet 通过解析你的笔记索引这些对象，并提供一个名为 index 的 API 让你与其交互。
使用 SLIQ
SilverBullet 默认会给每个对象设置一个主标签，你可以将之视为对象的类型。比如，笔记的主标签为 page
，任务项的主标签为 task
。如前所述，你可以使用API index
来获取对象，如 index.tag("page")
代表你库中的所有笔记， index.tag("task")
则代表笔记库中的所有任务。
要在笔记中动态地嵌入查询结果，你可以使用形如 ${query[[...]]}
的 Space Lua 表达式，其中的省略号代表可能的 SLIQ 语句。它的语法是：
query [[
from <<expression>>
[ where <<expression>> ]
[ group by <<expression>> [, ...] ]
[ having <<expression>> ]
[ order by <<sort_expression>> [, ...] ]
[ limit <<expression>> [, <<expression>>] ]
[ offset <<expression>> ]
[ select <<expression>> ]
]]
下面我将通过两个例子，对其语法进行简单介绍。
例 1：汇总游戏信息
这是dataview官网上的一个例子。假设你有一些关于游戏的笔记，它们的内容格式大致如下：
可见，每一款游戏都是一则笔记，带有game
的标签，并在frontmatter中记录了游戏的其他信息。现在，你想将这些信息汇总成表，对应的SLIQ可以这样编写：
${query[[
from game = index.tag("game")
order by game.rating desc
select {Game = game.name, ["Time Played"]=game["time-played"], Length=game.length, Rating=game.rating}
]]}
此处的 SLIQ 总计三行，解释如下：
第一行：通过from
语句确定要查找的对象，并将对象绑定到变量game
。每个 SLIQ 中都必须包含一个from
语句。
第二行：结果将根据对象的排名game.rating
降序排序。
第三行：使用select
语句选择最终要展示的对象属性。由于要将结果呈现为表格，选取的属性最后被封装在一个 lua table 中，并根据表头定义对应的键值。结果如下：
你还可以使用 SilverBullet 提供的聚合函数来对结果进行统计。比如，下面这段语句将统计打分大于 9 的游戏的数量：
from game = index.tag("game")
where game.rating > 9
select {total = count(game.name)}
例 2：列出所有待办事项
这也是一个相当常见的需求。我将展示一个稍微复杂的用例，先看这段 SLIQ 语句：
from t = tags.task
where table.includes(t.tags, "writing") and not t.done
select templates.taskItem(t)
这段语句的作用是筛选出所有未完成的、带 writing
标签的任务项。下面解释这三行：
第一行：选择所有任务项。 tags.task
是 index.tag("task")
的简写。
第二行： not t.done
代表筛选未完成的对象；前半句则要求对象的标签中含有 writing
。在 SilverBullet 中，除主标签外，其余人为添加的标签（如行内标签）会归并到对象的 tags
这一属性中。
第三行：使用模板将最终筛选得到的对象展示为一个任务列表。
SLIQ 的功能不止于此。篇幅所限，其他语句留待读者根据自身需求自行探索、使用。
软件设置
设置 SilverBullet 有两种方式：
图形界面
你可以使用命令 Configuration: Open
或快捷键 Ctrl/Cmd-,
呼出该面板。通过它，你可以设置部分选项、进行按键绑定和安装插件。
直接编辑
我在前文提过，SilverBullet 的配置其实就是一个 markdown 文档。实际上，你可以在任何文件的 space-lua 代码块中使用 Config API 来修改选项，如：
-- 设置顶栏的按钮
config.set("actionButtons", {
{
icon = "home",
description = "Go to the index page",
command = "Navigate: Home",
priority = 3,
dropdown = false,
},
...
}
但作者建议你将设置统一放在名为 CONFIG
的文件中。由于它是一个md文档，你可以在包含设置、自用函数的代码块附近添加说明，类似于 Emacs 中的 Literate Config。
若要修改 SilverBullet 的样式，你需在 Space Style 的代码块中设置相应的 CSS。你也可以参考官方论坛中用户贡献的主题。若你发现配置未生效，请尝试多刷新几次页面或使用命令 System: Reload
。
软件扩展
若仅仅改动设置无法令你满足，SilverBullet 还支持通过 Space Lua 和插件来增强其功能。
创建笔记模板
还记得 SLIQ 中那个游戏笔记的例子吗？每次创建这类笔记时，你其实无需手动输入 frontmatter。通过笔记模板来创建是更好的办法。
幸运的是，你不必写一些 Space Lua 来定义笔记模板，SilverBullet 提供了相当傻瓜的方法：新建一个带 #meta/template/page
标签的笔记，你便定义了一个笔记模板。下面以游戏笔记的模板为例：
---
command: "Template: New Game"
openIfExists: true
frontmatter: |
tags: game
time-played:
length:
rating:
tags: meta/template/page
---
|^|
创建完上述内容的笔记之后，你便可使用命令Template: New Game
来新建包含所需 frontmatter 的笔记了。其中， |^|
代表笔记新建后光标所处的位置。
创建斜杠命令
你可以在space-lua
代码块中使用 slashCommand.define
来定义新的斜杠命令。当然，更简单的方法是像创建笔记模板一样新建一个带 #meta/template/slash
标签的笔记。比如：
---
tags: meta/template/slash
description: Get current time
---
${os.date("%Y-%m-%d %H:%M:%S")} |^|
假设包含此内容的笔记名为 now
，则你现在可通过 /now
来插入当前的时间。
创建命令
SilverBullet 提供了大量的 API 供你使用。下面仅以一个例子，展示如何用command.define
灵活地创建多个命令。
-- 定义命令要使用的函数，使用内建的API获取光标处的标题文本
-- 若参数level等于当前的标题层级，则将标题还原为普通文本
-- 若不等，则修改为对应level的标题
local function toggleHead(level)
local line = editor.getCurrentLine()
local text = line.text
local currentLevel = string.match(text, "^(#+)%s*")
currentLevel = currentLevel and #currentLevel or 0
local textC = line.textWithCursor
local posC = string.find(textC, "|^|", 1, true)
local lineHead
if posC > currentLevel + 1 then
local bodyTextC = string.gsub(textC, "^#+%s*", "")
if currentLevel == level then
lineHead = bodyTextC
else
lineHead = string.rep("#", level) .. " " .. bodyTextC
end
else
local bodyText = string.gsub(text, "^#+%s*", "")
if currentLevel == level then
lineHead = "|^|" .. bodyText
else
lineHead = string.rep("#", level) .. " |^|" .. bodyText
end
end
editor.replaceRange(line.from, line.to, lineHead, true)
end
-- 使用循环定义6种标题层级的命令，并将它们绑定到Ctrl-(1～6)。
for lvl = 1, 6 do
command.define {
name = "Header: Toggle Level " .. lvl,
key = "Ctrl-" .. lvl,
run = function()
toggleHead(lvl)
end
}
end
使用插件
SilverBullet 中的插件是一种自包含的 js 文件（以 .plug.js
结尾），运行在沙箱化的 Web Worker 中，通过 syscall 与编辑器通信……作为普通用户，你也许并不想知道那么多。你可能更关心现在有哪些插件，怎么安装？
SilverBullet 目前的插件数量与 Obsidian 相差甚远，但已具备许多热门功能（如 Excalidraw、GraphView、前文提到的 Mermaid 图表等）的支持。下面介绍几个我认为值得安装的插件：
为SilverBullet添加基本的 Git 支持。你可以设置该插件，使其每隔一段时间自动将你的笔记提交到别的仓库中去。
显示笔记库的目录树。
笔记库全文搜索工具
除了使用图形设置界面中的入口，你还可以在plugs
设置项里添加插件地址来安装插件。（添加后需运行命令Plugs: Update
）
-- 直接在CONFIG文件中安装插件
config.set {
plugs = {
"ghr:LogeshG5/silverbullet-drawio"
}
}
你可以在论坛的插件板块发掘更多插件。如果你想自己开发插件，可以参考这篇指南。
结语
尽管在社区中声名不显，但我认为 SilverBullet 是一款被低估了的软件，绝对值得一试。每次在新设备上，打开浏览器就能阅读、编辑我的笔记时，我都要感谢它提供的便利。
鉴于SilverBullet最近发布的 CLI 功能，我认为其还有相当多的潜力待挖掘。作者也同时在开发 SilverBullet+ 来探索可能的盈利模式。除却热爱，很难想象 Zef Hemel 在整个过程中耗费了多少心力。我也真心期望这样的开发者能收获更多的支持。
- SilverBullet+ 是 SilverBullet 的桌面版本，支持 Windows/MacOS/Linux。目前 beta 版可免费下载，对想快速尝试 SilverBullet 的人来说是最便利的方式。
- 除了阅读官方文档外，许多使用技巧都四散在 SilverBullet 的官方论坛中。比如有用户在笔记中记录并渲染吉他的和弦指法，这样的例子我无法在文中尽述。
- 本文仅题图使用 AI（GPT Image 2）生成。Prompt大致为「请根据SilverBullet.md的 logo 生成一张 App Store 横幅样式的图片。要求将 logo 放在成图的左下角，且背景中需有记事本、笔、咖啡和笔记本电脑」。图片经过几次修改，电纸书和手机都是后续为补足画面空余而加入。

<!-- 正文结束 -->

## 相关文章
<!-- 相关文章开始 -->

<!-- 相关文章结束 -->