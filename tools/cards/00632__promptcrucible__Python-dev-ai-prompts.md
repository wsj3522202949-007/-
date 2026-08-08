---
id: tool-00632
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Python-dev-ai-prompts
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/promptcrucible/python-dev-ai-prompts
created: 2026-07-18
updated: 2026-07-18
no: 632
category: 二、网文 / 长篇 AI 写作系统 库
repo: promptcrucible/Python-dev-ai-prompts
stars: 0
url: https://github.com/promptcrucible/python-dev-ai-prompts
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
content_hash: caf5b248b2b39879
  - methods/最强写作方法论_全球最强综合版.md
---

# promptcrucible/Python-dev-ai-prompts

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/promptcrucible/python-dev-ai-prompts
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：10 free AI prompts from the Solopreneur Pack — cold email writing, sales page hooks, competitor research, content repurposing, weekly business review, and more. Same structured format as the full pack. Replace the brackets, run the prompt, use the output today. Instant download. No spam.
- **本地描述**：10 free AI prompts from the Solopreneur Pack — cold email writing, sales page hooks, competitor research, content repurposing, weekly business review, and more. Same structured format as the full pack. Replace the brackets, run the prompt, use the output today. Instant download. No spam.
- **拉取时间**：2026-07-23 22:57:30

---

# 🐍 Python Developer AI Prompts
### Free structured AI prompts for Python developers — built for Claude, ChatGPT, and Cursor.

[![PromptCrucible](https://img.shields.io/badge/PromptCrucible-Prompts%20built%20for%20people%20building%20alone-E8540A?style=flat-square)](https://promptcrucible.gumroad.com)
[![Prompts](https://img.shields.io/badge/Free%20Prompts-5%20inside-0D0D0D?style=flat-square)](#free-prompts)
[![Full Pack](https://img.shields.io/badge/Full%20Pack-55%20prompts%20%40%20%2420-E8540A?style=flat-square)](https://promptcrucible.gumroad.com)

---

## What is this?

A collection of structured AI prompts for Python developers. Every prompt has:

- A clear **title** and **use case**
- **[BRACKETS]** showing exactly what to replace with your specifics
- A **Pro Tip** that makes the output sharper

These are not generic "help me write Python" prompts. Each one is built around a specific task you face when writing real Python code — documentation, architecture, code review, testing, and debugging.

**Works with:** Claude · ChatGPT · Cursor · Any capable AI model

---

## 5 Free Prompts

---

### 001 — Generate a Google-Style Docstring

**Best for:** Functions, methods, classes

```
Write a complete Google-style docstring for this Python function.
Include: a one-line summary, a detailed description of what it does,
an Args section with each parameter's name, type, and description,
a Returns section with the return type and description, a Raises
section for any exceptions that can be raised, and a usage Example.

Function to document:
[PASTE FUNCTION HERE]
```

> 💡 **Pro Tip:** Run this on every public function before committing.
> Undocumented code is technical debt that compounds every time
> a new developer joins the project.

---

### 002 — Full Function Code Review

**Best for:** All Python code, pre-PR reviews

```
Review this Python function for issues across all of these dimensions:

(1) Correctness — does it do what it claims, are there logical errors?
(2) Edge cases — what inputs would cause unexpected behaviour or crashes?
(3) Performance — are there O(n²) operations that could be optimised?
(4) Readability — is the naming clear, are there magic numbers?
(5) Security — does it validate inputs, could it be exploited?
(6) Python-specific — are there more Pythonic ways to write this?

List every issue found and provide the corrected code for each.

Function to review:
[PASTE FUNCTION HERE]
```

> 💡 **Pro Tip:** Run this on every function before it goes into a
> pull request. One structured review catches more bugs than ten
> quick reads.

---

### 003 — Write Unit Tests for a Function

**Best for:** pytest, any Python function

```
Write comprehensive pytest unit tests for this Python function.

Include tests for:
- The happy path with typical inputs
- Edge cases (empty inputs, zero, None, very large values)
- Error cases (what exceptions should be raised and when)
- Boundary conditions (minimum and maximum valid values)

Use descriptive test names that explain what is being tested.
Use pytest fixtures for any setup needed.
Mock any external dependencies.

Function to test:
[PASTE FUNCTION HERE]
```

> 💡 **Pro Tip:** Name tests as
> `test_[function_name]_[scenario]_[expected_result]`.
> A test name should tell you exactly what failed without
> reading the test body.

---

### 004 — Design a Project Folder Structure

**Best for:** New projects, refactoring existing codebases

```
Design the folder structure for a Python project called [PROJECT NAME].

The project is: [describe — web app, CLI tool, data pipeline, API, etc.]
It will use: [list key libraries/frameworks]
It needs to handle: [describe the main responsibilities]

Provide:
- The complete directory tree with every folder and key files
- A brief explanation of what goes in each directory
- Where configuration lives
- Where tests live
- Where utilities and shared code live
- Any conventions to follow when adding new files

The structure must support: [describe growth — multiple modules,
background workers, multiple environments, etc.]
```

> 💡 **Pro Tip:** Decide your folder structure before writing a single
> line of code. Restructuring a live project costs 10x more than
> planning it correctly upfront.

---

### 005 — Debug This Error

**Best for:** Any Python traceback, any error

```
Help me debug this Python error.

Error message:
[PASTE FULL TRACEBACK HERE]

Code that produced it:
[PASTE RELEVANT CODE HERE]

Context:
[Describe what the code is supposed to do, what input triggered
the error, and what you have already tried]

Provide:
- The exact cause of this error
- Why it is happening in this specific case
- The fix with corrected code
- Whether this error could occur in other places in the codebase
- How to write a test that would catch this error in the future
```

> 💡 **Pro Tip:** Always paste the full traceback — not just the
> last line. The root cause is often several frames up the stack.

---

## Get the Full 10 as a PDF

The formatted PDF version of all 10 free prompts — clean layout,
print-ready, easy to reference while coding.

**→ [Download the free PDF here](https://github.com/promptcrucible/Python-dev-ai-prompts/raw/main/PromptCrucible_10_Free_Prompts.pdf)**

---

## Full Pack — 55 Prompts

The complete Python Developer AI Prompt Pack covers 6 categories:

| # | Category | Prompts |
|---|---|---|
| 01 | Code Documentation | 10 |
| 02 | Architecture & Project Planning | 10 |
| 03 | Code Review & Debugging | 10 |
| 04 | Testing & Quality | 8 |
| 05 | Performance, Security & Deployment | 7 |
| 06 | Python Patterns & Best Practices | 10 |
| **Total** | | **55** |

**Early buyer price: $20 → [Get the full pack](https://promptcrucible.gumroad.com)**

Price increases as the pack grows. Existing buyers receive all updates free.

---

## How to Use These Prompts

1. Copy the prompt
2. Replace every `[BRACKET]` with your specific details
3. Paste into Claude, ChatGPT, or Cursor
4. Use the output

The more specific you are when filling in the brackets,
the more useful the output.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## About PromptCrucible

Structured AI prompt packs for solopreneurs and Python developers.
Built by one person. Tested on real code and real businesses.

**→ [promptcrucible.gumroad.com](https://promptcrucible.gumroad.com)**
