---
id: tool-01847
type: tool
area: 库
status: active
tags: [Python, 协议传染, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: Novel_Generator_By_AI
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/coderblog-winson/novel_generator_by_ai
created: 2026-07-18
updated: 2026-07-18
no: 1847
category: 二、网文 / 长篇 AI 写作系统 库
repo: coderblog-winson/Novel_Generator_By_AI
stars: 11
url: https://github.com/coderblog-winson/novel_generator_by_ai
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 6c207af9fb579c78
  - methods/最强写作方法论_全球最强综合版.md
---

# coderblog-winson/Novel_Generator_By_AI

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/coderblog-winson/novel_generator_by_ai
- **Stars**：11
- **语言**：Python
- **License**：AGPL-3.0
- **Topics**：—
- **GitHub 描述**：A multi-functional novel generator based on a large language model, helping you to efficiently create long stories with rigorous logic and unified settings
- **本地描述**：A multi-functional novel generator based on a large language model, helping you to efficiently create long stories with rigorous logic and unified settings
- **拉取时间**：2026-07-23 23:32:52

---

<p align="center">
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="./README_CN.md"><img alt="简体中文版自述文件" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
</p>

# 📖 Automatic novel（eBook） generation tool

This project is base on [AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator)

## 💎 In addition to the official functions, I have also added some new features:
 1. Supports the generation of novels in multiple languages, and the interface also supports multiple languages. Currently, only Chinese and English are available, but other languages ​​can be added easily.
 2. Automatically load the current chapter every time it starts
 3. The expansion function has been optimized. The original version can only be expanded once and the original content is rewrite each time. However, due to the limitations of the AI ​​model, it is impossible to write too long content once. Therefore, my approach now is to continue writing on the original content and superimpose the new content every time. In this way, after many operations, a long enough content can be generated.
 4. English counting is also supported during expansion
 5. Add a button to each content page to facilitate the copying of the current content directly
 6. Support increase and decrease the font size in editor

 The following is the official instructions (I made some changes based on this modified version):

<div align="center">

✨ **Core functions** ✨

 | Functional Modules                | Key Capabilities                                                        |
 |-----------------------------------|-------------------------------------------------------------------------|
 | 🎨 Novel Setting Workshop         | World View Architecture / Character Setting / Plot Blueprint            |
 | 📖 Intelligent chapter generation | Multi-stage generation to ensure plot consistency                       |
 | 🧠 Status Tracking System         | Role Development Trajectory / Foreshadowing Management System           |
 | 🔍 Semantic Retrieval Engine      | Vector-based long-range context consistency maintenance                 |
 | 📚 Knowledge Base Integration     | Support local document reference                                        |
 | ✅ Automatic review mechanism      | Detect plot conflicts and logical conflicts                             |
 | 🖥 Visual Workbench               | Full process GUI operation, configuration/generation/review integration |

</div>

> A multi-functional novel generator based on a large language model, helping you to efficiently create long stories with rigorous logic and unified settings

---
## 📑 Catalog Navigation

 1. [Environmental Preparation] (#-Environmental Preparation)
 2. [Project Architecture]      (#-Project Architecture)
 3. [Configuration Guide]       (#⚙️-Configuration Guide)
 4. [Operation Instructions]    (#🚀-Operation Instructions)
 5. [User Tutorial]             (#📘-User Tutorial)
 6. [Troubleshooting]           (#❓-Troubleshooting)

---
## 🛠 Environmental preparation

 Ensure that the following operating conditions are met:
 - **Python 3.9+** Running Environment (recommended between 3.10-3.12)
 - **pip** Package Management Tool
 - Valid API key:
 - Cloud services: OpenAI / DeepSeek, etc.
 - Local services: Ollama and other OpenAI-compatible interfaces
---

## 📥 Installation Instructions

1. **Download Project**
   
    - Download the project ZIP file via [GitHub](https://github.com), or clone the project using the following command:
    ```bash
    git clone https://github.com/coderblog-winson/eBook_Generator
    ```

2. **Installing the compilation tool (optional)**
   
    - If some packages cannot be installed normally, access [Visual Studio Build Tools](https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/) to      download and install the C++ compilation tool for building some module packages;
    - When installing, only the MSBuild tool is included by default. You need to manually check the **C++ desktop development option in the list bar in the upper left corner.

3. **Installing dependencies and running**
   
    - Open the terminal and enter the project source file directory:
    ```bash
    cd AI_NovelGenerator
    ```
    - Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    - After the installation is completed, run the main program:
    ```bash
    python main.py
    ```

>If partial dependencies are missing, follow-up ** manual execution**
>```bash
>pip install XXX
>```
>Just install

## 🗂 Project Architecture
```
novel-generator/
├── main.py                      # Entry file, run GUI
├── ui.py                        # Graphic interface
├── novel_generator.py           # Chapter generation core logic
├── consistency_checker.py       # Consistency check to prevent plot conflicts
|—— chapter_directory_parser.py  # Directory analysis
|—— embedding_adapters.py        # Embedding Interface Packaging
|—— llm_adapters.py              # LLM Interface Packaging
├── prompt/[lang code].py        # Definition AI prompt words with multiple language
├── utils.py                     # Commonly tool functions, file operations
├── config_manager.py            # Manage configuration (API Key, Base URL)
├── config.json                  # User profile (optional)
└── vectorstore/                 # (Optional) Local vector database storage
```

---

## ⚙️ Configuration Guide
### 📌 Basic configuration（config.json）
```json
{
    "api_key": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "base_url": "https://api.openai.com/v1",
    "interface_format": "OpenAI",
    "model_name": "gpt-4o-mini",
    "temperature": 0.7,
    "max_tokens": 4096,
    "embedding_api_key": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "embedding_interface_format": "OpenAI",
    "embedding_url": "https://api.openai.com/v1",
    "embedding_model_name": "text-embedding-ada-002",
    "embedding_retrieval_k": 4,
    "topic": "The star-distanced railway protagonist star travels to the Genshin Impact Continent, saves the Tivat continent, and develops love, hate and love with the characters in it",
    "genre": "Fantasy",
    "num_chapters": 120,
    "word_number": 4000,
    "filepath": "D:/AI_NovelGenerator/filepath"
}
```

### 🔧 Configuration instructions
1. **Generate model configuration**
   - `api_key`: API key for big model service
   - `base_url`: API terminal address (fill in Ollama and other addresses for local services)
   - `interface_format`: Interface mode
   - `model_name`: Main Generative Model Name (such as gpt-4, claude-3, etc.)
   - `temperature`: Creativity parameters (0-1, the higher the higher the creative)
   - `max_tokens`: Maximum reply length of the model

2. **EmbeddingModel configuration**
   - `embedding_model_name`: Model name (such as Ollama's nomic-embed-text)
   - `embedding_url`: Service address
   - `embedding_retrieval_k`: 

3. **Novel parameter configuration**
   - `topic`: Core story theme
   - `genre`: Type of work
   - `num_chapters`: Total chapter count
   - `word_number`: Number of words in a single chapter
   - `filepath`: Generate file storage path

---

## 🚀 Operation instructions
### **Method 1: Use the Python interpreter**
```bash
python main.py
```
After execution, the GUI will be launched, and you can perform various operations in the graphical interface.

### **Method 2: Package as an executable file**
If you want to use this tool on a machine without a Python environment, you can use **PyInstaller** to package it:

```bash
pip install pyinstaller
pyinstaller main.spec
```
After packaging, an executable file (such as `main.exe` under Windows) will be generated in the `dist/` directory.

---

## 📘 Usage tutorial
1. **After starting, complete the basic parameter setting first：**  
   - **API Key & Base URL**（such as `https://api.openai.com/v1`）  
   - **Model name**（Such as `gpt-3.5-turbo`, `gpt-4o`, etc.）  
   - **Temperature** (0~1, determines the level of creative writing)
   - **Topic** (such as "AI Rebellion in Wasteland World")
   - **Genre** (such as "Science Fiction"/"Magic"/"Urban Fantasy")
   - **Number of chapters**, **Number of words per chapter** (such as 10 chapters, about 3000 words per chapter)
   - **Save path** (It is recommended to create a new output folder)
  
2. **Click "Step1. Generate architecture"**  
   - The system will generate:
     - `Novel_setting.txt`: Contains worldview, character information, thunder points and dark lines, etc.  
   - You can view or modify the architecture in the generated `Novel_setting.txt`.

3. **Click "Step2. Generate Outline"**  
   - The system will generate all chapters based on the completed `Novel_setting.txt` content:
     - `Novel_outline.txt`：Includes titles and brief tips for each chapter.
   - Chapter titles and descriptions can be viewed, modified, or supplemented in the generated file.

4. **Click "Step3. Generate Draft"**  
   - Before generating the chapter, you can: 
     - **Set chapter number**(If you generate Chapter 1, fill in `1`)
     - **Providing any expectations or tips for the plot of this chapter in the "Guide to this chapter" input box**
   - After clicking the button, the system will:
     - Automatically read the previous settings, `Novel_outline.txt`, and finalized chapters
     - Call vector search and review the plot to ensure context coherence
     - Outline of Generating the Chapter (`outline_X.txt`) and Text (`chapter_X.txt`)
   - After the generation is completed, you can view and edit the draft content of this chapter in the text box on the left.

5. **Click "Step4. Final chapter"**  
   - The system will:  
     - **Update global summary** (write `global_summary.txt`)
     - **Update role status** (write to `character_state.txt`)
     - **Update the vector search library** (Make sure that subsequent chapters can call the latest information)
     - **Update plot points** (such as `plot_arcs.txt`)
   - After the finalization is completed, you can see the finalized text in `chapter_X.txt`.

6. **Consistency check (optional)**
   - Click the "[Optional] Consistency Review" button to detect conflicts on the latest chapters, such as character logic, plot inconsistencies, etc.
   - If there is a conflict, a detailed prompt will be output in the log area.

7. **Repeat steps 4-6** until all chapters are generated and finalized!
   
> **Vector search configuration tips**  
> 1. The embedding model needs to display the specified interface and model name;
> 2. When using the **Embedding** of local Ollama**, you need to start the Ollama service in advance:
>    ```bash
>    ollama serve  # Start the service
>    ollama pull nomic-embed-text  # Download/Enable the model
>    ```
> 3. It is recommended to clear the vectorstore directory after switching different Embedding models.
> 4. Cloud Embedding must ensure that the corresponding API permissions are enabled

8. **Detail introduction**

   - You can find the detail introduction [here](https://medium.com/stackademic/the-powerful-novel-generator-by-ai-78a3710c07b9).

---

## ❓ Troubleshooting
### Q1: Expecting value: line 1 column 1 (char 0)

This problem is most likely due to the API not responding correctly, maybe it responds to an html? Other contents lead to the error;


### Q2: HTTP/1.1 504 Gateway Timeout？
Confirm whether the interface is stable;

### Q3:How to switch between different Embedding providers?
Just enter the corresponding input in the GUI interface.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

If you have any more questions or needs, please feel free to ask in the **Project Issues**.
