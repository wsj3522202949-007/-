---
id: tool-01304
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-bias-from-user-prompts
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/shekinah-lungu/ai-bias-from-user-prompts
created: 2026-07-18
updated: 2026-07-18
no: 1304
category: 二、网文 / 长篇 AI 写作系统 库
repo: shekinah-lungu/AI-bias-from-user-prompts
stars: 0
url: https://github.com/shekinah-lungu/ai-bias-from-user-prompts
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 802ec7db84fe5082
  - methods/最强写作方法论_全球最强综合版.md
---

# shekinah-lungu/AI-bias-from-user-prompts

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/shekinah-lungu/ai-bias-from-user-prompts
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：Probing Psychometric Traits from Writing Using Context Steering (CoS) 
- **本地描述**：Probing Psychometric Traits from Writing Using Context Steering (CoS)
- **拉取时间**：2026-07-23 23:17:07

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI-bias-from-user-prompts
Probing Psychometric Traits from Writing Using Context Steering (CoS) 
1. Motivation 

Large language models (LLMs) are powerful tools for generating natural language, but their generative nature also raises concerns about privacy and bias, especially when used in sensitive contexts like education, hiring, or mental health. One underexplored risk is that LLMs might infer private psychometric information from a user’s writing — such as whether someone is anxious, introverted, or depressed — even if the person never explicitly states these traits. This could pose serious implications for user trust and autonomy, especially if the model then changes its behavior based on these inferred traits. 

This project explores whether LLMs can infer psychometric properties from natural writing samples using a technique called Context Steering (CoS). I also investigate whether LLMs treat people differently based on these inferred traits, thereby introducing bias or fairness risks. 

Paper Summary – Context Steering in My Own Words 

The CoS paper introduces a new way to personalize LLM outputs by tuning the “influence” of context during generation. Imagine telling a language model, “I am a toddler,” and then asking it to explain Newton’s Second Law. Normally, you just hope that the model picks up on the context and changes its tone accordingly. With CoS, you actually have a knob (called λ or lambda) that lets you control how much that context shows up in the response. 

How does it work? It runs the model twice: 

Once with the context included 

Once without 

It then compares the difference in token likelihoods to create a “context influence” score, and scales that influence with λ. The bigger λ is, the more personalized (and context-heavy) the output becomes. Smaller λ leads to more neutral or generic text. Interestingly, when λ is negative, it can even subtract the context’s influence — leading to behavior as if the context weren’t there. 

Beyond just personalization, the authors show that CoS can be used to do Bayesian inference: you can run it in reverse to figure out what context most likely caused a given text. For example, if someone writes “I always overthink everything I say,” the model might infer that the context “I have anxiety” best explains that sentence. This opens up fascinating (and potentially dangerous) territory around inference of private information. 
