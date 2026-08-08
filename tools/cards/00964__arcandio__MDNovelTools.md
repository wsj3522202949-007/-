---
id: tool-00964
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: MDNovelTools
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/arcandio/mdnoveltools
created: 2026-07-18
updated: 2026-07-18
no: 964
category: 二、网文 / 长篇 AI 写作系统 库
repo: arcandio/MDNovelTools
stars: 1
url: https://github.com/arcandio/mdnoveltools
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 335dbeeea47d023a
  - methods/最强写作方法论_全球最强综合版.md
---

# arcandio/MDNovelTools

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/arcandio/mdnoveltools
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：fiction, markdown, novel, writing
- **GitHub 描述**：Use Markdown to Write Books!
- **本地描述**：Use Markdown to Write Books!
- **拉取时间**：2026-07-23 23:07:10

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# MD Novel Tools

[Github Home](https://github.com/arcandio/MDNovelTools)

* **What is it?** It's a toolkit to mimic Literature & Latte's wonderful Scrivener, but for plaintext Markdown files.
* **Why you do this?** Writing, synchronizing, and editing long-form documents is easier when document versions can be compared. What better way to compare and keep track of your writing than using [Git](https://git-scm.com/), or another source control management system?
* **How does it work?** Right now, you need to have Python and Pandoc installed. Then you download the source and run the `tools.pyw` file and boom, you get an app:

![Screenshot](https://github.com/arcandio/MDNovelTools/blob/main/screenshot.png)

## Features

### Tree View

* `Double-click` a file to open it in your default Markdown editor.
* Resizable columns.

### Toolbox

* `Pick Dir` selects a directory to use as the base level for your manuscript. *It will look for/put other, non-manuscript files in the parent of this directory.*
* `Rebuild Tree` refreshes the file tree. The app doesn't automatically do this for you. (It's hard to watch files, cross platform, in Python.)
* `Compile MS`
* `Spread Newlines`†: Inserts a space between lines with text.
* `Metadata` Creates or opens a metadata file next to your manuscript folder. Default provided with common items.
* `Always on Top` Makes the app float over other windows.
* `Toggle Date` hides or shows the Date column, which may or may not be useful to all writers.

† Operates on selected files

### Comments

* `> Comments look like this. <` They're Blockquotes that end with a `<` character.
  * Markdown doesn't have a dedicated commenting system out of the box, so we've opted to use BlockQuote because a a lot of fiction doesn't use this typographical convention. I'm looking for other solutions as well.
  * Comments are stripped from the text when you `Compile MS`

## Suggested Markdown Editors

* [Typora](https://typora.io/)
* [Sublime Text](https://www.sublimetext.com/3)
* [Atom.io](https://atom.io/)

