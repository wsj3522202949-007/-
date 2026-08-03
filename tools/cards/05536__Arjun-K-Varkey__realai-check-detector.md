---
id: tool-05536
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: realai-check-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/arjun-k-varkey/realai-check-detector
created: 2026-07-18
updated: 2026-07-18
no: 5536
category: 一、去 AI 味 / Humanizer 库
repo: Arjun-K-Varkey/realai-check-detector
stars: 2
url: https://github.com/arjun-k-varkey/realai-check-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Arjun-K-Varkey/realai-check-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/arjun-k-varkey/realai-check-detector
- **Stars**：2
- **语言**：Python
- **License**：None
- **Topics**：ai-detection, deepfake, fact-checking, huggingface, ifcn, misinformation, python3
- **GitHub 描述**：Open-source prototype for detecting AI-generated text and fact-checking claims in news articles. Supports RealAI Check fact-checking initiative.
- **本地描述**：Open-source prototype for detecting AI-generated text and fact-checking claims in news articles. Supports RealAI Check fact-checking initiative.
- **拉取时间**：2026-07-25 18:22:19

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

# RealAI Check – AI Misinformation Detector Prototype

An open-source tool to detect potential AI-generated text and fact-check claims in news articles. Built to support transparent, **IFCN-aligned** verification.

Part of the [RealAI Check](https://arjun-k-varkey.github.io/realaicheck.github.io/) independent fact-checking project focused on AI-generated misinformation and deepfakes.

## Features

- Detects if article text is likely AI-generated (Hugging Face RoBERTa model)
- Extracts key factual claims with strict filtering
- Performs balanced web searches for supporting and challenging evidence
- Outputs structured JSON report
- Automatically saves reports with timestamp

## How to Run (Easy Setup)

1.  **Clone or Download This Repo**
    ```bash
    git clone https://github.com/Arjun-K-Varkey/realai-check-detector.git
    cd realai-check-detector
    ```

2.  **Set Up Python Environment (Recommended)**
    ```bash
    python3 -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    
    Note: First run downloads large models (~1–2 GB). Only happens once!
    ```    

4.  **Run the Detector**
    ```bash
    python3 misinfo_detector.py
    
    Enter any news article URL when prompted.
    ```
    
5.  **Output**
    ```bash
    Full analysis printed in terminal
    
    Report saved as JSON in the reports/ folder
    Example filename: misinfo_report_20260103_152833.json
    ```
    **Sample Output**
    ```bash
    See a real analysis of the January 3, 2026 Venezuela/U.S. strikes event:
    reports/misinfo_report_20260103_152833.json
    ```
    **Example URLs to Test**
    ```bash
    BBC: https://www.bbc.com/news/articles/ce3ewqew4weo
    AP News (Venezuela event): https://apnews.com/article/venezuela-us-explosions-caracas-ca712a67aaefc30b1831f5bf0b50665e
    ```

## Limitations
    
- AI detector trained on older models (~80–90% accuracy on modern text)
- Fact-checking uses automated web search — always verify manually
- Works best on single news articles (not homepages)
           
## Contributing

- Found a bug? Want to improve claim extraction or add features? Open an issue or pull request!
- Made by ArKaVi Team – January 2026
- Human verification is always required — this is a prototype to assist, not replace, fact-checking.
   
