---
id: tool-07449
type: tool
area: 库
status: active
tags: [TTS, Python, 协议传染, 需API密钥, 英文文档]
title: webnovelreader
summary: 小说转语音/有声书
source: https://github.com/nabeelshar/webnovelreader
created: 2026-07-18
updated: 2026-07-18
no: 7449
category: 画龙补充 / 扩容入库 — 补充源
repo: nabeelshar/webnovelreader
stars: 26
url: https://github.com/nabeelshar/webnovelreader
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/QUICK_START.md
---

# nabeelshar/webnovelreader

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/nabeelshar/webnovelreader
- **Stars**：26
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：books, novel, novels, reading, story, webnovel, webnovels, wuxia, wuxiaworkd
- **GitHub 描述**：A webnovel reader app for Android with translation and offline reading features
- **本地描述**：webnovelreader
- **拉取时间**：2026-07-25 19:22:13

---

 

# NovelDokusha
Android web novel reader. Reader focused on simplicity, improving reading immersion.
Search from a large catalog of content, open your pick and just enjoy.

> **Note**: This is an actively maintained fork by [@Nabeelshar](https://github.com/Nabeelshar). The [original repository](https://github.com/nanihadesuka/NovelDokusha) is no longer actively maintained.

# License
Copyright © 2023, [nani](https://github.com/nanihadesuka), Released under [GPL-3](LICENSE) FOSS

## Features
  - **Live translation** - Google Translate with optional Gemini AI
  - **Auto-detect source language** when translating chapters
  - **Bring your own Google Translate key** (free; see [docs/GOOGLE_TRANSLATE_API_KEY.md](docs/GOOGLE_TRANSLATE_API_KEY.md))
  - **Multiple sources** from where to read novels:
    - **Chinese Sources** (with GBK encoding support):
      - 69书吧 (69shuba.com) - With automatic Cloudflare bypass
      - UU看书 (uukanshu.net)
      - 顶点小说 (ddxss.cc)
      - 乐阅读 (27k.net)
      - Twkan (twkan.com)
    - Additional English and international sources
  - **Multiple databases** to search for novels
  - **Local source** to read local EPUBs
  - **Easy backup and restore**
  - **Light and dark themes**
  - Follows modern **Material 3** guidelines
  - **Advanced Reader Features**:
    - Infinite scroll
    - Custom font, font size
    - **Live translation** with Gemini AI
    - **Text to speech**:
      - Background playback
      - Adjust voice, pitch, speed
      - Save your preferred voices
  - **Automatic Cloudflare bypass** - Seamless access to protected sources

  
## Screenshots
 
|              Library               |                Finder                |
|:----------------------------------:|:---------------------------------related:
  - methods/QUICK_START.md
---:|
|    ![](screenshots/library.png)    |     ![](screenshots/finder.png)      |
|             Book info              |            Book chapters             |
|   ![](screenshots/book_info.png)   |  ![](screenshots/book_chapers.png)   |
|               Reader               |           Database search            |
|    ![](screenshots/reader.png)     | ![](screenshots/database_search.png) |
|           Global search            |                                      |
| ![](screenshots/global_search.png) |                                      |

## Tech stack
  - Kotlin
  - XML views
  - Jetpack compose
  - Material 3
  - Coroutines
  - LiveData
  - Room (SQLite) for storage
  - Jsoup
  - Okhttp
  - Coil, glide
  - Gson, Moshi
  - Google MLKit for translation
  - Android TTS
  - Android media (TTS playback notification controls)
