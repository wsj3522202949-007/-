---
id: tool-05353
type: tool
area: 库
status: active
tags: [去AI味, CSS, 协议宽松, 需API密钥, 英文文档]
title: wraith
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/quantumsenpai/wraith
created: 2026-07-18
updated: 2026-07-18
no: 5353
category: 一、去 AI 味 / Humanizer 库
repo: QuantumSenpai/wraith
stars: 0
url: https://github.com/quantumsenpai/wraith
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: d1ee5fa6189c2388
  - methods/改稿润色指令库.md
---

# QuantumSenpai/wraith

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/quantumsenpai/wraith
- **Stars**：0
- **语言**：CSS
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI text humanizer — make AI writing undetectable. Built with Groq LLM + Vercel serverless. Liquid glass UI.
- **本地描述**：AI text humanizer — make AI writing undetectable. Built with Groq LLM + Vercel serverless. Liquid glass UI.
- **拉取时间**：2026-07-25 18:15:27

---

<div align="center">

# ⊗ WRAITH

### *Write. Rewrite. Avoid The Hunt.*

**AI text humanizer that makes AI-generated writing undetectable.**

[![Live Demo](https://img.shields.io/badge/Live_Demo-wraith--human.vercel.app-3b82f6?style=for-the-badge&logo=vercel&logoColor=white)](https://wraith-human.vercel.app/)
[![Made with Groq](https://img.shields.io/badge/Powered_by-Groq_LLM-06b6d4?style=for-the-badge)](https://groq.com)
[![Deploy](https://img.shields.io/badge/Deployed_on-Vercel-black?style=for-the-badge&logo=vercel)](https://vercel.com)
![Free](https://img.shields.io/badge/100%25-FREE-4ade80?style=for-the-badge)

<br/>

![WRAITH Banner](https://img.shields.io/badge/⊗_WRAITH-Liquid_Glass_UI-3b82f6?style=flat-square&labelColor=080c12&color=3b82f6)

</div>

---

## ✦ What is WRAITH?

WRAITH is a free AI text humanizer that rewrites AI-generated content to sound completely human. It reduces AI detection scores on tools like GPTZero, ZeroGPT, Quillbot Detector and more.

> **Paste AI text → Pick tone → Get human-sounding output**

No login. No credit card. No limits on personal use.

---

## ⚡ Features

| Feature | Details |
|---------|---------|
| 🧠 **LLM Backend** | Groq `llama-3.3-70b-versatile` — blazing fast |
| 🎨 **Liquid Glass UI** | Apple-style glassmorphism with blue accent |
| 🎭 **4 Tone Modes** | Academic · Casual · Mixed · Creative |
| 💪 **3 Strength Levels** | Light · Standard · Aggressive |
| 📊 **Score Meters** | AI score (before) + Human score (after) |
| 📋 **Copy & Download** | One-click copy or save as `.txt` |
| ⌨️ **Keyboard Shortcut** | `Ctrl + Enter` to humanize instantly |
| 🔐 **Key Hidden** | API key stored as Vercel env variable — never exposed |
| 📱 **Responsive** | Works on mobile and desktop |
| 🆓 **100% Free** | No login, no paywall |

---

## 🎯 Which Tone to Use?

| Tone | Best For | Detection Score |
|------|----------|-----------------|
| **Academic** | University assignments, reports | Medium reduction |
| **Casual** | Social media, blogs, messages | High reduction |
| **Mixed** ⭐ | General purpose — best balance | High reduction |
| **Creative** | Stories, essays, personal writing | Medium reduction |

> **Pro tip:** Use **Aggressive + Mixed** for best results across all checkers.

---

## 🔍 Where to Check Your Output

| Checker | Strictness | Expected Score After WRAITH |
|---------|------------|----------------------------|
| [ZeroGPT](https://zerogpt.com) | 🟢 Lenient | 20–40% |
| [Quillbot Detector](https://quillbot.com/ai-content-detector) | 🟢 Lenient | 25–45% |
| [GPTZero](https://gptzero.me) | 🟡 Medium | 40–55% |
| [Copyleaks](https://copyleaks.com) | 🟡 Medium | 35–55% |
| [Winston AI](https://gowinston.ai) | 🔴 Strict | 45–65% |
| [Turnitin](https://turnitin.com) | 🔴 Strictest | Varies |

> **Honest disclaimer:** WRAITH can reduce scores to **35–50%** on most checkers. Getting to absolute 0% is not possible with any free tool. For best results, make 2–3 manual edits after humanizing.

---

## 🛠️ Tech Stack

```
Frontend        →  HTML · CSS · Vanilla JS
UI Style        →  Liquid Glassmorphism · Blue Accent
LLM             →  Groq API (llama-3.3-70b-versatile)
Backend         →  Vercel Serverless Function (Node.js)
Deployment      →  Vercel
Fonts           →  Syne · DM Sans · JetBrains Mono
```

---

## 📁 Project Structure

```
wraith/
├── index.html          # Main UI
├── style.css           # Liquid glass styling
├── script.js           # Frontend logic + API calls
├── vercel.json         # Vercel routing config
└── api/
    └── humanize.js     # Serverless function (hides API key)
```

---

## 🚀 Self-Host / Deploy Your Own

### 1. Clone the repo
```bash
git clone https://github.com/QuantumSenpai/wraith.git
cd wraith
```

### 2. Get a free Groq API key
- Go to [console.groq.com](https://console.groq.com)
- Sign up (no credit card needed)
- Create an API key

### 3. Deploy to Vercel
```bash
npm i -g vercel
vercel
```

### 4. Add environment variable
In Vercel dashboard → Settings → Environment Variables:
```
GROQ_KEY = your_groq_api_key_here
```

### 5. Redeploy
```bash
vercel --prod
```

Your own WRAITH instance is live! 🔥

---

## ⚠️ Disclaimer

WRAITH is built for **legitimate use cases** — rewriting your own content, improving readability, learning about NLP and AI writing patterns. Use responsibly.

---

## 👤 Built by

**Krishnendu Adak (Kisu)**
- GitHub: [@QuantumSenpai](https://github.com/QuantumSenpai)
- LinkedIn: [krishnendu158](https://linkedin.com/in/krishnendu158)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<div align="center">

**⊗ WRAITH** — *Making AI writing human, one sentence at a time.*

![visitors](https://img.shields.io/badge/dynamic/json?color=3b82f6&label=visits&query=value&url=https://api.countapi.xyz/hit/wraith-human/visits&style=flat-square)

</div>
