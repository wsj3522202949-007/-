---
id: tool-00626
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ECS289G-Project
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/abrar-syed/ecs289g-project
created: 2026-07-18
updated: 2026-07-18
no: 626
category: 二、网文 / 长篇 AI 写作系统 库
repo: abrar-syed/ECS289G-Project
stars: 0
url: https://github.com/abrar-syed/ecs289g-project
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# abrar-syed/ECS289G-Project

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/abrar-syed/ecs289g-project
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：interactive-storytelling, multimodal, python, story-generation, vuejs
- **GitHub 描述**：A Multimodal framework for story generation
- **本地描述**：A Multimodal framework for story generation
- **拉取时间**：2026-07-23 22:57:19

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# [ECS 289G-Project] Constructing Compelling Narratives: A Multimodal Framework for Story Generation

!`[Architecture](architecture.png)`

## How to run?

After cloning the repository

### Client

Install and check that the client compiles:
```
cd client
npm i
npm run build
```

### Backend

Install and activate the environment (conda provided):
```
conda env create -f environment.yml
conda activate MultiModalStory
```

Install environment globally in the directory: 
```
pip install -e .
pip install git+https://github.com/openai/CLIP.git
```

After installation run:
```
python -m spacy download en_core_web_sm
```
In python terminal:
```
nltk.download('wordnet')
nltk.download('sentiwordnet')
nltk.download('averaged_perceptron_tagger')
```

### Large Data Management

```
dvc pull -f
```

Which will pull:
- backend/outputs (five preset stories)
- backend/story_generator/downloaded (transformers)
- client/public/unsplash25k (styled images)

### Running the framework during development

Client: 
```
cd client
npm run devw
```

Backend (with server auto reload): 
```
uvicorn backend.server:app --reload --reload-dir backend
```

Open the uvicorn server `localhost:8000` in your web browser
