---
id: tool-05357
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Eclipsis
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/spectrixdev/eclipsis
created: 2026-07-18
updated: 2026-07-18
no: 5357
category: 一、去 AI 味 / Humanizer 库
repo: SpectrixDev/Eclipsis
stars: 4
url: https://github.com/spectrixdev/eclipsis
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8c9a0d3d3ac79446
  - methods/改稿润色指令库.md
---

# SpectrixDev/Eclipsis

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/spectrixdev/eclipsis
- **Stars**：4
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-Powered Paraphrase Tool: A Flask web app that lets you generate text with Ollama, and rewrite it sentance by sentance to avoid AI Detectors with the help of tools.
- **本地描述**：AI-Powered Paraphrase Tool: A Flask web app that lets you generate text with Ollama, and rewrite it sentance by sentance to avoid AI Detectors with the help of tools.
- **拉取时间**：2026-07-25 18:15:35

---

# Eclipsis
> An AI-Powered Paraphrasing Tool 🤖

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![Flask](https://img.shields.io/badge/Framework-Flask-orange.svg)](https://flask.palletsprojects.com/en/2.0.x/)
=============================

A Flask web app I made for fun in an hour or two that lets you generate text with any LLM locally through [Ollama](https://ollama.com/), and rewrite it sentence by sentence to avoid AI Detectors with the help of tools.

## What is this? 🤔
[![Index](https://i.imgur.com/iXKA6Zz.png)](https://i.imgur.com/iXKA6Zz.png) [![ParaphrasePage](https://i.imgur.com/2hz7qBE.png)](https://i.imgur.com/2hz7qBE.png)

This project is a web-based tool that uses AI-powered language generation to help users paraphrase sentences and avoid detection by AI-powered plagiarism detectors. The tool allows users to choose any Language Model (LLM) through Ollama to generate new sentences and rewrite them sentence by sentence to create unique content.


**How does it work?** 🤔
------------------

1. Users input a sentence or paragraph into the tool.
2. Use any LLM you like from Ollama, run locally on your device.
3. The user can then rewrite the generated sentence or paragraph sentence by sentence to create a unique piece of writing.
4. The tool provides a side-by-side comparison of the original sentence and the rewritten sentence, allowing users to easily compare and refine their work.

Why? It's an easy way to generate a piece of writing with AI and then write it in your own words, allowing you to decide if you want to rephrase anything, keep it the same, etc. It also let's you evade AI detectors such as GPTZero confidently.

**Setup** 🛠
------
### Clone the Repository

To get started, clone this repository to your local machine using Git:

```markdown
git clone https://github.com/SpectrixDev/Eclipsis.git
```

### Install Requirements

Next, install the required dependencies using pip:

```markdown
pip install -r requirements.txt
```

### Download Ollama and a model of your choice
Download some models from [Ollama](https://ollama.com/library). Make sure to follow the instructions on the Ollama website for downloading and installing the models. The program should automatically know what models are installed on your machine (tested on Windows)

### Run the Web App

Lastly, run the web app using Python:

```markdown
python app.py
```

This will start the Flask development server, and you can access the web app by navigating to `http://localhost:5000` in your web browser.
		

-----------
**License** 📝
-------

This project is licensed under the MIT License. See the LICENSE file for details.

**Contributing** 🤝
---------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

Contributions are welcome! This was rushed for fun. If you'd like to help improve this project, please fork the repo and submit a pull request.
