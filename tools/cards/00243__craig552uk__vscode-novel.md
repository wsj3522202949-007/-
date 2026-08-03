---
id: tool-00243
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: vscode-novel
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/craig552uk/vscode-novel
created: 2026-07-18
updated: 2026-07-18
no: 243
category: 二、网文 / 长篇 AI 写作系统 库
repo: craig552uk/vscode-novel
stars: 0
url: https://github.com/craig552uk/vscode-novel
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# craig552uk/vscode-novel

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/craig552uk/vscode-novel
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A project framework for creative writing in VSCode
- **本地描述**：A project framework for creative writing in VSCode
- **拉取时间**：2026-07-23 22:46:10

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---



## Installation

Install dependencies with homebrew

```
$ brew install python3 go-task
```

Install python libraries. Follow instructions if prompted to setup venv

```
$ pip -m install reportlab
```

View available tasks with

```
$ task --list
```

## Workflow

1. Write the book in the `manuscript` folder, one folder per-chapter, one scene per file. Files are in markdown. Prefix file and folder names with numbers to enforce ordering.

2. I like to edit in Word, so I run `task manuscript:docx` to generate a Word file in `prepare/editing` containing the full manuscript.

3. After editing, I begin typesetting the paperback, hard cover and eBook. I like to use Apple Pages for this. A template file is included. I export the paperback and hard cover files to PDF ready for upload to KDP.

4. After typesetting, I update `PAPERBACK_PAGE_COUNT` and `HARDCOVER_PAGE_COUNT` in `metadata.env` then run `task cover:all` to generate cover template files. I use these to design the covers.

5. Finally I upload the finished files to KDP and publish my book!


## Project Structure

`/manuscript`

This is where you write your book.

`/notes`

This is where you keep research, plot, character descriptions and other reference material

