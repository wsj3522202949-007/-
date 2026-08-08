---
id: tool-01062
type: tool
area: 库
status: active
tags: [CSS, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-Prompt-Improver
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/fatimaafzal696-rgb/ai-prompt-improver
created: 2026-07-18
updated: 2026-07-18
no: 1062
category: 二、网文 / 长篇 AI 写作系统 库
repo: fatimaafzal696-rgb/AI-Prompt-Improver
stars: 0
url: https://github.com/fatimaafzal696-rgb/ai-prompt-improver
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: eaa48270f4c85625
  - methods/最强写作方法论_全球最强综合版.md
---

# fatimaafzal696-rgb/AI-Prompt-Improver

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/fatimaafzal696-rgb/ai-prompt-improver
- **Stars**：0
- **语言**：CSS
- **License**：None
- **Topics**：—
- **GitHub 描述**：PromptCraft AI is an AI-powered web app that transforms simple prompts into clear, detailed, and effective instructions for AI tools. Users can choose Better, Professional, or Expert modes to enhance prompt quality, improve AI responses, save time, and boost productivity for writing, coding, research, and content creation.
- **本地描述**：PromptCraft AI is an AI-powered web app that transforms simple prompts into clear, detailed, and effective instructions for AI tools. Users can choose Better, Professional, or Expert modes to enhance prompt quality, improve AI responses, save time, and boost productivity for writing, coding, research, and content creation.
- **拉取时间**：2026-07-23 23:09:57

---

# PromptCraft AI 🚀

> Transform basic prompts into expert-level AI instructions using advanced prompt engineering and Google Gemini AI.

![PromptCraft AI](https://img.shields.io/badge/AI-Powered-cyan?style=for-the-badge) ![Flask](https://img.shields.io/badge/Backend-Flask-blue?style=for-the-badge) ![Gemini](https://img.shields.io/badge/API-Google%20Gemini-orange?style=for-the-badge)

---

## ✨ Features

- **Three improvement modes**: Better, Professional, Expert
- **Live quality scoring** with animated circular gauges
- **Before vs After comparison** side-by-side view
- **Prompt history** stored in browser localStorage (last 20 prompts)
- **Copy-to-clipboard** one-click copy
- **Character counter** with 5000-character limit
- **Quick example prompts** to get started instantly
- **Responsive design**: works on desktop and mobile
- **Dark mode by default** with premium glassmorphism design

---

## 🛠️ Project Structure

```
AI-Prompt-Improver/
│
├── app.py               ← Flask server + Gemini API integration
├── requirements.txt     ← Python dependencies
├── .env                 ← Environment variables (API key)
│
├── templates/
│   └── index.html       ← Main HTML template
│
├── static/
│   ├── style.css        ← Premium dark theme CSS
│   └── script.js        ← Frontend logic
│
└── README.md
```

---

## 🔑 Getting a Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the generated API key
5. Paste it into your `.env` file (see setup below)

> **Note**: The Gemini API has a free tier that allows generous usage for personal projects.

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Steps

**1. Clone or navigate to the project folder:**

```bash
cd path/to/AI-Prompt-Improver
```

**2. Create a virtual environment (recommended):**

```bash
python -m venv venv
```

Activate it:
- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Configure your API key:**

Open the `.env` file and replace the placeholder:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

**5. Run the application:**

```bash
python app.py
```

**6. Open in browser:**

Navigate to [http://localhost:5000](http://localhost:5000)

---

## 🎯 How to Use

1. **Enter your prompt** in the text area on the left panel
2. **Select an improvement mode**:
   - ✨ **Better**: Quick grammar and clarity fix, keeping the prompt concise
   - 💼 **Professional**: Adds context, structure, and professional-grade instructions
   - 🚀 **Expert**: Full expert-level rewrite with role, objectives, constraints, audience, and success criteria
3. Click **"Improve Prompt"** (or press `Ctrl+Enter`)
4. View your improved prompt on the right panel
5. Switch between **"Improved Only"** and **"Before vs After"** views
6. Click **Copy** to copy to clipboard

---

## 🧠 Prompt Engineering Modes

### ✨ Better Mode
- Fixes grammar and spelling errors
- Improves clarity and precision
- Removes redundancy
- Keeps the original intent intact

### 💼 Professional Mode
- Adds context and background information
- Creates structured format with clear sections
- Improves specificity and actionability
- Uses professional and precise language

### 🚀 Expert Mode
Transforms your prompt into a comprehensive instruction including:
- **Role**: Specific expert persona for the AI
- **Objectives**: Clear, measurable goals
- **Context**: Rich background information
- **Constraints**: Specific limitations and rules
- **Output Format**: Exact formatting requirements
- **Target Audience**: Who the output is for
- **Success Criteria**: What makes a perfect response

---

## 🔌 API Endpoints

| Method | Endpoint       | Description                  |
|--------|----------------|------------------------------|
| GET    | `/`            | Serves the main application  |
| POST   | `/api/improve` | Improves a prompt via Gemini |
| GET    | `/api/health`  | Health check / API key status|

### POST `/api/improve`

**Request body:**
```json
{
  "prompt": "Write a blog post about AI",
  "mode": "expert"
}
```

**Response:**
```json
{
  "success": true,
  "original_prompt": "Write a blog post about AI",
  "improved_prompt": "...",
  "mode": "expert",
  "original_score": 22,
  "improved_score": 89,
  "explanation": "Added expert role, objectives, and structured output format.",
  "improvements_made": ["Role Definition", "Output Format", "Success Criteria"]
}
```

---

## ⚙️ Configuration

| Variable         | Description                  | Required |
|------------------|------------------------------|----------|
| `GEMINI_API_KEY` | Your Google Gemini API key   | ✅ Yes   |

---

## 🐛 Troubleshooting

**"No API Key" shown in the header:**
- Ensure your `.env` file exists and contains a valid `GEMINI_API_KEY`
- Restart the Flask server after editing `.env`

**"API returned unexpected response format":**
- This is rare. Try clicking "Improve Prompt" again.

**Port 5000 already in use:**
- Change the port in `app.py`: `app.run(port=5001)`

---

## 📄 License

MIT License — feel free to use and modify for your own projects.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*Built with ❤️ using Python Flask and Google Gemini AI*
