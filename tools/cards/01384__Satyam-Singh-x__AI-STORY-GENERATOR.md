---
id: tool-01384
type: tool
area: 库
status: active
tags: [TTS, Python, 协议未明, 需API密钥, 英文文档]
title: AI-STORY-GENERATOR
summary: 小说转语音/有声书
source: https://github.com/satyam-singh-x/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1384
category: 二、网文 / 长篇 AI 写作系统 库
repo: Satyam-Singh-x/AI-STORY-GENERATOR
stars: 1
url: https://github.com/satyam-singh-x/ai-story-generator
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 174a7ab4256c831d
  - methods/最强写作方法论_全球最强综合版.md
---

# Satyam-Singh-x/AI-STORY-GENERATOR

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/satyam-singh-x/ai-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Turn images into stories ✨ AI-generated narratives with voice, themes & downloadable PDFs.
- **本地描述**：Turn images into stories ✨ AI-generated narratives with voice, themes & downloadable PDFs.
- **拉取时间**：2026-07-23 23:19:29

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

📖 TaleForge — AI Story Generator from Images

TaleForge is an AI-powered storytelling application that transforms images into beautifully written stories with narration, themed UI, and downloadable story PDFs.

Built using Streamlit, Google Gemini, and Python, TaleForge blends creativity, design, and AI into a polished storytelling experience.

Live-demo: https://ai-story-generator-satyam.streamlit.app/



✨ Features

✅ Generate stories from images using AI

✅ Multiple genres (Comedy, Thriller, Fairy Tale, Mythology, etc.)

✅ Beautiful animated UI with dynamic themes

✅ AI-powered narration (Text-to-Speech)

✅ Download stories as professionally formatted PDFs

✅ Image previews inside PDFs

✅ Automatic page numbering

✅ Clean & responsive interface

✅ Secure API handling using .env

🎭 Supported Story Genres

Comedy

Thriller

Fairy Tale

Mythological

Sci-Fi

Mystery

Adventure

Romantic

Horror

Morale

Each genre dynamically changes:

Theme colors

Animations

Story tone



🖥️ Tech Stack

Layer	Technology

Frontend	Streamlit

AI Model	Google Gemini

Image Processing	Pillow

Text-to-Speech	gTTS

PDF Generation	ReportLab

Styling	CSS (embedded)

Environment	Python + dotenv



📁 Project Structure

TaleForge/

│
├── app.py                     # Main Streamlit application

├── Story_generator_fn.py      # AI logic & narration

├── requirements.txt

└── README.md


⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Satyam-Singh-x/AI-STORY-GENERATOR.git

cd AI-STORY-GENERATOR

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up Environment Variables

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key_here


⚠️ Never upload your .env file to GitHub

4️⃣ Run the App

streamlit run app.py

🧠 How It Works

Upload 1–10 images

Choose a story genre

AI analyzes images and generates a story

Story is narrated using TTS

Story + images exported as a PDF

Theme changes dynamically based on genre

📄 PDF Features

✔ Cover page with title

✔ Embedded images

✔ Multi-page story formatting

✔ Page numbers

✔ Clean typography

🔊 Narration

Narration is generated using Google Text-to-Speech (gTTS) and plays directly in the browser.

🎨 UI Highlights

Dynamic theme switching

Animated transitions

Dark sidebar with readable contrast

Responsive layout

Clean typography



🔐 Security

API keys loaded via .env

.env should be added to .gitignore

No credentials hardcoded

🚀 Future Improvements

🎧 Voice selection

🌍 Multi-language support

🧠 Story memory

📱 Mobile optimization

🎬 Story-to-video generation

☁️ Cloud deployment



🧑‍💻 Author

Satyam

AI Developer | Storytelling Enthusiast | Full-Stack Learner

“Turning imagination into experience using AI.”

⭐ If You Like This Project

⭐ Star this repository

🍴 Fork it

📢 Share it

💡 Contribute ideas
