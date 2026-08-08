---
id: tool-01053
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 需API密钥, 英文文档]
title: crewai-multiagent-instagram-pipeline
summary: 多 Agent 协作自动产文
source: https://github.com/debbrath/crewai-multiagent-instagram-pipeline
created: 2026-07-18
updated: 2026-07-18
no: 1053
category: 二、网文 / 长篇 AI 写作系统 库
repo: debbrath/crewai-multiagent-instagram-pipeline
stars: 1
url: https://github.com/debbrath/crewai-multiagent-instagram-pipeline
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 291933ae2dd95d96
  - methods/最强写作方法论_全球最强综合版.md
---

# debbrath/crewai-multiagent-instagram-pipeline

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/debbrath/crewai-multiagent-instagram-pipeline
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：crewai, langchain, nanobanana, segmind
- **GitHub 描述**：CrewAI-powered multi-agent pipeline that automates Instagram content creation—from topic research and caption generation to image prompt design and final content preparation. The system demonstrates how multi-agent AI workflows can collaborate to perform tasks such as topic research, caption writing, prompt generation, and image preparation.
- **本地描述**：CrewAI-powered multi-agent pipeline that automates Instagram content creation—from topic research and caption generation to image prompt design and final content preparation. The system demonstrates how multi-agent AI workflows can collaborate to perform tasks such as topic research, caption writing, prompt generation, and image preparation.
- **拉取时间**：2026-07-23 23:09:42

---

# 🧠 CrewAI Multi-Agent Instagram Pipeline 

This project automates the end-to-end Instagram content pipeline using CrewAI multi-agent systems.
It can research a topic, write content, review drafts, generate image prompts, and finally produce AI images (via Segmind, Stable Diffusion, or Nano Banana).

<br/>

## ✨ Features

- 🧠 Research Agent – finds insights on a given topic

- ✍️ Writer Agent – drafts engaging Instagram-style content

- ✅ Reviewer Agent – improves and fact-checks text

- 🎨 Image Prompt Agent – generates prompts for visuals

- 🖼️ Image Generator – creates final images via external APIs


<br/>

📂 Project Structure

```
crewai-multiagent-instagram-pipeline/
│── .env                # API keys & secrets
│── requirements.txt    # Python dependencies
│── main.py             # Pipeline entry point
│── agents.py           # Multi-agent definitions
│── tasks.py            # Task orchestration
│── image_gen.py        # Image generation integration
│── README.md           # Documentation

```

<br/>

## 🛠 Installation & Local Development
### 1. Prerequisites
```bash
- Python 3.12.10
- pip (Python package manager)
```
### 2. Clone the repository

```bash
git clone https://github.com/debbrath/crewai-multiagent-instagram-pipeline.git
cd crewai-multiagent-instagram-pipeline
```
### Step 3: Open VSCode
- Launch VSCode.
- Open your project folder

### 4. Create and activate a virtual environment
```bash
# On Windows PowerShell
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate

On Linux/Mac
python -m venv env
source env/bin/activate

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
cd F:\Python\Multi-Tool-Medical-AIAgent
.\.venv\Scripts\Activate.ps1

python -m venv .venv
.\.venv\Scripts\Activate.ps1

### 5. Install dependencies
```bash
pip install -r requirements.txt
```
### 6. Add a .env file:

OPENAI_API_KEY=your_openai_key
SERPAPI_API_KEY=your_serpapi_key
IMAGERY_API_KEY=your_segmind_or_nanobanana_key
OPENAI_MODEL=gpt-4o
Run locally

### 6. Run 

python main.py

Example:

Enter topic: AI in Healthcare


✅ The pipeline will:

Research the topic

Generate a caption + blog-style content

Create an AI image prompt

Generate images

Save outputs locally

```
```
![Screenshot](https://github.com/debbrath/crewai-multiagent-instagram-pipeline/blob/main/image/1.png)
```

```
![Screenshot](https://github.com/debbrath/crewai-multiagent-instagram-pipeline/blob/main/image/2.png)
```

```
![Screenshot](https://github.com/debbrath/crewai-multiagent-instagram-pipeline/blob/main/image/3.png)
```

```
<br/>

## 🛠 Technologies Used

Python 3.12+

CrewAI

LangChain

Segmind / Stable Diffusion API

SerpAPI

<br/>

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

✍️ Author

Debbrath Debnath

📫 [Connect on LinkedIn](https://www.linkedin.com/in/debbrathdebnath/)

🌐 [GitHub Profile](https://github.com/debbrath) 




