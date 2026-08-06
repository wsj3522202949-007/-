---
id: tool-00599
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: aiml_prompts_250107
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/giacomo9999/aiml_prompts_250107
created: 2026-07-18
updated: 2026-07-18
no: 599
category: 二、网文 / 长篇 AI 写作系统 库
repo: giacomo9999/aiml_prompts_250107
stars: 0
url: https://github.com/giacomo9999/aiml_prompts_250107
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# giacomo9999/aiml_prompts_250107

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/giacomo9999/aiml_prompts_250107
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Exercise in writing LLM prompts
- **本地描述**：Exercise in writing LLM prompts
- **拉取时间**：2026-07-23 22:56:31

---

# Unit AI-1SB: Prompts

## Summary

How do we approach prompting as programming in natural language? What best practices can we apply?

Above all, we want our code to be **maintainable** (adaptable to changing requirements), which is why we make our code **readable** (understandable at a glance), **modular** (separating functionality), and **flexible** (avoiding hard-coded values and tight coupling). These best practices also allow us to build confidence in our code through **testing**. ✅️

There are three key strategies we rely on as software engineers: pseudocode, pair programming, and code review.

- Pseudocode should be language-agnostic – it should be the same whether the “end language” is JS, C++, or natural language. Keep it relatively high level, explaining your approach and the necessary steps.
- Pair programming is all about honing technical communication through the driver-navigator approach. It compels you to clarify your intent (what exactly you want your code to do and how) and to clarify your explanation.
- Performing code review deepens your understanding of a codebase (and a language!) and develops your technical communication; receiving it is a great growth opportunity.

Writing good, clean code is about more than whether it “works” (produces the intended output when executed). This is just as true for prompting as it is for writing JS! Think of the prompt you send to an LLM as a module – a set of functions and data to be run – and lead with your engineering mindset! 🧠

## Challenges

- Copy each [example prompt](https://github.com/giacomo9999/aiml_prompts_250107/blob/main/example-prompts/) from this repo into a shared Google doc. Think about what purpose each part of the prompt serves. What components can you identify? Use color coding or highlighting to “diagram” the prompts.
- In VS Code, break each prompt into modular components (“functions”) that can be combined into the original prompt (“module”).
- Do code review on the modularized prompts. Include things of interest, surprises, and potential opportunities for improvement. Refactor and add comments to the code where appropriate
- Pair program through the [prompting challenges](https://github.com/giacomo9999/aiml_prompts_250107/blob/main/prompting-challenges/) provided, following the driver/navigator approach to write pseudocode and draft prompts for each challenge. **Don't “run” your prompts with an LLM!** You're just whiteboarding. 📝


-related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Note: The solutions we used draw heavily on methodology from this Medium article: https://medium.com/the-modern-scientist/best-prompt-techniques-for-best-llm-responses-24d2ff4f6bca
