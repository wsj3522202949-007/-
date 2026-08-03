---
id: tool-00730
type: tool
area: 库
status: active
tags: [TTS, Python, 协议宽松, 需API密钥, 英文文档]
title: genAI-Story-Generator-and-Narrator
summary: 小说转语音/有声书
source: https://github.com/aayushbishtt/genai-story-generator-and-narrator
created: 2026-07-18
updated: 2026-07-18
no: 730
category: 二、网文 / 长篇 AI 写作系统 库
repo: aayushbishtt/genAI-Story-Generator-and-Narrator
stars: 1
url: https://github.com/aayushbishtt/genai-story-generator-and-narrator
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# aayushbishtt/genAI-Story-Generator-and-Narrator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/aayushbishtt/genai-story-generator-and-narrator
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：aayushbishtt/genAI-Story-Generator-and-Narrator
- **拉取时间**：2026-07-23 23:00:19

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Story Generator 📸 -> 📖

Hi there! I built this little app because I thought it would be cool to take a bunch of random photos and let AI weave them into a proper story. It basically looks at your images, figures out what's happening, and writes a narrative for you. Plus, it reads the story out loud so you don't even have to read it yourself!

I used Python and Streamlit for the web interface, and under the hood, it's powered by Google's new Gemini models (specifically `gemini-2.5-flash-lite`) to do the creative writing.

## What it actually does

*   **Upload Photos:** You can drop in anywhere from 1 to 10 images.
*   **Pick a Vibe:** Want a mystery? A fairy tale? A sci-fi thriller? You just pick the genre from the dropdown.
*   **AI Magic:** It sends your images to Gemini, which writes a story connecting them all together.
*   **Listen to it:** It uses Google's Text-to-Speech to generate an audio file of the story automatically.

## How to run it

If you want to try this out on your own machine, here is what you need to do:

### 1. Get the code
Clone this repo (or just download the files):
```bash
git clone <your-repo-url>
cd storyGenerator
```

### 2. The Setup
You'll need Python installed. Then, grab the libraries I used:
```bash
pip install -r requirements.txt
```

### 3. API Key
Since this uses Google's Gemini, you need an API key. It's free to get one from [Google AI Studio](https://aistudio.google.com/).
Once you have it, create a file named `.env` in this folder and paste it in like this:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

### 4. Launch it! 🚀
Run this command:
```bash
streamlit run app.py
```
Your browser should open up automatically. Just upload some pics and hit the generate button.

## The Code
*   `app.py`: This is the main file that runs the Streamlit UI.
*   `story_generator.py`: This handles the calls to Gemini and the text-to-speech stuff.

Enjoy! Let me know if you make any cool stories with it.
