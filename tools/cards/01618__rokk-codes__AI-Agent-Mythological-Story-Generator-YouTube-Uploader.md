---
id: tool-01618
type: tool
area: 库
status: active
tags: [TTS, Python, 协议未明, 需API密钥, 英文文档]
title: AI-Agent-Mythological-Story-Generator-YouTube-Uploader
summary: 小说转语音/有声书
source: https://github.com/rokk-codes/ai-agent-mythological-story-generator-youtube-uploader
created: 2026-07-18
updated: 2026-07-18
no: 1618
category: 二、网文 / 长篇 AI 写作系统 库
repo: rokk-codes/AI-Agent-Mythological-Story-Generator-YouTube-Uploader
stars: 1
url: https://github.com/rokk-codes/ai-agent-mythological-story-generator-youtube-uploader
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# rokk-codes/AI-Agent-Mythological-Story-Generator-YouTube-Uploader

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rokk-codes/ai-agent-mythological-story-generator-youtube-uploader
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：rokk-codes/AI-Agent-Mythological-Story-Generator-YouTube-Uploader
- **拉取时间**：2026-07-23 23:26:13

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Mythological Story Generator & YouTube Uploader (Automated AI Images)

This repo automates the creation and publishing of AI-generated mythological stories with AI voiceover, AI-generated scene images, and video upload to YouTube.

## Features

- **AI Story Generation:** Uses GPT-4 (or compatible LLM) for unique mythological stories.
- **Scene Extraction:** Splits story into scenes for image prompts.
- **AI Image Generation:** Uses OpenAI DALL·E for scene images (swap for Stable Diffusion API if preferred).
- **Text-to-Speech:** Converts story to narrated audio using ElevenLabs.
- **Video Creation:** Combines narration with generated images into a video.
- **YouTube Upload:** Publishes the video automatically to your channel.

## Setup

1. **Clone the repo and install dependencies:**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   pip install -r requirements.txt
   ```

2. **Environment Variables:**
   - `OPENAI_API_KEY`: Your OpenAI API key (for story & image generation).
   - `ELEVENLABS_API_KEY`: Your ElevenLabs API key.
   - `ELEVENLABS_VOICE_ID`: Your desired ElevenLabs voice ID.

3. **YouTube API Setup:**
   - Follow [YouTube Data API v3 guide](https://developers.google.com/youtube/v3/guides/uploading_a_video) to obtain OAuth credentials.
   - Save your `client_secrets.json` in the repo directory.

## Usage

Run the main script:
```bash
python main.py
```

## Customization

- Edit the story prompt in `main.py` for different mythologies.
- To use another image API (e.g., Stability AI), update `image_gen.py`.

## License

MIT
