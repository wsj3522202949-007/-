---
id: tool-01661
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ComicCrafterAI
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/subhro91/comiccrafterai
created: 2026-07-18
updated: 2026-07-18
no: 1661
category: 二、网文 / 长篇 AI 写作系统 库
repo: Subhro91/ComicCrafterAI
stars: 2
url: https://github.com/subhro91/comiccrafterai
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Subhro91/ComicCrafterAI

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/subhro91/comiccrafterai
- **Stars**：2
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：ComicCrafter AI is a generative AI-based comic generator that runs locally on edge devices. It creates comic-style stories from user prompts using: - Mistral LLM for story generation - Stable Diffusion for image creation - Streamlit for the web interface
- **本地描述**：ComicCrafter AI is a generative AI-based comic generator that runs locally on edge devices. It creates comic-style stories from user prompts using: - Mistral LLM for story generation - Stable Diffusion for image creation - Streamlit for the web interface
- **拉取时间**：2026-07-23 23:27:30

---

ComicCrafter AI

Hey there! Welcome to ComicCrafter AI - your creative companion for turning ideas into comic stories!

About This Project
-----------------
ComicCrafter AI helps you create comic-style stories right on your own computer. It uses AI to generate both the story and images based on your ideas. The tech behind it includes Mistral LLM for crafting the narrative and Stable Diffusion for creating the visuals, all wrapped up in a simple Streamlit interface.

Getting Started
-----------------
What you'll need:
- Python 3.10
- An NVIDIA GPU (I've tested it with RTX 3060)
- At least 8GB of RAM
- Git

Setting Up
-----------------
1. First, grab the code:
   git clone https://github.com/yourusername/ComicCrafterAI.git
   cd ComicCrafterAI

2. Set up your environment:
   python -m venv .venv
   .venv\Scripts\activate  # for Windows
   source .venv/bin/activate  # for Linux/Mac

3. Install what you need:
   pip install -r requirements.txt

4. You'll need to download:
   - Mistral 7B
   - Stable Diffusion 1.5 

Quick Start (Windows)
-----------------
For Windows users, we've made things super easy! Just double-click the "setup_and_run.bat" file in the main folder, and it will:
1. Check if you have Python and Git installed
2. Set up the virtual environment
3. Install all required dependencies
4. Automatically download Stable Diffusion WebUI
5. Automatically download the Mistral 7B model
6. Automatically download the Stable Diffusion 1.5 model
7. Start Stable Diffusion WebUI
8. Launch ComicCrafter AI in your browser automatically

Everything is downloaded and set up automatically - you don't need to download any models or software separately! Just be patient during the first run as downloading the models can take some time depending on your internet connection.

Requirements for the automatic setup:
- Python 3.10
- Git
- Internet connection
- About 10GB of free disk space

Running the App
-----------------
1. First, start the Stable Diffusion WebUI:
   cd stable-diffusion-webui
   ./webui.bat --api

2. Then in a new terminal window, launch ComicCrafterAI:
   streamlit run app/main.py

How Things Are Organized
-----------------
- app/: This is where the main code lives
  - utils/: Helper functions and tools
  - config.py: Settings for the application
  - main.py: The main interface built with Streamlit
- models/: Where the AI models go (you'll need to download these)
- docs/: Extra documentation

Questions or Ideas?
--------------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
Feel free to reach out if you have any questions or want to chat about the project!

Happy comic creating!
