---
id: tool-00362
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: StoryPal
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/yigitcankzl/storypal
created: 2026-07-18
updated: 2026-07-18
no: 362
category: 二、网文 / 长篇 AI 写作系统 库
repo: yigitcankzl/StoryPal
stars: 1
url: https://github.com/yigitcankzl/storypal
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d827f6d8e72ce5d7
  - methods/最强写作方法论_全球最强综合版.md
---

# yigitcankzl/StoryPal

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/yigitcankzl/storypal
- **Stars**：1
- **语言**：JavaScript
- **License**：MIT
- **Topics**：ai, education, groq, hackathon, image-generation, react, text-to-speech, vite
- **GitHub 描述**：AI-powered personalized storybook generator that turns any educational topic into an illustrated, narrated story — with your child as the hero.
- **本地描述**：AI-powered personalized storybook generator that turns any educational topic into an illustrated, narrated story — with your child as the hero.
- **拉取时间**：2026-07-23 22:49:40

---

<div align="center">

# StoryPal

### Every Lesson Becomes an Adventure.

[![React](https://img.shields.io/badge/React_18-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vite.dev)
[![Tailwind](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![Groq](https://img.shields.io/badge/Groq_AI-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![Hugging Face](https://img.shields.io/badge/FLUX.1--schnell-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![Framer Motion](https://img.shields.io/badge/Framer_Motion-0055FF?style=for-the-badge&logo=framer&logoColor=white)](https://www.framer.com/motion)

An AI-powered web app that generates personalized, illustrated educational storybooks for children ages 3-12 — with voice narration, fun facts, and interactive quizzes.

**Built for a Hackathon**

</div>

---

## Demo

![StoryPal Demo](assets/demo.gif)

![StoryPal Screenshot 1](https://github.com/yigitcankzl/StoryPal/blob/main/assets/1.png)
![StoryPal Screenshot 2](https://github.com/yigitcankzl/StoryPal/blob/main/assets/2.png)

## The Problem

Children learn best through stories, but **personalized** educational content is expensive and hard to find. Generic storybooks don't adapt to a child's age, interests, or the specific topic a parent or teacher wants to teach. Meanwhile, children between ages 3-12 are at the most critical stage of learning — and making education feel like play is key to retention.

## Our Solution

StoryPal lets any parent, teacher, or caregiver create a fully personalized illustrated storybook in under a minute. The child becomes the main character, a companion animal joins the journey, and three AI systems work together to write, illustrate, and narrate the story. 35+ curated topics or unlimited custom topics. No accounts, no subscriptions.

## Features

- **Your Child Is the Hero** — Name, age-appropriate language, and optional companion animal woven into every page
- **35+ Curated Topics** — Science, health, emotions, life skills, history — organized by category
- **Write Any Topic** — Free text input for unlimited custom topics
- **AI Illustrations** — Unique watercolor-style children's book art for every page via FLUX.1-schnell
- **Voice Narration** — Client-side Kokoro TTS reads the story aloud, no server needed
- **Fun Fact Boxes** — Every page includes a "Did you know?" fact to deepen learning
- **Interactive Quiz** — End-of-story multiple-choice quiz with animated feedback
- **3 Story Tones** — Adventure Quest, Curiosity Explorer, or Fun & Silly
- **PDF Export** — Download a printable storybook with cover page and illustrations
- **Story Library** — Save stories to localStorage and re-read anytime
- **Surprise Me!** — Random topic picker for spontaneous learning adventures
- **Fully Responsive** — Works on mobile, tablet, and desktop with touch/swipe support

## Built With

<div align="center">

### Frontend

[![React](https://img.shields.io/badge/React_18-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vite.dev)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![shadcn/ui](https://img.shields.io/badge/shadcn/ui-000000?style=for-the-badge&logo=shadcnui&logoColor=white)](https://ui.shadcn.com)
[![Framer Motion](https://img.shields.io/badge/Framer_Motion-0055FF?style=for-the-badge&logo=framer&logoColor=white)](https://www.framer.com/motion)
[![React Router](https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=reactrouter&logoColor=white)](https://reactrouter.com)

### AI & Machine Learning

[![Groq](https://img.shields.io/badge/Groq_API-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![LLaMA 3.3](https://img.shields.io/badge/LLaMA_3.3_70B-0467DF?style=for-the-badge&logo=meta&logoColor=white)](https://llama.meta.com)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![FLUX.1](https://img.shields.io/badge/FLUX.1--schnell-333333?style=for-the-badge&logo=blackforestlabs&logoColor=white)](https://huggingface.co/black-forest-labs/FLUX.1-schnell)

### Voice & Export

[![Kokoro TTS](https://img.shields.io/badge/Kokoro--82M_TTS-FF6F00?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX)
[![ONNX](https://img.shields.io/badge/ONNX_Runtime-005CED?style=for-the-badge&logo=onnx&logoColor=white)](https://onnxruntime.ai)
[![jsPDF](https://img.shields.io/badge/jsPDF-EC1C24?style=for-the-badge&logoColor=white)](https://github.com/parallax/jsPDF)

</div>

## Architecture

```
┌──────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Story Form  │────>│  Groq API        │────>│  Story JSON     │
│  Child info  │     │  LLaMA 3.3 70B   │     │  title, pages,  │
│  Topic       │     │  ~3 seconds      │     │  quiz, prompts  │
│  Tone/Pages  │     └──────────────────┘     └────────┬────────┘
└──────────────┘                                       │
                     ┌──────────────────┐              │
                     │  Hugging Face    │<─────────────┤
                     │  FLUX.1-schnell  │  imagePrompts│
                     │  Parallel gen    │              │
                     │  ~15 seconds     │              │
                     └──────────────────┘              │
                     ┌──────────────────┐              │
                     │  Kokoro TTS      │<─────────────┘
                     │  Client-side     │  page text
                     │  82M ONNX model  │
                     │  Zero API cost   │
                     └──────────────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │  Storybook       │
                     │  Viewer          │
                     │  Audio + Images  │
                     │  Fun Facts + Quiz│
                     │  PDF Export      │
                     └──────────────────┘
```

No backend server. Fully client-side. Deployable as a static site.

## Tech Stack

<table>
<tr><td><b>Layer</b></td><td><b>Technology</b></td><td><b>Purpose</b></td></tr>
<tr>
<td>Frontend</td>
<td>

![React](https://img.shields.io/badge/React_18-61DAFB?style=flat-square&logo=react&logoColor=black)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![shadcn/ui](https://img.shields.io/badge/shadcn/ui-000?style=flat-square&logo=shadcnui&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Framer Motion](https://img.shields.io/badge/Framer_Motion-0055FF?style=flat-square&logo=framer&logoColor=white)
![React Router](https://img.shields.io/badge/React_Router-CA4245?style=flat-square&logo=reactrouter&logoColor=white)

</td>
<td>UI components, styling, animations, routing</td>
</tr>
<tr>
<td>Story AI</td>
<td>

![Groq](https://img.shields.io/badge/Groq_API-F55036?style=flat-square&logo=groq&logoColor=white)
![LLaMA](https://img.shields.io/badge/LLaMA_3.3_70B-0467DF?style=flat-square&logo=meta&logoColor=white)

</td>
<td>Age-appropriate story generation with structured JSON output</td>
</tr>
<tr>
<td>Illustrations</td>
<td>

![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![FLUX](https://img.shields.io/badge/FLUX.1--schnell-333?style=flat-square)

</td>
<td>Watercolor children's book illustrations, parallel generation</td>
</tr>
<tr>
<td>Voice</td>
<td>

![Kokoro](https://img.shields.io/badge/Kokoro--82M_TTS-FF6F00?style=flat-square&logo=huggingface&logoColor=white)
![ONNX](https://img.shields.io/badge/ONNX_Runtime-005CED?style=flat-square&logo=onnx&logoColor=white)

</td>
<td>Client-side text-to-speech narration, zero API cost</td>
</tr>
<tr>
<td>Export</td>
<td>

![jsPDF](https://img.shields.io/badge/jsPDF-EC1C24?style=flat-square&logoColor=white)
![html2canvas](https://img.shields.io/badge/html2canvas-333?style=flat-square)

</td>
<td>Downloadable PDF storybook with cover and illustrations</td>
</tr>
</table>

## Quick Start

### Prerequisites

- Node.js 18+
- [Groq API key](https://console.groq.com) (free tier available)
- [Hugging Face API key](https://huggingface.co/settings/tokens) (free tier available)

### Setup

```bash
# Install dependencies
npm install

# Copy environment file and add your API keys
cp .env.example .env

# Start development server
npm run dev
```

### Environment Variables

| Variable | Required | Description |
|---|---|---|
| `VITE_GROQ_API_KEY` | Yes | Groq API key for story generation ([free](https://console.groq.com)) |
| `VITE_HF_API_KEY` | Yes | Hugging Face token for FLUX illustrations ([free](https://huggingface.co/settings/tokens)) |

### Build for Production

```bash
npm run build
```

Output is in `dist/` — deploy to any static host (Vercel, Netlify, GitHub Pages).

## How It Works

| Step | What Happens | Time |
|---|---|---|
| 1. **Child Details** | Enter name, age (3-12), optional companion animal | User input |
| 2. **Pick a Topic** | Browse 35+ curated topics in 5 categories, or write your own | User input |
| 3. **Set Preferences** | Choose story tone and page count (4-8) | User input |
| 4. **Story Generation** | Groq (LLaMA 3.3 70B) writes age-appropriate story with fun facts | ~3 seconds |
| 5. **Illustrations** | FLUX.1-schnell generates watercolor-style art for each page in parallel | ~15 seconds |
| 6. **Voice Narration** | Kokoro TTS (client-side) creates audio for each page | ~1-3s/page |
| 7. **Read & Learn** | Interactive storybook viewer with animations, audio, and fun fact boxes | - |
| 8. **Quiz Time** | Multiple-choice questions test what was learned | - |
| 9. **Export** | Download as PDF or save to story library | - |

## Topic Categories

| Category | Topics | Examples |
|---|---|---|
| Science & Nature | 8 | How do plants grow? What lives in the ocean? |
| Body & Health | 7 | Why do we brush our teeth? How do our eyes see? |
| Emotions & Social Skills | 8 | Making new friends, Dealing with fear |
| Life Skills | 7 | Learning to tell time, Road safety |
| History & Discovery | 5 | How did dinosaurs live? Ancient Egypt |

Plus **unlimited custom topics** — just type what you want to teach.

## Accessibility

StoryPal is designed with children and accessibility in mind:

- **Keyboard navigation** — Arrow keys, spacebar, escape for full storybook control
- **Touch & swipe** — Swipe between pages on mobile and tablet
- **Screen reader support** — ARIA labels, live regions, semantic HTML
- **Large touch targets** — 48px minimum for all interactive elements
- **High contrast** — WCAG AA compliant color palette
- **Age-adaptive content** — Vocabulary and sentence complexity calibrated to child's age

## License

This project is licensed under the MIT License — see the [LICENSE](https://github.com/yigitcankzl/StoryPal/blob/main/LICENSE) file for details.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">

**StoryPal** — Because every child learns best when they're the hero of their own story.

Built by [**yigitcankzl**](https://github.com/yigitcankzl) for a **Hackathon**

</div>
