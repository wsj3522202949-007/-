---
id: tool-01839
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: Story-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/sayanpal12/story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1839
category: 二、网文 / 长篇 AI 写作系统 库
repo: SayanPal12/Story-Generator
stars: 1
url: https://github.com/sayanpal12/story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# SayanPal12/Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sayanpal12/story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered interactive story generator. Enter a topic, make choices, shape your narrative. Built with Streamlit, LangGraph & Groq. Fast generation, multiple endings, perfect for creative writing.
- **本地描述**：AI-powered interactive story generator. Enter a topic, make choices, shape your narrative. Built with Streamlit, LangGraph & Groq. Fast generation, multiple endings, perfect for creative writing.
- **拉取时间**：2026-07-23 23:32:39

---

# 📖 Interactive AI Story Generator

An interactive story generation application powered by AI that creates dynamic, choice-driven narratives. Users guide the story's progression by making decisions at key plot points, creating a unique storytelling experience every time.

## ✨ Features

- 🎭 **Dynamic Story Generation**: AI-powered creative storytelling using Groq's LLM models
- 🔀 **Interactive Choices**: Make decisions that shape the narrative direction
- 💾 **Session Persistence**: Story progress is maintained throughout your session
- 🎨 **Modern UI**: Clean, responsive interface built with Streamlit
- 🔄 **Story Continuity**: Seamless story progression based on user choices
- 📝 **Multiple Endings**: Different paths lead to unique story conclusions
- 🚀 **Fast Generation**: Powered by Groq's high-performance inference

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: LangGraph (LangChain)
- **AI Model**: Groq API (Llama 3.1 8B)
- **State Management**: LangGraph MemorySaver
- **Language**: Python 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get one here](https://console.groq.com))

## 🚀 Installation

1. **Clone the repository**
```bash
   git clone https://github.com/SayanPal12/Story-Generator.git
   cd story-generator
```

2. **Create a virtual environment**
```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Run the application**
```bash
   streamlit run frontend.py
```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - Enter your Groq API key in the sidebar
   - Start creating stories!

## 📦 Dependencies
```txt
streamlit>=1.28.0
langchain>=0.1.0
langchain-groq>=0.0.1
langgraph>=0.0.40
groq>=0.4.0
```

## 🎮 Usage

1. **Enter your Groq API Key** in the sidebar
2. **Input a story topic** (e.g., "space adventure", "mystery mansion")
3. **Read the generated story** segment
4. **Choose from multiple options** to guide the narrative
5. **Continue making choices** until you reach an ending
6. **Start a new story** anytime with the reset button

## 🏗️ Project Structure
```
story-generator/
│
├── frontend.py           # Streamlit UI and user interactions
├── backend.py            # LangGraph agent and story generation logic
├── requirements.txt      # Project dependencies
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

## 🔑 Configuration

The application requires a Groq API key for operation. You can:
- Enter it directly in the sidebar (recommended for local development)
- Set it as an environment variable: `GROQ_API_KEY=your_key_here`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/SayanPal12/Story-Generator/blob/main/LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing fast LLM inference
- [LangChain](https://langchain.com/) for the agent framework
- [Streamlit](https://streamlit.io/) for the intuitive UI framework

## 🗺️ Roadmap

- [ ] Add story export functionality (PDF/TXT)
- [ ] Implement story history and bookmarks
- [ ] Add multiple genre templates
- [ ] Support for image generation in stories
- [ ] Multi-language support
- [ ] User authentication and cloud storage

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

⭐ If you find this project useful, please consider giving it a star!
