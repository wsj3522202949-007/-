---
id: tool-04878
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 需API密钥, 英文文档, 去AI味]
title: Email-Intent-Urgency-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/tejassswa17/email-intent-urgency-detector
created: 2026-07-18
updated: 2026-07-18
no: 4878
category: 一、去 AI 味 / Humanizer 库
repo: tejassswa17/Email-Intent-Urgency-Detector
stars: 0
url: https://github.com/tejassswa17/email-intent-urgency-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# tejassswa17/Email-Intent-Urgency-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/tejassswa17/email-intent-urgency-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：langchain, workflows
- **GitHub 描述**：An AI-powered email classification system that analyzes email text to detect intent, urgency, and tone using LangChain, Pydantic, and LLMs.
- **本地描述**：An AI-powered email classification system that analyzes email text to detect intent, urgency, and tone using LangChain, Pydantic, and LLMs.
- **拉取时间**：2026-07-25 17:57:50

---

# Email Intent & Urgency Detector

An AI-powered email classification system that analyzes email text to detect **intent**, **urgency**, and **tone** using Large Language Models (LLMs), LangChain, and Pydantic.

This project helps automate email understanding for support systems, ticketing platforms, and customer communication workflows.

---

## Features

- Intent Detection
- Urgency Classification
- Tone Analysis
- Structured JSON Output
- Pydantic Validation
- Modular Project Architecture
- Supports Groq and Gemini APIs

---

## Tech Stack

- Python
- LangChain
- Pydantic
- Groq / Gemini API
- dotenv

---

## Project Structure

```bash
Email-Intent-Urgency-Detector/
│
├── main.py          # Entry point
├── model.py         # LLM configuration
├── prompt.py        # Prompt template
├── parser.py        # Pydantic schemas & parser
├── requirements.txt
└── .env
```

---

## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/tejassswa17/Email-Intent-Urgency-Detector.git
cd Email-Intent-Urgency-Detector
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

---

## Run Application

```bash
python main.py
```

---

## Example Input

```text
Please resolve the payment issue immediately.
```

## Example Output

```json
{
  "intent": "Request",
  "urgency": "High",
  "tone": "Urgent"
}
```

---

## Supported Categories

### Intent
- Request
- Complaint
- Inquiry
- Information
- Feedback
- Unclear

### Urgency
- Low
- Medium
- High
- Critical
- Unclear

### Tone
- Polite
- Neutral
- Urgent
- Angry
- Professional
- Unclear

---

## Future Improvements

- Streamlit UI
- REST API Integration
- Multi-language Support
- Fine-tuned Email Classification Models

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---
