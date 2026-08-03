---
id: tool-00197
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: Storybook-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/naakaarafr/storybook-generator
created: 2026-07-18
updated: 2026-07-18
no: 197
category: 二、网文 / 长篇 AI 写作系统 库
repo: naakaarafr/Storybook-Generator
stars: 9
url: https://github.com/naakaarafr/storybook-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# naakaarafr/Storybook-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/naakaarafr/storybook-generator
- **Stars**：9
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-powered storybook creator using 5 specialized agents to generate complete illustrated stories. Input any topic and get a professional 5-chapter book with custom FLUX.1-dev images, formatted as PDF/HTML. Perfect for parents, educators & storytellers! 🤖📚✨
- **本地描述**：AI-powered storybook creator using 5 specialized agents to generate complete illustrated stories. Input any topic and get a professional 5-chapter book with custom FLUX.1-dev images, formatted as PDF/HTML. Perfect for parents, educators & storytellers! 🤖📚✨
- **拉取时间**：2026-07-23 22:44:46

---

# 📚 Storybook Generator

> **Create beautiful, illustrated storybooks about any topic using AI!**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green.svg)](https://crewai.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.0%20Flash-orange.svg)](https://ai.google.dev)
[![FLUX](https://img.shields.io/badge/FLUX-1.dev-purple.svg)](https://huggingface.co/black-forest-labs/FLUX.1-dev)

An intelligent multi-agent system that creates professional storybooks with custom illustrations. Perfect for parents, educators, and anyone who loves storytelling!

## ✨ Features

- 🤖 **Multi-Agent AI System**: 5 specialized AI agents working together
- 📖 **Complete Storybooks**: 5 chapters, ~100 words each, age-appropriate for 4-8 years
- 🎨 **Custom Illustrations**: AI-generated images using FLUX.1-dev model
- 📄 **Professional Output**: High-quality PDF and HTML formats
- 🎯 **Any Topic**: Create stories about anything your child loves
- 🔄 **Smart Rate Limiting**: Handles API quotas gracefully
- 📱 **Mobile-Friendly**: Responsive HTML output for all devices

## 🎬 Demo

```bash
$ python main.py

📚 What topic would you like your storybook to be about?

💡 Here are some popular topics for inspiration:
   • Animals (farm animals, jungle animals, pets)
   • Space and planets
   • Friendship and kindness
   [...]

✏️  Enter your story topic: magical forest animals

📖 You chose: 'magical forest animals'
Is this correct? (y/n): y

🎨 Creating a wonderful storybook about 'magical forest animals' for you!
⏳ This may take several minutes due to rate limiting...
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google AI API key (for Gemini)
- Hugging Face API key (for FLUX.1-dev)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/naakaarafr/Storybook-Generator.git
   cd Storybook-Generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # Create a .env file or export directly
   export GOOGLE_API_KEY="your_google_ai_api_key_here"
   export HUGGINGFACE_API_KEY="your_huggingface_api_key_here"
   ```

4. **Install PDF tools (optional but recommended):**
   ```bash
   # Option 1: WeasyPrint (recommended)
   pip install weasyprint
   
   # Option 2: mdpdf
   pip install mdpdf
   
   # Option 3: pdfkit + wkhtmltopdf
   pip install pdfkit
   # Then install wkhtmltopdf from https://wkhtmltopdf.org/downloads.html
   ```

5. **Run the generator:**
   ```bash
   python main.py
   ```

## 🔑 API Keys Setup

### Google AI (Gemini) API Key
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new project or select existing one
3. Generate an API key
4. Set the `GOOGLE_API_KEY` environment variable

### Hugging Face API Key
1. Visit [Hugging Face](https://huggingface.co/settings/tokens)
2. Create a new token with "Read" permissions
3. Set the `HUGGINGFACE_API_KEY` environment variable

## 🛠️ How It Works

The system uses 5 specialized AI agents in a sequential workflow:

```mermaid
graph LR
    A[Story Outliner] --> B[Story Writer]
    B --> C[Image Generator]
    C --> D[Content Formatter]
    D --> E[PDF Converter]
```

### 🤖 The AI Agents

1. **📋 Story Outliner**
   - Creates story structure and character profiles
   - Develops 5 chapter outlines
   - Ensures age-appropriate themes

2. **✍️ Story Writer**
   - Writes complete story content
   - ~100 words per chapter
   - Maintains narrative consistency

3. **🎨 Image Generator**
   - Creates custom illustrations using FLUX.1-dev
   - One image per chapter
   - Handles generation failures gracefully

4. **📝 Content Formatter**
   - Formats content with professional styling
   - Creates publication-ready layouts
   - Handles images and placeholders

5. **📄 PDF Converter**
   - Converts to high-quality PDF
   - Multiple conversion methods
   - Fallback to enhanced HTML

## 📁 Project Structure

```
storybook-generator/
├── agents.py              # AI agent definitions
├── config.py              # Configuration and rate limiting
├── crew.py                # CrewAI crew setup
├── main.py                # Main application entry point
├── tasks.py               # Task definitions for agents
├── tools.py               # Custom tools and utilities
├── template.md            # Story template (auto-generated)
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── output/
    ├── story.md           # Generated markdown story
    ├── story.pdf          # Generated PDF (if conversion succeeds)
    ├── story.html         # Enhanced HTML version
    └── *.png              # Generated illustrations
```

## ⚙️ Configuration

### Rate Limiting
The system includes intelligent rate limiting for API calls:

- **Gemini API**: 15 requests per minute (configurable)
- **Automatic retries** with exponential backoff
- **Smart waiting** between failed requests
- **Usage tracking** and warnings

### Customization

You can customize the system by modifying:

- `config.py`: API settings and rate limits
- `agents.py`: Agent behaviors and goals
- `tasks.py`: Task descriptions and requirements
- `tools.py`: Image generation and PDF conversion

## 📊 Output Files

After successful generation, you'll find:

- **📖 story.md**: Markdown version of your storybook
- **📄 story.pdf**: Professional PDF (if conversion succeeds)
- **🌐 story.html**: Enhanced HTML with print functionality
- **🖼️ *.png**: Generated illustrations (or placeholder descriptions)

## 🎨 Sample Topics

Try these engaging topics:

**Animals & Nature:**
- Magical forest animals
- Ocean adventure with dolphins
- Farm animals' friendship
- Jungle safari expedition

**Space & Science:**
- Journey to the moon
- Robot friends from space
- Solar system exploration
- Time machine adventures

**Fantasy & Magic:**
- Princess and the dragon
- Wizard's apprentice
- Fairy garden secrets
- Enchanted castle mystery

**Everyday Adventures:**
- First day at school
- Family camping trip
- Cooking with grandma
- Neighborhood helpers

## 🔧 Troubleshooting

### Common Issues

**❌ "No PDF conversion tools found"**
```bash
# Install one of these:
pip install weasyprint       # Recommended
pip install mdpdf           # Alternative
pip install pdfkit          # Requires wkhtmltopdf
```

**❌ "Rate limit exceeded"**
- The system handles this automatically
- Wait for the specified time
- Check your API quotas

**❌ "Image generation failed"**
- Images will be replaced with detailed descriptions
- Check your Hugging Face API key
- Verify API quota availability

**❌ "Font errors with WeasyPrint"**
- Usually safe to ignore
- PDF is often created successfully
- Try using mdpdf as alternative

### Environment Variables

Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_google_ai_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
```

## 📋 Requirements

### Python Packages
```txt
crewai>=0.28.0
langchain-google-genai>=1.0.0
pillow>=9.0.0
requests>=2.28.0
markdown>=3.4.0

# PDF conversion (choose one or more)
weasyprint>=60.0  # Recommended
mdpdf>=1.0.0      # Alternative
pdfkit>=1.0.0     # Requires wkhtmltopdf
```

### System Requirements
- Python 3.8+
- Internet connection for API calls
- 500MB+ free disk space
- Optional: wkhtmltopdf for pdfkit

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **🐛 Bug Reports**: Open an issue with details
2. **💡 Feature Requests**: Suggest new capabilities
3. **🔧 Code Improvements**: Submit pull requests
4. **📚 Documentation**: Help improve docs
5. **🎨 Templates**: Create new story templates

### Development Setup

```bash
# Clone and setup
git clone https://github.com/naakaarafr/storybook-generator.git
cd storybook-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt  # If it exists
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[CrewAI](https://crewai.com)**: Multi-agent orchestration framework
- **[Google Gemini](https://ai.google.dev)**: Advanced language model
- **[FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)**: State-of-the-art image generation
- **[Hugging Face](https://huggingface.co)**: AI model hosting and inference

## 📞 Support

- **📧 Issues**: [GitHub Issues](https://github.com/naakaarafr/storybook-generator/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/naakaarafr/storybook-generator/discussions)
- **📖 Documentation**: Check this README and code comments

## 🎯 Roadmap

Future enhancements planned:

- [ ] **Multiple Languages**: Support for non-English stories
- [ ] **Custom Characters**: Upload and use custom character descriptions
- [ ] **Interactive Mode**: Real-time story editing and preview
- [ ] **Audio Narration**: Text-to-speech integration
- [ ] **Batch Generation**: Create multiple stories at once
- [ ] **Template Library**: Pre-made story templates
- [ ] **Character Consistency**: Maintain character appearance across images
- [ ] **Story Variations**: Generate alternative versions of the same story

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">

</div>
