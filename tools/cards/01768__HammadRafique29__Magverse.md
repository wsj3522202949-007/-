---
id: tool-01768
type: tool
area: 库
status: active
tags: [TTS, HTML, 协议宽松, 本地优先, 英文文档, 本地写作]
title: Magverse
summary: 小说转语音/有声书
source: https://github.com/hammadrafique29/magverse
created: 2026-07-18
updated: 2026-07-18
no: 1768
category: 二、网文 / 长篇 AI 写作系统 库
repo: HammadRafique29/Magverse
stars: 4
url: https://github.com/hammadrafique29/magverse
tier: "B"
use_case: "小说转语音/有声书"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: bd5913f9e09712e8
  - methods/最强写作方法论_全球最强综合版.md
---

# HammadRafique29/Magverse

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hammadrafique29/magverse
- **Stars**：4
- **语言**：HTML
- **License**：Apache-2.0
- **Topics**：ai, automation, image-generation, ollama, story-generation, story-teller, storytelling, video-generation
- **GitHub 描述**：🎬 Presenting the AI Story Video Generator — a powerful desktop app that turns a single line of story idea ✍️ into a full story video 📽️. Powered entirely by open-source tools including Ollama AI, 🖼️ image generation models, and 🎧  xtts-v2 for voice narration.
- **本地描述**：🎬 Presenting the AI Story Video Generator — a powerful desktop app that turns a single line of story idea ✍️ into a full story video 📽️. Powered entirely by open-source tools including Ollama AI, 🖼️ image generation models, and 🎧  xtts-v2 for voice narration.
- **拉取时间**：2026-07-23 23:30:34

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 🎬 AI Story Video Generator

Turn a single line of text ✍️ into a complete story video 📽️, all on your desktop!
**AI Story Video Generator** is a powerful and creative Electron-based desktop app that uses cutting-edge open-source AI tools to generate story-based videos from just a one-line idea.

- [**Contact Developer For Backend**](mailto:hammadrafique029@gmail.com?subject=Support%20Request&body=Hi%20Mag%2C%0AI%20want%20backend%20code...)
- hammadrafique029@gmail.com

<br>

## ✨ Features

- 🧠 Powered by **Ollama AI** for text-to-story generation
- 🖼️ Uses open-source **image generation models** to visualize scenes
- 🎧 Integrated with **xtts-v2** for natural-sounding voice narration
- 🖥️ Cross-platform desktop app built with **Electron**
- 🔓 100% open-source — customize or extend as you wish!

<br>

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/HammadRafique29/AI-Story-Video-Generator.git
cd AI-Story-Video-Generator
````


### 2. Install Dependencies

Make sure you have [Node.js and npm](https://nodejs.org/en/download/) installed.

```bash
npm install
```



### 3. Install Ollama

Ollama is used to run local AI models like `llama2`, `mistral`, or `gemma`.
Follow official instructions here: [https://ollama.com/download](https://ollama.com/download)


```bash
ollama run llama2
```


### 4. Install xtts-v2 (Text-to-Speech)

You’ll need to set up `xtts-v2` locally. The easiest way is using Docker. Below command will starts the TTS service used to narrate your generated story.

```bash
docker run -it -p 8020:8020 cugui/xtts-api
```



### 5. Run the App

```bash
npm start
```


<br>

## 📁 Project Structure

```
📦AI-Story-Video-Generator
├── 📜main.js                # Electron main process
├── 📜preload.js             # Preload script to expose APIs to renderer
├── 📜package.json
├── 📁renderer/              # Frontend files (HTML/CSS/JS)
│   ├── 📜index.html
│   ├── 📁styles/
│   │   └📜main.css
│   └── 📁scripts/
│       ├📜main.js           # Handles routing, UI logic
│       └📜api.js            # API call functions
├── 📁backend/               # Custom API logic handled by Node
│   └── 📁routes/
│       ├📜index.js          # API route registration
│       └📜example.js        # Example API route
├── 📁public/                # Static files (images, icons)
│   └📜favicon.ico
└── 📁assets/                # Optional: Fonts, sounds, etc.
```


## 🚀 Coming Soon

* GUI for selecting voice/speaker
* Model selection for advanced users
* Export options (MP4, GIF)
* Story templates & genres



## 📄 License

This project is licensed under the **MIT License**, feel free to use, modify, and distribute.


## 🙌 Credits

Made with ❤️ by **Hammad Rafique**.
 Thanks to the open-source community for Ollama, xtts-v2, and the amazing image generation models that make this magic possible! 💫

## 🤝 Contributing

PRs and suggestions welcome! Open an issue or submit a pull request if you'd like to improve or extend the app.


## 💬 Questions?

Feel free to reach out via [GitHub Issues](https://github.com/HammadRafique29/AI-Story-Video-Generator/issues)
