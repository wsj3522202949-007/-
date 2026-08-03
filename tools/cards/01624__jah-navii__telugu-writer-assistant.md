---
id: tool-01624
type: tool
area: 库
status: active
tags: [校对, HTML, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: telugu-writer-assistant
summary: 错别字/语法/风格校对
source: https://github.com/jah-navii/telugu-writer-assistant
created: 2026-07-18
updated: 2026-07-18
no: 1624
category: 二、网文 / 长篇 AI 写作系统 库
repo: jah-navii/telugu-writer-assistant
stars: 0
url: https://github.com/jah-navii/telugu-writer-assistant
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# jah-navii/telugu-writer-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jah-navii/telugu-writer-assistant
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：NLP Project - telugu document writer assistant. A grammarly/doc type tool for telugu writing.
- **本地描述**：NLP Project - telugu document writer assistant. A grammarly/doc type tool for telugu writing.
- **拉取时间**：2026-07-23 23:26:23

---

# Telugu Grammar Checker

A rule-based NLP system that detects grammatical errors in **Telugu sentences** — including subject–verb agreement, tense consistency, and double negations.

---

## Features

- Detects **grammar inconsistencies** using linguistic rules  
- Combines **Stanza** (for POS tagging & dependency parsing) with **custom rules**  
- Checks for:
  - Subject–verb agreement  
  - Tense consistency  
  - gender mismatch
  - Case/postposition errors  
  - Negation conflicts

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## How to Run

Ensure dependencies are installed and the Stanza Telugu model is downloaded.

Open the Jupyter notebook telugu_grammar_checker.ipynb

Execute the cells or script.

Provide a Telugu sentence in the last cell

The system prints whether the sentence is correct or lists grammar error(s) with explanations.


## Example Outputs

✓ Sentence Correct: నేను ఆపిల్ తిన్నాను

✖ Sentence: నేను ఆపిల్ తిన్నాము
 - Subject–verb number mismatch (నేను vs తిన్నాము)

✓ Sentence Correct: మేము ఆపిల్ తిన్నాము

✓ Sentence Correct: వారు వస్తున్నారు

✖ Sentence: ఆమె తిన్నాడు
 - Gender disagreement between ఆమె and తిన్నాడు

✓ Sentence Correct: ఆపిల్ ను తినాను

✖ Sentence: నేను తినలేదు లేదు
 - Double negatives: తినలేదు లేదు
