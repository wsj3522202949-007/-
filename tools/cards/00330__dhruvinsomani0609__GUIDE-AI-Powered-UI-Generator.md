---
id: tool-00330
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: GUIDE-AI-Powered-UI-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/dhruvinsomani0609/guide-ai-powered-ui-generator
created: 2026-07-18
updated: 2026-07-18
no: 330
category: 二、网文 / 长篇 AI 写作系统 库
repo: dhruvinsomani0609/GUIDE-AI-Powered-UI-Generator
stars: 1
url: https://github.com/dhruvinsomani0609/guide-ai-powered-ui-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# dhruvinsomani0609/GUIDE-AI-Powered-UI-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dhruvinsomani0609/guide-ai-powered-ui-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：GUIDE is a local AI tool that turns natural language prompts into responsive HTML/CSS UIs using Ollama and open-source LLMs. It helps developers and designers instantly generate clean interfaces like forms or dashboards—directly in the browser without writing boilerplate code.
- **本地描述**：GUIDE is a local AI tool that turns natural language prompts into responsive HTML/CSS UIs using Ollama and open-source LLMs. It helps developers and designers instantly generate clean interfaces like forms or dashboards—directly in the browser without writing boilerplate code.
- **拉取时间**：2026-07-23 22:48:42

---

# 🎨 GUIDE - AI-Powered UI Generator

## Transform natural language descriptions into professional UI components using local AI models*

## 🌟 Overview

**GUIDE** is a sophisticated, local-first UI generation tool that leverages the power of open-source Large Language Models (LLMs) to convert natural language prompts into production-ready HTML, CSS, and Figma components. Built with privacy and performance in mind, GUIDE operates entirely offline using [Ollama](https://ollama.com) for AI inference.

### ✨ Key Features

- 🤖 **AI-Powered Generation**: Convert natural language to clean HTML/CSS using local LLMs
- 🔌 **Figma Integration**: Optional plugin for seamless Figma workflow integration
- 🎨 **Professional Output**: Generate responsive UI components
- ⚡ **Real-time Preview**: Instant live preview of generated UI components

---

### Project Structure

```
guide-ui-generator/
├── 📁 backend/
│   ├── app.py              # FastAPI main application
|
├── 📁 frontend/
│   ├── index.html          # Main interface
│   ├── code.js             # Images, icons, etc.
│   ├── style.css                # Stylesheets
│   └── index.js    
|   ├── manifest.json                     
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

Ensure you have the following installed:

- 🐍 **Python 3.10+** - [Download](https://python.org/downloads/)
- 🧠 **Ollama** - [Installation Guide](https://ollama.com)
- 🌐 **Modern Web Browser** (Chrome, Firefox, Safari, Edge)
- 🖼️ **Figma Desktop** (Optional, for plugin usage)

### 1. Clone Repository

```bash
git clone https://github.com/your-username/guide-ui-generator.git
cd guide-ui-generator
```

### 2. Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate # Windows

source venv/bin/activate # macOS/Linux

# Install dependencies
pip install -r requirements.txt

pip install fastapi uvicorn httpx pydantic

# Start FastAPI server
uvicorn app:app --reload --port 8000
```

### 3. Setup Ollama

In a separate terminal:

```bash
# Download and run recommended model
ollama pull codellama:instruct
ollama run codellama:instruct

# Alternative models
ollama pull llama3
ollama pull mistral
```

### 4. Launch Frontend

Open `index.html` in your web browser or serve it locally:

```bash
# Using Python's built-in server
python -m http.server 3000

# Or using Node.js
npx serve .
```

Navigate to `http://localhost:3000` and start generating!

---

## 🎯 Examples

### Basic Usage

```bash
# Example prompts that generate professional UI components:

"Create a modern login form with email and password fields"
→ Responsive login form with validation styling

"Design a red exit button with hover effects"
→ Styled button with smooth transitions

"Build a dashboard with navigation sidebar"
→ Complete dashboard layout with responsive design

"Create a contact form with name, email, and message"
→ Professional contact form with proper spacing
```

---

---

## 🧠 Recommended Models

![alt text](image.png)

### Model Configuration

Edit `MODEL_NAME` in `app.py` to switch models:

```python
MODEL_NAME = "codellama:instruct"  # Change this line
```

---

## 🔌 Figma Plugin Setup

### Installation

1. Open **Figma Desktop Application**
2. Navigate to `Plugins → Development → New Plugin`
3. Select `Import plugin from manifest`
4. Choose `plugin/manifest.json` from this repository
5. Click **Save** and run the plugin

### Usage

1. Start the backend server (`uvicorn app:app --reload --port 8000`)
2. Open the GUIDE plugin in Figma
3. Enter your UI prompt in the plugin interface
4. Click **Generate UI Components**
5. Components will be created directly in your Figma canvas


## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Ollama](https://ollama.com) for providing excellent local LLM infrastructure
- [FastAPI](https://fastapi.tiangolo.com) for the robust backend framework
- [Figma](https://figma.com) for the comprehensive plugin API
- The open-source community for continuous inspiration

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

