---
id: tool-04987
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Phishing-Email-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/billuramukhtarova/ai-phishing-email-detector
created: 2026-07-18
updated: 2026-07-18
no: 4987
category: 一、去 AI 味 / Humanizer 库
repo: billuramukhtarova/AI-Phishing-Email-Detector
stars: 0
url: https://github.com/billuramukhtarova/ai-phishing-email-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 34d414169b236ca7
  - methods/改稿润色指令库.md
---

# billuramukhtarova/AI-Phishing-Email-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/billuramukhtarova/ai-phishing-email-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A cybersecurity tool that detects possible phishing emails using text, sender, and link analysis.
- **本地描述**：A cybersecurity tool that detects possible phishing emails using text, sender, and link analysis.
- **拉取时间**：2026-07-25 18:02:00

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Phishing Email Detector

This project is a cybersecurity tool that detects possible phishing emails.

## Features

- Email text analysis
- Sender email check
- Link checker
- TXT file upload
- Analysis history
- AI-style explanation

## Tools Used

- Python
- Streamlit
- Regular Expressions
- URL Parsing
- CSV / Excel history

## How It Works

The system analyzes the email text, sender address, and links.  
It gives a risk score and explains why the email may be suspicious.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

# If we are in the Power Shell(PS). We have to go venv

```PS
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate

```(venv)PS
python -m pip install streamlit
python -m streamlit run app.py
