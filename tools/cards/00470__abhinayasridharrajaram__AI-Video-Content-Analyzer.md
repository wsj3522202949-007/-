---
id: tool-00470
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Video-Content-Analyzer
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/abhinayasridharrajaram/ai-video-content-analyzer
created: 2026-07-18
updated: 2026-07-18
no: 470
category: 二、网文 / 长篇 AI 写作系统 库
repo: abhinayasridharrajaram/AI-Video-Content-Analyzer
stars: 2
url: https://github.com/abhinayasridharrajaram/ai-video-content-analyzer
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: f69d8281f4f55291
  - methods/最强写作方法论_全球最强综合版.md
---

# abhinayasridharrajaram/AI-Video-Content-Analyzer

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/abhinayasridharrajaram/ai-video-content-analyzer
- **Stars**：2
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：This project is an AI-powered video analyzer that turns long videos into structured chapters with summaries and key insights.
- **本地描述**：This project is an AI-powered video analyzer that turns long videos into structured chapters with summaries and key insights.
- **拉取时间**：2026-07-23 22:52:48

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI-Video-Content-Analyzer
This project is an AI-powered video analyzer that turns long videos into structured chapters with summaries and key insights.

# Execution Instructions

# Python version 3.10

To create a virtual environment and install requirements in Python 3.10 on different operating systems, follow the instructions below:

### For Windows:

Open the Command Prompt by pressing Win + R, typing "cmd", and pressing Enter.

Change the directory to the desired location for your project:


`cd C:\path\to\project`

Create a new virtual environment using the venv module:


`python -m venv myenv`

Activate the virtual environment:

`myenv\Scripts\activate`


Install the project requirements using pip:

`pip install -r requirements.txt`

### For Linux/Mac:
Open a terminal.

Change the directory to the desired location for your project:

`cd /path/to/project`

Create a new virtual environment using the venv module:

`python3.10 -m venv myenv`


Activate the virtual environment:

`source myenv/bin/activate`

Install the project requirements using pip:

`pip install -r requirements.txt`

These instructions assume you have Python 3.10 installed and added to your system's PATH variable.

## Execution Instructions if Multiple Python Versions Installed

If you have multiple Python versions installed on your system, you can use the Python Launcher to create a virtual environment with Python 3.10. Specify the version using the -p or --python flag. Follow the instructions below:

For Windows:
Open the Command Prompt by pressing Win + R, typing "cmd", and pressing Enter.

Change the directory to the desired location for your project:

`cd C:\path\to\project`

Create a new virtual environment using the Python Launcher:

`py -3.10 -m venv myenv`

Note: Replace myenv with your desired virtual environment name.

Activate the virtual environment:

`
myenv\Scripts\activate
`

Install the project requirements using pip:

`pip install -r requirements.txt`


### For Linux/Mac:
Open a terminal.

Change the directory to the desired location for your project:

`cd /path/to/project
`
Create a new virtual environment using the Python Launcher:


`python3.10 -m venv myenv`


Note: Replace myenv with your desired virtual environment name.

Activate the virtual environment:

`source myenv/bin/activate`

Install the project requirements using pip:

`pip install -r requirements.txt`


By specifying the version using py -3.10 or python3.10, you can ensure that the virtual environment is created using Python 3.10 specifically, even if you have other Python versions installed.


```
video-analyzer-updated
├─ .DS_Store
├─ Code Folder.zip
├─ chaptered_transcription.json
├─ engine.py
├─ filtered_transcription.json
├─ filtered_transcription_with_descriptions.json
├─ input
│  └─ Lora Ben v1.mp4
├─ ml_pipeline
│  ├─ __pycache__
│  │  └─ utils.cpython-310.pyc
│  └─ utils.py
├─ notebook
│  ├─ filtered_transcription.json
│  ├─ filtered_transcription_with_descriptions.json
│  └─ video_analyzer_comprehensive.ipynb
├─ readme.md
└─ requirements.txt

```
