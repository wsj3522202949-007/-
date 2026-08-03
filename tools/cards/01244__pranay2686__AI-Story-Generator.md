---
id: tool-01244
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Story-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/pranay2686/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1244
category: 二、网文 / 长篇 AI 写作系统 库
repo: pranay2686/AI-Story-Generator
stars: 1
url: https://github.com/pranay2686/ai-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# pranay2686/AI-Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/pranay2686/ai-story-generator
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI Story Generator is a web app that generates creative short stories from user prompts using the DeepSeek Coder 6.7B-Instruct model, with a clean Gradio interface.
- **本地描述**：AI Story Generator is a web app that generates creative short stories from user prompts using the DeepSeek Coder 6.7B-Instruct model, with a clean Gradio interface.
- **拉取时间**：2026-07-23 23:15:22

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pranay2686/AI-Story-Generator/blob/main/Ai_Story_clean.ipynb)

# AI-Story-Generator
AI Story Generator is a web app that generates creative short stories from user prompts using the DeepSeek Coder 6.7B-Instruct model, with a clean Gradio interface.

This is an AI-powered creative story generator built using the DeepSeek Coder model and Gradio interface.


## :link:Features

- Generate creative short stories based on your prompts
- Custom-styled Gradio interface
- Built with Transformers, Accelerate, and BitsAndBytes


## :link:Try It in Google Colab

Click the badge below to run the notebook directly in Google Colab:

[https://colab.research.google.com/github/pranay2686/AI-Story-Generator/blob/main/Ai_Story_clean.ipynb](https://colab.research.google.com/github/pranay2686/AI-Story-Generator/blob/main/Ai_Story_clean.ipynb)

Before Running the Code we should set Runtime from CPU to T4-GPU and then start running the Code in the Colab.

## :link:Screenshots

<b>1. We will get an interface like this. </b>

![Image Alt](https://github.com/pranay2686/AI-Story-Generator/blob/main/screenshots/1.png)

<b>2. We can give a Prompt to Generate Story. </b>

![Image Alt](https://github.com/pranay2686/AI-Story-Generator/blob/main/screenshots/2.png)

<b>3. As Shown in the image below it will generate a story. </b>

![Image Alt](https://github.com/pranay2686/AI-Story-Generator/blob/main/screenshots/3.png)

<b>4. This is the final output after it generating story.</b>

![Image Alt](https://github.com/pranay2686/AI-Story-Generator/blob/main/screenshots/4.png)

## :link:Installation: To run locally

 cloning the Repo in VS Code Terminal:
 ```bash
     git clone https://github.com/pranay2686/Ai-Story-Generator.git
```
To Run Locally in VS Code use app.py and requirements.txt files that i shared.

For Creating Folder
 ```bash
 cd Ai-Story-Generator
```
This Command below is to Create Virtual Environment:
  ```bash
  python -m venv venv
```
This Command in the below is to Activate Virtual Environment:
 ```bash
 venv\Scripts\activate (on Windows) or source venv/bin/activate (on Mac or Linux)
```
The below command is to install All dependencies in the requirements.txt:
```bash
  pip install -r requirements.txt
```
To run the code finally use the below command:
```bash
  python app.py
```

## :link:Note:
In my opinion, I would not suggest running this code locally using VS Code, especially if you're using a CPU. This is because the DeepSeek model we're using is quite large, and generating output on a CPU can take a very long time. Instead, I recommend using the Google Colab link I’ve provided. Colab uses a T4 GPU, which significantly speeds up the execution and provides faster and more accurate results.

## :link:Important Notes for Local Use

This notebook uses the `deepseek-ai/deepseek-coder-6.7b-instruct` model, which:

- Requires a GPU with **at least 10 GB VRAM** (e.g. NVIDIA T4, V100, A100)
- **Will not work** on most CPUs because it uses bitsandbytes GPU quantization
- May run **extremely slowly or crash** if attempted on CPU
- For best performance, we recommend:
  - Running in **Google Colab** with GPU enabled
  - Using a local machine with a **CUDA-enabled GPU**

If your laptop or desktop has a compatible NVIDIA GPU, you may also try running the notebook locally. Otherwise, Colab is the easiest way to run this project.

**Note:** Free Colab accounts may have limited GPU quotas.




