---
id: tool-05197
type: tool
area: 库
status: active
tags: [去AI味, JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: text-tools-humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/biswa2das/text-tools-humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5197
category: 一、去 AI 味 / Humanizer 库
repo: Biswa2Das/text-tools-humanizer
stars: 0
url: https://github.com/biswa2das/text-tools-humanizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Biswa2Das/text-tools-humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/biswa2das/text-tools-humanizer
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A privacy-focused Chrome extension that humanizes text using a local LLM (LM Studio). No cloud calls. No data leaves your machine. Customize tone, perspective, style, and even auto-mask PII before rewriting.
- **本地描述**：A privacy-focused Chrome extension that humanizes text using a local LLM (LM Studio). No cloud calls. No data leaves your machine. Customize tone, perspective, style, and even auto-mask PII before rewriting.
- **拉取时间**：2026-07-25 18:09:41

---

## **Text Tools – Humanizer AI (Chrome Extension)**

A privacy-focused Chrome extension that humanizes text using a **local LLM** (LM Studio). No cloud calls. No data leaves your machine.
Customize tone, perspective, style, and even auto-mask PII before rewriting.

---

## 🚀 Features

### ✅ **Humanize Text Using Local LLM**

* Works offline using **LM Studio**
* Adjustable **tone**, **style**, and **perspective**
* Designed for clarity, readability, and natural-sounding results

### ✅ **Privacy First**

* Mask PII before rewriting (emails, phones, names)
* Option to restore PII afterward
* Nothing is sent to the internet — ever

### ✅ **Polished UI**

* Clean, responsive popup interface
* Advanced options panel
* Live word + character count
* Copy-to-clipboard
* Keyboard shortcut: **Ctrl + Enter**

---

## 📦 Files Overview

| File            | Purpose                                                           |
| --------------- | ----------------------------------------------------------------- |
| `manifest.json` | Chrome extension manifest (Manifest V3)                           |
| `popup.html`    | Extension popup UI                                                |
| `popup.js`      | Full logic for LLM requests, PII masking, UI state, and rewriting |
| `icons/`        | Extension icons (16/48/128px)                                     |

---

## 🔧 Requirements

### ✅ LM Studio Running Locally

This extension expects LM Studio at:

```
http://localhost:1234/v1/chat/completions
```

Be sure to:

1. Open LM Studio
2. Load and **start a model** (e.g., `llama-3.2-3b-instruct`)
3. Enable the **local HTTP server**

---

## 🧪 How to Load the Extension in Chrome (Developer Mode)

1. Open **chrome://extensions**
2. Enable **Developer mode** (top right)
3. Click **Load unpacked**
4. Select your extension folder (the one containing `manifest.json`)

You should now see the extension in your toolbar 🎉

---

## 📁 Project Structure

```
text-tools-humanizer/
│── manifest.json
│── popup.html
│── popup.js
│── icons/
│     ├── icon16.png
│     ├── icon48.png
│     └── icon128.png
└── README.md
```

---

## 🛠 How It Works (Short Explanation)

* The text is optionally masked using the **PIIMasker** class
* A dynamic prompt is created based on:

  * text length
  * tone
  * style
  * perspective
* Extension sends request to LM Studio running locally
* Response is cleaned by `PostProcessor`
* PII is optionally restored
* Output is placed in UI

Everything is fully local.

---

## ✅ Roadmap / Future Ideas

* Add custom model selection
* Add "rewrite multiple versions"
* Add export functionality
* Option to save presets

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📜 License

MIT License 

