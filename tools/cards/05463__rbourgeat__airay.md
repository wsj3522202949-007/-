---
id: tool-05463
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: airay
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/rbourgeat/airay
created: 2026-07-18
updated: 2026-07-18
no: 5463
category: 一、去 AI 味 / Humanizer 库
repo: rbourgeat/airay
stars: 4
url: https://github.com/rbourgeat/airay
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# rbourgeat/airay

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rbourgeat/airay
- **Stars**：4
- **语言**：JavaScript
- **License**：None
- **Topics**：ai, generative-ai, generative-art
- **GitHub 描述**：A simple AI detector (Image & Text)
- **本地描述**：A simple AI detector (Image & Text)
- **拉取时间**：2026-07-25 18:19:37

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AIRAY

A simple Flask-based web app that can detect if an image is AI-generated or if a text is written by AI. Uses OpenAI’s CLIP model for image analysis and a RoBERTa-based model for text analysis.

![demo](./frontend/images/demo.gif)

## Running the App

### Option 1: Run with Docker

1. Requirements:

Download and install Docker from the [Docker website](https://www.docker.com/products/docker-desktop).

2.	Clone the repository:

```bash
git clone https://github.com/rbourgeat/airay.git
cd airay
```

3.	Build and run the containers:

```bash
docker compose up --build
```

4.	The app will be available at [localhost:5042](http://localhost:5042).

### Option 2: Run Natively

1. Requirements:

Download and install Python from the [Python website](https://www.python.org/downloads/).

Download and install Node.js from the [Node.js website](https://nodejs.org/).

2.	Install backend dependencies and start the server:

```bash
git clone https://github.com/rbourgeat/airay.git
cd airay
cd backend
python3 -m pip install -r requirements.txt
python3 main.py
```

3.	Install frontend dependencies and start the server:

```bash
cd ..
cd frontend
npm install
npm run dev
```

4.	The app will be available at [localhost:5042](http://localhost:5042).

## Contributing

If you have suggestions for improving this project or find a bug, feel free to open an issue. Your feedback and contributions are greatly appreciated !
