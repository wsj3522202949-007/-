---
id: tool-00007
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 本地写作]
title: storyteller
summary: 搭大纲/分卷/节拍
source: https://github.com/facedeer/storyteller
created: 2026-07-18
updated: 2026-07-18
no: 7
category: 二、网文 / 长篇 AI 写作系统 库
repo: FaceDeer/storyteller
stars: 23
url: https://github.com/facedeer/storyteller
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# FaceDeer/storyteller

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/facedeer/storyteller
- **Stars**：23
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A simple framework for using a local Koboldcpp LLM to help with story-writing
- **本地描述**：A simple framework for using a local Koboldcpp LLM to help with story-writing
- **拉取时间**：2026-07-23 22:39:03

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# storyteller
A simple framework for using a local Koboldcpp LLM to help with story-writing

This application uses PyQt to provide an interface to a local [Koboldcpp](https://github.com/LostRuins/koboldcpp) instance that's designed to make story-writing easier to keep organized and make good use of a smaller context size than the story can fit into.

It divides the story up into chapters, and scenes within those chapters, and when generating the text for scenes it combines the text and summaries of previous scenes and chapters to hopefully provide the salient details needed for the current scene to generate well.

The following shows what is included in the prompt (outlined in green) that is used to generate a scene's text (outlined in red). In a nutshell:

* The background information is always included first.
* Each "previous chapter" summary is included.
* The summary of each previous scene in the current chapter is included. Scene summaries from previous chapters are not included, it is expected that all salient information from them is contained in the "previous chapter" summary following it.
* The summary of the scene immediately prior to the current one is not included, instead the complete text of the previous scene is included.
* Finally, the summary of the current scene is used to tell the LLM what it is supposed to write about in the current scene.

![](https://github.com/FaceDeer/storyteller/blob/main/Images/Outline.png)

Since the complete text of the previous scene is included in the prompt for the next scene, it's important to proofread and edit each secene in the story after it's generated before going ahead and generating the next one. This ensures that mistakes the LLM makes aren't propagated forward.
