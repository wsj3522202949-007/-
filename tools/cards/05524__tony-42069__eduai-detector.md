---
id: tool-05524
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: eduai-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/tony-42069/eduai-detector
created: 2026-07-18
updated: 2026-07-18
no: 5524
category: 一、去 AI 味 / Humanizer 库
repo: tony-42069/eduai-detector
stars: 2
url: https://github.com/tony-42069/eduai-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# tony-42069/eduai-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/tony-42069/eduai-detector
- **Stars**：2
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI text detection tool designed for educational use, helping teachers identify potentially AI-generated content in student submissions.
- **本地描述**：An AI text detection tool designed for educational use, helping teachers identify potentially AI-generated content in student submissions.
- **拉取时间**：2026-07-25 18:21:53

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# EduAI Detector



An AI text detection tool designed for educational use, helping teachers identify potentially AI-generated content in student submissions.



## Features



- AI-generated text detection using statistical analysis

- Simple web interface for text submission

- Detailed analysis metrics and explanations

- RESTful API for integration with other tools



## Installation



1. Clone the repository:

```bash

git clone https://github.com/tony-42069/eduai-detector.git

cd eduai-detector

```



2. Create and activate a virtual environment:

```bash

python -m venv venv

# On Windows:

.\venv\Scripts\Activate.ps1

# On Unix or MacOS:

source venv/bin/activate

```



3. Install dependencies:

```bash

pip install -e .

```



## Usage



1. Start the server:

```bash

python main.py

```



2. Open your web browser and visit:

- Web Interface: http://127.0.0.1:8000/

- API Documentation: http://127.0.0.1:8000/docs



## Project Structure



```

eduai-detector/

├── src/

│   └── eduai_detector/

│       ├── core/           # Core detection logic

│       ├── interface/      # API and web interface

│       └── utils/          # Utility functions

├── tests/                  # Test files

├── docs/                   # Documentation

└── main.py                # Application entry point

```



## Development



- Built with FastAPI for the backend API

- Uses statistical analysis for AI text detection

- Includes a simple web interface for easy testing



## License



[MIT License](LICENSE)
