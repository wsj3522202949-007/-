---
id: tool-07246
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档]
title: ai-poem-crafter
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/eternalflame02/ai-poem-crafter
created: 2026-07-18
updated: 2026-07-18
no: 7246
category: 画龙补充 / 扩容入库 — 补充源
repo: eternalflame02/ai-poem-crafter
stars: 2
url: https://github.com/eternalflame02/ai-poem-crafter
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4d77585b3485121a
  - methods/QUICK_START.md
---

# eternalflame02/ai-poem-crafter

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/eternalflame02/ai-poem-crafter
- **Stars**：2
- **语言**：Python
- **License**：MIT
- **Topics**：ai, awan, poem-generator, python, streamlit, streamlit-webapp
- **GitHub 描述**：This Streamlit-based web app allows users to generate custom poems using AI. By selecting a mood, poem length, and optional theme, users can craft unique poems and download or copy them to their clipboard. The app utilizes the AwanLLM API for natural language generation.
- **本地描述**：ai-poem-crafter
- **拉取时间**：2026-07-25 19:15:25

---

# AI Poem Crafter ✨📝

**AI Poem Crafter** is a creative web app that generates beautiful poems using the **AwanLLM API**! 🎤🎶 Whether you're in the mood for a happy, sad, or nostalgic poem, this app allows you to customize the mood, length, and even theme to create a unique piece of art. 🌟

### Key Features 🌟
- **Generate Poems**: Select a mood, length, and theme (optional) to generate a personalized poem. 🖋️
- **Poem History**: Keep track of all your generated poems with titles, moods, and content. 📜
- **Download Poems**: Download your poems as text files with the title as the filename. 💾
- **Copy to Clipboard**: Easily copy any poem to your clipboard for sharing. 📋
- **Clear History**: Reset your poem history with a single click. 🧹

---

## How to Use 💡

1. **Choose Your Poem Settings**: 
   - Select a **mood** (e.g., Happy, Sad, Romantic, etc.)
   - Choose your **poem length** (Short, Medium, or Long).
   - Optionally, enter a **theme** or keywords.
   
2. **Generate Your Poem**: 📝 
   - Click the **"Generate Poem"** button and wait as the AI crafts your masterpiece! ✨
   
3. **Poem History**: 🏛️
   - View all the poems you've created, with the option to expand them for full reading.
   
4. **Download or Copy**: 🔽
   - **Download** poems as `.txt` files or **copy** them directly to your clipboard for easy sharing.

5. **Clear History**: 🧹
   - Use the **"Clear Poem History"** button to reset all your poem data.

---

## Requirements 📦

- Python 3.7+ 🐍
- **Streamlit** 📊
- **Requests** 🔌
- **Pyperclip** 📋

---

## Installation ⚙️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/eternalflame02/AI-Poem-Crafter.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app locally**:
   ```bash
   streamlit run poemcrafter.py
   ```

---

## Deploy to Streamlit Cloud ☁️

1. Sign in to your **Streamlit** account [here](https://streamlit.io).
2. Go to your dashboard and click **"New app"**.
3. Connect your **GitHub repository** and deploy the app.
4. **Set your API_KEY** as a secret in Streamlit Cloud:
   - In **Streamlit Cloud**, navigate to **Settings** > **Secrets** and add your **API_KEY**.
   - Example:
     ```toml
     [secrets]
     API_KEY = "your-api-key-here"
     ```

---

## Contributing 🤝

I welcome contributions! Feel free to fork the repo, create branches, and submit pull requests. 

---

## License 📜

This project is licensed under the **MIT License**. See the [LICENSE](https://github.com/eternalflame02/ai-poem-crafter/blob/main/LICENSE) file for details. 📄

---

Thanks for checking out **AI Poem Crafter**! 🌟

related:
  - methods/QUICK_START.md
---
