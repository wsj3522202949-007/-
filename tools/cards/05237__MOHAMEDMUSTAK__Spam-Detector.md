---
id: tool-05237
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Spam-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/mohamedmustak/spam-detector
created: 2026-07-18
updated: 2026-07-18
no: 5237
category: 一、去 AI 味 / Humanizer 库
repo: MOHAMEDMUSTAK/Spam-Detector
stars: 1
url: https://github.com/mohamedmustak/spam-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# MOHAMEDMUSTAK/Spam-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mohamedmustak/spam-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A rule-based AI system that classifies text messages as Spam or Not Spam using keyword scoring and pattern detection techniques in Python.
- **本地描述**：A rule-based AI system that classifies text messages as Spam or Not Spam using keyword scoring and pattern detection techniques in Python.
- **拉取时间**：2026-07-25 18:11:09

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Spam Detector (Rule-Based AI)
## Overview
This is a simple AI-based Python project that classifies a message as Spam or Not Spam using rule-based scoring and pattern detection. The system analyzes common spam keywords, suspicious links, and excessive punctuation to determine whether a message is spam.
## Tech Stack
- Python 3
- Regular Expressions (re module)
## How It Works
The program assigns a spam score based on:
- Presence of common spam keywords (e.g., "free", "win", "cash")
- Detection of suspicious links (http:// or https://)
- Excessive exclamation marks
If the total score exceeds a defined threshold, the message is classified as Spam.
## How to Run
1. Make sure Python is installed.
2. Clone this repository or download the project files.
3. Open terminal inside the project folder.
4. Run:
python spam_detector.py
5. Enter a message when prompted.
## Example
Input:
Congratulations! You have won free cash!!! Click here now!
Output:
Result: Spam
## Use Cases
- Email filtering systems
- Message moderation tools
- Basic cybersecurity automation
- NLP learning projects
- Beginner AI demonstrations
## Future Improvements
- Machine Learning-based spam classifier
- Dataset training support
- Web interface using Flask or Streamlit
- Improved scoring algorithm
- Probability-based output
## Author
Mohamed Mustak M
