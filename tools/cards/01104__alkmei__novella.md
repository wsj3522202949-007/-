---
id: tool-01104
type: tool
area: 库
status: active
tags: [Python, 协议传染, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: novella
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/alkmei/novella
created: 2026-07-18
updated: 2026-07-18
no: 1104
category: 二、网文 / 长篇 AI 写作系统 库
repo: alkmei/novella
stars: 0
url: https://github.com/alkmei/novella
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# alkmei/novella

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/alkmei/novella
- **Stars**：0
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：python3, tools, writing
- **GitHub 描述**：Novella is a command-line tool that allows users to create and manage stories based on text files.
- **本地描述**：Novella is a command-line tool that allows users to create and manage stories based on text files.
- **拉取时间**：2026-07-23 23:11:14

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Novella
 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
> novella lets you manage stories

Novella is a command-line tool that allows users to create and manage stories based on plaintext files.

## Usage

At this moment, novella is very barebones, consisting of just core modules and a dream. Below are planned usages for it.


```shell
novella [OPTIONS] COMMAND [ARGS]...
```

**Commands**:

- `chapter`: Handles chapters
- `compile`: Compiles a story
- `init`: Initializes a story

## `chapter`

```shell
novella chapter [OPTIONS] COMMAND [ARGS]...
novella chapter new TITLE [PATH]
```

## `compile`

```shell
novella compile [PATH]
```

## `init`

```shell
novella init TITLE [PATH]
```

**Options**
* `--author`: Specify author name. Default: Anonymous
