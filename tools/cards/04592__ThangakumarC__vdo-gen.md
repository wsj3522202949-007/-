---
id: tool-04592
type: tool
area: 库
status: active
tags: [TTS, Python, 协议未明, 需API密钥, 英文文档]
title: vdo-gen
summary: 小说转语音/有声书
source: https://github.com/thangakumarc/vdo-gen
created: 2026-07-18
updated: 2026-07-18
no: 4592
category: 五、写作 IDE / 本地优先工作台 库
repo: ThangakumarC/vdo-gen
stars: 1
url: https://github.com/thangakumarc/vdo-gen
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e24b7d09e92cd71a
  - methods/QUICK_START.md
---

# ThangakumarC/vdo-gen

- **分类**：五、写作 IDE / 本地优先工作台 库
- **链接**：https://github.com/thangakumarc/vdo-gen
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：elevenlabs, imagemagick, mistral-7b-instruct, n8n, openrouter, pexelsapi
- **GitHub 描述**：AI-powered short video generator that automatically creates motivational stories with stock footage, text overlays, voice narration, background music, and uploads to YouTube via n8n automation.
- **本地描述**：AI-powered short video generator that automatically creates motivational stories with stock footage, text overlays, voice narration, background music, and uploads to YouTube via n8n automation.
- **拉取时间**：2026-07-25 17:49:39

related:
  - methods/QUICK_START.md
---

# AI-Powered Video Generator

**Automated short motivational video generator with YouTube integration.**


## Overview

This project automatically creates short motivational videos using AI-generated stories, stock footage, text overlays, voice narration, and background music. Videos are then automatically uploaded to YouTube using an n8n workflow, with email notifications upon completion.


## Features

- Generates a **motivational story** with 6–8 scenes, including **title**, **description**, and **tags** using Mistral.
- Searches for **matching stock videos** from Pexels API.
- Converts story text into **voice narration** using ElevenLabs TTS.
- Adds **subtitles** and **background music** using MoviePy.
- Automatically uploads final video to **YouTube** via n8n.
- Sends **email notifications** once the video is uploaded.
- Handles **temporary files cleanup** automatically.


## Tech Stack

- Python (MoviePy, Requests)
- ImageMagick
- ElevenLabs Text-to-Speech API
- Pexels Video API
- OpenRouter API (mistral-7b-instruct) 
- n8n for workflow automation
- Gmail API for notifications


## Installation

1. Install ImageMagick (make sure it’s added to PATH):
   
2. Clone the repository:

```
git clone https://github.com/ThangakumarC/vdo-gen.git
cd vdo-gen
```
3. Install dependencies:
```
   pip install -r requirements.txt
```
4. Set up API keys in .env:

   PEXELS_API_KEY
   
   ELEVENLABS_API_KEY
   
   OPENROUTER_API_KEY

## Run the Python script to generate videos:
```
  python app.py
```
Temporary files are created for each scene and audio, then cleaned automatically.
Final video and metadata are saved in C:/n8n_temp for n8n workflow.

## n8n Workflow Automation

The n8n workflow (VdoGen) triggers the script, uploads the video to YouTube, and sends an email notification.

Workflow handles reading metadata and video files, merging them, uploading, and cleaning up temporary files.

Import **VdoGen.json** into your n8n instance.
It automates:

- Running the Python script

- Reading generated video + metadata

- Uploading to YouTube with captions and tags

- Sending notification email

- Cleaning temp files

Workflow Screenshot:
<img width="1132" height="451" alt="Screenshot 2025-10-12 231127" src="https://github.com/user-attachments/assets/51979a10-408c-4f08-9694-537d4066c8c8" />

Final Generated video:
https://github.com/user-attachments/assets/170feb77-951b-49d4-b036-7ecba023d301

Email Screenshot:
<img width="1045" height="345" alt="image" src="https://github.com/user-attachments/assets/6627f830-95c2-41e5-8838-0b0b8141f842" />


