---
id: tool-01253
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ContentGenerator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/devnandanraj/contentgenerator
created: 2026-07-18
updated: 2026-07-18
no: 1253
category: 二、网文 / 长篇 AI 写作系统 库
repo: DevnandanRaj/ContentGenerator
stars: 1
url: https://github.com/devnandanraj/contentgenerator
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
content_hash: 472be529c427f77a
  - methods/最强写作方法论_全球最强综合版.md
---

# DevnandanRaj/ContentGenerator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/devnandanraj/contentgenerator
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：chackra-ui, gen-ai, openai, react
- **GitHub 描述**：A Gen AI project for content generation using OpenAI, it crafts custom jokes, Shayari, and stories based on your keywords. It's easy to use, learns from you, and values your privacy. If you want a quick laugh, personalized poetry, or a unique story, it's your simple, go-to tool for adding a touch of fun.
- **本地描述**：A Gen AI project for content generation using OpenAI, it crafts custom jokes, Shayari, and stories based on your keywords. It's easy to use, learns from you, and values your privacy. If you want a quick laugh, personalized poetry, or a unique story, it's your simple, go-to tool for adding a touch of fun.
- **拉取时间**：2026-07-23 23:15:39

---

# Creative AI Studio - ContentGenerator 🎨✨

**Full-Stack AI-Powered Creative Content Generator**

Transform your keywords into engaging content with the power of Google Gemini AI. Creative AI Studio is a modern React application with a Node.js backend that creates personalized jokes, Shayari, stories, and much more on demand.

