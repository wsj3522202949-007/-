---
id: tool-04982
type: tool
area: 库
status: active
tags: [去AI味, JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: Humane
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/vishal-muralidharan/humane
created: 2026-07-18
updated: 2026-07-18
no: 4982
category: 一、去 AI 味 / Humanizer 库
repo: vishal-muralidharan/Humane
stars: 0
url: https://github.com/vishal-muralidharan/humane
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: b1ecab266a0958d6
  - methods/改稿润色指令库.md
---

# vishal-muralidharan/Humane

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/vishal-muralidharan/humane
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Humane is a specialized web application built with React and Vercel, engineered to bypass strict enterprise AI detectors by intentionally injecting high perplexity and burstiness. Featuring sophisticated multi-mode text generation and a Firebase admin workbench, it harvests text pairs to train future custom open-weight models.
- **本地描述**：Humane is a specialized web application built with React and Vercel, engineered to bypass strict enterprise AI detectors by intentionally injecting high perplexity and burstiness. Featuring sophisticated multi-mode text generation and a Firebase admin workbench, it harvests text pairs to train future custom open-weight models.
- **拉取时间**：2026-07-25 18:01:49

---

# Humane: AI Text Humanizer

Humane is a specialized web application designed to artificially inject high perplexity and high burstiness into AI-generated text. Built with a minimalist, hacker-vibe aesthetic, this tool utilizes advanced prompt engineering via the Grok API to transform predictable, rhythmic AI text into natural, human-passing content. 

The application also serves as a data collection engine, silently harvesting input-output pairs into a Firebase NoSQL database to build a curated dataset for future open-source model fine-tuning.

---

## 🚀 Core Features & Modes

Humane offers three distinct transformation modes to suit varying content needs:

| Mode | Description | Mechanics |
| :--- | :--- | :--- |
| **Casual** | Basic and least AI detection. | Bannes specific AI words and forces a conversational "coffee-break" tone. |
| **Formal** | More formal tone where a little AI detection is okay. | Balances professional readability with rhythmic structure. |
| **Report** | Needs to be perfect but with humanized words; higher AI detection expected. | Prioritizes exact grounding and logical transitions over raw perplexity. |

---

## 🛠️ Tech Stack

* **Frontend**: React (scaffolded via Vite).
* **Styling**: Tailwind CSS for a clean, modern, minimalist single-page layout.
* **Icons**: Lucide-react for simple UI icons.
* **Backend API**: Vercel Serverless Functions (Node.js).
* **Database**: Firebase Firestore for NoSQL document storage.
* **Authentication**: Firebase Authentication for secure admin access.
* **LLM Engine**: Grok API (handling the core text transformation).

---

## 🧠 The "Humanizing" Engine

Humane relies on three advanced Tier 1 prompt engineering techniques to bypass standard AI detectors:

* **Chain-of-Thought (CoT) Prompting**: The model is instructed to first analyze the input text and identify robotic phrasing before executing the rewrite.
* **Meta-Cognition Loop**: This forces the LLM to map out the flaws in the AI text before generating the final output, resulting in much higher perplexity scores.
* **Dual Persona Adversarial Prompt**: The system tells the model it is an acclaimed editor reviewing a draft written by a boring AI.
* **Adversarial Edge**: Framing the task as an "editing" job triggers more critical neural pathways in the model, leading to better constraint adherence.
* **Injecting Contextual Imperfections**: The prompt explicitly forces the model to occasionally start a sentence with a conjunction like And, But, or Because.
* **Conversational Flow**: The model is asked to use conversational em-dashes to break up thoughts or include mild, context-appropriate colloquialisms.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📊 Admin Data Workbench

The backend includes a secure, private dashboard that functions as a Data Science Workbench for Phase 2 dataset curation. 

* **Human-in-the-loop Rating**: Features a 1-5 star rating or Good/Bad toggle to evaluate outputs.
* **Diff Viewer**: Highlights changed words so admins can instantly see if the model changed too much or too little.
* **AI Detection Score Column**: Displays scores from detector APIs (like GPTZero) directly next to the entry.
* **Token Usage Tracker**: Monitors daily API consumption and token volume.
* **
