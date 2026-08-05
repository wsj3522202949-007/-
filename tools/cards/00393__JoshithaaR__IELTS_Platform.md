---
id: tool-00393
type: tool
area: 库
status: active
tags: [多Agent, TTS, 校对, TypeScript, 协议未明, 需API密钥, 英文文档, 改稿润色]
title: IELTS_Platform
summary: 多 Agent 协作自动产文
source: https://github.com/joshithaar/ielts_platform
created: 2026-07-18
updated: 2026-07-18
no: 393
category: 二、网文 / 长篇 AI 写作系统 库
repo: JoshithaaR/IELTS_Platform
stars: 0
url: https://github.com/joshithaar/ielts_platform
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# JoshithaaR/IELTS_Platform

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/joshithaar/ielts_platform
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI IELTS Copilot: A production-grade, AI-powered platform for mastering the IELTS exam. Features comprehensive evaluation across Speaking, Writing, Reading, and Listening modules using advanced LLMs (Groq) for near real-time, multi-dimensional feedback and custom study plans.
- **本地描述**：AI IELTS Copilot: A production-grade, AI-powered platform for mastering the IELTS exam. Features comprehensive evaluation across Speaking, Writing, Reading, and Listening modules using advanced LLMs (Groq) for near real-time, multi-dimensional feedback and custom study plans.
- **拉取时间**：2026-07-23 22:50:36

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI IELTS Copilot

**AI IELTS Copilot** is a state-of-the-art, cost-effective IELTS training ecosystem built with Next.js 14. Designed to simulate the real exam experience, the platform acts as a relentless, intelligent language tutor. It leverages high-speed Large Language Models (via APIs) to evaluate and grade a candidate's proficiency across all four core IELTS skills.

## ✨ Key Features

- 🎙️ **Speaking Module**: Interactive voice recording using Native Web Speech API for real-time transcription and automatic band evaluation (Fluency, Lexical Resource, Grammar).
- ✍️ **Writing Examiner**: Granular, line-by-line AI critique of Task 1 and Task 2 essays.
- 🎧 **Reading & Listening**: Simulated full mock test environments mapped accurately to real IELTS conditions.
- 🧠 **Multi-Agent Architecture**: 
  - **Examiner Agent**: Grades the candidate.
  - **Feedback Agent**: Identifies behavioral blockers and specific mistakes.
  - **Planner Agent**: Constructs a tailored 7-day study plan based on the user's explicit weaknesses.
- 💾 **Local Progress Tracking**: Built-in visual dashboard ensuring students can track continuous score improvements over time natively in their browser.

## 🛠️ Tech Stack

- **Frontend**: [Next.js 14](https://nextjs.org/) (App Router), React 18, Tailwind CSS, Lucide React
- **Voice/Audio**: Native Browser Web Speech API (`SpeechRecognition`)
- **AI Integration**: Designed to plug into fast inference APIs (like Groq) using the standard OpenAI SDK format.

## 🚀 Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites

- Node.js (v18 or higher recommended)
- npm or yarn

### Installation 

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <your-repository-url>
   cd IELTS
   ```

2. **Install dependencies**:
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Set up environment variables**:
   Create a `.env.local` file in the root directory and add your necessary API keys (e.g., your Groq API key or OpenAI API key, depending on your setup).
   ```env
   # Example
   GROQ_API_KEY=your_groq_api_key_here
   # or
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Start the development server**:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

5. **Open the app**:
   Navigate to [http://localhost:3000](http://localhost:3000) in your web browser to see the application in action.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

## 📝 License

This project is licensed under the `[MIT License](LICENSE)`.
