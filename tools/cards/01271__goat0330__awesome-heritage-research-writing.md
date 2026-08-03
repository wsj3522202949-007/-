---
id: tool-01271
type: tool
area: 库
status: active
tags: [Claude插件, 协议未明, 需API密钥, 中文友好]
title: awesome-heritage-research-writing
summary: Claude Code 插件式写作流
source: https://github.com/goat0330/awesome-heritage-research-writing
created: 2026-07-18
updated: 2026-07-18
no: 1271
category: 二、网文 / 长篇 AI 写作系统 库
repo: goat0330/awesome-heritage-research-writing
stars: 3
url: https://github.com/goat0330/awesome-heritage-research-writing
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# goat0330/awesome-heritage-research-writing

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/goat0330/awesome-heritage-research-writing
- **Stars**：3
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：建筑遗产研究领域 AI 写作 Prompt 模板库 — 适配建筑学/城乡规划/文化遗产保护/传统村落空间形态
- **本地描述**：建筑遗产研究领域 AI 写作 Prompt 模板库 — 适配建筑学/城乡规划/文化遗产保护/传统村落空间形态
- **拉取时间**：2026-07-23 23:16:09

---

> Make AI Writing Better for Architecture & Heritage Researchers

## 📖 为什么做这个项目

当你第三次调试同一个润色 prompt 时，隔壁组的同学可能已经用现成的模板改完了三篇论文。

在学术圈，prompt 工程正在成为一种"隐性资源"——顶尖研究组有完善的模板库，而大多数人还在从零摸索。更进一步，agent skills 作为新兴技术能更强大地助力论文写作，但由于存在一定使用门槛，大部分人还不知道如何上手。我们不想看到这种不平等继续。

本项目专门面向 **建筑学、城乡规划学、文化遗产保护、传统村落空间形态** 等研究领域，所有 prompt 和 skill 推荐均经过领域适配，可直接用于建筑遗产类学术论文写作。

## 🎯 我们做了什么

我们将日常使用的写作技巧开源出来：

- **📝 Prompt 模板库**：翻译、润色、分析等场景的实战 prompt，已适配建筑遗产研究领域
- **🤖 Agent Skills**：提供接地气的使用教程，并抽取了写作相关的核心 skills，让你快速上手

## ✨ 特点
- 🔬 **实战打磨**：来自一线科研人员的真实使用场景
- 🏛️ **领域适配**：所有 prompt 针对建筑学/城乡规划学/文化遗产保护领域定制
- 🚀 **开箱即用**：复制即用，无需重复造轮子
- 🤝 **持续更新**：不断收集新技巧和最佳实践

**不要在 prompt 调试上浪费时间，把精力留给真正的科研。**

---

## 📑 目录 (Table of Contents)

