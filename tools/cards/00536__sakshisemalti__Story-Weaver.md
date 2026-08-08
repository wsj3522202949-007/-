---
id: tool-00536
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Story-Weaver
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/sakshisemalti/story-weaver
created: 2026-07-18
updated: 2026-07-18
no: 536
category: 二、网文 / 长篇 AI 写作系统 库
repo: sakshisemalti/Story-Weaver
stars: 3
url: https://github.com/sakshisemalti/story-weaver
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 77bc333542989515
  - methods/最强写作方法论_全球最强综合版.md
---

# sakshisemalti/Story-Weaver

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sakshisemalti/story-weaver
- **Stars**：3
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-Powered Interactive Story Generator — Microsoft Agents League 2026 Contest
- **本地描述**：AI-Powered Interactive Story Generator — Microsoft Agents League 2026 Contest
- **拉取时间**：2026-07-23 22:54:40

---

# 📖 The Story Weaver
### AI-Powered Interactive Story Generator — Microsoft Agents League 2026 Contest

> *"Every reader becomes the author. Every choice rewrites the world."*

---

## 🧠 About Project

**The Story Weaver** is a full-stack web application that lets anyone create and experience a personalized, AI-generated interactive story — in real time, right in the browser.

You pick a genre, describe your characters, and paint the world you want to inhabit. The AI writes your opening scene. Then *you* drive the story forward by making choices at the end of each chapter. Every decision changes what happens next. When the tale concludes, you can download the entire story you co-created — as a text file or structured JSON.

It's part interactive fiction, part creative writing tool, part AI playground. No writing skills required. No account needed. Just imagination.

---

## 💡 The Problem It Solves

Most AI writing tools are just blank text boxes — you prompt, it generates, and you're done. There's no interactivity, no personal investment, no sense that *your* decisions matter.

The Story Weaver flips this. It puts the reader in the driver's seat:

- **Writers** use it to explore story directions they haven't thought of
- **Readers** experience stories that feel personal because they shaped them
- **Educators** use it for creative writing exercises and narrative thinking
- **Developers** can see a working pattern for human-in-the-loop AI generation

The core insight is simple: AI-generated text becomes far more engaging when the human has agency over where it goes.

---

## 🤖 GitHub Copilot — Benefit

| Area | Copilot's Role |
|------|----------------|
| Server scaffolding | Generated from comments |
| Ollama HTTP API | Suggested + completed with error handling |
| Prompt design | Suggested role-based format and context trimming |
| React components | Completed logic from function signatures |
| Voice categorization | Drafted keyword-matching system |
| Bug fixes | Suggested Picsum as Unsplash replacement |
| Export functions | Near-complete autocomplete |

Copilot saved an estimated **4–6 hours** of development time and caught two bugs (the `exec` hanging issue and the missing `onvoiceschanged` handler for Chrome) before they became blockers.

---

## ✨ Features

### 🎭 Story Generation
- Choose from **6 genres**: Fantasy, Sci-Fi, Mystery, Horror, Romance, Adventure
- Describe your **characters** and **setting** in your own words — total creative freedom
- AI writes a unique **opening scene** every single time — no two stories are alike
- **3 branching choices** per chapter let you steer the narrative
- **3 chapters + epilogue** give every story a proper arc and satisfying conclusion
- Graceful **mock fallback** if the AI is unavailable — the app never crashes or breaks

### 🖼 Scene Illustrations
- Every chapter gets a **mood-matched scene image** from Picsum Photos CDN
- Images load instantly — no API key, no rate limits, no delays
- Seeds are deterministic: same genre + chapter always = same image, every time

### 🔊 Voice Narration
- Full **text-to-speech narration** using the browser's Web Speech API — no external service needed
- **Voice picker** with three categories:
  - 👩 **Female** — Samantha, Zira, Karen and similar voices
  - 👨 **Male** — Daniel, Alex, David and similar voices
- Browse and select **any installed system voice** by name from a dropdown
- Pitch auto-adjusts per category for the best dramatic effect
- Stops automatically on each new chapter; restart anytime

### ✍️ Reading Experience
- **Typewriter animation** reveals story text character by character for cinematic effect
- **Skip button** for readers who want to read at their own pace
- **Chapter progress bar** shows how far through the story you are
- **Collapsible story history** lets you review every past chapter and the choices you made

### 📥 Export Your Story
- **Download as `.txt`** — clean, readable plain text with chapter headings
- **Download as `.json`** — structured data with metadata, all chapter text, choices made, and image URLs
- Keep, share, or print the story you created

### 📱 Responsive Design
- Works beautifully on mobile, tablet, and desktop
- Dark gothic parchment aesthetic with warm amber candlelight accents
- Typography: Playfair Display (headings) + Crimson Text (body) + JetBrains Mono (UI labels)

---

## 🏗 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18, React Router v6 |
| Styling | TailwindCSS 3 |
| Build Tool | Vite |
| Backend | Node.js, Express |
| Local AI | Ollama HTTP API |
| AI Model | gemma:2b (swappable via `.env`) |
| Voice | Web Speech API (browser-native, no cost) |
| Images | Picsum Photos CDN |
| IDs | UUID v4 |

