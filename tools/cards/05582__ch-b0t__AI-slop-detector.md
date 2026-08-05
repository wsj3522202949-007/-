---
id: tool-05582
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 需API密钥, 英文文档, 去AI味]
title: AI-slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ch-b0t/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5582
category: 一、去 AI 味 / Humanizer 库
repo: ch-b0t/AI-slop-detector
stars: 1
url: https://github.com/ch-b0t/ai-slop-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ch-b0t/AI-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ch-b0t/ai-slop-detector
- **Stars**：1
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI generated text detector extension for chrome
- **本地描述**：AI generated text detector extension for chrome
- **拉取时间**：2026-07-25 18:24:02

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Slop Detector Chrome Extension

A Chrome extension that detects AI-generated text with a Google Translate-style interface. Simply highlight text on any webpage, and get an AI detection score from 1-10. Setup requires users to have an anthropic API key

!`[AI Slop Detector Demo](assets/ai-detector-poc-gif.gif)`

## Features

- **Google Translate-style UI**: Floating icon appears when text is selected
- **AI Detection**: Uses Anthropic's Claude API to analyze text
- **Clean Interface**: Minimal, non-intrusive popup panel
- **Toggle On/Off**: Easy extension control via popup menu
- **Smart Selection**: Automatically ignores text in editable fields

## Installation

1. Clone or download this repository
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable "Developer mode" (toggle in top-right)
4. Click "Load unpacked"
5. Select the extension directory

## Setup

1. **Add API Key**: 
   - Click the extension icon in Chrome's toolbar
   - Enter your Anthropic API key in the settings (optional - you can also hardcode it in `background.js`)
   - Or edit `background.js` and replace `YOUR_API_KEY_HERE` with your actual API key

2. **Toggle Extension**:
   - Use the ON/OFF toggle in the popup to enable/disable the extension

## Usage

1. Make sure the extension is enabled (toggle is ON)
2. Highlight any text on a webpage
3. Click the floating icon that appears above the selection
4. View the AI detection score (1-10) and reasoning in the popup panel

## Project Structure

```
/extension
  /assets          - Extension icons
  /popup           - Browser action popup (settings)
  /content         - Content script (selection detection)
  /panel           - Detection result panel (iframe)
  background.js    - Service worker (API calls)
  manifest.json    - Extension manifest
```

## Development Notes

- All scripts are external (no inline scripts) to comply with CSP
- Uses Manifest V3
- Panel is isolated in an iframe to prevent CSS conflicts
- Extension respects editable fields (textarea, input, contenteditable)

## API Configuration

The extension uses Anthropic's Claude API. You can:
- Set the API key in the popup settings (stored locally)
- Or hardcode it in `background.js` (line 3)

Default model: `claude-3-sonnet-20240229`

## Icons

You'll need to add icon files to the `assets/` directory:
- `assets/icon16.png`
- `assets/icon32.png`
- `assets/icon48.png`
- `assets/icon128.png`

**Quick Icon Creation:**
1. Open `create_icons.html` in your browser
2. Right-click each canvas and "Save image as..."
3. Save them with the correct names in the `assets/` folder

Alternatively, you can create your own icons using any image editor. The icons should be square PNG files with the specified dimensions.

