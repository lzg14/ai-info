<!-- {"title": "The creator of Claude Code just revealed his workflow, and developers are losing their minds", "date": "2026-01-05"} -->
# The creator of Claude Code just revealed his workflow, and developers are losing their minds
📅 2026-01-05
📢 来源：[VentureBeat AI](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are)

> Claude Code creator Boris Cherny reveals his viral workflow for running multiple AI agents simultaneously—transforming how developers build software with Anthropic's coding tool.

<!-- 正文开始 -->

When the creator of the world's most advanced coding agent speaks, Silicon Valley doesn't just listen — it takes notes.
For the past week, the engineering community has been dissecting a thread on X from Boris Cherny, the creator and head of Claude Code at Anthropic. What began as a casual sharing of his personal terminal setup has spiraled into a viral manifesto on the future of software development, with industry insiders calling it a watershed moment for the startup.
"If you're not reading the Claude Code best practices straight from its creator, you're behind as a programmer," wrote Jeff Tang, a prominent voice in the developer community. Kyle McNease, another industry observer, went further, declaring that with Cherny's "game-changing updates," Anthropic is "on fire," potentially facing "their ChatGPT moment."
The excitement stems from a paradox: Cherny's workflow is surprisingly simple, yet it allows a single human to operate with the output capacity of a small engineering department. As one user noted on X after implementing Cherny's setup, the experience "feels more like Starcraft" than traditional coding — a shift from typing syntax to commanding autonomous units.
Here is an analysis of the workflow that is reshaping how software gets built, straight from the architect himself.
How running five AI agents at once turns coding into a real-time strategy game
The most striking revelation from Cherny's disclosure is that he does not code in a linear fashion. In the traditional "inner loop" of development, a programmer writes a function, tests it, and moves to the next. Cherny, however, acts as a fleet commander.
"I run 5 Claudes in parallel in my terminal," Cherny wrote. "I number my tabs 1-5, and use system notifications to know when a Claude needs input."
By utilizing iTerm2 system notifications, Cherny effectively manages five simultaneous work streams. While one agent runs a test suite, another refactors a legacy module, and a third drafts documentation. He also runs "5-10 Claudes on claude.ai" in his browser, using a "teleport" command to hand off sessions between the web and his local machine.
This validates the "do more with less" strategy articulated by Anthropic President Daniela Amodei earlier this week. While competitors like OpenAI pursue trillion-dollar infrastructure build-outs, Anthropic is proving that superior orchestration of existing models can yield exponential productivity gains.
The counterintuitive case for choosing the slowest, smartest model
In a surprising move for an industry obsessed with latency, Cherny revealed that he exclusively uses Anthropic's heaviest, slowest model: Opus 4.5.
"I use Opus 4.5 with thinking for everything," Cherny explained. "It's the best coding model I've ever used, and even though it's bigger & slower than Sonnet, since you have to steer it less and it's better at tool use, it is almost always faster than using a smaller model in the end."
For enterprise technology leaders, this is a critical insight. The bottleneck in modern AI development isn't the generation speed of the token; it is the human time spent correcting the AI's mistakes. Cherny's workflow suggests that paying the "compute tax" for a smarter model upfront eliminates the "correction tax" later.
One shared file turns every AI mistake into a permanent lesson
Cherny also detailed how his team solves the problem of AI amnesia. Standard large language models do not "remember" a company's specific coding style or architectural decisions from one session to the next.
To address this, Cherny's team maintains a single file named CLAUDE.md in their git repository. "Anytime we see Claude do something incorrectly we add it to the CLAUDE.md, so Claude knows not to do it next time," he wrote.
This practice transforms the codebase into a self-correcting organism. When a human developer reviews a pull request and spots an error, they don't just fix the code; they tag the AI to update its own instructions. "Every mistake becomes a rule," noted Aakash Gupta, a product leader analyzing the thread. The longer the team works together, the smarter the agent becomes.
Slash commands and subagents automate the most tedious parts of development
The "vanilla" workflow one observer praised is powered by rigorous automation of repetitive tasks. Cherny uses slash commands — custom shortcuts checked into the project's repository — to handle complex operations with a single keystroke.
He highlighted a command called /commit-push-pr, which he invokes dozens of times daily. Instead of manually typing git commands, writing a commit message, and opening a pull request, the agent handles the bureaucracy of version control autonomously.
Cherny also deploys subagents — specialized AI personas — to handle specific phases of the development lifecycle. He uses a code-simplifier to clean up architecture after the main work is done and a verify-app agent to run end-to-end tests before anything ships.
Why verification loops are the real unlock for AI-generated code
If there is a single reason Claude Code has reportedly hit $1 billion in annual recurring revenue so quickly, it is likely the verification loop. The AI is not just a text generator; it is a tester.
"Claude tests every single change I land to claude.ai/code using the Claude Chrome extension," Cherny wrote. "It opens a browser, tests the UI, and iterates until the code works and the UX feels good."
He argues that giving the AI a way to verify its own work — whether through browser automation, running bash commands, or executing test suites — improves the quality of the final result by "2-3x." The agent doesn't just write code; it proves the code works.
What Cherny's workflow signals about the future of software engineering
The reaction to Cherny's thread suggests a pivotal shift in how developers think about their craft. For years, "AI coding" meant an autocomplete function in a text editor — a faster way to type. Cherny has demonstrated that it can now function as an operating system for labor itself.
"Read this if you're already an engineer... and want more power," Jeff Tang summarized on X.
The tools to multiply human output by a factor of five are already here. They require only a willingness to stop thinking of AI as an assistant and start treating it as a workforce. The programmers who make that mental leap first won't just be more productive. They'll be playing an entirely different game — and everyone else will still be typing.

<!-- 正文结束 -->