---
id: tool-05064
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: linkedin_slop_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/tah00r/linkedin_slop_detector
created: 2026-07-18
updated: 2026-07-18
no: 5064
category: 一、去 AI 味 / Humanizer 库
repo: TaH00R/linkedin_slop_detector
stars: 1
url: https://github.com/tah00r/linkedin_slop_detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# TaH00R/linkedin_slop_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/tah00r/linkedin_slop_detector
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Simple tool that scores a LinkedIn post and finds out AI Slop score
- **本地描述**：Simple tool that scores a LinkedIn post and finds out AI Slop score
- **拉取时间**：2026-07-25 18:04:44

---

# AI-SLOP

AI-SLOP is a Chrome extension that analyzes LinkedIn posts and estimates how likely they are to have been generated using AI-style writing patterns.

Instead of looking for topics, AI-SLOP looks for common patterns often found in AI-generated LinkedIn content:

* Generic life lessons
* GPT-style phrasing
* Engagement bait
* Corporate buzzwords
* Storytelling templates
* Startup pitch-deck structures
* Excessive formatting
* Emoji overload

Posts are classified into categories ranging from **Likely Human** to **Very Likely AI**, along with a confidence score and explanation of detected signals.

---

## Features

* Real-time LinkedIn post analysis
* AI likelihood score (0-100%)
* Confidence labels
* Detailed reasoning panel
* Dynamic feed support using MutationObserver
* Runs entirely in the browser
* No APIs
* No backend
* No data collection

---

## How It Works

AI-SLOP scans LinkedIn posts and runs them through multiple detectors.

Examples include:

* AI phrase detection
* Engagement bait detection
* Corporate buzzword detection
* Story-pattern detection
* Formatting analysis
* Emoji analysis
* Structural template detection

The results are combined into a final AI-likelihood score.

Example:

```text
🔴 Very Likely AI (87%)

Detected Signals:
• 3 AI-style phrases detected
• 2 story patterns detected
• 4 buzzwords detected
• AI-style section headers detected
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/TaH00R/linkedin_slop_detector.git
cd linkedin_slop_detector
```

### Install dependencies

```bash
npm install
```

### Build the extension

```bash
npm run build
```

### Load into Chrome

1. Open:

```text
chrome://extensions
```

2. Enable **Developer Mode**

3. Click **Load unpacked**

4. Select the project folder

5. Open LinkedIn

6. Refresh the page

---

## Project Structure

```text
src/
├── content/
├── data/
├── detectors/
├── options/
├── popup/
├── scoring/
├── storage/
├── styles/
├── ui/
└── tests/

dist/
└── content.js
```

---

## Disclaimer

AI-SLOP does not determine with certainty whether a post was written by AI.

It estimates the likelihood that a post contains writing patterns commonly associated with AI-generated content.

False positives and false negatives are expected.

---

## Why?

Because sometimes you scroll LinkedIn and wonder:

> "Did a person write this, or did ChatGPT clock in for another shift?"

AI-SLOP attempts to answer that question.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

MIT License
