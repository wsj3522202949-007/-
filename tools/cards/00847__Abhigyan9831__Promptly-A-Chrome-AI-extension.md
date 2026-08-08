---
id: tool-00847
type: tool
area: 库
status: active
tags: [校对, JavaScript, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: Promptly-A-Chrome-AI-extension
summary: 错别字/语法/风格校对
source: https://github.com/abhigyan9831/promptly-a-chrome-ai-extension
created: 2026-07-18
updated: 2026-07-18
no: 847
category: 二、网文 / 长篇 AI 写作系统 库
repo: Abhigyan9831/Promptly-A-Chrome-AI-extension
stars: 0
url: https://github.com/abhigyan9831/promptly-a-chrome-ai-extension
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: c8175add78f768c5
  - methods/最强写作方法论_全球最强综合版.md
---

# Abhigyan9831/Promptly-A-Chrome-AI-extension

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/abhigyan9831/promptly-a-chrome-ai-extension
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A Chrome-integrated AI assistant powered by Gemini Nano for writing, translation, and summarization.
- **本地描述**：A Chrome-integrated AI assistant powered by Gemini Nano for writing, translation, and summarization.
- **拉取时间**：2026-07-23 23:03:43

---

[README.md](https://github.com/user-attachments/files/23266089/README.md)

# Promptly

Promptly is an elegant Chrome extension that brings the power of on-device AI directly into your browser. It allows you to summarize, translate, rewrite, proofread, generate content, and even analyze images and uploaded files — all through a simple, intuitive interface.


---


## Features

### Multifunctional AI Modes

- **Prompt Mode** — Chat freely with an AI assistant or analyze uploaded images. Learning, questions and suggestions. Code Review etc.
- **Summarization Mode** — Generate concise summaries for long passages.
- **Translation Mode** — Translate text between 11 languages with ease.
- **Writer /  Rewriter /  Proofreader** — Create, improve, or correct writing seamlessly.


### Accessibility & Multilingual UI
- Full UI translations for **11 languages**: English, Chinese, Japanese, Russian, Polish, Spanish, French, German, Korean, Arabic, and Portuguese.
- Dynamic UI adaptation via the `start.js` multilingual dictionary.


### File Support
- Upload text files, **PDFs**, **Word documents**, or **images** (JPG, PNG, etc.).
- See the name and file type directly in the text area.
- Images are processed through multimodal AI for analysis.
- (Future versions: integrate OCR to read text from images & memes.).

### Image Analysis
Supports multimodal input:
- Extract text (OCR)
- Describe diagrams or code screenshots
- Generate accessibility descriptions for the visually impaired.

### Voice & Read Aloud Support

- Voice input (future feature)

- Text-to-Speech playback for generated results.(future feature)

---



## Project Structure


```plaintext
Promptly/
│
├── background.js # Handles extension click events (opens start.html in a new tab)
├── start.html # Main UI and styling for the extension
├── start.js # Core logic, multilingual support, and AI mode handling
├── manifest.json 
└── icons_1.jpeg #  Folder for icons or images


## Example `manifest.json`

Create this file in your root directory:

```




---
## How it works

Promptly uses Chrome’s experimental **on-device AI APIs**, such as:

- LanguageModel (general reasoning & multimodal)

- Summarizer

- Translator

- Rewriter

- Writer

- Proofreader

These APIs run locally (after download) for privacy and offline access.

Note: These experimental APIs require Chrome Canary or Dev Channel with specific flags enabled (see setup below).
## Installation

- **Download the Project**

        git clone https://github.com/Abhigyan9831/Promptly-A-Chrome-AI-extension.git
    Or download the ZIP and extract it.
- **Open Chrome Extensions**
    - Go to chrome://extensions
    - Enable Developer Mode(Top Right of the Web Page)
- **Load the Extension**
    - Click *Load unpacked*
    - Select the extracted folder containing manifest.json
- **Launch**
    - Click the 🧩 Extensions icon → Promptly
    - The popup interface will appear with new webpage.

    related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
        


## Chrome Experimental Setup

Note: Promptly relies on on-device AI models still under development.

To enable them:
- Use Official Chrome Build v144+ stable build or Chrome Canary (v128+). Mostly Latest
  chrome version works most cases.
- Visit:
  chrome://flags/#optimization-guide-on-device-model
-   Enable:

    -  Optimization guide on device model

    -  Prompt API

    - Summarizer API

    - Translator API

    - Rewriter API

    - Writer API
- Relaunch Chrome.
Once enabled, the models will automatically download the first time you use them.
## Usage

- Click on the Promptly icon in your Chrome toolbar. The popup will open in a tab (handled by background.js).


- Choose one of the AI modes:

- Summarize, Translate, Ask or Learn or Question anything using Prompt, Learn, Write, Rewrite, or Proofread for correcting errors.

- Optionally:

    - Upload a text file or image for analysis.

    - Select your UI language from the dropdown.

    - Click "Search (🔍)" button for AI to process your input.

    - Wait for sometime and then view your result.

## Demonstration Video
- How the extension is installed and launched.
- Each mode (Summarization, Translation, Writer, etc.) in action.
- Image and text input examples.
- Explanation of APIs and tools used.

YouTube : https://youtu.be/zagkeXzKwb0
## Technical Highlights

- Modular structure for **future API** fallbacks and **OCR integration**.
- Built-in multilingual support with a centralized translation object.
- Async typeWriterEffect() for realistic typing.
- Cleanly managed state for selected modes, languages, and attached files.


## Upcoming Enhancements

- Full speech recognition for voice input.
- Improved read-aloud control panel.
- Persistent history of prompts and results.
## Developer Notes
- This extension uses experimental features and may not work on all Chrome builds.
- To debug: open the popup, then press Right-click → Inspect.
- Logs and AI progress appear in the Console tab.
## Privacy
Promptly processes data locally using on-device AI APIs.
Your files and text never leave your computer unless explicitly sent through a third-party model (if added in the future). Promptly all time for new prompt it creates a new session locally and never store the search or inference data in any Database, it temporarily stores the ddata locally on your RAM once the window or page is refreshed the data is completely flushed out.
## License

[MIT](https://choosealicense.com/licenses/mit/)

This project is released under the MIT License.
You are free to use, and distribute it — just include attribution.

## Credits

Built with passion by Abhigyan Bhattacharya.
Designed for creators, researchers, and students who love productivity and learning.

