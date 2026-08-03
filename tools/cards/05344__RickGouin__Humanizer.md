---
id: tool-05344
type: tool
area: 库
status: active
tags: [PHP, 协议传染, 本地优先, 英文文档, 去AI味, 本地写作]
title: Humanizer
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/rickgouin/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5344
category: 一、去 AI 味 / Humanizer 库
repo: RickGouin/Humanizer
stars: 0
url: https://github.com/rickgouin/humanizer
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# RickGouin/Humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rickgouin/humanizer
- **Stars**：0
- **语言**：PHP
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：Web based tool to make LLM generated text feel more like a person wrote it.
- **本地描述**：Web based tool to make LLM generated text feel more like a person wrote it.
- **拉取时间**：2026-07-25 18:15:07

---

# Humanizer

A lightweight, browser-based text transformation tool built with PHP, HTML, CSS, and vanilla JavaScript.  
Rewrites user-submitted text using configurable linguistic patterns to make writing sound more natural, conversational, and human.

---

## Features

- Pattern-based word and phrase replacements  
  - e.g. “kind of” becomes “kinda” and “in practice” becomes “in real life”
- Optional conversational sentence prefixes  
  - e.g. “Honestly,”, “To be honest,”, “In my experience,”
- Simple, fast, no-dependencies frontend
- Copy-to-clipboard support with graceful fallback
- Fully configurable transformation rules

---

## What the script detects and updates

- Dash Overuse & Dash Style
Detects excessive em dashes and hyphen breaks common in AI-generated text and converts them into commas, periods, or parentheses when appropriate, while preserving valid hyphenated terms, dates, versions, and identifiers.
- Unnatural Sentence Breaks
Identifies dash-based interruptions within sentences and restructures them into smoother, more natural sentence flows that read like human-written prose.
- Remove Certain Words
Removes or replaces words identified by this study as being common indicators of AI generated text.
- Contraction Opportunities
Converts formal phrase pairs (such as “do not” or “it is”) into natural contractions (“don’t,” “it’s”) in casual contexts, while avoiding sentence starts and protected content.
- Overly Formal or Generic Phrasing
Replaces stiff, vague, or AI-heavy wording with clearer, more natural alternatives based on the selected writing persona.
- Repetitive Sentence Openers
Detects repetitive or robotic sentence beginnings and occasionally inserts natural human-style lead-ins, with strict limits to prevent overuse.
- Missing Human Qualifiers (Hedges)
In academic or formal writing, selectively adds cautious qualifiers such as “to some extent” or “in many cases” to better reflect human reasoning and uncertainty.
- Technical Context Signals
In technical personas, inserts real-world framing phrases like “In practice” or “Under the hood” to signal hands-on experience rather than abstract explanation.
- Overuse of Intensifiers
Removes or softens vague intensifiers such as “really,” “very,” and “quite” when they reduce clarity, precision, or professionalism.
- Sales & Marketing Flatness
In marketing mode, detects benefit-light language and may add a single outcome-focused sentence to emphasize value, while avoiding repetitive or overly promotional phrasing.
- Spacing & Punctuation Noise
Cleans up extra spaces, awkward punctuation spacing, and duplicated commas that commonly appear after automated text generation or editing.

---

## How It Works

1. Users paste text into the input field
2. PHP processes the text using a rule system:
   - Regex-based replacements
   - Sentence-level transformations
3. The transformed output is displayed instantly
4. JavaScript enables one-click copying of results

All transformations are deterministic and rule-based — **no APIs, no external services, no tracking**.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Tech Stack

- **PHP** – server-side text processing
- **HTML/CSS** – UI structure and styling
- **Vanilla JavaScript** – clipboard handling and UI feedback
