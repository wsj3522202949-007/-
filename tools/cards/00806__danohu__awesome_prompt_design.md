---
id: tool-00806
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: awesome_prompt_design
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/danohu/awesome_prompt_design
created: 2026-07-18
updated: 2026-07-18
no: 806
category: 二、网文 / 长篇 AI 写作系统 库
repo: danohu/awesome_prompt_design
stars: 10
url: https://github.com/danohu/awesome_prompt_design
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# danohu/awesome_prompt_design

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/danohu/awesome_prompt_design
- **Stars**：10
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Curated list of resources about writing prompts for AI: Stable Diffusion, ChatGPT, etc
- **本地描述**：Curated list of resources about writing prompts for AI: Stable Diffusion, ChatGPT, etc
- **拉取时间**：2026-07-23 23:02:32

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Awesome Prompt Design
Curated list of resources about writing prompts for AI: Stable Diffusion, ChatGPT, etc

To keep the main list on-topic, I've shuffled some resources onto separate pages:
- `[Slightly less awesome items](semi-awesomeness.md)`
- `[General AI Awesomeness](general-ai-awesomeness.md)`


## Images

* [img2prompt](https://replicate.com/methexis-inc/img2prompt): turn any image into a text prompt
* [prompt parrot](https://github.com/kyrick/cog-prompt-parrot): generate variations on a text prompt
* [types of film](https://www.lomography.com/films) to guide photography styles in prompting
* [Prompt Combinator](https://wainwrightmark.github.io/prompt-combinator/): systematically generate all possible permutations from a group of elements
* Artist styles: which artists can you imitate in [Dall-E](https://docs.google.com/spreadsheets/d/1d-N9BZ80qw3v2_3gWctYkRVuoMx6zs_We6c3h_yACJY/edit#gid=0) or [Midjourney](https://docs.google.com/spreadsheets/d/1d-N9BZ80qw3v2_3gWctYkRVuoMx6zs_We6c3h_yACJY/edit#gid=0)? Or check this huge [compilation of artist styles](https://asc.fooo.ooo/) for inspiration
* [Generate architectural images](https://twitter.com/nickfloats/status/1635116672054079488), using ChatGPT to prompt midjourney

### Midjourney

* On the midjourney discord: [#prompt-faqs](https://discord.com/channels/662267976984297473/1017917091606712430) and [#prompt-chat](https://discord.com/channels/662267976984297473/992207085146222713)
* Making [portraits](https://www.betchashesews.com/midjourney-portraits/) with midjourney

### Stable Diffusion

* Search engines for images generated with Stable Diffusion: [Lexica](https://lexica.art/), [Stable Diffusion Web](https://stablediffusionweb.com/prompts)


## Text

### General

- [Language learning prompts](https://github.com/squidgyai/squidgy-prompts) from the _Squidgies_ app (but usable beyond it)

###  GPT
* [Getting tabular data from unstructured text with GPT](https://robertorocha.info/getting-tabular-data-from-unstructured-text-with-gpt-3-an-ongoing-experiment/)
* [The art to start](https://medium.com/merzazine/the-art-to-start-designing-prompts-for-gpt-3-introduction-89848c208007):  designing prompts for GPT
* [OpenAI Cookbook](https://github.com/openai/openai-cookbook/tree/main)

### ChatGPT
* [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)
* [LearnGPT](https://www.learngpt.com/):  "the best ChatGPT examples from around the world"
* [Tricks to get around ChatGPT safeguards](https://twitter.com/davisblalock/status/1602600453555961856). Many of these loopholes have since been closed
* Specific tricks and examples:
	* [Building a virtual machine inside ChatGPT](https://www.engraved.blog/building-a-virtual-machine-inside/)

### Copilot
* [Microsoft guide](https://microsoft.github.io/prompt-engineering/) to writing prompts for copilot and other codex-based tools
* [Learning Rust with ChatGPT, Copilot and Advent of Code](https://simonwillison.net/2022/Dec/5/rust-chatgpt-copilot/) (Simon Willison)


### Libraries

see also `[General AI Awesomeness](general-ai-awesomeness.md)` for more tools

- [Langchain](https://langchain.readthedocs.io/en/latest/index.html) -- python library to manage the plumbing work around LLMs. For instance, use it to summarize documents you have and include them within your prompt
- [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel/tree/python-preview) - "a lightweight SDK enabling integration of AI Large Language Models (LLMs) with conventional programming languages"
- [Lambdaprompt](https://github.com/approximatelabs/lambdaprompt) - "Write LLM prompts with jinja templates, compose them in python as functions, and call them directly or use them as a webservice"
- [Llamaindex](https://github.com/jerryjliu/llama_index): link your data to LLMs, using data connectors and indices

##  Communities

* Reddit: [Prompt Design](https://www.reddit.com/r/PromptDesign/). 
* [London Prompt Engineers](https://www.meetup.com/london-prompt-engineers/)
* [AItuts](https://aituts.com/): collection of prompts and articles

## Individual Creators

This section is tilted towards those who share tips on their methods. I'm not including people who just make great art, without explaining how to do it

* [Merzmensch](https://medium.com/merzazine/the-art-to-start-designing-prompts-for-gpt-3-introduction-89848c208007)

## Other Collections

* [Awesome Generative Art](https://github.com/kosmos/awesome-generative-art)
* Pinboard searches: [prompts](https://pinboard.in/t:prompts), [prompt design](https://pinboard.in/t:prompt%20design)
* A [Trello board](https://trello.com/b/4BPkSY1w/100-ai-prompts-resources-prompt-lovers) of AI prompts




