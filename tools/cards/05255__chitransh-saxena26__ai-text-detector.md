---
id: tool-05255
type: tool
area: 库
status: active
tags: [CSS, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/chitransh-saxena26/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5255
category: 一、去 AI 味 / Humanizer 库
repo: chitransh-saxena26/ai-text-detector
stars: 0
url: https://github.com/chitransh-saxena26/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# chitransh-saxena26/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/chitransh-saxena26/ai-text-detector
- **Stars**：0
- **语言**：CSS
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：chitransh-saxena26/ai-text-detector
- **拉取时间**：2026-07-25 18:11:48

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---


# AI Text Detector

A web-based AI text detection tool that identifies AI-generated text using Hugging Face's Transformers.


## Features

- Detects AI-generated text using RoBERTa-large OpenAI Detector
- Simple Flask backend for API requests
- User-friendly frontend for easy text input and results display
- Cross platform


## Tech Stack

**Backend:** Flask, Transformers(HuggingFace)

**Frontend:** HTML, CSS, JavaScript

## Installation

Clone the repository:

```bash
    git clone https://github.com/chitransh-saxena26/ai-text-detector.git  

    cd ai-text-detector  

```
    
Install dependencies:

```
    pip install -r requirements.txt
```
## Usage

Run the flask 
```python

    python app.py

```
connect the flask with the website using JavaScript
```javascript

    const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text })
    });
```



## Deployment

The flask backend is still not deployed due to the model being too large. And most hosting website offers limited space for free package.
