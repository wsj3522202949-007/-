---
id: tool-05580
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议传染, 本地优先, 英文文档, 本地写作]
title: humanize
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/rithulkamesh/humanize
created: 2026-07-18
updated: 2026-07-18
no: 5580
category: 一、去 AI 味 / Humanizer 库
repo: rithulkamesh/humanize
stars: 1
url: https://github.com/rithulkamesh/humanize
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# rithulkamesh/humanize

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rithulkamesh/humanize
- **Stars**：1
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：humanization, nlp, text-processing, writing-style
- **GitHub 描述**：An open-source, rule-based system for humanizing text using open datasets and deterministic transformations.
- **本地描述**：An open-source, rule-based system for humanizing text using open datasets and deterministic transformations.
- **拉取时间**：2026-07-25 18:23:57

---

Humanize
========

**An open-source, rule-based system for humanizing text using open datasets and deterministic transformations.**

Humanize is a small, transparent toolkit for improving the naturalness of text that feels overly rigid or machine-like.

It does not generate new content.
It does not depend on hosted AI services.
It does not require an internet connection.

Instead, it works by applying simple, inspectable transformations informed by open, human-written reference data.

Why this exists
---------------

Many tools that claim to “humanize” text rely on large language models running behind closed APIs.
They are expensive, opaque, and difficult to reason about.

Humanize takes a different path.

Human writing has measurable structure:
sentence length varies,
punctuation creates pauses,
perfect symmetry is rare,
and slight irregularity often reads as more natural than polish.

These properties can be modeled and applied deterministically, without guessing or generation.

What Humanize does
------------------

- Accepts a block of text as input
- Analyzes structural features such as sentence length and rhythm
- Compares them against open reference examples of human writing
- Applies rule-based transformations to adjust flow and pacing
- Outputs revised text while preserving the original meaning

All steps are explicit and reproducible.

What Humanize does not do
-------------------------

- It does not generate text from scratch
- It does not scrape or reuse proprietary content
- It does not require API keys or paid services
- It does not train models on user input
- It does not run background processes or telemetry

Offline-first by design
-----------------------

Humanize is designed to run entirely offline.

Reference data is stored as plain text files.
Transformations are rule-based.
The core pipeline is deterministic.

You should be able to clone the repository, disconnect from the internet, and still use the system end to end.

Open datasets
-------------

Style reference data consists of short, human-written text chunks stored as individual files.
All included data is either user-contributed with consent or released under permissive licenses.

The intent is not to reproduce content, but to capture structural patterns common in human writing.

Contributors retain control over their submissions, and data can be removed upon request.

License
----related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

Humanize is licensed under the **GNU General Public License v3 (GPLv3)**.

This ensures that all distributed modifications and forks remain open source.
The intent is to keep the project transparent, auditable, and freely usable by the community.

If you build on this project, those improvements should remain available to others as well.
