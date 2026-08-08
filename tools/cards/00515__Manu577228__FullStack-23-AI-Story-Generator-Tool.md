---
id: tool-00515
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: FullStack-23-AI-Story-Generator-Tool
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/manu577228/fullstack-23-ai-story-generator-tool
created: 2026-07-18
updated: 2026-07-18
no: 515
category: 二、网文 / 长篇 AI 写作系统 库
repo: Manu577228/FullStack-23-AI-Story-Generator-Tool
stars: 1
url: https://github.com/manu577228/fullstack-23-ai-story-generator-tool
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1930461d4872b048
  - methods/最强写作方法论_全球最强综合版.md
---

# Manu577228/FullStack-23-AI-Story-Generator-Tool

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/manu577228/fullstack-23-ai-story-generator-tool
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：django, pythonanywhere, reactjs, sqlite, vercel
- **GitHub 描述**：Story Generator along with Image Generator using React, Tailwind, SQLite & Django.
- **本地描述**：Story Generator along with Image Generator using React, Tailwind, SQLite & Django.
- **拉取时间**：2026-07-23 22:54:04

---

# 🎭 AI Story Studio!

<div align="center">

![AI Story Studio Banner](https://img.shields.io/badge/AI-Story%20Studio-blueviolet?style=for-the-badge&logo=openai)
![React](https://img.shields.io/badge/React-18.x-61DAFB?style=for-the-badge&logo=react)
![Django](https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google)

**Transform your ideas into captivating stories with the power of AI**

[Demo](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage) • [API](#api)

</div>

---

## 📖 About

AI Story Studio is a full-stack web application that leverages Google's Gemini AI to generate creative, engaging stories from user prompts. Built with React for a stunning frontend experience and Django for a robust backend API.

## ✨ Features

- 🎨 **Beautiful UI** - Modern gradient design with animated particles
- 🤖 **AI-Powered** - Uses Google Gemini AI models for story generation
- ⚡ **Real-time Generation** - Watch stories come to life instantly
- 📋 **Copy to Clipboard** - Easy sharing with one click
- 🎯 **Smart Fallback** - Multiple model support for reliability
- 💾 **Story History** - Automatic saving to database
- 🌐 **CORS Enabled** - Seamless frontend-backend communication
- 📱 **Responsive Design** - Works on all devices

## 🎬 Demo

![App Screenshot](https://via.placeholder.com/800x400/0f0c29/ffffff?text=AI+Story+Studio+Screenshot)

### Sample Story Prompts

Try these creative prompts:
- *"A detective discovers a mysterious time capsule in an abandoned mansion"*
- *"In 2157, a time traveler accidentally brings a smartphone back to ancient Rome"*
- *"A forbidden forest whispers secrets to anyone who enters at midnight"*

## 🛠️ Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Tailwind CSS** - Utility-first styling
- **Fetch API** - HTTP requests
- **React Hooks** - State management

### Backend
- **Django 5** - Python web framework
- **Google Gemini AI** - Story generation
- **SQLite** - Database
- **Django CORS Headers** - Cross-origin support
- **python-dotenv** - Environment management

## 📋 Prerequisites

Before you begin, ensure you have:
- **Node.js** (v16 or higher)
- **Python** (3.10 or higher)
- **pip** (Python package manager)
- **Google Gemini API Key** ([Get it here](https://ai.google.dev/))

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-story-studio.git
cd ai-story-studio
```

### 2. Backend Setup (Django)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start Django server
python manage.py runserver
```

Backend will run on: `http://127.0.0.1:8000`

### 3. Frontend Setup (React)

```bash
# Open new terminal and navigate to frontend
cd frontend

# Install dependencies
npm install

# Start React app
npm start
```

Frontend will run on: `http://localhost:3000`

## 📁 Project Structure

```
ai-story-studio/
├── backend/
│   ├── api/
│   │   ├── models.py          # Story database model
│   │   ├── views.py           # API endpoints
│   │   └── urls.py            # API routing
│   ├── backend/
│   │   ├── settings.py        # Django configuration
│   │   └── urls.py            # Main URL routing
│   ├── manage.py
│   ├── requirements.txt
│   └── .env                   # Environment variables
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js             # Main React component
│   │   ├── index.js
│   │   └── index.css          # Tailwind imports
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md
```

## 🔧 Configuration

### Backend Configuration

**backend/.env**
```env
GEMINI_API_KEY=your_actual_api_key_here
SECRET_KEY=your_django_secret_key
DEBUG=True
```

**backend/settings.py**
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

### Frontend Configuration

**frontend/src/App.js**
```javascript
const API_URL = "http://127.0.0.1:8000/api/generate-story/";
```

## 📡 API Documentation

### Generate Story

**Endpoint:** `POST /api/generate-story/`

**Request Body:**
```json
{
  "prompt": "Your story idea here"
}
```

**Response:**
```json
{
  "story": "Once upon a time..."
}
```

**Status Codes:**
- `200` - Success
- `405` - Method not allowed
- `500` - Server error

## 💡 Usage

1. **Start Both Servers**
   - Backend: `python manage.py runserver`
   - Frontend: `npm start`

2. **Enter a Story Prompt**
   - Type your creative idea in the textarea
   - Use Ctrl+Enter for quick generation

3. **Generate Story**
   - Click "Generate Story" button
   - Wait for AI to craft your story

4. **Copy & Share**
   - Use the copy button to save your story
   - Clear to start fresh

## 🎨 Customization

### Change AI Models

Edit `backend/api/views.py`:
```python
MODEL_CANDIDATES = [
    "models/gemini-3-flash-preview",
    "models/gemini-2.5-flash-lite",
    "models/gemini-2.0-flash",
]
```

### Adjust Story Length

Modify `max_output_tokens` in `views.py`:
```python
config={
    "max_output_tokens": 8192,  # Increase for longer stories
}
```

### Customize UI Colors

Edit Tailwind classes in `App.js`:
```javascript
className="bg-gradient-to-br from-[#0f0c29] via-[#302b63] to-[#24243e]"
```

## 🐛 Troubleshooting

### CORS Errors
```bash
# Add to Django settings.py
CORS_ALLOW_ALL_ORIGINS = True  # For development only
```

### Module Not Found
```bash
# Backend
pip install -r requirements.txt

# Frontend
npm install
```

### API Key Invalid
- Verify your Gemini API key in `.env`
- Check [Google AI Studio](https://ai.google.dev/) for valid key

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Manu577228/FullStack-23-AI-Story-Generator-Tool/blob/main/LICENSE) file for details.

## 👤 Author

**Bharadwaj**

- YouTube: [@code-with-Bharadwaj](https://www.youtube.com/@code-with-Bharadwaj)
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Google Gemini AI for powerful story generation
- React team for the amazing framework
- Django community for robust backend tools
- Tailwind CSS for beautiful styling

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/ai-story-studio?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/ai-story-studio?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/ai-story-studio)
![GitHub license](https://img.shields.io/github/license/yourusername/ai-story-studio)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">

**If you find this project helpful, please give it a ⭐!**

Made with ❤️ by [Bharadwaj](https://www.youtube.com/@code-with-Bharadwaj)

</div>
