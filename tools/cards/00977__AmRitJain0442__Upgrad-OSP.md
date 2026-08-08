---
id: tool-00977
type: tool
area: 库
status: active
tags: [提示词, Python, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: Upgrad-OSP
summary: 提示词/写作工作流
source: https://github.com/amritjain0442/upgrad-osp
created: 2026-07-18
updated: 2026-07-18
no: 977
category: 二、网文 / 长篇 AI 写作系统 库
repo: AmRitJain0442/Upgrad-OSP
stars: 1
url: https://github.com/amritjain0442/upgrad-osp
tier: "B"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e21b982e8b354955
  - methods/最强写作方法论_全球最强综合版.md
---

# AmRitJain0442/Upgrad-OSP

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/amritjain0442/upgrad-osp
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Two-Panel Interface: • Left Panel: AI Tutor chat (guidance, tips, quiz) -- (use a faster model like gemini-flash-latest to give them real time guidance on the prompts that they are writing and while that one generates, show the breakdown of the prompt and also make that left one also resizable.)
- **本地描述**：Two-Panel Interface: • Left Panel: AI Tutor chat (guidance, tips, quiz) -- (use a faster model like gemini-flash-latest to give them real time guidance on the prompts that they are writing and while that one generates, show the breakdown of the prompt and also make that left one also resizable.)
- **拉取时间**：2026-07-23 23:07:33

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Two-Panel Interface:
• Left Panel: AI Tutor chat (guidance, tips, quiz) -- (use a faster model like gemini-flash-latest to give them real time guidance on the prompts that they are writing and while that one generates, show the breakdown of the prompt and also make that left one also resizable.)
• Right Panel: Workspace (document upload, prompt testing, results)
Add markdown parsing/rendering in both of them. and instruct the ai properly.

Lesson Flow:

1.  Welcome → AI tutor introduces lesson ("Learn to prevent AI hallucination")
2.  Upload Phase → Highlights upload button, user uploads doc
3.  Prompt Phase → Workspace shows doc preview, prompt input appears
4.  Proactive Tips → If user types simple prompt without constraints (e.g., just "summarize"), tutor suggests
    adding constraints like "Based only on the text provided"
5.  Generate → Calls /api/summarize, displays result in workspace
6.  Feedback → AI tutor analyzes if prompt had constraints, provides feedback
7.  Quiz → Multiple choice question to reinforce learning
8.  Unlock → Next submodule becomes available

and also, add highlighting around the steps that the user has to take next and everything should be just in memory. and use the models from @app/base_model.py and ask me any doubts you have before proceeding. And i need you to give me a whole guide to the prompt engineering, like, a lesson plan for this type and use pydantic-ai and also stream the responses. and also, use the theme from the old one, but improve it and make it clean and good. and i dont want any gradients and others. ask me any doubts you have before proceeding. And use get-library-docs tool to get the docs of "/pydantic/pydantic-ai" to know to to implement it.

Smart Features:
• Markdown parsing for formatted AI responses
• UI element highlighting during lessons
• State management (tracks current step, attempts, completion)
• Proactive intervention (detects weak prompts, offers suggestions)
• Progressive unlocking of submodules
