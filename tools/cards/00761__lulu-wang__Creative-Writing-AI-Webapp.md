---
id: tool-00761
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Creative-Writing-AI-Webapp
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/lulu-wang/creative-writing-ai-webapp
created: 2026-07-18
updated: 2026-07-18
no: 761
category: 二、网文 / 长篇 AI 写作系统 库
repo: lulu-wang/Creative-Writing-AI-Webapp
stars: 7
url: https://github.com/lulu-wang/creative-writing-ai-webapp
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 201da34f84a226b0
  - methods/最强写作方法论_全球最强综合版.md
---

# lulu-wang/Creative-Writing-AI-Webapp

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/lulu-wang/creative-writing-ai-webapp
- **Stars**：7
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Creative writing sentence generator using user input prompts. Coded with OpenAI API, Stable Diffusion, HTML/CSS and Python (Flask) backend.
- **本地描述**：Creative writing sentence generator using user input prompts. Coded with OpenAI API, Stable Diffusion, HTML/CSS and Python (Flask) backend.
- **拉取时间**：2026-07-23 23:01:13

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Creative Writing Generator Webapp
Creative writing sentence generator using user input prompts. AI images are generated from the prompt results.

Coded using the OpenAI API, HTML/CSS and Python (Flask) backend.
Powered by GPT-3.5. 

AI generated images from stable diffusion.

Preview Demo (v1):

With AI-generated images (stable diffusion): 

![gif](https://github.com/lulu-wang/Creative-Writing-AI-Webapp/assets/16969709/3e8b3127-fc80-470a-8f57-69e57d10f656)

Longer:
![gif2](https://github.com/lulu-wang/Creative-Writing-AI-Webapp/assets/16969709/56d20bef-d580-4916-87c1-f42eca069006)



## Setup (local)

1. Clone and navigate into the project directory.

2. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```
3. Make sure to have API keys for Open AI and Stable Diffusion. Update these values in .env.example.

4. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```
   

5. Run the app:

   ```bash
   $ flask run
   ```

You can see the app at [http://localhost:5000](http://localhost:5000)
