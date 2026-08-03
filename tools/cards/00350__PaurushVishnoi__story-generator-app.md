---
id: tool-00350
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: story-generator-app
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/paurushvishnoi/story-generator-app
created: 2026-07-18
updated: 2026-07-18
no: 350
category: 二、网文 / 长篇 AI 写作系统 库
repo: PaurushVishnoi/story-generator-app
stars: 1
url: https://github.com/paurushvishnoi/story-generator-app
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# PaurushVishnoi/story-generator-app

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/paurushvishnoi/story-generator-app
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Generates a story based on the inputs given to the user using Streamlit and Open AI
- **本地描述**：Generates a story based on the inputs given to the user using Streamlit and Open AI
- **拉取时间**：2026-07-23 22:49:19

---

# 📚 Story World – AI Story & Cover Generator

An interactive **Streamlit web app** that lets you create short stories with **GPT-4o** and (optionally) generate a matching **cover illustration** with **OpenAI Images (DALL·E)**.

---

## ✨ Features

- 🖊️ **Custom Story Generation**  
  Enter a character, topic, location, mood, and choose length/style. GPT-4o creates a full, self-contained story.

- 🎨 **Optional Cover Image**  
  Generate a cinematic illustration for your story using OpenAI’s latest image model.

- 💾 **Download Support**  
  Save your story as a `.txt` file and the cover as a `.png`.

- 🖥️ **Simple UI**  
  Built with [Streamlit](https://streamlit.io/) for fast, shareable apps.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🚀 Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/story-generator-app.git
cd story-generator-app
```

### 2. Create & activate a virtual environment (optional)
```
python -m venv .venv
source .venv/bin/activate 
```

```
# Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set your API key
``` 

cd story-generator-app -> Create .env 

Add your OpenAI API key:

OPENAI_API_KEY=sk-xxxx
```

In case you dont have API key 

Create an API key from your OpenAI dashboard.
```
Login to Open AI -> https://platform.openai.com/settings/profile/api-keys

Click "+ Create a new secret key" -> Name your key for e.g.:- "My demo key" -> Copy the generated key
```

### 5. Run the app
```
streamlit run streamlit_app.py
```

## ⚠️ Notes & Gotchas

### 🖼️ Image Generation (gpt-image-1 / DALL·E 3)
- Requires your **OpenAI account/organization to be identity verified**.  
- If you see a `403: organization must be verified` error, go to  
  [OpenAI Org Settings → General](https://platform.openai.com/settings/organization/general)  
  and complete verification.

### 💰 API Costs
- Both **GPT-4o** and **DALL·E** are **paid API calls**.  
- Monitor your usage in the [OpenAI dashboard](https://platform.openai.com/).


## 🙌 Acknowledgements

- [OpenAI GPT-4o](https://platform.openai.com/) – for storytelling  
- [OpenAI Images (DALL·E)](https://platform.openai.com/docs/guides/images) – for cover art  
- [Streamlit](https://streamlit.io/) – for the UI  