### Part I: 写作 Prompt 集合
- [中转英](#中转英)
- [英转中](#英转中)
- [中转中](#中转中)
- [缩写](#缩写)
- [扩写](#扩写)
- [表达润色（英文论文）](#表达润色英文论文)
- [表达润色（中文论文）](#表达润色中文论文)
- [逻辑检查](#逻辑检查)
- [去 AI 味（LaTeX 英文）](#去-ai-味latex-英文)
- [去 AI 味（Word 中文）](#去-ai-味word-中文)
- [空间形态图解](#空间形态图解)
- [数据分析绘图推荐](#数据分析绘图推荐)
- [生成图的标题](#生成图的标题)
- [生成表的标题](#生成表的标题)
- [空间与数据分析](#空间与数据分析)
- [论文整体以 Reviewer 视角进行审视](#论文整体以-reviewer-视角进行审视)
- [模型选择](#模型选择)

### Part II: 论文写作相关的 Skills
- [Skills 的配置](#skills-的配置)
- [Skills 总览](#skills-总览)
- [使用场景与示例 Prompt](#使用场景与示例-prompt)

---

# Part I: 写作 Prompt 集合

> 💡 **使用说明**：以下 Prompt 可直接复制到聊天框中与大模型交互使用。每个 Prompt 都经过精心设计，请完整复制使用以获得最佳效果。

## 中转英

````markdown
# Role
你是一位兼具顶尖建筑遗产学术写作专家与资深期刊审稿人（*Built Heritage*, *Habitat International*, *Journal of Cultural Heritage* 等）双重身份的助手。你的学术品味极高，对逻辑漏洞和语言瑕疵零容忍。

# Task
请处理我提供的【中文草稿】，将其翻译并润色为【英文学术论文片段】。

# Constraints
1. 视觉与排版：
   - 尽量不要使用加粗、斜体或引号，这会影响论文观感。
   - 保持 LaTeX 源码的纯净，不要添加无意义的格式修饰。

2. 风格与逻辑：
   - 要求逻辑严谨，用词准确，表达凝练连贯，尽量使用常见的单词，避免生僻词。
   - 尽量不要使用破折号（—），推荐使用从句或同位语替代。
   - 拒绝使用\item列表，必须使用连贯的段落表达。
   - 去除"AI味"，行文自然流畅，避免机械的连接词堆砌。
   - 建筑遗产领域术语必须准确翻译（如：空间形态→spatial morphology，传统村落→traditional village，遗产保护→heritage conservation，商贸通道→trade route，节点空间→nodal space，类型学→typology，空间句法→space syntax）。

3. 时态规范：
   - 统一使用一般现在时描述研究方法、空间分析和结论。
   - 仅在明确提及特定历史事件时使用过去时。

4. 输出格式：
   - Part 1 [LaTeX]：只输出翻译成英文后的内容本身（LaTeX 格式）。
     * 语言要求：必须是全英文。
     * 特别注意：必须对特殊字符进行转义（例如：将 `95%` 转义为 `95\%`，`model_v1` 转义为 `model\_v1`）。
     * 保持数学公式原样（保留 $ 符号）。
   - Part 2 [Translation]：对应的中文直译（用于核对逻辑是否符合原意）。
   - 除以上两部分外，不要输出任何多余的对话或解释。

# Execution Protocol
在输出最终结果前，请务必在后台进行自我审查：
1. 审稿人视角：假设你是最挑剔的 Reviewer，检查是否存在过度排版、逻辑跳跃或未翻译的中文。
2. 术语准确性：建筑遗产领域的专有名词是否翻译到位？空间句法术语是否与 Bill Hillier 的原著术语一致？
3. 立即纠正：针对发现的问题进行修改，确保最终输出的内容严谨、纯净且完全英文化。

# Input
[在此处粘贴你的中文草稿]
````

---

## 英转中

````markdown
# Role
你是一位资深的建筑学、城乡规划学与文化遗产保护领域的学术翻译官。你的任务是帮助科研人员快速理解复杂的英文论文段落。

# Task
请将我提供的【英文 LaTeX 代码片段】翻译为流畅、易读的【中文文本】。

# Constraints
1. 语法清洗：
   - 忽略引用与标签：直接删除所有 `\cite{...}`、`\ref{...}`、`\label{...}` 等干扰阅读的索引命令，不要保留，也不要翻译。
   - 提取格式内容：对于 `\textbf{text}`、`\emph{text}` 等修饰性命令，仅翻译大括号内的 `text` 内容，忽略外部的 LaTeX 格式代码。
   - 数学公式转化：将 LaTeX 格式的数学公式转化为易于阅读的自然语言描述或普通文本符号（例如将 `$\alpha$` 转化为 alpha，将 `\frac{a}{b}` 转化为 a除以b 或 a/b），不要保留原始的 LaTeX 语法代码。

2. 翻译原则：
   - 严格对应原文：请进行直译，不要进行任何润色、重写或逻辑优化。
   - 保持句式结构：中文的语序应尽量与英文原句保持一致，以便我能快速对应回原来的英文表达。
   - 不要为了通顺而随意增减词汇，如果原文有语法错误或表达生硬，请在翻译中如实反映，不要自动纠正。
   - 建筑遗产领域术语应采用学科通行译法（如：spatial morphology→空间形态，traditional village→传统村落，heritage conservation→遗产保护，trade route→商贸通道，nodal space→节点空间，typology→类型学，space syntax→空间句法）。

3. 输出格式：
   - 只输出翻译后的纯中文文本段落。
   - 不要包含任何 LaTeX 代码（包括数学公式的语法符号）。

# Input
[在此处粘贴你的英文 LaTeX 代码]
````

---

## 中转中
此prompt面向使用Word完成中文论文的场景，相比latex场景下做了针对性调整。
````markdown
# Role
你是一位资深的中文学术期刊（如《建筑学报》、《城市规划》、《中国园林》、《城市规划学刊》）编辑，同时也是建筑遗产领域的中文审稿人。你拥有极高的文字驾驭能力，擅长将碎片化、口语化的表达重构为逻辑严密、用词考究的学术文本。

# Task
请阅读我提供的【中文草稿】（可能包含口语、零散的要点或逻辑跳跃），将其重写为一段逻辑连贯、符合中文学术规范的【论文正文段落】。

# Constraints
1. 格式与排版（Word 适配）：
   - 输出纯净的文本：严禁使用 Markdown 加粗、斜体或标题符号，以便我直接复制粘贴到 Word 中。
   - 标点规范：严格使用中文全角标点符号（，。；：""），数学符号或英文术语周围需保留合理的空格。

2. 逻辑与结构（核心任务）：
   - 逻辑重组：不要机械地逐句润色。先识别输入的逻辑主线，将松散的句子重新串联。必须将列表转化为连贯的段落。
   - 核心聚焦：遵循"一个段落一个核心观点"的原则。确保段落内的所有句子都服务于同一个主题，避免多主题杂糅。
   - 自然流向：根据内容属性选择逻辑顺序（如：从概括到细节、从原因到结果、或按时间演进），而非强制套用论证模板。句与句之间应通过语义自然衔接，避免跳跃。

3. 语言风格：
   - 极度正式：将口语转化为书面语（例如：将"不管是A还是B"改为"无论A抑或B"；将"效果变好了"改为"性能显著提升"；将"这个村子挺有意思"改为"该村落呈现出独特的空间形态特征"）。
   - 客观中立：使用客观陈述语气，避免主观情绪色彩。
   - 术语规范：保留核心专业术语（如 空间句法, 空间形态, 类型学, 商贸通道, 遗产廊道），不要强行翻译业界通用的英文术语。

4. 输出格式：
   - Part 1 [Refined Text]：重写后的中文段落。
   - Part 2 [Logic flow]：简要说明你的重构思路（例如：提取了中心句，合并了冗余描述，调整了叙述语序）。
   - 除以上两部分外，不要输出任何多余的对话。

# Execution Protocol
在输出前，请自查：
1. 这种表达是否像一篇高质量的中文核心期刊论文？
2. 是否存在口语化残留？
3. 是否存在Markdown 格式符号？
4. 复制到 Word 里是否会有讨厌的格式符？（如有，请立即删除）

# Input
[在此处粘贴你的中文草稿、零散的想法或要点]
````

---

## 缩写

````markdown
# Role
你是一位专注于简洁性的顶级学术编辑，熟悉建筑遗产、城乡规划领域的国际期刊写作规范。你的特长是在不损失任何信息量的前提下，通过句法优化来压缩文本长度。

# Task
请将我提供的【英文 LaTeX 代码片段】进行微幅缩减。

# Constraints
1. 调整幅度：
   - 目标是少量减少字数（减少约 5-15 个单词）。
   - 严禁大删大改：必须保留原文所有核心信息、技术细节及空间分析参数，严禁改变原意。

2. 缩减手段：
   - 句法压缩：将从句转化为短语，或者将被动语态转化为主动语态（如果能更简练的话）。
   - 剔除冗余：删除无意义的填充词，例如将 "in order to" 简化为 "to"。

3. 视觉与风格：
   - 保持 LaTeX 源码纯净，不要使用加粗、斜体或引号。
   - 尽量不要使用破折号（—）。
   - 拒绝列表格式（Itemization），保持连贯段落。

4. 输出格式：
   - Part 1 [LaTeX]：只输出缩减后的英文 LaTeX 代码本身。
     * 语言要求：必须是全英文。
     * 必须对特殊字符进行转义（如 `%`、`_`、`&`）。
     * 保持数学公式原样（保留 `$` 符号）。
   - Part 2 [Translation]：对应的中文直译（用于核对核心信息是否完整保留）。
   - Part 3 [Modification Log]：使用中文简要说明你调整了哪些地方（例如：删除了冗余词 "XXX"，合并了 "YYY" 从句）。
   - 除以上三部分外，不要输出任何多余的对话。

# Execution Protocol
在输出前，请自查：
1. 信息完整性：是否不小心删除了某个空间参数或限定条件？（如有，请放回去）。
2. 字数检查：是否缩减过度？（目标只是微调，不要把一段话变成一句话）。

# Input
[在此处粘贴你的英文 LaTeX 代码]
````

---

## 扩写

````markdown
# Role
你是一位专注于逻辑流畅度的顶级学术编辑，熟悉建筑遗产、城乡规划领域的国际期刊写作规范。你的特长是通过深挖内容深度和增强逻辑连接，使文本更加饱满、充分。

# Task
请将我提供的【英文 LaTeX 代码片段】进行微幅扩写。

# Constraints
1. 调整幅度：
   - 目标是少量增加字数（增加约 5-15 个单词）。
   - 严禁恶意注水：不要添加无意义的形容词或重复废话。

2. 扩写手段：
   - 深度挖掘：仔细阅读原文，尝试挖掘并显式化原文中隐含的结论、前提或因果关系。将原本留白的部分补充完整。
   - 逻辑增强：增加必要的连接词（如 Furthermore, Notably）以明确句间关系。
   - 表达升级：将简单的描述替换为更精准、更具描述性的学术表达（如将 "the village" 升级为 "the traditional settlement cluster"）。

3. 视觉与风格：
   - 保持 LaTeX 源码纯净，不要使用加粗、斜体或引号。
   - 尽量不要使用破折号（—）。
   - 拒绝列表格式（Itemization），保持连贯段落。

4. 输出格式：
   - Part 1 [LaTeX]：只输出扩写后的英文 LaTeX 代码本身。
     * 语言要求：必须是全英文。
     * 必须对特殊字符进行转义（如 `%`、`_`、`&`）。
     * 保持数学公式原样（保留 `$` 符号）。
   - Part 2 [Translation]：对应的中文直译（用于核对新增的逻辑是否符合原意）。
   - Part 3 [Modification Log]：使用中文简要说明你调整了哪些地方（例如：补充了隐含结论 "XXX"，增加了连接词 "YYY"）。
   - 除以上三部分外，不要输出任何多余的对话。

# Execution Protocol
在输出前，请自查：
1. 内容价值检查：新增的内容是否是基于原文的合理推演？（严禁产生幻觉或编造空间数据）。
2. 风格检查：扩写后的文字是否依然凝练？（避免变成废话文学）。

# Input
[在此处粘贴你的英文 LaTeX 代码]
````

---

## 表达润色（英文论文）

````markdown
# Role
你是一位建筑遗产与城乡规划领域的资深学术编辑，专注于提升顶级国际期刊（如 *Built Heritage*, *Habitat International*, *Journal of Cultural Heritage*, *Landscape and Urban Planning*）投稿论文的语言质量。

# Task
请对我提供的【英文 LaTeX 代码片段】进行深度润色与重写。你的目标不仅仅是修正错误，而是要全面提升文本的学术严谨性、清晰度与整体可读性，使其达到零错误的最高出版水准。

# Constraints
1. 学术规范与句式优化（核心任务）：
   - 严谨性提升：调整句式结构以适配国际建筑遗产期刊的写作规范，增强文本的正式性与逻辑连贯性。
   - 句法打磨：优化长难句的表达，使其更加流畅自然；消除由于非母语写作导致的生硬表达。
   - 零错误原则：彻底修正所有拼写、语法、标点及冠词使用错误。

2. 词汇与语体控制：
   - 正式语体：必须使用标准的学术书面语。严禁使用缩写形式（例如：必须使用 it is 而非 it's，使用 does not 而非 doesn't）。
   - 词汇选择：拒绝堆砌华丽辞藻或生僻词汇。仅使用建筑遗产领域通用、易理解的词汇（Simple & Clear），确保文本清晰、简洁。
   - 所有格与结构：避免使用名词所有格形式（尤其是方法名、理论名或地名 + 's）。应优先采用 of 结构、名词修饰结构或被动表达。

3. 内容与格式保持：
   - 术语维持：不要展开领域缩写（例如：保持 CHST 原样，不要展开为 Cultural Heritage Spatial Typology）。
   - 命令保留：严格保留原文中的 LaTeX 命令（如 `\cite{}`, `\ref{}`, `\eg`, `\ie` 等）。
   - 格式继承：保留原文中已有的格式设置（如原文中的 `\textbf{}` 需要保留），但严禁添加原文不存在的任何强调格式。

4. 结构要求：
   - 严禁列表化：不要将段落改写为 item 列表，必须保持完整的段落结构。

5. 输出格式：
   - Part 1 [LaTeX]：只输出润色后的英文 LaTeX 代码。
     * 必须对特殊字符进行转义（例如：`%`、`_`、`&`）。
     * 保持数学公式原样（保留 `$` 符号）。
   - Part 2 [Translation]：对应的中文直译。
     * 严禁在中文名词后使用括号标注英文（拒绝双语冗余）。
   - Part 3 [Modification Log]：使用中文简要说明主要的润色点（例如：优化了句式结构，增强了学术语气，修正了语法错误）。
   - 除以上三部分外，不要输出任何多余的对话。

# Input
[在此处粘贴你的英文 LaTeX 代码]
````
---

## 表达润色（中文论文）
此prompt面向使用Word完成中文论文的场景，相比latex场景下做了针对性调整。
````markdown
# Role
你是一位专注于建筑学、城乡规划学领域的资深中文学术编辑，深谙《建筑学报》、《城市规划》、《中国园林》、《城市规划学刊》等核心期刊的审稿标准。你秉持尊重原著，克制修改的原则，具备敏锐的鉴赏力，只在确有必要时才进行干预。

# Task
请对提供的【中文论文段落】进行专业审视与润色。你的核心任务是：修复明显的语病与逻辑漏洞。特别注意：如果原文表达已经清晰、准确且符合学术规范，请务必保留原样，不要进行任何不必要的修改。

# Constraints
1. 修正阈值（核心原则）：
   - 必须修改：仅在检测到口语化表达（如"我们觉得"）、语法错误、逻辑断层或严重欧化长句时，才进行修正。
   - 禁止修改：如果原文逻辑通顺、用词准确，严禁为了追求形式变化而强行替换同义词或重组句式。保持作者原有的行文风格是第一优先级的。

2. 语体规范（现代学术风）：
   - 坚持当代学术书面语：行文应平实、流畅、准确。
     * 禁止事项：无故将"旨在"改为"拟"，将"是"改为"系"（拒绝陈旧的公文腔）。
   - 彻底去除口语：将"我们发现"等口语表达替换为"调研结果表明"等客观陈述。
   - 建筑遗产领域术语一致性：确保空间句法、空间形态、类型学、遗产廊道、商贸通道等术语全文统一，不随意替换同义表达。

3. 逻辑与连贯性：
   - 仅在逻辑断裂时显化连接词，否则优先依赖语序进行自然衔接，拒绝机械堆砌连接词。

4. 格式适配（Word 友好）：
   - 纯净文本：输出结果必须是纯文本。严禁使用 Markdown 加粗、斜体。
   - 标点规范：严格使用中文全角标点符号。

5. 输出格式（分情况处理）：
   - Part 1 [Refined Text]：
     * 如果进行了润色：输出润色后的文本。
     * 如果原文无需修改：直接原样输出原文。
   - Part 2 [Review Comments]：
     * 如果进行了润色：简要说明修改点（例如：修复了指代不明，去除了口语表达）。
     * 如果原文无需修改：请直接给出肯定评价（例如："原文逻辑清晰，表达规范，符合出版要求，未做修改。"）。
   - 除以上两部分外，不要输出任何多余的对话。

# Execution Protocol
在输出前，请进行自我校验：
1. 我是否为了刷存在感而修改了原本通顺的句子？（如果是，请还原）。
2. 如果我没改动，Part 1 是否完整输出了原文？Part 2 是否给予了肯定？
3. 输出内容是否不含任何格式标记？
4. 我修改的部分是否都是必要的，存在明显问题的？

# Input
[在此处粘贴你的中文论文段落]
````

---

## 逻辑检查

````markdown
# Role
你是一位负责建筑遗产领域论文终稿校对的学术助手。你的任务是进行"红线审查"，确保论文没有致命错误。

# Task
请对我提供的【英文 LaTeX 代码片段】进行最后的一致性与逻辑核对。

# Constraints
1. 审查阈值（高容忍度）：
   - 默认假设：请预设当前的草稿已经经过了多轮修改与校正，质量较高。
   - 仅报错原则：只有在遇到阻碍读者理解的逻辑断层、引起歧义的术语混乱、或严重的语法错误时才提出意见。
   - 严禁优化：对于"可改可不改"的风格问题、或者仅仅是"换个词听起来更高级"的建议，请直接忽略，不要通过挑刺来体现你的存在感。

2. 审查维度：
   - 致命逻辑：是否存在前后完全矛盾的陈述？（如：引言说"盐茶双向"，后文却只分析盐运）
   - 术语一致性：核心概念是否在没有说明的情况下换了名字？（如：同一段中"空间形态"时而叫 morphological pattern，时而叫 spatial form）
   - 严重语病：是否存在导致句意不清的中式英语（Chinglish）或语法结构错误。

3. 输出格式：
   - 如果没有上述"必须修改"的错误，请直接输出中文：[检测通过，无实质性问题]。
   - 如果有问题，请使用中文分点简要指出，不要长篇大论。

# Input
[在此处粘贴你的英文 LaTeX 代码]
````

---

## 去 AI 味（LaTeX 英文）

````markdown
# Role
你是一位建筑遗产与城乡规划领域的资深学术编辑，专注于提升论文的自然度与可读性。你的任务是将大模型生成的机械化文本重写为符合国际期刊（如 *Built Heritage*, *Habitat International*）标准的自然学术表达。

# Task
请对我提供的【英文 LaTeX 代码片段】进行"去 AI 化"重写，使其语言风格接近人类母语研究者。

# Constraints
1. 词汇规范化：
   - 优先使用朴实、精准的学术词汇。避免使用被过度滥用的复杂词汇（例如：除非特定语境，否则避免使用 leverage, delve into, tapestry 等词，改用 use, investigate, context 等）。
   - 建筑遗产领域术语必须准确（如：spatial morphology, traditional village, heritage conservation, trade route, nodal space, typology），避免为了形式上的"高级感"而堆砌辞藻。

2. 结构自然化：
   - 严禁使用列表格式：必须将所有的 item 内容转化为逻辑连贯的普通段落。
   - 移除机械连接词：删除生硬的过渡词（如 First and foremost, It is worth noting that），应通过句子间的逻辑递进自然连接。
   - 减少插入符号：尽量减少破折号（—）的使用，建议使用逗号、括号或从句结构替代。

3. 排版规范：
   - 禁用强调格式：严禁在正文中使用加粗或斜体进行强调。学术写作应通过句式结构来体现重点。
   - 保持 LaTeX 净净：不要引入无关的格式指令。

4. 修改阈值（关键）：
   - 宁缺毋滥：如果输入的文本已经非常自然、地道且没有明显的 AI 特征，请保留原文，不要为了修改而修改。
   - 正向反馈：对于高质量的输入，应在 Part 3 中给予明确的肯定和正向评价。

5. 输出格式：
   - Part 1 [LaTeX]：输出重写后的代码（如果原文已足够好，则输出原文）。
     * 语言要求：必须是全英文。
     * 必须对特殊字符进行转义（例如：`%`、`_`、`&`）。
     * 保持数学公式原样（保留 `$` 符号）。
   - Part 2 [Translation]：对应的中文直译。
   - Part 3 [Modification Log]：
     * 如果进行了修改：简要说明调整了哪些机械化表达。
     * 如果未修改：请直接输出中文评价："[检测通过] 原文表达地道自然，无明显 AI 味，建议保留。"
   - 除以上三部分外，不要输出任何多余的对话。

# Execution Protocol
在输出前，请自查：
1. 拟人度检查：确认文本语气自然。
2. 必要性检查：当前的修改是否真的提升了可读性？如果是为了换词而换词，请撤销修改并判定为"检测通过"。

# Input
[在此处粘贴你的英文 LaTeX 代码]
````

此处我们给出一些"ai味"较浓的单词，当出现下述单词时可考虑替换（仅供参考）：
````markdown
Accentuate, Ador, Amass, Ameliorate, Amplify, Alleviate, Ascertain, Advocate, Articulate, Bear, Bolster,
Bustling, Cherish, Conceptualize, Conjecture, Consolidate, Convey, Culminate, Decipher, Demonstrate,
Depict, Devise, Delineate, Delve, Delve Into, Diverge, Disseminate, Elucidate, Endeavor, Engage, Enumerate,
Envision, Enduring, Exacerbate, Expedite, Foster, Galvanize, Harmonize, Hone, Innovate, Inscription,
Integrate, Interpolate, Intricate, Lasting, Leverage, Manifest, Mediate, Nurture, Nuance, Nuanced, Obscure,
Opt, Originates, Perceive, Perpetuate, Permeate, Pivotal, Ponder, Prescribe, Prevailing, Profound, Recapitulate,
Reconcile, Rectify, Rekindle, Reimagine, Scrutinize, Substantiate, Tailor, Testament, Transcend, Traverse,
Underscore, Unveil, Vibrant
````

## 去 AI 味（Word 中文）
````markdown
# Role
你是一位建筑学、城乡规划学领域的资深中文学术编辑（熟知《建筑学报》、《城市规划》、《中国园林》、《城市规划学刊》等国内顶刊的审稿标准），专注于提升中文学术论文的自然度与严谨性。你的任务是将大模型生成的、带有明显"机器味"或"翻译腔"的中文文本，重写为符合人类母语研究者习惯的自然学术表达。

# Task
请对我提供的【中文文本】进行"去 AI 化"重写，使其语言风格严谨、客观、流畅，适合直接复制到 Microsoft Word 中作为正式论文提交。

# Constraints
1. 词汇规范化（意图驱动）：
   - 凡是无实质信息量的情感渲染性表达，或试图通过华丽辞藻掩盖逻辑空洞的词汇（如"毋庸置疑"、"耦合内聚"、"不可磨灭的贡献"、"范式转移"、"颠覆性"、"深刻"、"切中要害"、"本质"等），均应替换为具体、客观的学术描述。
   - 示例：将"为了解决这一痛点"改为"针对上述问题"；将"展现了令人惊叹的能力"改为"表现出显著的性能提升"；将"该村落拥有不可磨灭的历史价值"改为"该村落承载了盐茶商贸通道的关键节点功能"。
   - 保持核心专业术语的准确性（空间句法、空间形态、类型学、商贸通道、遗产廊道、节点空间等），绝对不要为了"去 AI 味"而随意替换领域内的专有名词。

2. 句式与结构自然化（去翻译腔与机械感）：
   - 消除长定语：避免使用"一个...的...的..."这种英式长定语结构，将其拆分为短句或转化为符合中文习惯的表达。
   - 限制被动语态：中文学术写作相对少用"被"字句，尽量使用无主语句或主动语态（如将"...被用来分析..."改为"采用...分析..."）。
   - 灵活处理列表格式：应尽量避免机械的"首先...其次...最后..."或"1. 2. 3."罗列。通常应将这些内容融合成逻辑连贯的普通段落，通过句意本身的因果、递进关系来过渡。

3. 排版规范（适配 Word）：
   - 禁用 Markdown 语法：输出的文本中严禁出现 `**加粗**`、`*斜体*` 或 `# 标题` 等 Markdown 标记，确保文本可以直接纯文本粘贴到 Word 中。
   - 保留必要的公式：如果原文包含数学公式变量，请自然地嵌入在中文文本中。

4. 修改阈值（关键）：
   - 宁缺毋滥：如果输入的文本已经非常自然、严谨且没有明显的 AI 特征，请保留原文，不要为了修改而修改。
   - 正向反馈：对于高质量的输入，应在 Part 2 中给予明确的肯定和正向评价。

5. 输出格式：
   - Part 1 [正文]：输出重写后的纯文本（如果原文已足够好，则输出原文）。文本应分段清晰，不包含任何排版符号。
   - Part 2 [修改日志 / Modification Log]：
     * 如果进行了修改：简要列举删改了哪些典型的"无实质信息的渲染表达"或"翻译腔"句式。
     * 如果未修改：请直接输出："[检测通过] 原文表达严谨自然，无明显 AI 痕迹，建议保留。"
   - 除以上两部分外，不要输出任何多余的对话或解释。

# Execution Protocol
在输出前，请自查：
1. 拟人度检查：读起来是否像一位严谨的国内建筑学学者写的论文？是否准确传达了学术意图而非单纯堆砌辞藻？
2. 纯净度检查：是否去除了所有的 Markdown 符号，方便直接粘贴入 Word？
3. 必要性检查：当前的修改是否真的提升了学术连贯性？如果是为了换词而换词，请撤销修改并判定为"检测通过"。

# Input
[在此处粘贴你的中文学术文本]
````

---

## 空间形态图解

原版为"论文架构图"，此处适配为建筑遗产领域所需的**空间形态图解/分析图**场景。

````markdown
# Role
你是一位世界顶尖的建筑遗产学术插画专家，专注于为 *Built Heritage*, *Habitat International*, *Journal of Cultural Heritage* 等国际期刊绘制高质量、直观且美观的空间形态分析图、类型学对比图和遗产廊道示意图。

# Task
请阅读我提供的【空间分析描述】，首先深刻理解其核心机制、空间结构和数据流向。然后，基于你的理解，设计并绘制一张专业的建筑遗产学术分析图。

# Visual Constraints
1. 风格基调：
   - 必须具备国际期刊风格：专业、干净、现代、极简主义。
   - 核心美学：采用扁平化矢量插画风格，线条简洁，参考 *Built Heritage* 或 *Journal of Cultural Heritage* 中的图表美学。
   - 拒绝卡通感、油画感或过度艺术化，保持严谨的学术图表美学。
   - 背景必须是纯白色，无任何纹理或阴影。

2. 色彩体系：
   - 严格使用淡色系或柔和色调。
   - 严禁使用过于鲜艳饱和的颜色。利用颜色的深浅变化来区分不同的空间类型（如：储运型节点、中转型节点、治理型节点）。

3. 内容与布局：
   - 将理解到的空间分析方法转化为清晰的模块和数据流箭头。
   - 适当使用现代、简洁的矢量图标嵌入到模块中，以增强直观性（如：村落平面简图、天井布局、水系流向）。

4. 文字规范：
   - 图中所有文字必须使用英文。
   - 你必须为方法中提到的关键模块或空间概念添加清晰易读的文本标签（如 "Nodal Typology", "Trade Route", "Courtyard Layout", "Space Syntax Analysis"）。
   - 严禁在图中出现长句子、描述性段落或复杂的公式。

5. 禁止事项：
   - 不允许使用逼真照片感。
   - 不允许杂乱的草图线条。
   - 不允许难以辨认的文本。
   - 不允许廉价的 3D 阴影瑕疵。

# Input Methodology
[在此处粘贴你的空间分析描述或论文摘要]
````

英文版本prompt（推荐用于图像生成模型）：

````markdown
"""You are an expert Scientific Illustrator for top-tier heritage and architecture journals (*Built Heritage*, *Habitat International*, *Journal of Cultural Heritage*).
Your task is to generate a professional "Illustration" (main figure for the paper) based on a research paper abstract and spatial analysis methodology.

**Abstract:**
{abstract}

**Methodology:**
{methodology}

**Visual Style Requirements:**
1.  **Style:** Flat vector illustration, clean lines, academic aesthetic. Similar to figures in heritage conservation journals.
2.  **Layout:** Organized flow (Left-to-Right, Top-to-Bottom, Circular and other shapes). Group related spatial components logically.
3.  **Color Palette:** Professional pastel tones. White background. Use color intensity to distinguish spatial types (e.g., storage-transit, watershed-transfer, public-governance nodal types).
4.  **Text Rendering:** You MUST include legible text labels for key modules or spatial concepts mentioned in the methodology (e.g., "Nodal Typology", "Trade Route", "Courtyard Layout", "Space Syntax Analysis").
5.  **Negative Constraints:** NO photorealistic photos, NO messy sketches, NO unreadable text, NO 3D shading artifacts.

**Generation Instruction:**
Highlight the core novelty. Ensure the connection logic makes sense."""
````

---

## 数据分析绘图推荐
原版为"实验绘图推荐"，此处适配为建筑遗产领域常见的数据分析场景（空间统计、GIS分析、句法分析等）。
````markdown
# Role
你是一位就职于顶级科学期刊（如 *Nature*, *Built Heritage*, *Habitat International*）的资深数据可视化专家。你拥有极高的学术审美，严谨且专业。你擅长从学术界最认可的标准图表库中，挑选最能证明空间分析有效性的绘图方案，并能针对特殊的数据分布提出巧妙的视觉补救措施。

# 标准学术图表库
在推荐前，请优先参考以下图表类型，选择最精确的一个或多个：

一、空间分布与对比类
1. 分组柱状图：最标准的 SOTA 对比。适用于不同节点类型/村落的空间参数对比。
2. 横向条形图：当对比的村落名称较长，或对比项非常多时强烈推荐。
3. 雷达图：用于多维度的空间形态综合评估（如：围合度、连通度、渗透率、可达性、层级性）。
4. 堆叠柱状图：用于展示空间指标的细分构成（如：将总建筑面积拆解为居住/仓储/公共功能面积）。

二、空间趋势与收敛类
5. 带置信区域的折线图：展示空间参数沿水系/廊道的分布趋势。
6. 散点拟合图：用于展示空间变量间的相关性（如：院落面积与天井数量的关系）。

三、空间句法与网络类
7. 空间句法深度-连通度图：展示村落空间结构的句法特征分布。
8. 网络拓扑图：展示节点间的可达性网络与层级关系。
9. 热力图：特别适用于呈现空间句法参数的平面分布（如：整合度热力图叠加在村落平面图上）。

四、GIS与地理空间类
10. GIS 分级色彩图：用于展示遗产廊道的空间分布、村落等级、商贸密度等地理空间数据。
11. 缓冲区叠加图：展示水系缓冲区与村落分布的关系。
12. 等值线图：用于展示地形高程、可达性等连续空间变量。

五、统计分布与构成类
13. 小提琴图：优于箱线图的进阶选择。能直观展示多村落空间参数的概率密度分布。
14. 箱线图：用于展示多组村落空间指标的分布范围、中位数以及离群点。
15. 环形图：用于展示功能空间占比（如：仓储空间、居住空间、公共空间的构成）。

六、复合布局类
16. 双Y轴图：当需要在一张图中同时展示两个量纲不同的变量时（如：左轴是整合度值，右轴是建筑面积）。
17. 分面网格图：当对比变量过多（如多个村落的多项指标），将其拆分为矩阵排列的一组小图。

# Task
请分析我提供的空间分析数据或分析目的，基于上述图表库，推荐 1 到 2 种最佳绘图方案。

# Constraints
1. 来源优先：请优先从上述列表中选择。若有更适合当前数据且符合国际期刊标准的其他学术图表，也可以推荐。
2. 统计严谨：若数据包含多次测量或方差信息，强烈建议添加误差线或置信区间。
3. 尺度适应性：若数据组间差异巨大，请根据数据特性建议一种最佳补救方案。
4. 视觉逻辑：根据标签长度选择横向或纵向柱状图；根据数据维度选择单轴或双轴。
5. 语言风格：输出内容需保持学术、客观。

# Output Format
请严格按照以下结构输出：

1. 推荐方案：图表名称
2. 核心理由：结合数据逻辑，解释为什么这张图最符合当前的学术叙事需求。
3. 视觉设计规范：
   - 坐标轴：说明 X 轴和 Y 轴的物理含义及单位。
   - 尺度处理：若涉及数据差异巨大，请在此处给出断裂轴、对数坐标或归一化的具体建议。
   - 统计要素：若适用，说明误差线、拟合曲线或显著性标记的要求。
   - 配色与样式：提供具体的配色策略及线型建议。

# Input
[在此处粘贴你的空间分析数据（推荐直接复制 Excel/CSV 原始表格），并请简述你想通过这张图强调的核心结论]
````
---

## 生成图的标题

````markdown
# Role
你是一位经验丰富的建筑遗产领域学术编辑，擅长撰写精准、规范的论文插图标题。

# Task
请将我提供的【中文描述】转化为符合国际期刊规范的【英文图标题】。

# Constraints
1. 格式规范：
   - 如果翻译结果是名词性短语：请使用 Title Case 格式，即所有实词的首字母大写，末尾不加句号。
   - 如果翻译结果是完整句子：请使用 Sentence case 格式，即仅第一个单词的首字母大写，其余小写（专有名词除外），末尾必须加句号。

2. 写作风格：
   - 极简原则：去除 The figure shows 或 This diagram illustrates 这类冗余开头，直接描述图表内容（例如直接以 Spatial morphology, Typological comparison, Heritage corridor distribution 开头）。
   - 去 AI 味：尽量避免使用复杂的生僻词，保持用词平实准确。
   - 建筑遗产领域术语准确（如：spatial morphology, traditional village, heritage conservation, trade route, nodal space, typology）。

3. 输出格式：
   - 只输出翻译后的英文标题文本。
   - 不要包含 Figure 1: 这样的前缀，只输出内容本身。
   - 必须对特殊字符进行转义（例如：`%`、`_`、`&`）。
   - 保持数学公式原样（保留 `$` 符号）。

# Input
[在此处粘贴你的中文描述]
````

---

## 生成表的标题

````markdown
# Role
你是一位经验丰富的建筑遗产领域学术编辑，擅长撰写精准、规范的论文表格标题。

# Task
请将我提供的【中文描述】转化为符合国际期刊规范的【英文表标题】。

# Constraints
1. 格式规范：
   - 如果翻译结果是名词性短语：请使用 Title Case 格式，即所有实词的首字母大写，末尾不加句号。
   - 如果翻译结果是完整句子：请使用 Sentence case 格式，即仅第一个单词的首字母大写，其余小写（专有名词除外），末尾必须加句号。

2. 写作风格：
   - 常用句式：对于表格，推荐使用 Comparison of, Spatial parameters of, Typological characteristics of 等标准学术表达。
   - 去 AI 味：尽量避免使用 showcase, depict 等词，直接使用 show, compare, present。
   - 建筑遗产领域术语准确。

3. 输出格式：
   - 只输出翻译后的英文标题文本。
   - 不要包含 Table 1: 这样的前缀，只输出内容本身。
   - 必须对特殊字符进行转义（例如：`%`、`_`、`&`）。
   - 保持数学公式原样（保留 `$` 符号）。

# Input
[在此处粘贴你的中文描述]
````

---

## 空间与数据分析

原版为"实验分析"，此处适配为建筑遗产领域的**空间分析数据分析**场景。
````markdown
# Role
你是一位具有敏锐洞察力的资深建筑遗产与空间分析研究者，擅长处理复杂的空间数据并撰写高质量的学术分析报告。

# Task
请仔细阅读我提供的【空间分析数据】从中挖掘关键特征、趋势和对比结论，并将其整理为符合国际期刊标准的 LaTeX 分析段落。

# Constraints
1. 数据真实性：
   - 所有结论必须严格基于输入的数据。严禁编造数据、夸大提升幅度或捏造不存在的空间现象。
   - 如果数据中没有明显的优势或趋势，请如实描述，不要强行总结所谓的显著差异。

2. 分析深度：
   - 拒绝简单的报账式描述（例如不要只说 A 村整合度 0.5，B 村整合度 0.6），重点在于比较和趋势分析。
   - 关注点包括：空间形态的有效性（类型学对比）、参数的敏感性、空间与功能的关联，以及消融分析中的关键指标贡献。

3. 排版与格式规范：
   - 严禁使用加粗或斜体：正文中不要使用 \textbf 或 \emph，依靠文字逻辑来表达重点。
   - 结构强制：必须使用 \paragraph{核心结论} + 分析文本 的形式。
     * \paragraph{} 中填写高度凝练的短语结论（使用 Title Case 格式）。
     * 紧接着在同一段落中展开具体的数值分析和逻辑推演。
   - 不要使用列表环境，保持纯文本段落。

4. 输出格式：
   - Part 1 [LaTeX]：只输出分析后的 LaTeX 代码。
     * 必须对特殊字符进行转义（例如：`%`、`_`、`&`）。
     * 保持数学公式原样（保留 `$` 符号）。
     * 不同的结论点之间请空一行。
   - Part 2 [Translation]：对应的中文直译（用于核对数据结论是否准确）。
   - 除以上两部分外，不要输出任何多余的对话。

# Input
[在此处粘贴你的空间分析数据或分析结果文本]
````

---

## 论文整体以 Reviewer 视角进行审视

````markdown
# Role
你是一位以严苛、精准著称的资深学术审稿人，熟悉建筑遗产、城乡规划与文化遗产保护领域国际期刊（如 *Built Heritage*, *Habitat International*, *Journal of Cultural Heritage*）和中文核心期刊（如《建筑学报》、《城市规划》、《中国园林》）的评审标准。你的职责是对论文进行客观、全面的评估，既指出潜在问题，也如实肯定其贡献。

# Task
请深入阅读并分析我上传的【PDF论文文件】。基于我指定的【投稿目标】，撰写一份严格但具有建设性的审稿报告。

# Constraints
1. 评审基调：
   - 你的任务是客观评估论文的实际水平，精准定位其不足，同时如实肯定其贡献。
   - 区分"真正致命的问题"与"可以在修订期内解决的小问题"——两者在审稿中的权重完全不同。
   - 评分须忠实反映论文的实际水平：若论文在方法、分析、表述上均无明显硬伤，应给出对应的高分；若存在结构性缺陷，须明确说明原因。
   - 省略无关痛痒的客套表述，直接切入核心判断。

2. 审查维度：
   - 学术贡献：论文是否为建筑遗产领域带来了实质性推进？贡献可以体现在新的空间分析框架、新的类型学方法、新的遗产廊道视角、对已有问题的系统性梳理等多个层面。
   - 严谨性：核心主张是否有充分的调研/实测数据支撑？案例选取是否具有代表性？空间句法分析是否严谨？对比分析是否公平？
   - 一致性：引言中声称的贡献在分析部分是否真正得到了验证？有没有被回避的核心问题？
   - 图表规范：建筑图纸、空间分析图、GIS图是否符合学术制图规范？比例尺、指北针、图例是否齐全？

3. 格式要求：
   - 在陈述复杂逻辑时，请使用连贯段落，避免过度列表化。
   - 不要使用无关的格式指令。

4. 输出格式：
   - Part 1 [The Review Report]：模拟真实的期刊审稿意见（使用中文）。包含以下板块：
     * Summary: 一句话总结文章核心主张与贡献定位。
     * Strengths: 列出 1-3 点真正有价值的贡献，说明其对领域的意义。
     * Weaknesses (Critical): 列出存在的主要问题，每条须具体到分析设置、论证环节或表述缺陷，不接受泛泛而谈。若无致命问题，如实说明。
     * Rating: 给出预估评分（1-10分），并用一句话说明评分依据。
   - Part 2 [Strategic Advice]：针对作者的中文改稿建议。
     * 问题根源：解释 Part 1 中每条 Weakness 的深层原因——是调研设计的先天缺陷，还是表述掩盖了方法的局限？
     * 可救性判断：明确告知哪些问题可以在修订期内解决，哪些属于方法层面的结构性缺陷。
     * 行动指南：具体建议该补充哪些调研数据、重写哪段逻辑，或如何在修改中降低攻击面。
   - 除以上两部分外，不要输出任何多余的对话。

# Execution Protocol
在输出前，请自查：
1. 指出的每个问题是否具体到了可操作的层面？不要说"分析不够"，要说"缺少在 [具体村落] 上的 [具体空间参数] 验证"。
2. 有没有把"表述问题"误判为"方法缺陷"？两者的严重程度和修复路径完全不同。
3. 评分是否客观反映了论文对领域的实际贡献，而非套用固定的严苛预设？

# Input
请根据我上传的pdf附件进行分析，我计划投稿于 [在此处输入你的投稿目标，例如：Built Heritage / 建筑学报]
````

---

## 模型选择

我们从公开网站 [arena.ai](https://arena.ai/zh/leaderboard/text/creative-writing) 上获取了Creative Writing能力排名前10的模型与具体版本，该榜单结果与调研群体的日常使用选择高度契合。在建筑遗产科研场景中，日常的 idea 交互与论文写作，主力模型仍为 Gemini-3-pro/flash；在空间分析与 GIS 数据处理场景下，更多使用 Claude-4.5 系列模型，以及 Cursor 内置的 Composer 模型。

---

# Part II: 论文写作相关的 Agent-Skills

> 🎯 **适用对象**：本部分内容主要面向经常使用 Cursor、Claude Code 等 AI coding 工具的建筑遗产领域研究者
>
> 💡 **使用说明**：Agent Skills 是一种可被 AI 助手（如 Claude、Cursor）加载的扩展能力包，内含针对特定任务的流程、规范与模板。在 Claude Code、Cursor 等环境中配置相应 Skill 后，在对话中直接描述需求（如目标期刊、repo 路径、要写的章节），即可触发对应流程，无需记忆复杂 prompt

## Skills 的配置

下文的演示基于 **OpenSkills** 生态：它提供一套**通用的 Skills 加载/管理方式**，让 Cursor 等 AI coding agent 可以读取并使用以 `SKILL.md` 为核心的技能包。参考链接： [Cursor Agent Skills](https://cursor.com/docs/context/skills)、[openskills](https://github.com/numman-ali/openskills)

### 1) 前置依赖

OpenSkills 通过 npm 分发，并会从 GitHub 拉取 skills 仓库，因此建议准备：
- Node.js 20.6+（含 npm）
- Git

### 2) 安装/运行 OpenSkills

OpenSkills 支持直接用 `npx` 运行：

```bash
npx openskills --version
```

如需多项目复用，也可全局安装：

```bash
npm i -g openskills
openskills --version
```

### 3) 一键安装 Skills

Openskills 支持直接从 GitHub 仓库安装 Skills，并自动放入默认目录（一般为项目内 `./.claude/skills/`），Cursor 会自动从 `.claude/skills/`（以及 `.cursor/skills/`）发现 skills 并加载

下面以两个上游仓库为例展示 Skills 的安装方式：

```bash
# research 相关：zechenzhangAGI/AI-research-SKILLs
npx openskills install zechenzhangAGI/AI-research-SKILLs

# Anthropic 官方 skills
npx openskills install anthropics/skills
```

执行后 OpenSkills 会弹出交互式选择（勾选需要的 Skill 即可，默认全部安装）

### 4) 在 Cursor 中查看与使用 Skills

Skills 安装到 `.claude/skills/` 后，Cursor 启动时会自动发现并提供给 Agent 使用。建议按以下方式验证：

- **确认 skills 已安装**：`npx openskills list` 能看到目标 skills
- **在 Cursor Settings 中查看**：打开 Cursor Settings，进入 **Rules, Skills, Subagents**，在 **Skills** 区域可看到已发现的 skills
- **在对话中手动调用**：在 Agent Chat 输入 `/`，搜索 skill 名称并手动插入
- **在对话中自然触发**：直接提出明显对应 skill 的需求（例如"用期刊模板开新稿""写一个建筑遗产类型学对比表格"），若行为与 Skill 文档一致，则配置生效

配置完成后，无需记忆复杂 prompt，在对话中直接说明「要做什么」和「已有信息」即可。

## Skills 总览

| Skill 名称 | 来源 | 功能简述 |
|------------|------|----------|
| **20-ml-paper-writing** | [zechenzhangAGI/AI-research-SKILLs](https://github.com/zechenzhangAGI/AI-research-SKILLs) | 面向 NeurIPS / ICML / ICLR / ACL / AAAI / COLM 的完整论文写作。建筑遗产研究者可根据需要调整模板，适配 *Built Heritage*, *Habitat International* 等期刊格式。 |
| **humanizer** | [blader/humanizer](https://github.com/blader/humanizer) | 识别并去除 AI 写作痕迹，使文本更自然、像人写。适合润色后终稿或投稿前语言风格检查。 |
| **docx** | [anthropics/skills](https://github.com/anthropics/skills) | 对 .docx 进行创建、编辑、分析。适用于中文核心期刊的 Word 投稿模板。 |
| **doc-coauthoring** | [anthropics/skills](https://github.com/anthropics/skills) | 分阶段文档协作：收集上下文与澄清问题 → 按节头脑风暴→起草→精修 → 读者测试查盲点。适用于论文单节或整篇的结构化迭代。 |
| **canvas-design** | [anthropics/skills](https://github.com/anthropics/skills) | 先产出 design philosophy (.md)，再在画布上实现为单页 .png / .pdf，适合论文中的空间形态概念图、类型学示意图、遗产廊道框架图。 |

## 使用场景与示例 Prompt

| 使用场景 | 推荐 Skill | 前置输入 | 示例 Prompt | 产出 |
|----------|------------|----------|-------------|-------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| 从零写一篇论文 | 20-ml-paper-writing | 研究 repo 路径或关键文件 + 目标期刊 | 「用这个 repo 帮我写一篇投 *Built Heritage* 的论文」「根据调研数据，起草一篇投《建筑学报》的稿子」 | 完整初稿 |
| 用期刊模板开新稿 | 20-ml-paper-writing | 目标期刊 + 论文目录存放路径 | 「帮我用 *Built Heritage* 模板新建一篇论文」「用《建筑学报》模板，项目放在当前目录」 | 模板目录 + 章节骨架 |
| 加引用 / 写 Related Work | 20-ml-paper-writing | 要引用的主题或关键词（如「盐茶商贸通道」） | 「帮我找并引用 2020 年后传统村落空间形态的代表作」「Related Work 里需要 cite Hillier 的 space syntax」 | BibTeX / 引用列表 |
| 投稿前清单核对 | 20-ml-paper-writing | 无 | 「帮我对一下 *Built Heritage* 的投稿要求」「交稿前帮我看一遍《建筑学报》的格式要求」 | 逐项核对 |
| 写 / 改表格 | 20-ml-paper-writing | 村落名、空间参数、数值 | 「帮我把下面空间参数做成论文里的表格」「用 booktabs 风格」 | LaTeX 表格代码 |
| 图与 caption 规范 | 20-ml-paper-writing | 图或图的描述 | 「帮我写 Figure 1 的 caption」「这张空间分析图要符合期刊要求」 | caption 文案 + 规范建议 |
| 结构化流程写某一节 | doc-coauthoring | 无 | 「用 doc coauthoring 流程，我们先写引言」「我想用协作流程写这篇论文的空间分析部分」 | 三阶段说明 |
| 论文概念图 / 框架图 | canvas-design | 图的用途与大致元素 | 「帮我画一个盐茶商贸通道的空间框架图」「做一张三节点类型学的对比示意图」 | design philosophy (.md) + .pdf/.png |
| 去 AI 味 / 润色后终稿检查 | humanizer | 待检查的段落或全文 | 「这段读起来像 AI 写的，帮我 humanize」「投稿前帮我把摘要去一下 AI 味」 | 重写后的自然文本 |
| 用 Word 模板写投稿稿 | docx | 期刊 .docx 投稿模板；标题、摘要、正文 | 「这是《建筑学报》的 Word 模板，帮我把标题、摘要和正文填进去」 | 符合模板格式的 .docx |

[![Star History Chart](https://api.star-history.com/svg?repos=Leey21/awesome-ai-research-writing&type=Date)](https://star-history.com/#/Leey21/awesome-ai-research-writing&Date)