![React](https://img.shields.io/badge/React-18.2.0-61DAFB?logo=react&logoColor=white)
![Chakra UI](https://img.shields.io/badge/Chakra_UI-2.8.1-319795?logo=chakra-ui&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-Express-339933?logo=node.js&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_2.5-4285F4?logo=google&logoColor=white)

---

## ✨ Features

### 🎨 Content Generation
- **14+ Content Types** - Jokes, Shayari, Stories, Riddles, Pickup Lines, Roasts, Compliments, Dad Jokes, Haiku, Rap Lyrics, Tweet Threads, Acrostic Poems, Motivational Speeches, and Quotes
- **Tone Customization** - Choose from Funny, Serious, Romantic, or Motivational tones
- **Length Control** - Short, Medium, or Long output options
- **Trending Topics** - Quick-start with curated keyword suggestions

### 🎯 User Experience
- **Modern UI** - Beautiful gradient designs with smooth animations
- **Dark Mode** - Toggle between light and dark themes
- **History Tracking** - Save and revisit your last 50 generations
- **Quick Actions** - Copy, Download, and Share generated content
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Confetti Celebrations** - Fun animations on successful generation

### ⚡ Performance & Security
- **Rate Limiting** - Protection against API abuse (100 requests per 15 minutes)
- **Error Handling** - Comprehensive error messages and user feedback
- **Local Storage** - Client-side history and preferences
- **Fast API** - Optimized backend responses with Gemini 2.5 Flash

---

## 🛠️ Tech Stack

### Frontend
- **React** 18.2.0 - UI framework
- **Chakra UI** 2.8.1 - Component library
- **Framer Motion** 12.x - Smooth animations
- **React Icons** 5.x - Icon library
- **React Confetti** 6.x - Celebration effects
- **Axios** 1.5.1 - API requests

### Backend
- **Node.js** + **Express.js** - Server framework
- **Google Gemini API** (2.5 Flash) - AI content generation
- **Helmet** - Security headers
- **CORS** - Cross-origin resource sharing
- **Express Rate Limit** - API rate limiting
- **dotenv** - Environment configuration

---

## 📋 Prerequisites

- **Node.js** (v14.0.0 or higher)
- **npm** (v6.0.0 or higher)
- **Google Gemini API Key** ([Get one free here](https://aistudio.google.com/apikey))

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ContentGenerator.git
cd ContentGenerator
```

### 2. Setup Backend

```bash
cd backend
npm install
```

Create a `.env` file in the `backend` directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
PORT=5000
```

Start the backend server:
```bash
npm start
```

The backend will run on **http://localhost:5000**

### 3. Setup Frontend

Open a new terminal in the project root:

```bash
npm install
```

Create a `.env` file in the root directory:
```env
REACT_APP_API_URL=http://localhost:5000
```

Start the React app:
```bash
npm start
```

The app will open at **http://localhost:3000**

---

## 📖 Usage

1. **Select Content Type** - Choose from 14+ content types (jokes, stories, quotes, etc.)
2. **Enter Keyword** - Type your keyword or click a trending topic
3. **Customize** - Select tone (funny, serious, romantic, motivational) and length (short, medium, long)
4. **Generate** - Click the ✨ Generate button
5. **Enjoy** - Copy, download, or share your AI-generated content!

---

## 🎯 Content Types

| Type | Description | Icon |
|------|-------------|------|
| Shayari | Urdu/Hindi poetry with elegant verses | 📜 |
| Joke | Clever and witty humor | 😂 |
| Quote | Inspirational and meaningful quotes | 💭 |
| Story | Engaging short narratives | 📖 |
| Riddle | Brain teasers with answers | 🤔 |
| Pickup Line | Charming and respectful lines | 💘 |
| Roast | Playful, light-hearted roasts | 🔥 |
| Compliment | Genuine and heartwarming compliments | 🌟 |
| Dad Joke | Classic pun-based humor | 👨 |
| Haiku | Traditional 5-7-5 syllable poems | 🎋 |
| Rap Lyrics | Rhyming verses with wordplay | 🎤 |
| Tweet Thread | Engaging social media threads | 🐦 |
| Acrostic | Poems where first letters spell words | ✍️ |
| Motivational Speech | Powerful and inspiring speeches | 💪 |

---

## 📁 Project Structure

```
ContentGenerator/
├── backend/                    # Node.js Express backend
│   ├── server.js              # Main server file
│   ├── package.json           # Backend dependencies
│   ├── .env                   # Environment variables (Gemini API key)
│   └── README.md              # Backend documentation
├── src/                       # React frontend source
│   ├── Components/            # React components
│   │   ├── Content.jsx       # Main content generator
│   │   ├── ContentCard.jsx   # Generated content display
│   │   ├── Header.jsx        # App header with branding
│   │   ├── HistorySidebar.jsx # Generation history panel
│   │   └── Footer.jsx        # App footer
│   ├── hooks/                # Custom React hooks
│   │   └── useLocalStorage.js # localStorage hook
│   ├── utils/                # Utility functions
│   │   ├── animations.js     # Framer Motion configs
│   │   └── constants.js      # App constants
│   ├── App.js                # Main app component
│   ├── App.css               # App styles
│   ├── index.js              # React entry point
│   └── index.css             # Global styles
├── public/                    # Public assets
│   ├── index.html
│   ├── favicon.ico
│   └── manifest.json
├── .env                       # Frontend env (API URL)
├── package.json               # Frontend dependencies
└── README.md                  # This file
```

---

## 🌐 API Endpoints

### Backend API

**Base URL:** `http://localhost:5000`

#### POST `/api/generate`
Generate content based on parameters.

**Request Body:**
```json
{
  "type": "joke",
  "keyword": "programming",
  "tone": "funny",
  "length": "short"
}
```

**Response:**
```json
{
  "success": true,
  "result": "Generated content here...",
  "metadata": {
    "type": "joke",
    "keyword": "programming",
    "tone": "funny",
    "length": "short",
    "model": "gemini-2.5-flash",
    "timestamp": "2025-12-15T13:00:00.000Z"
  }
}
```

#### GET `/api/content-types`
Get all available content types.

#### GET `/api/health`
Health check endpoint.

#### GET `/`
API information and available endpoints.

---

## 🎨 Customization

### Adding New Content Types

Edit `backend/server.js` and add to the `contentConfigs` object:

```javascript
'your-type': {
  systemPrompt: 'System instruction for AI...',
  userPromptTemplate: (keyword, tone, length) =>
    `Generate ${tone} content about "${keyword}". Length: ${length}.`
}
```

### Changing Themes

Modify colors in `src/index.css` or update Chakra UI theme in `src/index.js`.

---

## 🔧 Environment Variables

### Backend (`.env` in `backend/`)
```env
GEMINI_API_KEY=your_google_gemini_api_key
PORT=5000
NODE_ENV=development
```

### Frontend (`.env` in root)
```env
REACT_APP_API_URL=http://localhost:5000
```

---

## 🚀 Deployment

### Frontend (Netlify/Vercel)
1. Build the frontend: `npm run build`
2. Deploy the `build` folder
3. Set environment variable: `REACT_APP_API_URL=your_backend_url`

### Backend (Render/Heroku)
1. Deploy `backend` folder
2. Set environment variables:
   - `GEMINI_API_KEY`
   - `PORT` (usually auto-set)
3. Note the deployed URL and update frontend env

---

## 🐛 Troubleshooting

### API Key Issues
- Ensure your Gemini API key is valid at [Google AI Studio](https://aistudio.google.com/apikey)
- Check that the `.env` file is in the correct location
- Restart the backend server after updating `.env`

### CORS Errors
- Verify backend is running on port 5000
- Check `REACT_APP_API_URL` in frontend `.env`
- Ensure both servers are running

### Rate Limit Errors
- Wait a few moments between requests (free tier has limits)
- The app enforces 100 requests per 15 minutes per IP

---

## 📝 License

This project is open source and available under the [MIT License](https://github.com/DevnandanRaj/ContentGenerator/blob/main/LICENSE).

---

## 🙏 Acknowledgments

- Built with [React](https://reactjs.org/)
- UI components from [Chakra UI](https://chakra-ui.com/)
- Animations by [Framer Motion](https://www.framer.com/motion/)
- Powered by [Google Gemini API](https://ai.google.dev/)

---

## 📧 Support

For issues and questions:
- Open an issue on GitHub
- Check the [troubleshooting section](#-troubleshooting)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">
  Made with ❤️ and AI ✨<br>
  <strong>Powered by Google Gemini 2.5 Flash</strong>
</div>
