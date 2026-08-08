---
id: tool-01571
type: tool
area: 库
status: active
tags: [互动叙事, Python, 协议宽松, 需API密钥, 英文文档]
title: FastAPI_Adventure-AI_Story_Generator
summary: 互动叙事/聊天写故事
source: https://github.com/krushnasonawane24/fastapi_adventure-ai_story_generator
created: 2026-07-18
updated: 2026-07-18
no: 1571
category: 二、网文 / 长篇 AI 写作系统 库
repo: KrushnaSonawane24/FastAPI_Adventure-AI_Story_Generator
stars: 1
url: https://github.com/krushnasonawane24/fastapi_adventure-ai_story_generator
tier: "B"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 36b3a8b3f13f2a40
  - methods/最强写作方法论_全球最强综合版.md
---

# KrushnaSonawane24/FastAPI_Adventure-AI_Story_Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/krushnasonawane24/fastapi_adventure-ai_story_generator
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：An interactive storytelling platform powered by FastAPI and Google Gemini AI that creates dynamic choose-your-own-adventure narratives with multiple branching paths and endings.
- **本地描述**：An interactive storytelling platform powered by FastAPI and Google Gemini AI that creates dynamic choose-your-own-adventure narratives with multiple branching paths and endings.
- **拉取时间**：2026-07-23 23:24:53

---

# 🎭 Interactive Story Generator

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![React](https://img.shields.io/badge/react-18.0+-61dafb.svg)
![Deployment](https://img.shields.io/badge/deployed-Render-46E3B7.svg)

**An AI-powered choose-your-own-adventure story generator built with FastAPI and React**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-documentation)

### 🌐 **[Live Demo](https://fastapi-adventure-ai-story-generator-1.onrender.com)** 🚀

</div>

---

## 🎮 Demo

**Try it live:** [https://fastapi-adventure-ai-story-generator-1.onrender.com](https://fastapi-adventure-ai-story-generator-1.onrender.com)

> **Note:** First request may take 30-60 seconds as the free tier server spins up from sleep mode.

---

## 📖 About

Interactive Story Generator is a full-stack web application that uses AI (powered by Groq's Llama 3.3 70B) to create engaging choose-your-own-adventure stories. Users can input any theme, and the AI generates a complete branching narrative with multiple paths and endings.

## ✨ Features

- 🤖 **AI-Powered Story Generation** - Utilizes Groq's Llama-3.3-70b-versatile model for creative storytelling
- 🎨 **Modern Dark UI** - Premium gradient design with smooth animations
- 🌳 **Branching Narratives** - Multiple story paths with different endings
- 🎯 **Interactive Choices** - Player decisions shape the story outcome
- 📊 **Real-time Status** - Live updates on story generation progress
- 💾 **Session Management** - Cookie-based user session tracking
- 🚀 **Fast & Responsive** - Optimized for quick story generation
- 🎭 **Themed Examples** - Quick-start options like Pirates, Space, Medieval, etc.

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Database ORM
- **Pydantic** - Data validation
- **Groq API** - AI story generation (Llama 3.3 70B)
- **SQLite** - Lightweight database

### Frontend
- **React 18** - UI library
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Vite** - Build tool & dev server
- **CSS3** - Modern styling with animations

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- Groq API Key ([Get one here](https://console.groq.com))

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/KrushnaSonawane24/FastAPI_Adventure-AI_Story_Generator.git
cd FastAPI_Adventure-AI_Story_Generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp backend/.env.example backend/.env
# Add your Groq API key to backend/.env
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

## 🚀 Usage

### Start Backend Server

```bash
# From project root
python backend/main.py
```

Backend will run on `http://localhost:8000`

### Start Frontend Server

```bash
# From frontend directory
npm run dev
```

Frontend will run on `http://localhost:5173`

### Access the Application

Open your browser and navigate to `http://localhost:5173`

## 📚 API Documentation

Once the backend is running, access the interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Key Endpoints

#### Create Story

```http
POST /api/stories/create
Content-Type: application/json

{
  "theme": "pirates"
}
```

**Response:**
```json
{
  "job_id": "uuid-here",
  "status": "pending",
  "created_at": "2026-01-19T10:00:00",
  "story_id": null
}
```

#### Check Job Status

```http
GET /api/jobs/{job_id}
```

**Response:**
```json
{
  "job_id": "uuid-here",
  "status": "completed",
  "story_id": 7,
  "completed_at": "2026-01-19T10:00:30"
}
```

#### Get Complete Story

```http
GET /api/stories/{story_id}/complete
```

## 📁 Project Structure

```
FastAPI_Adventure-AI_Story_Generator/
├── backend/
│   ├── core/
│   │   ├── config.py          # App configuration
│   │   ├── models.py          # Pydantic models
│   │   ├── prompts.py         # AI prompts
│   │   └── story_generetor.py # Story generation logic
│   ├── DB/
│   │   └── database.py        # Database setup
│   ├── models/
│   │   ├── job.py            # Job model
│   │   └── story.py          # Story model
│   ├── routers/
│   │   ├── job.py            # Job endpoints
│   │   └── story.py          # Story endpoints
│   ├── schemas/
│   │   └── story.py          # API schemas
│   ├── .env.example          # Environment template
│   └── main.py               # FastAPI app entry
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── LoadingStatus.jsx
│   │   │   ├── StoryGame.jsx
│   │   │   ├── StoryGenerator.jsx
│   │   │   ├── StoryLoader.jsx
│   │   │   └── ThemeInput.jsx
│   │   ├── App.css           # Main styles
│   │   ├── App.jsx           # Main component
│   │   ├── main.jsx          # Entry point
│   │   └── util.js           # API config
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── .gitignore
├── README.md
└── requirements.txt
```

## 🎨 Features Showcase

### 1. Theme Input
- Clean, modern input form
- Clickable example themes (Pirates, Space, Medieval, etc.)
- Real-time validation

### 2. Loading State
- Animated spinner
- Status updates
- Background job processing

### 3. Story Gameplay
- Interactive choice buttons
- Smooth transitions
- Win/lose endings
- Restart & new story options

### 4. Responsive Design
- Works on desktop, tablet, and mobile
- Dark theme with gradient accents
- Smooth animations and hover effects

## 🔧 Configuration

### Environment Variables

Create `backend/.env` from `.env.example`:

```env
DATABASE_URL=sqlite:///./database.db
API_PREFIX=/api
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
GROQ_API_KEY=your_groq_api_key_here
```

### Frontend API Configuration

Update `frontend/src/util.js` if needed:

```javascript
export const API_BASE_URL = "http://localhost:8000/api";
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/KrushnaSonawane24/FastAPI_Adventure-AI_Story_Generator/blob/main/LICENSE) file for details.

## 👨‍💻 Author

**KRUSHNA SONAWANE**

- GitHub: [@KrushnaSonawane24](https://github.com/KrushnaSonawane24)
- Project: [FastAPI Adventure AI Story Generator](https://github.com/KrushnaSonawane24/FastAPI_Adventure-AI_Story_Generator)

## 🙏 Acknowledgments

- [Groq](https://groq.com/) - For providing fast AI inference
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [React](https://react.dev/) - JavaScript library for building UIs
- [Vite](https://vitejs.dev/) - Next-generation frontend tooling

## 📧 Support

If you have any questions or run into issues, please open an issue on GitHub.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Built with using React & FastAPI

</div>
