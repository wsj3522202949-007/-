---
id: tool-01481
type: tool
area: 库
status: active
tags: [Makefile, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: novel_template
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/hhkarimi/novel_template
created: 2026-07-18
updated: 2026-07-18
no: 1481
category: 二、网文 / 长篇 AI 写作系统 库
repo: hhkarimi/novel_template
stars: 0
url: https://github.com/hhkarimi/novel_template
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# hhkarimi/novel_template

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hhkarimi/novel_template
- **Stars**：0
- **语言**：Makefile
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Template for writing novels using open-source tooling. Inspired by Scrivener
- **本地描述**：Template for writing novels using open-source tooling. Inspired by Scrivener
- **拉取时间**：2026-07-23 23:22:17

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Book template

Inspired by Scrivener, this repo is a workflow that uses open source tools to write and compile large documents, such as books for creative writing or technical documents. The directory structure *is* the organizational structure, and can be modified as desired. Note that the `Makefile` only searches directory `chapter/` for an ordered list of markdown (`.md`) files to include in book compilation.

## Usage

1. Clone the repo to your machine with `git clone {link}`.
2. write story in chapters
3. add front matter
4. Locally compile the book by running `make all`. Refer to `Makefile`

Note that files in `characters/`, `events/` and `research/` will not affect book compilation, only markdown files--that is with extension `.md`--will be included in the book compilation.

## Directory structure

```shell
novel_project
├── build
│   └── novel_project.epub
├── chapters
│   └── chapter_01.md
│   └── ...
└───characters
│   ├── Agathon.md
│   └── Brutus.md
└───events
│   │   some_cool_event.md
│   │   some_sad_event.md
│   │   some_narrative_changing_event.md
└───research
│   │   ancient_greek_breakfast.md
│   │   ancient_roman_consulate.md
│   └── important_dates.md
├── front_matter
├── research
├── Makefile
├── README.md
└── metadata.yaml
```

## Build

Run:

```shell
make all
```
