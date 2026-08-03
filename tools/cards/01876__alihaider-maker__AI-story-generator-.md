---
id: tool-01876
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-story-generator-
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/alihaider-maker/ai-story-generator-
created: 2026-07-18
updated: 2026-07-18
no: 1876
category: 二、网文 / 长篇 AI 写作系统 库
repo: alihaider-maker/AI-story-generator-
stars: 1
url: https://github.com/alihaider-maker/ai-story-generator-
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# alihaider-maker/AI-story-generator-

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/alihaider-maker/ai-story-generator-
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：interactive AI story generator with multi language support ,dynamic chapter controls ,and choice influence levels. Built with Azure open AI and Streamlit.
- **本地描述**：interactive AI story generator with multi language support ,dynamic chapter controls ,and choice influence levels. Built with Azure open AI and Streamlit.
- **拉取时间**：2026-07-23 23:33:40

---

# 📚 AI Story Generator - Extended Version

**Author:** Ali Haider  
**Version:** 2.0  
**License:** MIT

An enhanced interactive story generation application powered by Azure OpenAI, featuring multi-language support, dynamic chapter controls, and a modern web interface.

---

## 🌟 Features Implemented

### 1. 📏 Chapter Length Control
**What it does:** Allows users to select the desired length of each chapter.

**Options:**
- **Short** (~100-150 words): Concise, fast-paced storytelling
- **Medium** (~150-250 words): Balanced narrative depth (default)
- **Long** (~250-400 words): Detailed, immersive descriptions

**How it works:** The system adjusts the `max_tokens` parameter sent to the Azure OpenAI API and modifies the system prompt to request specific word counts. This ensures the AI generates content matching the user's preferred reading length.

**Code Location:** `LENGTH_CONFIG` dictionary in `main.py` (lines 45-58)

---

### 2. 🔇 Text-Only Mode
**What it does:** Provides a cost-aware option to disable image and audio generation.

**Benefits:**
- Reduces API costs significantly (no DALL-E image generation)
- Faster story generation
- Lower bandwidth usage
- Ideal for testing or text-focused users

**How it works:** When enabled via the `--text-only` flag or web UI toggle, the `text_only_mode` parameter skips calls to `generate_image()` and `narrate_text()` functions, only generating text content via GPT-4.

**Code Location:** `StoryConfig` dataclass and conditional checks in media generation functions (lines 310-350)

---

### 3. ⚡ Choice Influence Strength
**What it does:** Controls how dramatically user choices affect the story direction.

**Levels:**
- **Light:** Choices create subtle ripples; story maintains overall arc
- **Strong:** Choices significantly shape scenes and outcomes (default)
- **Chaotic:** Choices trigger wild, unpredictable, surreal twists

**How it works:** Each level appends specific instructions to the LLM prompt via `INFLUENCE_CONFIG`. The "Chaotic" mode encourages the AI to be bold and imaginative, while "Light" maintains narrative consistency.

**Code Location:** `INFLUENCE_CONFIG` dictionary and prompt construction (lines 60-75, 95-115)

---

### 4. 🌍 Language Selector
**What it does:** Generates stories in multiple languages with native voice synthesis.

**Supported Languages:**
- 🇺🇸 English (en-US)
- 🇸🇦 Arabic (ar-SA) - العربية
- 🇫🇷 French (fr-FR)
- 🇪🇸 Spanish (es-ES)
- 🇩🇪 German (de-DE)
- 🇯🇵 Japanese (ja-JP) - 日本語

**How it works:** 
1. The system prompt is dynamically generated to instruct the AI to respond in the selected language
2. Moral generation also adapts to the target language
3. Azure Speech SDK automatically selects appropriate neural voices using `LANGUAGE_VOICES` mapping
4. All UI elements and prompts are language-aware

**Code Location:** `Language` enum, `LANGUAGE_VOICES` mapping, and `get_system_prompt()` function (lines 25-42, 78-92)

---

### 5. 🌐 Web UI (Stretch Goal)
**What it does:** Provides a modern, interactive web interface using Streamlit.

**Features:**
- Intuitive sidebar configuration
- Real-time progress tracking
- Chapter-by-chapter navigation
- Audio playback within the browser
- Image display alongside text
- Export to TXT and JSON formats
- Responsive design

**How to launch:**
```bash
streamlit run web_ui.py
```

**Code Location:** `web_ui.py` - Complete Streamlit application

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Azure OpenAI API access
- Azure Speech Services (optional, for audio)
- Azure OpenAI DALL-E deployment (optional, for images)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/ai-story-generator.git
cd ai-story-generator
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables:**
Create a `.env` file:
```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=gpt4-story
AZURE_OPENAI_IMAGE_DEPLOYMENT=dall-e-3  # Optional
AZURE_OPENAI_API_VERSION=2024-05-01-preview
AZURE_SPEECH_KEY=your-speech-key        # Optional
AZURE_SPEECH_REGION=westus2             # Optional
```

### Usage

**Interactive CLI Mode:**
```bash
python main.py
```

**Quick Demo (no input required):**
```bash
python main.py --demo
```

**Web Interface:**
```bash
streamlit run web_ui.py
# Or
python main.py --web
```

---

## 🏗️ Architecture

```
ai-story-generator/
├── main.py           # Core story generation engine
├── web_ui.py         # Streamlit web interface
├── requirements.txt  # Python dependencies
├── README.md         # Documentation
└── .env             # Environment variables (not in repo)
```

### Key Components

1. **StoryConfig** (dataclass): Holds all generation parameters
2. **StoryState** (dataclass): Tracks story progression and history
3. **Enums**: Type-safe configuration options (Language, ChapterLength, InfluenceStrength)
4. **Prompt Engineering**: Dynamic prompt construction based on settings
5. **Azure Integration**: REST API fallback + SDK support

---


## 📝 License

This project is open source and available under the MIT License.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Created with ❤️ by Ali Haider**

*Empowering creativity through AI storytelling*
