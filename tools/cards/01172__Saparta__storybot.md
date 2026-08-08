---
id: tool-01172
type: tool
area: 库
status: active
tags: [TTS, JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: storybot
summary: 小说转语音/有声书
source: https://github.com/saparta/storybot
created: 2026-07-18
updated: 2026-07-18
no: 1172
category: 二、网文 / 长篇 AI 写作系统 库
repo: Saparta/storybot
stars: 2
url: https://github.com/saparta/storybot
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 35f1a606e4ab4d1b
  - methods/最强写作方法论_全球最强综合版.md
---

# Saparta/storybot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/saparta/storybot
- **Stars**：2
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：makes a reddit story generator that takes a link of a reddit story and then ties it to an AI voice over. at the end it straps everyting together with a caption overlay and a random funny video background
- **本地描述**：makes a reddit story generator that takes a link of a reddit story and then ties it to an AI voice over. at the end it straps everyting together with a caption overlay and a random funny video background
- **拉取时间**：2026-07-23 23:13:13

---

# Storybot 🎥🤖

Storybot is a full-stack web application that automatically transforms Reddit stories into short-form videos, complete with AI voiceovers, background gameplay clips, and captions.  

Designed for creators who want to publish consistent, engaging content on platforms like Instagram Reels, TikTok, and YouTube Shorts — Storybot handles the entire pipeline from scraping to rendering.

---

## 🚀 Features

- **Reddit Scraper** → Pulls trending or custom Reddit posts (title + body) via Reddit API.  
- **AI Voiceover** → Converts text to natural-sounding narration.  
- **Background Video Selector** → Automatically fetches gameplay or stock clips (e.g., GTA ramps, Minecraft parkour, FailArmy).  
- **Video Composition** → Merges voiceover + background + captions into a polished vertical short (1080x1920).  
- **Content Cleaning** → Removes unwanted text (usernames, links, profanity if configured).  
- **Batch Mode** → Queue and generate multiple stories at once.  
- **Web Interface** → Dashboard to start jobs, preview results, and download videos.

---

## 🛠️ Tech Stack

**Frontend**  
- React + Vite + TailwindCSS  
- Custom color palette:  
  - `#2ba7d0` (blue)  
  - `#793200` (brown)  
  - `#ffeace` (cream)  
  - `#8f7158` (tan)  
- Authentication (planned) for managing queues and downloads  

**Backend**  
- Node.js + Express  
- REST APIs for each pipeline stage:  
  - `/fetch-posts` → Reddit scraper  
  - `/text-to-speech` → AI voiceover  
  - `/search-video` → Background clips  
  - `/compose-video` → Final rendering  

**Other Components**  
- **Reddit API (OAuth)** for fetching posts  
- **FFmpeg** for audio/video processing  
- **Docker Compose** for containerized frontend + backend  
- (Optional) Python CLI for local experiments  

---

## 📂 Project Structure

storybot/
│
├── backend/ # Express API services
│ ├── routes/ # Reddit, TTS, Video, Compose endpoints
│ ├── services/ # Core logic for scraping and processing
│ └── Dockerfile
│
├── frontend/ # React + Vite app
│ ├── src/
│ │ ├── components # UI widgets
│ │ ├── pages # Dashboard views
│ │ └── assets # Logo, styles
│ └── Dockerfile
│
├── docker-compose.yml
└── README.md

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## ⚡ Getting Started

### Prerequisites
- Node.js (>= 18)  
- Docker & Docker Compose  
- Reddit API credentials (Client ID + Secret)  
- FFmpeg installed locally (for testing outside Docker)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/storybot.git
   cd storybot

