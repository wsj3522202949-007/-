---
id: tool-03872
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 需API密钥, 英文文档, 改稿润色]
title: ComicCrafted
summary: 错别字/语法/风格校对
source: https://github.com/axion004/comiccrafted
created: 2026-07-18
updated: 2026-07-18
no: 3872
category: 十三、语法 / 风格检查 / 校对 库
repo: Axion004/ComicCrafted
stars: 1
url: https://github.com/axion004/comiccrafted
tier: "B"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/改稿润色指令库.md
  - methods/自检清单_升级版.md
---

# Axion004/ComicCrafted

- **分类**：十三、语法 / 风格检查 / 校对 库
- **链接**：https://github.com/axion004/comiccrafted
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-powered comic generator using GPT and Stable Diffusion to convert short scenarios into full comic strips. Outputs 6-panel stories styled as manga, Belgian, or American comics using OpenAI + Stability APIs.
- **本地描述**：AI-powered comic generator using GPT and Stable Diffusion to convert short scenarios into full comic strips. Outputs 6-panel stories styled as manga, Belgian, or American comics using OpenAI + Stability APIs.
- **拉取时间**：2026-07-24 00:00:35

---

# ComicCrafter 🎨🦸‍♂️  
**Generate full comic strips from simple scenarios using Generative AI!**

ComicCrafter uses powerful language and image generation tools to bring your creative ideas to life as comic strips.

---

## 🚀 How It Works

1. A **Large Language Model** (OpenAI GPT) turns your scenario into 6 descriptive comic panels with dialogues.
2. **Stable Diffusion** (via Stability API) generates an image for each panel.
3. Text is added to each image using Pillow.
4. All panels are merged into a final comic strip.

---

## 🧪 Example Scenarios

**Style: Belgium Comic**  
Characters: Francis (a medieval knight), Madeline (a long-haired princess)  
Francis fights a dragon terrorizing the kingdom. The twist: the dragon was the princess's friend!

**Style: Manga**  
Characters: Adrien (blond hair), Vincent (black hair)  
They build a new product overnight and present it at work.

**Style: American Comic**  
Characters: Peter (tall, blond), Steven (short, black hair)  
Aliens attack New York. Peter and Steven try to escape before the army steps in.

related:
  - methods/改稿润色指令库.md
  - methods/自检清单_升级版.md
---

## ⚙️ Requirements

Install all required libraries:

```bash
pip install -r requirements.txt
```

🧾 Setup Instructions
Clone the repository

```bash
git clone https://github.com/yourusername/ComicCrafter.git
cd ComicCrafter
Set up API keys
```

Rename the .env.example file to .env and add your keys:

```env
OPENAI_API_KEY=your_openai_key
STABILITY_KEY=your_stability_key
Edit the script
```

In kartoon.py, change:

SCENARIO: Your story idea

STYLE: Choose from 'manga', 'american', etc.

Run the script

```bash
python kartoon.py
```
📁 Output
Your comic strip will be saved as:
strip-[style].png in the project folder.


