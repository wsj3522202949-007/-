---
id: tool-04205
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: AI-song-generator-app
summary: 润色/改写/扩写等通用文本处理
source: https://github.com/sueson/ai-song-generator-app
created: 2026-07-18
updated: 2026-07-18
no: 4205
category: 十、其他 AI 写作 / 文本工具 库
repo: sueson/AI-song-generator-app
stars: 0
url: https://github.com/sueson/ai-song-generator-app
tier: "C"
use_case: "润色/改写/扩写等通用文本处理"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4684423c19aaab5a
  - methods/QUICK_START.md
---

# sueson/AI-song-generator-app

- **分类**：十、其他 AI 写作 / 文本工具 库
- **链接**：https://github.com/sueson/ai-song-generator-app
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A mobile app that generates songs from user-written stories or lyrics using OpenAI, Suno APIs, and Genius APIs.
- **本地描述**：A mobile app that generates songs from user-written stories or lyrics using OpenAI, Suno APIs, and Genius APIs.
- **拉取时间**：2026-07-24 00:04:56

related:
  - methods/QUICK_START.md
---

## Get started

1. Install dependencies

   ```bash
   npm install
   ```

2. Start the app

   ```bash
   node index.js
   ```

   ```bash
    npx expo run:android
   ```


## If the song credits gets over
1. Go to https://www.musicapi.ai/
2. Login and generate api key and put the key in /backend/.env/MUSIC_API_BEARER_TOKEN
3. Then the app will generate songs like usual.

## Screenshots of the application

<div style="display:flex; align-items:center; justify-content: center; gap: 10px">
   <img src="./assets/images/onboarding page.png" width="400" alt="onBoarding page">
   <img src="./assets/images/Sign up.png" width="400" alt="sign-up page">
</div>

<div style="display:flex; align-items:center; justify-content: center; gap: 10px; margin-top: 10px">
   <img src="./assets/images/Sign in.png" width="400" alt="onBoarding page">
   <img src="./assets/images/Home-screen.png" width="400" alt="sign-up page">
</div>

<div style="display:flex; align-items:center; justify-content: center; gap: 10px; margin-top: 10px">
   <img src="./assets/images/Song player-screen.png" width="400" alt="onBoarding page">
   <img src="./assets/images/search-song-api.png" width="400" alt="sign-up page">
</div>
