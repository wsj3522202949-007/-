---
id: tool-05494
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: Bad-LLM-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/artturik/bad-llm-detector
created: 2026-07-18
updated: 2026-07-18
no: 5494
category: 一、去 AI 味 / Humanizer 库
repo: artturik/Bad-LLM-Detector
stars: 2
url: https://github.com/artturik/bad-llm-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# artturik/Bad-LLM-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/artturik/bad-llm-detector
- **Stars**：2
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Bad LLM Detector is a chrome extension that helps you identify AI generated texts while browsing the web
- **本地描述**：Bad LLM Detector is a chrome extension that helps you identify AI generated texts while browsing the web
- **拉取时间**：2026-07-25 18:20:47

---

# Bad LLM Detector

Chrome extension that helps you identify AI generated texts while browsing the web. It highlights words frequently used by large language models (LLMs) to give you quick (but not perfect) clues that the content might be AI generated.

The extension uses a customizable list of words, originally sourced from [FareedKhan-dev/Detect-AI-text-Easily](https://github.com/FareedKhan-dev/Detect-AI-text-Easily).

> **Disclaimer**: Detection is not accurate! The name "BAD" in "Bad LLM Detector" reflects a LOTS of false-positive and false-negative results.

Use this extension as a fun and quick way to identify potential AI-written content, but always verify content sources manually.

---

## Features
- Automatically highlights commonly used LLM words on any webpage
- **Built-in default word list**: Based on LLM-generated text analysis (can be disabled)
- **Custom word lists**: Add your own words
- **Detected words statistic**
- **External word list URLs**: Subscribe to third-party .txt word lists from URLs
- **Enable/disable lists**: Toggle any list on or off without removing it
- Visual badge indicator showing the number of detected words on each page

---

## How to Install (Unpacked Extension)
1. Download or clone this repository to your local machine
   ```bash
   git clone https://github.com/artturik/Bad-LLM-Detector.git
   ```
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable **Developer Mode**
4. Click **Load unpacked**
5. Select the folder where you downloaded/cloned the extension
6. The extension will now appear in your extensions list

---

### Detection Mode
Choose how detected words are displayed on web pages:

#### Highlight Mode (Default)
- Detected words are styled with custom colors, borders, backgrounds, etc.
- The original word remains visible but highlighted
- Configure appearance in the "Highlight Style" section

#### Replace Mode
- Detected words are replaced with custom text
- Default replacement: `Maybe AI: $0`
- Supports `$0` placeholder to include the original word
  - Example: `[$0]` would replace "delve" with "[delve]"

### Adding External Word Lists
1. Go to the Options page
2. Under "External Word Lists", enter:
   - **List URL**: A direct URL to a .txt file (e.g., `https://example.com/llm-words.txt`)
   - **List Name**: A friendly name for the list
3. Click "Add List"
4. The list will be fetched immediately and updated on every browser startup

### Word List Format
External word lists should be plain text files (`.txt`) with:
- One word or phrase per line
- Comments starting with `#` (ignored)
- Empty lines (ignored)

Example:
```
# My LLM words list
Delve
Leverage
# This is a comment
Revolutionary
```

See `example-wordlist.txt` for a complete example.

---

## License
MIT License

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Credits
- Word list inspired by [FareedKhan-dev/Detect-AI-text-Easily](https://github.com/FareedKhan-dev/Detect-AI-text-Easily)
- findAndReplaceDOMText by James Padolsey
