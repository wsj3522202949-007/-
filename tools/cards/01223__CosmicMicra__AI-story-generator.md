---
id: tool-01223
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/cosmicmicra/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1223
category: 二、网文 / 长篇 AI 写作系统 库
repo: CosmicMicra/AI-story-generator
stars: 1
url: https://github.com/cosmicmicra/ai-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: a3568995b310540c
  - methods/最强写作方法论_全球最强综合版.md
---

# CosmicMicra/AI-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/cosmicmicra/ai-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：ai-stories, child-safety, generative-ai, generative-ai-projects, python, streamlit, tts, whisper
- **GitHub 描述**：Interactive bedtime story application for children aged 5–10, featuring multi-layer safety, AI-powered story generation, and audio narration.
- **本地描述**：Interactive bedtime story application for children aged 5–10, featuring multi-layer safety, AI-powered story generation, and audio narration.
- **拉取时间**：2026-07-23 23:14:45

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=2d1b69,7c3aed,f472b6&height=140&section=header&text=🌙%20Sleepy%20Seeds&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=42&desc=AI-Powered%20Bedtime%20Stories%20·%20Safe%20for%20Children%205–10&descAlignY=65&descColor=e9d5ff&descSize=15"/>

[![Python](https://img.shields.io/badge/Python-3.10-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/GPT--4%20Mini-Story%20Gen-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Whisper](https://img.shields.io/badge/Whisper-Voice%20Input-00b5ad?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/research/whisper)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ed?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

<br/>

> **An interactive bedtime story app for children aged 5–10.**  
> Multi-layer safety · AI story generation · voice input · audio narration · PDF export.

</div>

---

## 📸 Screenshots

**Home — Speak, Choose, or Type your story**
![Sleepy Seeds Home](https://github.com/CosmicMicra/AI-story-generator/blob/main/sleepy_home.png)

**Category Picker — Princess, Animals, Space, Surprise Me! and more**
![Category Picker](https://github.com/CosmicMicra/AI-story-generator/blob/main/sleepy_category.png)

**Generated Story — Read Aloud · Download PDF · New Story**
![Generated Story](https://github.com/CosmicMicra/AI-story-generator/blob/main/sleepy_story.png)

> *Curious what happens when **Cumulus the Cloud** goes looking for the end of the rainbow? 🌈☁️  
> [📄 Download the story to find out!](https://github.com/CosmicMicra/AI-story-generator/blob/main/bedtime_story.pdf)

---

## 🌙 What it does

Sleepy Seeds lets children request a bedtime story by speaking, picking a category, or typing — then generates a calm, age-appropriate, morally positive story using GPT-4 Mini. Every request passes through a **3-layer safety pipeline** before a single word is generated.

```
Child Input (voice 🎙 / category 🧸 / text ⌨️)
        │
        ▼
┌───────────────────┐
│  Safety Sanitizer  │  ← Layer 1: Keyword filter (violence, adult themes, grooming)
└────────┬──────────┘
         ▼
┌───────────────────┐
│ Semantic Analyzer  │  ← Layer 2: Subtle unsafe content detection
└────────┬──────────┘
         ▼
┌───────────────────┐
│    Classifier      │  ← Categorizes & routes request
└────────┬──────────┘
         ▼
┌───────────────────┐
│  Story Generator   │  ← GPT-4 Mini · 300–400 words · temp 0.7
└────────┬──────────┘
         ▼
┌───────────────────┐
│   LLM Judge        │  ← Scores safety + age-appropriateness + quality
│   Score < 7?  ──────→  Refiner improves the story automatically
└────────┬──────────┘
         ▼
  ✅ Safe bedtime story
  🔊 Read Aloud  ·  📄 Download PDF  ·  🔄 New Story
```

---

## ✨ Features

| Feature | Details |
|---|---|
| 🛡 **3-layer safety** | Keyword filter → semantic analysis → LLM judge/refiner |
| 🎙 **Voice input** | Real-time transcription via OpenAI Whisper API |
| 🧸 **Category picker** | Princess · Animals · Cars · Space · Surprise Me! and more |
| 🤖 **AI story generation** | GPT-4 Mini · 300–400 words · calming tone · positive themes |
| 🔊 **Read Aloud** | OpenAI TTS narrates the story |
| 📄 **PDF export** | Download a beautifully formatted story keepsake |
| 🐳 **Docker ready** | One-command containerized deployment |

---

## 🛡 Safety Architecture

**Layer 1 — Keyword Filter**
Catches obvious unsafe content: violence, adult themes, trauma, grooming attempts.

**Layer 2 — Semantic Analysis**
Detects subtle inappropriate content that keywords miss — context-aware filtering.

**Layer 3 — LLM Judge & Refiner**
Scores every story on safety, age-appropriateness, and quality (0–10).
Stories scoring below 7 are automatically refined before delivery.

### Edge Case Handling

| Input | Behavior |
|---|---|
| `"Tell me a story about a princess who loves flowers"` | ✅ Calm bedtime story generated |
| `"Tell me a story about a dragon fighting people"` | ↩️ Redirected to non-violent version |
| `"Harry Potter and the Chamber of Secrets"` | ⚠️ Keyword flagged, context safe → safe story generated |
| `"Keep this secret from parents"` | 🚫 Unsafe intent detected → request ignored, safe story instead |

---

## 🚀 Getting Started

**Option 1 — Run locally**

```bash
git clone https://github.com/CosmicMicra/Story-App-Sleepy-Seeds.git
cd Story-App-Sleepy-Seeds
pip install -r requirements.txt
export OPENAI_API_KEY='your-key-here'
streamlit run app.py
```

**Option 2 — Docker**

```bash
docker build -t sleepy-seeds .
docker run -p 8501:8501 sleepy-seeds
```

App runs at `http://localhost:8501`

---

## 🏗 Project Structure

```
sleepy-seeds/
├── app.py                      # Streamlit frontend
├── main.py                     # Core orchestration
├── styles.css                  # Custom UI styling
├── Dockerfile
├── requirements.txt
├── story/
│   ├── classifier.py           # Request categorization & routing
│   ├── generator.py            # GPT-4 Mini story creation
│   ├── judge.py                # Quality & safety scoring
│   ├── refiner.py              # Story improvement (score < 7)
│   └── sanitizer.py            # Multi-layer safety pipeline
├── audio/
│   ├── transcriber.py          # Whisper voice input
│   └── tts.py                  # Text-to-speech narration
└── utils/
    └── pdf_generator.py        # PDF export
```

---

## 🛠 Tech Stack

<p>
  <img src="https://skillicons.dev/icons?i=python,docker,css&perline=5"/>
</p>

| Component | Technology |
|---|---|
| **Frontend** | Streamlit · custom CSS |
| **Story Generation** | GPT-4 Mini (OpenAI) |
| **Voice Input** | OpenAI Whisper API |
| **Audio Narration** | OpenAI TTS |
| **Safety Pipeline** | Keyword filter · semantic analysis · LLM judge/refiner |
| **PDF Export** | pdf_generator.py |
| **Deployment** | Docker |

---

## 🌟 Future Enhancements

- 👤 **Personalized story profiles** — remember each child's favorite characters and themes
- 🎨 **DALL·E integration** — generate 2–3 illustrations per story
- 👨‍👩‍👧 **Parents dashboard** — monitor usage and story preferences

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 👩‍💻 Author

**Soniya Phaltane** · [@CosmicMicra](https://github.com/CosmicMicra)  
ML Engineer · AI Security · [soniyaphaltane-portfolio.netlify.app](https://soniyaphaltane-portfolio.netlify.app)

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=2d1b69,7c3aed,f472b6&height=80&section=footer"/>
</div>
