---
id: tool-00284
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Powered-Image-To-Story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/damnhamza123/ai-powered-image-to-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 284
category: 二、网文 / 长篇 AI 写作系统 库
repo: damnhamza123/AI-Powered-Image-To-Story-generator
stars: 1
url: https://github.com/damnhamza123/ai-powered-image-to-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5d7f7bace38c3999
  - methods/最强写作方法论_全球最强综合版.md
---

# damnhamza123/AI-Powered-Image-To-Story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/damnhamza123/ai-powered-image-to-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：generate stories form images 
- **本地描述**：generate stories form images
- **拉取时间**：2026-07-23 22:47:21

---

# 📖 Image-to-Audio Story Generator

An AI-powered application that takes an image as input and generates a creative short story, then converts it into speech — bringing pictures to life!  
Built using **Salesforce BLIP**, **LLaMA-based language models**, **gTTS**, and **Gradio**.

---

## 🚀 Features
- 🖼 **Image Captioning:** Extracts a meaningful caption from any uploaded image using Salesforce **BLIP**.
- ✍ **Story Generation:** Expands the caption into a creative short story using **LLaMA-based models**.
- 🔊 **Text-to-Speech:** Converts the generated story into natural-sounding audio using **gTTS**.
- 🌐 **Interactive UI:** Simple and intuitive **Gradio** interface for easy interaction.

---

## 🛠️ Tech Stack
- **Python 3.8+**
- [Salesforce BLIP](https://github.com/salesforce/BLIP) — For image captioning.
- [LLaMA-based Models](https://huggingface.co/models) — For story generation.
- [gTTS](https://pypi.org/project/gTTS/) — Google Text-to-Speech for audio output.
- [Gradio](https://www.gradio.app/) — Web-based UI.

---

## 📂 Project Structure
Image-to-Story/
│
├── app.py # Main application script
├── README.md # Project documentation
├── captions/ # Optional folder to store generated captions
├── stories/ # Optional folder to store generated stories
└── audio/ # Optional folder to store generated audio files

yaml
Copy
Edit

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📦 Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/Image-to-Story.git
cd Image-to-Story
2️⃣ Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
3️⃣ Install dependencies
Here are all required dependencies in one place:

bash
Copy
Edit
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers==4.30.2
pip install gradio==3.41.2
pip install gTTS==2.3.2
pip install Pillow==9.5.0
pip install sentencepiece==0.1.99
pip install accelerate==0.20.3
pip install timm==0.9.2
Or create a requirements.txt file with:

txt
Copy
Edit
torch
torchvision
torchaudio
transformers==4.30.2
gradio==3.41.2
gTTS==2.3.2
Pillow==9.5.0
sentencepiece==0.1.99
accelerate==0.20.3
timm==0.9.2
Then run:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Usage
1️⃣ Run the app

bash
Copy
Edit
python app.py
2️⃣ Open Gradio Interface
The console will display a local URL (e.g., http://127.0.0.1:7860/) — open it in your browser.

3️⃣ Upload an image

The app will:

Generate a caption.

Create a story from the caption.

Convert the story into audio.

Let you read and listen to it instantly.

🖥 Example
Input:

Generated Caption:

A small cat sits by the window watching the rain.

Generated Story:

Once upon a time, in a quiet little house, a curious cat named Whiskers spent her afternoons gazing at the raindrops racing down the window...

Audio Output:
🎧 Plays story audio

⚡ Future Improvements
Improve voice quality with advanced TTS models.

Add multiple language support for story generation.

Enable downloadable audio & story files.

Allow user control over story length and style.

📜 License
This project is licensed under the MIT License — feel free to use, modify, and share.

🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

👨‍💻 Author
Muhammad Hamza
📧 hamzakhanswati0@gmail.com

