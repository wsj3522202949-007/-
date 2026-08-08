---
id: tool-00843
type: tool
area: 库
status: active
tags: [提示词, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: prompt-library
summary: 提示词/写作工作流
source: https://github.com/fomativeh/prompt-library
created: 2026-07-18
updated: 2026-07-18
no: 843
category: 二、网文 / 长篇 AI 写作系统 库
repo: fomativeh/prompt-library
stars: 5
url: https://github.com/fomativeh/prompt-library
tier: "B"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e4567110e9c63145
  - methods/最强写作方法论_全球最强综合版.md
---

# fomativeh/prompt-library

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/fomativeh/prompt-library
- **Stars**：5
- **语言**：None
- **License**：None
- **Topics**：claude, coding, content-generation, customer-support, data-analysis, deepseek, education, gemini, generative-ai, llm, nlp, openai, professional-writing, prompt-engineering, prompt-library, prompt-template, prompts
- **GitHub 描述**：A collection of AI prompts I've built for real business use cases. Covers content creation, data analysis, coding help, customer support, education, and professional writing. Each prompt includes examples and I'm constantly adding new ones based on what works.
- **本地描述**：A collection of AI prompts I've built for real business use cases. Covers content creation, data analysis, coding help, customer support, education, and professional writing. Each prompt includes examples and I'm constantly adding new ones based on what works.
- **拉取时间**：2026-07-23 23:03:37

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Prompt Library

This repo contains a structured collection of prompts designed for multiple use cases.  
All prompts follow a consistent format with **Objective**, **Prompt**, and **Example Output** sections for clarity and reuse.

## How to Use

1. **Browse Categories**: Choose the category that matches your use case
2. **Select Prompt**: Pick the specific prompt that fits your needs
3. **Copy & Customize**: Copy the prompt text and modify it with your specific requirements
4. **Test & Iterate**: Use the prompt with your AI tool and refine based on results

### Example Usage

**Scenario**: You need to classify customer support tickets

1. Go to [Customer Support → Ticket Classification](https://github.com/fomativeh/prompt-library/blob/main/customer-support/ticket-classification)
2. Copy the prompt from `prompt-v1.md`
3. Replace the example ticket with your actual ticket text
4. Run it through ChatGPT/Claude/etc.

**Original prompt:**
```
Classify the following support ticket into a category and priority...
```

**Your customized version:**
```
Classify the following support ticket into a category and priority...

Ticket:
"Hi, my login isn't working and I have a presentation in 2 hours. Please help!"
```

## Structure

- **[Content Generation](https://github.com/fomativeh/prompt-library/blob/main/content-generation)** - Creative and informational text generation
- **[Data Analysis](https://github.com/fomativeh/prompt-library/blob/main/data-analysis)** - Data-focused prompts for classification, transformation, extraction, question answering, sentiment analysis, SQL generation, and summarization
- **[Coding](https://github.com/fomativeh/prompt-library/blob/main/coding)** - Programming and software development prompts for code generation, explanation, and debugging
- **[Customer Support](https://github.com/fomativeh/prompt-library/blob/main/customer-support)** - Ticket classification and empathetic response generation
- **[Education](https://github.com/fomativeh/prompt-library/blob/main/education)** - Lesson planning and quiz generation
- **[Professional Writing](https://github.com/fomativeh/prompt-library/blob/main/professional-writing)** - Emails and structured reports

## Prompt Format

Each prompt is written in this format:

### **Prompt: [Task Name]**

**Objective:** Short description of the task.  

**Prompt:**
```Prompt text goes here```

**Example Output:**\
```A typical output for the given prompt```
