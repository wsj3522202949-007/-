---
id: tool-05081
type: tool
area: 库
status: active
tags: [HTML, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/muntaha-islam0019/slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5081
category: 一、去 AI 味 / Humanizer 库
repo: Muntaha-Islam0019/slop-detector
stars: 0
url: https://github.com/muntaha-islam0019/slop-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Muntaha-Islam0019/slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/muntaha-islam0019/slop-detector
- **Stars**：0
- **语言**：HTML
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A red-pencil copy desk in your browser. Paste prose, see every AI writing tell underlined and scored.
- **本地描述**：A red-pencil copy desk in your browser. Paste prose, see every AI writing tell underlined and scored.
- **拉取时间**：2026-07-25 18:05:24

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# The Slop Detector

A red-pencil copy desk that runs in your browser. Paste any prose and it underlines every AI writing tell, scores the text on five dimensions, and tells you what to cut.

No build step, no server, no tracking. One HTML file, all the logic runs locally, nothing leaves the page.

## What it catches

- Throat-clearing openers ("Here's the thing", "It turns out")
- Adverb crutches and empty emphasis
- Business jargon ("lean into", "double down", "deep dive")
- Binary contrasts ("not X, it's Y") and negative listing
- False agency, where things act instead of people ("the data tells us")
- Vague declaratives that announce importance without naming it
- Em dashes, Wh- sentence openers, and metronomic rhythm

Red wavy underline means cut it. Blue dotted means look again. Hover any mark for the reason. The scorecard grades you on Directness, Rhythm, Trust, Authenticity, and Density, then stamps a verdict against a 35/50 threshold.

## Use it

Open `index.html` in any browser. That's the whole setup.

It loads with a deliberately awful sample so you can see the pencil work right away. Clear it, paste your own writing, and it re-scans as you type.

### Host it as a live page

Drop the file in a repo named `index.html`, turn on GitHub Pages in Settings, and you get a public link anyone can open on their phone.

## How it works

Plain HTML, CSS, and vanilla JavaScript. No dependencies except Google Fonts for the type. The detector runs phrase lists, word lists, and regex patterns over your text, then measures sentence-length variance to catch metronomic rhythm that the eye misses. The passive-voice and three-item-list checks are heuristics, so they flag candidates rather than certainties. A human still makes the call.

## Credits and license

Built by [Md. Muntaha Islam](https://www.linkedin.com/in/muntaha-islam0019/).

The detection rules are adapted from the stop-slop skill, used under the MIT License. See `[LICENSE](LICENSE)`.
