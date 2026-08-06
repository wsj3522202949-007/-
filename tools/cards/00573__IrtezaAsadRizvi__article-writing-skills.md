---
id: tool-00573
type: tool
area: 库
status: active
tags: [Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: article-writing-skills
summary: Claude Code 插件式写作流
source: https://github.com/irtezaasadrizvi/article-writing-skills
created: 2026-07-18
updated: 2026-07-18
no: 573
category: 二、网文 / 长篇 AI 写作系统 库
repo: IrtezaAsadRizvi/article-writing-skills
stars: 13
url: https://github.com/irtezaasadrizvi/article-writing-skills
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# IrtezaAsadRizvi/article-writing-skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/irtezaasadrizvi/article-writing-skills
- **Stars**：13
- **语言**：None
- **License**：MIT
- **Topics**：agent-skills, ai, ai-agents, article-generator, blogging, chatgpt, claude, claude-code, claude-code-plugin, claude-skills, karpathy, mcp, writing, writing-assistant, writing-tool
- **GitHub 描述**：Article, blog & paper writing prompts and Claude skills modelled on famous engineers and researchers. Works with Claude Code, ChatGPT, Gemini, and any LLM.
- **本地描述**：Article, blog & paper writing prompts and Claude skills modelled on famous engineers and researchers. Works with Claude Code, ChatGPT, Gemini, and any LLM.
- **拉取时间**：2026-07-23 22:55:46

---

# Article Writing Skills for Claude, ChatGPT, and other LLMs

> A curated collection of **writing skills, prompts, and system prompts** modeled on how famous engineers, scientists, and researchers think and write. Use them with **Claude Code**, **Claude**, **ChatGPT**, **Gemini**, **Cursor**, or any LLM to explore topics through the minds of people you admire.

**Keywords:** article writing prompts · blog writing prompts · paper writing prompts · technical writing skills · Claude skills · ChatGPT system prompts · LLM writing styles · engineer writing style · researcher writing style · thinking frameworks for LLMs · Andrej Karpathy writing style · Claude Code skills

---

## Available skills

| Skill | Thinking style |
|---|---|
| [`andrej-karpathy/`](https://github.com/IrtezaAsadRizvi/article-writing-skills/blob/main/andrej-karpathy/SKILL.md) | First-principles, code-forward, intuition-before-formalism — explore topics the way Andrej Karpathy writes about neural networks, training, and ML systems. |

*More skills are being added. Contributions welcome — see below.*

## What this repo is

This repo holds **"article-writing skills"** — structured prompts that capture *how* a specific well-known engineer or researcher approaches a topic: what they notice first, what they strip away, which analogies they reach for, how they build intuition before formalism, how they sequence an explanation.

You can load any skill into your LLM of choice (Claude, ChatGPT, Gemini, local models) and use it as a lens for exploring, drafting, or thinking through a technical topic.

## What these skills are *for*

✅ **Exploring a topic through someone else's way of thinking.** Ask *"how would this person see this?"* and get a genuinely different angle.
✅ **Overcoming a blank page.** Borrow a thinking framework to get moving on an article, blog post, paper, or explainer.
✅ **Learning hard topics.** Read a concept explained the way your favorite educator *would* explain it.
✅ **Improving your own technical writing** by studying the structures great writers use — not the surface voice.

## What these skills are *not* for

❌ **Ghostwriting as someone else.** The goal is not to produce prose that pretends to be authored by them.
❌ **Surface-level style transfer.** Copying sentence length, favorite words, or catchphrases misses the point.
❌ **A replacement for reading the originals.** These skills are lenses, not substitutes — always go read the source material.
❌ **Impersonation or deception.** Do not publish content that claims to be written by the person the skill is modeled on.

## How to use a skill

### With Claude Code

Drop the skill folder into `~/.claude/skills/` (or a project's `.claude/skills/`) and invoke it by name. See the [Claude Code skills documentation](https://docs.claude.com/en/docs/claude-code/skills) for details.

### With Claude (claude.ai) or ChatGPT

Open the skill's `SKILL.md`, copy its contents, and paste it as a **system prompt** or **custom instruction** in a new conversation. Then describe the topic you want to explore.

### With any other LLM

The skills are plain Markdown — they work anywhere you can supply a system prompt or preamble.

## Who this is for

- **Engineers** writing technical blog posts, design docs, or RFCs who want a better thinking scaffold.
- **Researchers** drafting papers, explainers, or talks who want to stress-test their framing.
- **Students and learners** who want to understand a topic the way a specific expert would explain it.
- **LLM power users** building custom GPTs, Claude Projects, Cursor rules, or agent prompts for writing.
- **Technical writers and developer advocates** looking for proven structures behind great technical writing.

## FAQ

**Is this a prompt library?**
Yes — specifically for *article, blog, and paper writing* through the lens of specific thinkers. Each skill is a self-contained prompt/instruction set.

**Does this work with ChatGPT as well as Claude?**
Yes. The skills are model-agnostic Markdown. They were authored with Claude Code's skill format in mind but work as system prompts in ChatGPT, Gemini, or any LLM.

**Will it make my writing sound exactly like Andrej Karpathy (or whoever)?**
No — and that's deliberate. The skills encode *thinking patterns*, not mannerisms. Your writing will still sound like you, but your framing, sequencing, and choice of examples will be informed by how the subject approaches problems.

**Can I contribute a new skill?**
Yes. Open a PR with a new folder named after the person and a `SKILL.md` that captures their thinking style (not their vocabulary). Focus on *how they think*: what they prioritize, what they omit, how they build up ideas.

**Is this affiliated with any of the people the skills are modeled on?**
No. These are independent, community-authored interpretations of publicly available writing. They are lenses, not endorsements.

## License & ethics

Licensed under the [MIT License](https://github.com/IrtezaAsadRizvi/article-writing-skills/blob/main/LICENSE) — free to use, modify, and share.

**Ethical note:** Use these skills to learn, explore, and improve your own writing. **Do not publish content as if it were authored by the person the skill is modeled on.** Always disclose AI assistance per the norms of your publication venue.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*If you found this repo useful, star it so others searching for **LLM writing prompts**, **Claude skills**, or **ChatGPT writing system prompts** can find it too.*
