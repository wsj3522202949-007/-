---
id: tool-01612
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: hey-jules
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/juleskid5102/hey-jules
created: 2026-07-18
updated: 2026-07-18
no: 1612
category: 二、网文 / 长篇 AI 写作系统 库
repo: juleskid5102/hey-jules
stars: 1
url: https://github.com/juleskid5102/hey-jules
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# juleskid5102/hey-jules

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/juleskid5102/hey-jules
- **Stars**：1
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI writing copilot that rewrites your text in any tone — right inside your browser. Free & open source.
- **本地描述**：AI writing copilot that rewrites your text in any tone — right inside your browser. Free & open source.
- **拉取时间**：2026-07-23 23:26:04

---

<div align="center">

# ✨ Hey Jules

### Your AI Writing Copilot — Right Inside Your Browser

**Highlight any text. Pick a tone. Let Jules rewrite it instantly.**

[Install on Chrome](https://chrome.google.com/webstore/detail/hey-jules) · `[Report Bug](../../issues)` · `[Request Feature](../../issues)`

---

![Hey Jules Demo](https://img.shields.io/badge/version-0.1.5-purple?style=for-the-badge)
![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-blue?style=for-the-badge&logo=googlechrome)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Free](https://img.shields.io/badge/price-FREE-brightgreen?style=for-the-badge)

</div>

---

## 😩 The Problem

We all do it. Every day.

> *"Is this message too harsh?"*
>
> *"Does this sound professional enough?"*
>
> *"Should I rewrite it one more time?"*

You know what you want to say — you just can't find the right words.

## ✨ The Solution

**Hey Jules** lives inside your browser. Select any text, pick a tone, and your message is instantly rewritten — right where you typed it. No copy-pasting. No switching tabs.

## 🎯 How It Works

```
1. Type anything in any text field on any website
2. Select / highlight the text
3. Click the ✨ icon that appears (or press Alt+J)
4. Pick a tone
5. Done — text is replaced instantly
```

## 🎨 6 Tones for Every Situation

| Tone | When to use | Example |
|------|-------------|---------|
| 💼 **Professional** | Emails to your boss | *"send me that file asap"* → *"Could you please send me that file at your earliest convenience?"* |
| 😊 **Friendly** | Chat with coworkers | *"Send me the report"* → *"Hey, could you send me the report when you get a chance? 😊"* |
| 😂 **Funny** | Social posts, casual chats | *"Meeting at 3pm"* → *"3pm meeting today — last one there buys coffee for the team 😅"* |
| ⚡ **Gen Z** | Social media, friends | *"This place has great food"* → *"this place is giving ELITE no cap 🔥 the food slaps fr ✨"* |
| 🕊️ **Softer** | Feedback, tough messages | *"This is all wrong, redo it"* → *"I think this could use a few adjustments — mind taking another look?"* |
| ✂️ **Shorter** | Long texts, TL;DR | Condenses to 40-60% while keeping all key info |

## 🌐 Works Everywhere

<div align="center">

**Facebook** · **Messenger** · **Gmail** · **LinkedIn** · **Slack** · **Notion** · **Twitter/X** · **ChatGPT** · **Google Docs**

*...and every website with a text input field*

</div>

## 🔑 Bring Your Own Key (BYOK)

Hey Jules uses **your own AI API key** — we never see or store it on any server. Choose your provider:

| Provider | Model | Get API Key |
|----------|-------|-------------|
| **Groq** ⭐ | Llama 3.3 70B | [console.groq.com/keys](https://console.groq.com/keys) |
| **Google Gemini** | Gemini 2.0 Flash | [aistudio.google.com](https://aistudio.google.com/apikey) |
| **OpenAI** | GPT-4o Mini | [platform.openai.com](https://platform.openai.com/api-keys) |
| **Anthropic** | Claude 3.5 Haiku | [console.anthropic.com](https://console.anthropic.com/) |
| **xAI** | Grok | [console.x.ai](https://console.x.ai/) |

> 💡 **Recommended:** Groq — blazing fast inference, free API key, great quality.

## 🚀 Quick Start

### Option 1: Download Release (Recommended)
1. Download the latest ZIP from [**Releases**](https://github.com/juleskid5102/hey-jules/releases/latest)
2. Unzip the file
3. Open `chrome://extensions/` → enable **Developer Mode** (top right)
4. Click **Load unpacked** → select the unzipped folder
5. Pin Hey Jules to your toolbar
6. Click the icon → enter your API key → start writing!

### Option 2: Build from Source
```bash
git clone https://github.com/juleskid5102/hey-jules.git
cd hey-jules
npm install
npm run build
```
Then load `build/chrome-mv3-prod/` as unpacked extension (same steps as above).

### Option 3: Chrome Web Store (Coming Soon)
> ⏳ Star this repo to get notified when it's live!

## 🏗️ Tech Stack

| Tech | Purpose |
|------|---------|
| [Plasmo](https://plasmo.com) | Chrome Extension framework |
| React 18 | UI components |
| TypeScript | Type safety |
| Direct REST API | AI calls (no SDK bloat) |

## 🤝 Contributing

Contributions are welcome! Whether it's:
- 🐛 Bug reports
- 💡 Feature requests
- 🌍 New tone ideas
- 🔧 Pull requests

Feel free to `[open an issue](../../issues)` or submit a PR.

## 📊 Comparison

| Feature | Hey Jules | Others |
|---------|-----------|--------|
| Inline replace (no copy-paste) | ✅ | ❌ |
| Fun tones (Funny, Gen Z) | ✅ | ❌ |
| BYOK (your own API key) | ✅ | ❌ |
| Works on every website | ✅ | ⚠️ |
| Free forever | ✅ | ❌ |
| Bilingual (Vietnamese + English) | ✅ | ❌ |

## ⭐ Star History

If Hey Jules saves you from one awkward message, consider giving it a ⭐!

## 📜 License

MIT — Free to use, modify, and distribute.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">

**Made with 💜 by [JulesX](https://github.com/juleskid5102)**

*"The editor in your head that you always wished you had."*

</div>
