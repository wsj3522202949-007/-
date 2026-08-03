---
id: tool-00207
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AIstorygenerator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/rohithvishwa/aistorygenerator
created: 2026-07-18
updated: 2026-07-18
no: 207
category: 二、网文 / 长篇 AI 写作系统 库
repo: rohithvishwa/AIstorygenerator
stars: 0
url: https://github.com/rohithvishwa/aistorygenerator
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# rohithvishwa/AIstorygenerator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rohithvishwa/aistorygenerator
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI based story generator
- **本地描述**：AI based story generator
- **拉取时间**：2026-07-23 22:45:04

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Fine Tuning LLM For Story Generation

In this project, I developed a custom dataset derived from an existing dataset using the Spacy NLP model to extract characters, objects, locations, vehicles, professions, and emotions from the stories. 

Dataset before :

![image](https://github.com/user-attachments/assets/5c2f15dc-8fd6-4f3c-a40b-ff0fb7b4d823)


Dataset after custom creation :

![image](https://github.com/user-attachments/assets/44fda2e4-796d-4871-a9e4-3bd0c0c287b6)


## How to Run the Story generator 

1. clone the repo 
2. go to the folder llm/app
3. run the fast API in one terminal
4. run the streamlit in another terminal

For Generating images for storytelling we need a high power GPU

1. go to the notebook : https://github.com/siva1999/llm/blob/main/storytelling/text_to_image.ipynb , run it in google collab under a GPU. this will run a fastAPI service.
2. the notebook will give a ngork public ip , paste it in : https://github.com/siva1999/llm/blob/main/app/streamlit_with_image.py  (line no : 171)
3. run the fast API 
4. run the streamlit

### Model Sample Output :


Simple Generator : https://github.com/siva1999/llm/blob/main/app/streamlit_output_simple.pdf

Advanced Generator : https://github.com/siva1999/llm/blob/main/app/streamlit_output_advanced.pdf

Custom Prompt Generator : https://github.com/siva1999/llm/blob/main/app/streamlit_output_own_prompt.pdf

Generated images with story : https://github.com/siva1999/llm/blob/main/app/generated_story_with%20image.pdf

## Results

Before Fine Tuning :

![image](https://github.com/user-attachments/assets/7f555319-7152-49df-87e0-7d437c5978f6)


After Fine Tuning :

![image](https://github.com/user-attachments/assets/e5eccf53-641a-400b-b877-5a05fad485d2)


I then fine-tuned the Google FLAN-T5 Large (783M parameters) language model using this custom dataset.

Fine tuned model is uploaded in the Huggingface : https://huggingface.co/siva1999/flan-t5-story-gen






