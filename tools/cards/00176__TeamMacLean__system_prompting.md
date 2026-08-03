---
id: tool-00176
type: tool
area: 库
status: active
tags: [CSS, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: system_prompting
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/teammaclean/system_prompting
created: 2026-07-18
updated: 2026-07-18
no: 176
category: 二、网文 / 长篇 AI 写作系统 库
repo: TeamMacLean/system_prompting
stars: 0
url: https://github.com/teammaclean/system_prompting
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# TeamMacLean/system_prompting

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/teammaclean/system_prompting
- **Stars**：0
- **语言**：CSS
- **License**：None
- **Topics**：—
- **GitHub 描述**：A guide to writing system prompts for AI code assistants
- **本地描述**：A guide to writing system prompts for AI code assistants
- **拉取时间**：2026-07-23 22:44:08

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# LLM Code Generation Guidelines

A collection of practical guides and system prompts for using LLMs effectively in software and analysis development.

## Overview

This repository contains guidelines for working with Large Language Models (LLMs) to generate code. The focus is on maintaining human control, creating sustainable workflows, and producing quality code through clear communication with AI assistants.

**Core Philosophy:** You stay in charge of design and decisions. The LLM implements what you specify.

**The Hare and The Tortoise:** LLMs are great servants and bad masters. If you expect to rush ahead and expect it to generate the whole of whatever you're creating in one go, you will end up with more code than you can follow/read/understand. In that mass there will be somewhere an error. This error will not be obvious to you, nor will it be to the LLM that generated it. What will follow is a slow and painful debugging process in which your early, apparent speed gains are lost incrementally. The quickest path to success is to use small, well specified steps very steadily. 

The repo contains guides and examples for using LLMs for analysis code and workflow generation.

## Questions These Materials Answer

- How do I get concise code instead of explanations?
- How do I maintain context across multiple sessions?
- How do I keep the LLM from suggesting things I don't want?
- How do I integrate LLM work with git workflow?
- How do I help the LLM understand my existing codebase?
- How do I prevent the LLM from making design decisions?


## Contents

1. **LLM-Code-Generation-Guide.md** - Comprehensive best practices guide
2. **System-Prompt-R-Analysis.md** - System prompt for R/RStudio work
3. **System-Prompt-Python-Package.md** - System prompt for Python package development  
4. **System-Prompt-Python-Script.md** - System prompt for Python scripting
5. **System-Prompt-Snakemake-Project.md** - System prompt for Snakemake workflows base on `blank_snake`

## Getting Started

### If You're New to LLM-Assisted Development

**Start here:** Read sections 1-3 of the main guide `01-LLM-Code-Generation.md`:
1. Writing Effective Prompts 
2. Controlling Output Verbosity
3. Engineering Process: Plan First

**Try this:** Practice with a simple task using the prompt templates. See how specific constraints improve results.

**Key insight:** Vague prompts get verbose, generic responses. Specific prompts with constraints get usable code.

### If You Want Structured Workflows

**Read:** 
4. Understanding Existing Codebases 
5. The TODO_TREE.md System 
6. Git Workflow Integration 

**Try this:** Create a TODO_TREE.md for a current project. Use it in your next LLM session.

**Key insight:** LLMs lack persistent memory. A work tree gives them context across sessions.

### If You Want Domain-Specific Prompts

**Use the system prompts:**
- **R users:** Statistical analysis and RStudio work → System-Prompt-R-Analysis.md
- **Python package developers:** Building libraries → System-Prompt-Python-Package.md
- **Python scripters:** Command-line tools → System-Prompt-Python-Script.md

**Try this:** Copy the relevant system prompt into your LLM's custom instructions or paste it at the start of sessions.

**Key insight:** System prompts set boundaries. They prevent LLMs from "helping" in ways you don't want.

## Quick Examples

### Getting Concise Code

**Instead of:**
```
"Can you help me write a function to validate email addresses?"
```

**Write:**
```
Write a Python function to validate email with regex.

Requirements:
- Accept string, return bool
- Check format: user@domain.tld
- Include type hints and docstring

Output: Code only.
```

### Using the TODO Tree

**Create tree:**
```markdown
## 1. Setup [>]
  ├─ 1.1 Database [✓]
  └─ 1.2 API structure [>] ← CURRENT
      ├─ 1.2.1 Routes [ ]
      └─ 1.2.2 Controllers [ ]
```

**Prompt LLM:**
```
TODO tree: [paste above]

I'm on task 1.2.1. Implement Express routes for user CRUD.
```

**After completing:**
```
Done with 1.2.1. Code: [paste]

Update tree: mark 1.2.1 done, move to 1.2.2.
```

### Maintaining Control (R Example)

**Wrong approach:**
```
"I have survey data. What analysis should I run?"
```

**Right approach:**
```
"Generate R code to run linear regression of satisfaction on age + income.
Use lm(). Output: just the code block."
```

The first invites unwanted suggestions. The second gets you code for your decision.

## Key Concepts Explained

### 1. Explicit Constraints
Tell the LLM exactly what you want and don't want. "Code only" prevents explanations. "Use only pandas" prevents alternative approaches.

### 2. Progressive Context Building
Don't dump entire codebases. Share directory structure, then configs, then relevant files. Layer by layer.

### 3. TODO Trees as Memory
Create a hierarchical task list (TODO_TREE.md). Update it as you work. Share it at the start of each session. The tree becomes the project's persistent memory.

### 4. Atomic Commits
One task = one commit = one tree update. Your git history mirrors your task tree.

### 5. Separation of Concerns
Design and analysis decisions: yours. Code implementation: LLM's. Keep this boundary clear.

## Common Pitfalls

**❌ Asking the LLM to make decisions:**
- "Should I use REST or GraphQL?"
- "What statistical test is appropriate?"
- "How should I structure this?"

**✅ Having LLM implement your decisions:**
- "Implement REST endpoints for [specification]"
- "Generate code for t-test comparing groups A and B"
- "Create [specific structure] following this pattern"

**❌ Overwhelming with context:**
- Pasting entire 5000-line files
- Sharing unrelated code
- No structure to information

**✅ Targeted context:**
- Relevant files only
- Directory tree for structure
- Specific sections of large files

**❌ Letting output run wild:**
- Open-ended questions
- No format specifications
- Accepting verbose explanations

**✅ Constraining output:**
- "Code only"
- "Format: [specify structure]"
- "No explanations unless asked"

## Workflow Summary

```
1. Plan task → Add to TODO_TREE.md
2. Share tree with LLM → Get context restoration
3. Request implementation → Be specific
4. Review code → Test it
5. Update tree → Mark done
6. Commit code + tree → Single atomic commit
7. Repeat
```

## Adapting These Guidelines

These materials are templates. Adapt them:

- **For your team:** Add your conventions, tech stack, processes
- **For your domain:** R prompts emphasize statistics; yours might emphasize embedded systems
- **For your style:** Prefer base R over tidyverse? Update the system prompt
- **For your workflow:** Use different status markers? Change the TODO_TREE legend

The principles remain: clarity, constraints, context, control.