---

## 🏗 Project Structure

```
story-app/
├── backend/
│   ├── server.js          # Express API + Ollama HTTP integration
│   ├── package.json
│   └── .env               # OLLAMA_URL, OLLAMA_MODEL, PORT, timeout
│
└── frontend/
    ├── index.html
    ├── vite.config.js
    ├── tailwind.config.js
    ├── postcss.config.js
    ├── package.json
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── index.css
        └── components/
            ├── Home.jsx              # Landing page — genre, characters, setting inputs
            ├── Story.jsx             # Interactive story page — scene + choices
            ├── End.jsx               # Epilogue + full story + download
            ├── TypeWriter.jsx        # Animated text reveal with skip
            └── VoiceNarration.jsx    # TTS with Female/Male/Dramatic picker
```

---

## 🚀 Quick Start
 
### 1.Clone the Repository
```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
### 2.Install Dependencies
```
# Install backend dependencies
cd backend
npm install

# Install frontend dependencies
cd ../frontend
npm install
```
### 3.Install & Start Ollama
Download and install Ollama: 👉 https://ollama.com
- Pull a model
```bash
ollama pull gemma:2b
ollama serve
# Runs on http://localhost:11434
```
### 4. Start the backend
```bash
cd backend
npm install
# create a file .env in backend folder
npm start
# Runs on http://localhost:3001
```
### 5. Start Frontend
```bash
cd frontend
npm install
npm run dev
# Runs on http://localhost:3000
```
🎉 You're Ready!
Open in your browser:
http://localhost:3000
Start weaving your AI-generated story.

---

## ⚙️ Environment Variables

`backend/.env`:

```env
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=gemma:2b
PORT=3001
OLLAMA_TIMEOUT_MS=30000
```

---

## 🛣 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/start` | Start a new story |
| POST | `/api/continue` | Continue story with a player choice |
| GET | `/api/story/:id` | Fetch full story by ID |

### POST `/api/start`
```json
{
  "genre": "fantasy",
  "characters": "a weary knight and a cunning sorceress",
  "setting": "a fog-shrouded ancient city"
}
```

**Response:**
```json
{
  "id": "uuid",
  "chapter": 0,
  "text": "The ancient stones hummed...",
  "choices": ["Cast a spell", "Draw your sword", "Summon a spirit"],
  "image": "https://picsum.photos/seed/10/800/400",
  "concluded": false
}
```

### POST `/api/continue`
```json
{
  "id": "story-uuid",
  "choice": "Draw your enchanted sword",
  "chapterIndex": 0
}
```

### GET `/api/story/:id`
Returns the full story object — all chapters, choices made, genre, characters, setting, and timestamps.

---

## 🤖 Switching AI Models

```env
OLLAMA_MODEL=gemma:2b        # default — balanced quality/speed
OLLAMA_MODEL=llama3.2:1b     # fastest — great for demos and low-end hardware
OLLAMA_MODEL=llama3.1:8b     # best quality — needs 8GB+ RAM
OLLAMA_MODEL=mistral:7b      # excellent creative and narrative writing
```

```bash
ollama pull mistral:7b
```

---

## 🎙 Voice Availability by Platform

| Platform | Available Voices |
|----------|-----------------|
| Windows (Edge/Chrome) | Zira (F), David (M), Mark (M), Aria (F) |
| macOS (Safari/Chrome) | Samantha (F), Alex (M), Daniel (UK·M), Karen (AU·F) |
| iOS / iPadOS | Siri voices, Samantha |
| Android Chrome | Google US English Female/Male |
| Linux | eSpeak — install via `sudo apt install espeak` |

The **🎭 Dramatic** tab surfaces British (en-GB), Australian (en-AU), and Irish (en-IE) accents — especially effective for Fantasy and Horror genres.

---

## 🐛 Troubleshooting

**Ollama hanging or timing out**
- Confirm it's running: `ollama serve`
- Confirm model is pulled: `ollama list`
- Raise the timeout: `OLLAMA_TIMEOUT_MS=60000` in `.env`
- Try a lighter model: `OLLAMA_MODEL=llama3.2:1b`

**Voice picker shows no voices**
- Chrome loads voices asynchronously — clicking the voice button once triggers the load
- Linux: install `espeak` for basic voice support

**Story 404 after server restart**
- Stories live in memory only. For persistence, swap the `Map` in `server.js` for SQLite or MongoDB.

---

## 📦 Production Build

```bash
cd frontend && npm run build
```

Add to `backend/server.js` to serve the built frontend:

```js
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
const __dirname = dirname(fileURLToPath(import.meta.url));
app.use(express.static(join(__dirname, '../frontend/dist')));
app.get('*', (_, res) => res.sendFile(join(__dirname, '../frontend/dist/index.html')));
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*Built for Microsoft Agents League Contest with GitHub Copilot and ❤️*
