---
id: tool-01439
type: tool
area: 库
status: active
tags: [提示词, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: llm-prompt-templates
summary: 提示词/写作工作流
source: https://github.com/jy02140251/llm-prompt-templates
created: 2026-07-18
updated: 2026-07-18
no: 1439
category: 二、网文 / 长篇 AI 写作系统 库
repo: jy02140251/llm-prompt-templates
stars: 4
url: https://github.com/jy02140251/llm-prompt-templates
tier: "B"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 7718d8c967b386d3
  - methods/最强写作方法论_全球最强综合版.md
---

# jy02140251/llm-prompt-templates

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jy02140251/llm-prompt-templates
- **Stars**：4
- **语言**：None
- **License**：None
- **Topics**：ai, chatgpt, claude, gemini, gpt-4, llm, openai, prompt-engineering, prompts
- **GitHub 描述**：Collection of 100+ battle-tested LLM prompts for coding, writing, and analysis. Works with GPT-4, Claude, Gemini. Copy-paste ready.
- **本地描述**：Collection of 100+ battle-tested LLM prompts for coding, writing, and analysis. Works with GPT-4, Claude, Gemini. Copy-paste ready.
- **拉取时间**：2026-07-23 23:21:03

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# LLM Prompt Templates

Battle-tested prompt templates for common AI tasks.

## Installation

```bash
npm install llm-prompt-templates
```

## Categories

### Coding
- Code review
- Bug fixing
- Code explanation
- Test generation
- Documentation
- Refactoring

### Writing
- Blog posts
- Technical docs
- Email drafts
- Summarization

### Analysis
- Data analysis
- Sentiment analysis
- Entity extraction
- Classification

## Usage

```typescript
import { getPrompt, fillPrompt } from 'llm-prompt-templates';

// Get a prompt
const prompt = getPrompt('coding/code-review');

// Fill variables
const filled = fillPrompt('coding/code-review', {
  code: myCode,
  language: 'typescript',
  focus: 'security',
});

// Use with any LLM
const response = await openai.chat.completions.create({
  model: 'gpt-4',
  messages: [{ role: 'user', content: filled }],
});
```

## Example Prompts

### Code Review
```
Review this {language} code for {focus}:

```{language}
{code}
```

Provide:
1. Issues found (severity: high/medium/low)
2. Suggested fixes
3. Best practices recommendations
```

### Summarization
```
Summarize the following text in {sentences} sentences.
Focus on: {focus}
Tone: {tone}

Text:
{text}
```

## License

MIT
