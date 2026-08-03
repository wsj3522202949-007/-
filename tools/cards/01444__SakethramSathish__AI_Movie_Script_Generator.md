---
id: tool-01444
type: tool
area: 库
status: active
tags: [Python, 协议传染, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI_Movie_Script_Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/sakethramsathish/ai_movie_script_generator
created: 2026-07-18
updated: 2026-07-18
no: 1444
category: 二、网文 / 长篇 AI 写作系统 库
repo: SakethramSathish/AI_Movie_Script_Generator
stars: 4
url: https://github.com/sakethramsathish/ai_movie_script_generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# SakethramSathish/AI_Movie_Script_Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sakethramsathish/ai_movie_script_generator
- **Stars**：4
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：Story2Screen is an AI-powered film pre-production system that converts raw story ideas into structured movie screenplays and cinematic trailers. It uses a multi-stage LLM pipeline for story analysis, plot structuring, screenplay writing, scene extraction, and trailer generation via a Streamlit interface.
- **本地描述**：Story2Screen is an AI-powered film pre-production system that converts raw story ideas into structured movie screenplays and cinematic trailers. It uses a multi-stage LLM pipeline for story analysis, plot structuring, screenplay writing, scene extraction, and trailer generation via a Streamlit interface.
- **拉取时间**：2026-07-23 23:21:12

---

# 🎬 Story2Screen - AI Movie Script Generator



**Transform any story into a professional movie screenplay and trailer with AI-powered automation.**



Story2Screen is an intelligent application that takes a narrative—whether it's a story idea, Reddit post, or creative concept—and automatically generates:

- ✨ A complete **movie screenplay** with proper formatting

- 🎥 A compelling **movie trailer** extracted from cinematic moments

- 📄 A downloadable **PDF** combining both outputs



---



## 🚀 Features



- **Story-to-Screenplay Pipeline**: Intelligent conversion from narrative text to professional screenplay format

- **AI-Powered Analysis**: Uses Google Gemini 2.5 Flash for creative and coherent story understanding

- **Scene Extraction**: Automatically identifies cinematic moments from the screenplay

- **Trailer Generation**: Creates an engaging trailer strictly from screenplay content

- **PDF Export**: Download scripts and trailers in professional PDF format

- **Streamlit Web Interface**: User-friendly web app with real-time processing feedback

- **Modular Architecture**: Clean separation of concerns for easy customization



---



## 📋 Workflow



```

Story Input

    ↓

Story Analysis (Analyze themes, characters, plot structure)

    ↓

Plot Building (Create detailed plot outline)

    ↓

Screenplay Writing (Generate formatted movie script)

    ↓

Scene Extraction (Identify key cinematic moments)

    ↓

Trailer Generation (Craft engaging trailer from scenes)

    ↓

PDF Export (Download as professional document)

```



---



## 💻 Tech Stack



- **Backend**: Python 3.8+

- **UI Framework**: [Streamlit](https://streamlit.io/) - Simple and elegant web interface

- **AI/LLM**: [Google Generative AI (Gemini 2.5 Flash)](https://ai.google.dev/) - Fast creative text generation

- **PDF Generation**: [fpdf](https://py-pdf.github.io/fpdf2/) - Professional document export

- **Environment Management**: python-dotenv - Secure API key handling



---



## 🔧 Installation



### Prerequisites

- Python 3.8 or higher

- Google Gemini API key ([get one free here](https://ai.google.dev/))



### Step 1: Clone the Repository

```bash

git clone <repository-url>

cd "AI Movie Script Generator"

```



### Step 2: Create Virtual Environment (Optional but Recommended)

```bash

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

```



### Step 3: Install Dependencies

```bash

pip install -r requirements.txt

```



### Step 4: Set Up Environment Variables

Create a `.env` file in the project root:

```env

GEMINI_API_KEY=your_api_key_here

```



---



## 🎯 Quick Start



### Running the Application

```bash

streamlit run app.py

```



The web interface will open at `http://localhost:8501`



### Basic Usage

1. **Paste your story** in the text area (story idea, Reddit post, plot synopsis, etc.)

2. **Click "🎥 Generate Script & Trailer"**

3. **Review the outputs**:

   - Movie screenplay with proper formatting

   - Generated trailer

4. **Download as PDF** for sharing or printing



---



## 📁 Project Structure



```

AI Movie Script Generator/

├── app.py                      # Main Streamlit application

├── requirements.txt            # Python dependencies

├── verify_prompts.py          # Utility for validating prompt quality

│

├── config/

│   ├── settings.py            # Gemini API configuration

│   └── __pycache__/

│

├── core/                       # Core processing modules

│   ├── story_analyzer.py      # Analyzes narrative structure and themes

│   ├── plot_builder.py        # Creates detailed plot outlines

│   ├── script_writer.py       # Generates screenplay from plot

│   ├── scene_extractor.py     # Identifies cinematic moments

│   ├── trailer_generator.py   # Creates trailer from scenes

│   └── __pycache__/

│

├── utils/                      # Utility functions

│   ├── formatter.py           # Text formatting and parsing

│   ├── pdf_generator.py       # PDF document creation

│   └── __pycache__/

│

├── prompts/                    # AI prompt templates

│   ├── analysis.txt           # Story analysis prompts

│   ├── plot.txt               # Plot building prompts

│   ├── scene_extract.txt      # Scene identification prompts

│   ├── screenplay.txt         # Screenplay writing prompts

│   └── trailer.txt            # Trailer generation prompts

│

├── outputs/                    # Generated output directory

│   ├── scripts/               # Saved screenplays

│   └── trailers/              # Saved trailers

│

└── README.md                  # This file

```



---



## 🔑 Configuration



### API Configuration

The application uses Google's Gemini 2.5 Flash model by default, configured in [config/settings.py](config/settings.py).



To use a different model:

```python

MODEL_NAME = "gemini-pro"  # or another available model

```



### Custom Prompts

Modify prompt templates in the `prompts/` directory to customize:

- Story analysis approach

- Plot structure preferences

- Screenplay format

- Trailer tone and style



---



## 📚 How It Works



### 1. Story Analysis

The application analyzes the input story to extract:

- Main themes and messages

- Character profiles and arcs

- Plot structure and key turning points

- Emotional tone and pacing



### 2. Plot Building

Creates a structured outline including:

- Three-act structure breakdown

- Scene-by-scene progression

- Character development points

- Dialogue and action requirements



### 3. Screenplay Writing

Generates a professional screenplay with:

- Proper screenplay formatting (INT./EXT., action, dialogue)

- Scene headings and descriptions

- Character names and dialogue

- Parenthetical directions



### 4. Scene Extraction

Identifies the most cinematic and impactful moments from the screenplay based on:

- Visual interest

- Emotional impact

- Plot importance

- Entertainment value



### 5. Trailer Generation

Creates an engaging trailer that:

- Showcases the story's best moments

- Maintains narrative coherence

- Builds suspense and interest

- Stays true to screenplay content



---



## 🤝 Contributing



Contributions are welcome! Feel free to:

- Report bugs and issues

- Suggest improvements

- Add new features

- Optimize existing code

- Enhance prompt templates



---



## ⚠️ Important Notes



- **API Usage**: Free tier of Google Gemini API may have rate limits. Check [pricing details](https://ai.google.dev/pricing)

- **Output Quality**: Results depend on story clarity and length. Well-structured input produces better screenplays

- **Customization**: Modify prompts and models for different genres and styles

- **Dependencies**: Ensure all packages in requirements.txt are installed



---



## 📝 License



This project is licensed under the GNU General Public License v3.0 (GPL-3.0).



You are free to:

- Use, modify, and distribute this software

- Use it for both commercial and non-commercial purposes



Under the condition that you:

- Include a copy of the license with any distribution

- Disclose the source code

- Include a notice of modifications

- Use the same license for derivative works



For more details, see the [GNU GPL v3.0 License](https://www.gnu.org/licenses/gpl-3.0.html).



---



## 🎓 Learning Resources



- [Screenwriting Basics](https://www.masterclass.com/articles/screenwriting-101)

- [Streamlit Documentation](https://docs.streamlit.io/)

- [Google Generative AI Guide](https://ai.google.dev/docs)

- [PDF Generation with fpdf](https://py-pdf.github.io/fpdf2/)



---



## 🐛 Troubleshooting



### Error: "GEMINI_API_KEY not found"

- Ensure `.env` file exists in project root

- Verify API key is correctly set: `GEMINI_API_KEY=your_key`

- Restart the Streamlit app



### Slow Generation

- This is normal for longer stories (can take 1-3 minutes)

- Gemini 2.5 Flash prioritizes quality over speed

- Check internet connection



### PDF Export Issues

- Ensure `fpdf` is installed: `pip install fpdf`

- Check write permissions in outputs directory



---



## 📧 Support



For issues, questions, or suggestions, please review the code documentation or check the prompts in the `prompts/` directory for customization options.



related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---



**Made with ❤️ for storytellers and screenwriters**



*Story2Screen - Because every great story deserves to be on screen.*

