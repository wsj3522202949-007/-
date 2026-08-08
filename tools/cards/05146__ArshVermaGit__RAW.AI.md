---
id: tool-05146
type: tool
area: 库
status: active
tags: [去AI味, TypeScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: RAW.AI
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/arshvermagit/raw.ai
created: 2026-07-18
updated: 2026-07-18
no: 5146
category: 一、去 AI 味 / Humanizer 库
repo: ArshVermaGit/RAW.AI
stars: 30
url: https://github.com/arshvermagit/raw.ai
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 0133747743dbd116
  - methods/改稿润色指令库.md
---

# ArshVermaGit/RAW.AI

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/arshvermagit/raw.ai
- **Stars**：30
- **语言**：TypeScript
- **License**：MIT
- **Topics**：academic-writing, ai-bypass, ai-detection, ai-writing, content-creation, content-generation, edge-functions, gpt-detection, machine-learning, natural-language-processing, nextgen-writing, react, supabase, text-humanization, typescript
- **GitHub 描述**：🎭 Transform AI-generated text into authentic human writing. Bypass GPTZero, Turnitin & all major AI detectors with 99.8% success. React + Supabase + Edge AI. 50+ languages. <3s response time. ⚡
- **本地描述**：🎭 Transform AI-generated text into authentic human writing. Bypass GPTZero, Turnitin & all major AI detectors with 99.8% success. React + Supabase + Edge AI. 50+ languages. <3s response time. ⚡
- **拉取时间**：2026-07-25 18:07:49

---

<div align="center">
  <img src="public/logo.png" alt="RAW.AI Logo" width="120" height="120" />
</div>

# RAW.AI 🚀

![License](https://img.shields.io/github/license/ArshVermaGit/RAW-AI?style=flat-square)
![Build Status](https://img.shields.io/github/actions/workflow/status/ArshVermaGit/RAW-AI/main.yml?style=flat-square)
![Version](https://img.shields.io/github/package-json/v/ArshVermaGit/RAW-AI?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)

> **Bypass AI detection with human-grade rewriting.**  
> Transform your AI-generated content into authentic, undetectable, and engaging text.

---

## 🌟 Introduction

**RAW.AI** is a state-of-the-art platform designed to humanize AI-generated text. Leveraging advanced models (including our proprietary "Ultra Logic" engine), we rewrite content to bypass even the most sophisticated AI detectors while maintaining the original meaning and enhancing readability.

Whether you're a student, professional, or content creator, RAW.AI ensures your voice remains yours—authentic, unique, and undetectable.

## ✨ Key Features

- **🤖 Advanced Humanization**: Convert AI text to human-like quality with a 99.9% detection bypass rate.
- **🛡️ Integrated AI Detector**: Analyze your text against top detectors (GPTZero, Turnitin, etc.) in real-time.
- **✍️ Multiple Writing Modes**:
  - **Standard**: Balanced humanization.
  - **Academic**: Formal and structured for research.
  - **Creative**: Expressive and varied for storytelling.
  - **Business**: Professional and concise.
- **💳 Secure Payments**: Seamless global transactions powered by **Razorpay**.
- **🔒 Enterprise Security**: End-to-end encryption and secure data handling via **Supabase**.
- **📱 Responsive Design**: A pixel-perfect "Hyper-Premium" UI that works on all devices.

## 🛠️ Tech Stack

This project is built with the latest modern web technologies:

- **Frontend**: [React](https://reactjs.org/), [TypeScript](https://www.typescriptlang.org/), [Vite](https://vitejs.dev/)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/), [Shadcn UI](https://ui.shadcn.com/)
- **Animations**: [Framer Motion](https://www.framer.com/motion/)
- **State Management**: [React Query](https://tanstack.com/query/latest)
- **Backend/Auth**: [Supabase](https://supabase.com/)
- **Payments**: [Razorpay](https://razorpay.com/)

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- **Node.js**: v18.0.0 or higher
- **npm**: v9.0.0 or higher
- **Git**

### Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/ArshVermaGit/RAW-AI.git
    cd RAW-AI
    ```

2.  **Install dependencies**

    ```bash
    npm install
    ```

3.  **Set up environment variables**
    Create a `.env` file in the root directory and add your keys (see `.env.example`):

    ```env
    VITE_SUPABASE_URL=your_supabase_url
    VITE_SUPABASE_PUBLISHABLE_KEY=your_supabase_key
    ```

### 3. Launch

```bash
npm run dev
```

---

## 📂 Directory Structure

```text
RAW-AI/
├── .github/               # Issue & Pull Request Templates
├── public/                # Static assets, Sitemap, robots.txt
├── src/
│   ├── components/        # UI System (Shadcn + Custom)
│   ├── contexts/          # State Management (Auth, Usage)
│   ├── hooks/             # Custom Hooks (useAuth, useUsage)
│   ├── pages/             # Route Views (Index, Profile, FAQ)
│   └── lib/               # Utility Tier
├── supabase/              # Migrations & Edge Function logic
└── ...                    # Build & Lint configs
```

---

## 💎 Pricing Tiers

| Plan      | Word Limit | Processing Speed | Best For             |
| :-------- | :--------- | :--------------- | :------------------- |
| **Lite**  | 5,000 /mo  | Instant          | Daily Emails & Posts |
| **Pro**   | 50,000 /mo | Professional     | Articles & Reports   |
| **Ultra** | Unlimited  | Deep             | Academic & Legal     |

---

## 🤝 Governance & Community

We adhere to strict professional and legal standards to maintain the highest quality of service and open-source collaboration.

- **[LICENSE](https://github.com/ArshVermaGit/RAW.AI/blob/main/LICENSE)**: Distributed under the **MIT License**.
- **[ROADMAP](https://github.com/ArshVermaGit/RAW.AI/blob/main/ROADMAP.md)**: Explore our vision for Q2-Q4 2026.
- **[SECURITY](https://github.com/ArshVermaGit/RAW.AI/blob/main/SECURITY.md)**: Responsible disclosure policy and vulnerability reporting.
- **[CODE OF CONDUCT](https://github.com/ArshVermaGit/RAW.AI/blob/main/CODE_OF_CONDUCT.md)**: Our commitment to inclusive and professional participation.
- **[CONTRIBUTING](https://github.com/ArshVermaGit/RAW.AI/blob/main/CONTRIBUTING.md)**: Guidelines for code, documentation, and feature contributions.

---

## ☕ Support the Project

If you find this tool helpful and want to support its development, consider buying me a coffee! Your support helps keep the project alive and free.

<div align="center">
    
<a href="https://www.buymeacoffee.com/ArshVerma">
  <img src="public/buy-me-a-coffee.png" width="200" />
</a>

</div>

## 📱 Connect with Me

I'd love to hear your feedback or discuss potential collaborations!

<div align="center">

[![GitHub](https://skillicons.dev/icons?i=github)](https://github.com/ArshVermaGit)
[![LinkedIn](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/arshvermadev/)
[![Twitter](https://skillicons.dev/icons?i=twitter)](https://x.com/TheArshVerma)
[![Gmail](https://skillicons.dev/icons?i=gmail)](mailto:arshverma.dev@gmail.com)

</div>

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<p align="center">
  Built with ❤️ by <a href="https://github.com/ArshVermaGit">Arsh Verma</a>
</p>
