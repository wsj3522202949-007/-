---
id: tool-00364
type: tool
area: 库
status: active
tags: [大纲规划, HTML, 协议未明, 需API密钥, 英文文档]
title: storyfix
summary: 搭大纲/分卷/节拍
source: https://github.com/android-tipster/storyfix
created: 2026-07-18
updated: 2026-07-18
no: 364
category: 二、网文 / 长篇 AI 写作系统 库
repo: Android-Tipster/storyfix
stars: 0
url: https://github.com/android-tipster/storyfix
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 0be48df30fc5d52b
  - methods/最强写作方法论_全球最强综合版.md
---

# Android-Tipster/storyfix

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/android-tipster/storyfix
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：ai, character-development, claude, creative-writing, developmental-editing, fiction-writing, nanowrimo, plot, story-structure, writing-tools
- **GitHub 描述**：AI fiction troubleshooter for stuck writers. 5 diagnostic tools: plot, character, scene, dialogue, world-building. BYOK.
- **本地描述**：AI fiction troubleshooter for stuck writers. 5 diagnostic tools: plot, character, scene, dialogue, world-building. BYOK.
- **拉取时间**：2026-07-23 22:49:43

---

# StoryFix — AI Fiction Troubleshooter

**[Live App](https://android-tipster.github.io/storyfix/)** | Free to use (bring your own Anthropic API key)

---

StoryFix is a purpose-built diagnostic tool for fiction writers who are stuck. Instead of opening a blank ChatGPT window and hoping for useful feedback, StoryFix asks the right questions and gives you structured editorial analysis — the kind a developmental editor would charge $50-200/hour to provide.

## Five Diagnostic Tools

### 1. Plot Diagnosis
Describe where you're stuck and what feels broken. Get: root cause analysis, the structural reason the problem exists, three concrete fixes ordered from least to most disruptive, a diagnostic question to test your solution, and one common mistake to avoid.

### 2. Character Audit
Paste a character description and the specific problem. Get: core diagnosis, the missing dimension, motivation surgery (want vs. need vs. wound), three concrete fixes, a scene suggestion that would reveal the missing layer, and a red flag about what will cause bigger problems later.

### 3. Scene Rescue
Paste a scene and describe what isn't working. Get: what the scene is actually doing vs. what it should do, three structural notes with quoted examples and specific fixes, line-level observations, what to keep, and the revision question that unlocks the whole thing.

### 4. Dialogue Doctor
Paste a dialogue exchange with character context. Get: subtext audit (where characters say too much or too little), voice distinctiveness analysis, three revision strategies with examples, two modeled line alternatives, and a clear definition of the underlying tension the dialogue should dance around.

### 5. World Consistency
Describe your world's rules and the inconsistency you've found. Get: classification of the problem type, how much readers will notice, three fix approaches with downstream implications, a recommended solution, ripple effects to check elsewhere in the manuscript, and a rule refinement to prevent the problem recurring.

---

## How It Works

- Powered by Claude (Anthropic) — bring your own API key
- Your API key and writing are stored only in your browser's localStorage
- Nothing is sent to any server other than Anthropic's API
- No account required, no signup, no data stored anywhere

Get an API key at [console.anthropic.com](https://console.anthropic.com/settings/keys) — the free tier gives you enough credits for hundreds of diagnoses.

---

## Stack

- 100% vanilla HTML, CSS, JavaScript
- No build step, no dependencies, no backend
- Single `index.html` file
- Hosted on GitHub Pages

---

## Revenue Path

| Tier | Mechanism |
|------|-----------|
| Free (current) | BYOK — user brings Anthropic API key |
| Pro ($8/month) | Hosted key, no API key required |
| Writing Group ($19/month) | 5 seats, shared session history |

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Topics

`fiction-writing`, `creative-writing`, `ai`, `claude`, `story-structure`, `developmental-editing`, `nanowrimo`, `writing-tools`, `plot`, `character-development`
