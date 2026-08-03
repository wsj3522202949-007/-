---
id: tool-00037
type: tool
area: 库
status: active
tags: [TTS, TypeScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: dialogue-consistency-checker
summary: 小说转语音/有声书
source: https://github.com/aashisho1o1/dialogue-consistency-checker
created: 2026-07-18
updated: 2026-07-18
no: 37
category: 二、网文 / 长篇 AI 写作系统 库
repo: Aashisho1o1/dialogue-consistency-checker
stars: 0
url: https://github.com/aashisho1o1/dialogue-consistency-checker
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Aashisho1o1/dialogue-consistency-checker

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/aashisho1o1/dialogue-consistency-checker
- **Stars**：0
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-powered character voice analysis for fiction writers using Chrome Built-in Prompt API
- **本地描述**：AI-powered character voice analysis for fiction writers using Chrome Built-in Prompt API
- **拉取时间**：2026-07-23 22:39:57

---

# Dialogue Consistency Checker

**AI-Powered Character Voice Analysis for Fiction Writers**

Built for the [Google Chrome Built-in AI Challenge 2025](https://googlechromeai.devpost.com/)

## 🎯 Problem Statement

Fiction writers struggle to maintain consistent character voices across long manuscripts. A character who speaks formally in Chapter 1 might inexplicably use modern slang in Chapter 10. These inconsistencies break reader immersion and damage story quality.

Current solutions require:
- Manual review (time-consuming, error-prone)
- Expensive cloud AI services (privacy concerns, cost barriers)
- External tools that don't integrate with writing workflow

## ✨ Solution

**Dialogue Consistency Checker** provides **real-time, on-device character voice analysis** using Chrome's Built-in AI. It:

1. **Analyzes dialogue** as you write
2. **Detects inconsistencies** in character speech patterns
3. **Shows red wavy underlines** on problematic dialogue
4. **Provides explanations** on hover
5. **Learns character voices** over time

### Key Innovation
**100% client-side processing** using Chrome's Prompt API means:
- ✅ **Privacy-first**: Your manuscript never leaves your browser
- ✅ **Cost-free**: No API bills or subscriptions
- ✅ **Works offline**: No internet needed after initial load
- ✅ **Instant feedback**: No cloud latency

## 🚀 Features

### Core Functionality
- **Smart Dialogue Detection**: Automatically identifies character dialogue
- **Voice Pattern Analysis**: Detects formality, vocabulary, tone inconsistencies
- **Visual Feedback**: Red wavy underlines (like Grammarly for character voices)
- **Confidence Levels**: High (red), Medium (orange), Low (green) markers
- **Hover Explanations**: Detailed reasons for each inconsistency
- **Character Profiles**: Builds voice profiles from your text
- **localStorage Persistence**: Remembers characters across sessions

### Chrome Built-in AI Integration
- **Prompt API** for dialogue consistency analysis
- **On-device processing** via Gemini Nano
- **Structured JSON outputs** for precise underline placement
- **Conservative flagging** (only high-confidence issues)

## 📋 Requirements

### Chrome Version
- **Chrome 128+** (Dev, Canary, or Beta)
- Built-in AI features must be enabled

### Enable Chrome AI (One-Time Setup)

1. **Download Chrome Dev/Canary**
   - [Chrome Dev](https://www.google.com/chrome/dev/)
   - [Chrome Canary](https://www.google.com/chrome/canary/)

2. **Enable AI Features**
   Visit: chrome://flags/#prompt-api-for-gemini-nano
   Set to "Enabled" and restart Chrome

3. **Verify Installation**
   Open DevTools Console and run:
   ```javascript
   await ai.languageModel.capabilities()
   // Should return: { available: "readily" }
   ```

## 🛠️ Installation & Usage

### Quick Start

```bash
# Clone repository
git clone https://github.com/Aashisho1o1/Owen.git
cd Owen
git checkout main-GoogleOct31
cd chrome-ai-dialogue-checker

# Install dependencies
npm install

# Run development server
npm run dev

# Open in Chrome Dev/Canary
# Visit http://localhost:5173
```

### Using the App

1. **Paste dialogue** into the editor (or click "Load Demo Text")
2. **Click "Analyze Dialogue"** button
3. **Wait 10-30 seconds** for Chrome AI to process
4. **Red wavy underlines appear** on inconsistencies
5. **Hover over underlines** to see explanations

## 🏆 Competition Fit

**Category**: Best Hybrid AI Application ($9,000)

**Chrome AI APIs Used**:
- ✅ Prompt API (window.ai.languageModel)

**Judging Criteria Alignment**:
- **Functionality**: Scalable to any language, any genre, any writer
- **Purpose**: Solves real pain point for 50,000+ fiction writers
- **Content**: Creative use of Chrome AI for novel writing assistance
- **User Experience**: Simple, intuitive, Grammarly-like UX
- **Technical Execution**: Extensive Chrome AI integration with structured outputs

## 📄 License

MIT License

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Built with ❤️ using Chrome Built-in AI • Privacy-First • Cost-Free • Offline-Capable**
