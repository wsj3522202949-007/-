---
id: tool-00959
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-Based-Story-Book-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/eshabalaji/ai-based-story-book-generator
created: 2026-07-18
updated: 2026-07-18
no: 959
category: 二、网文 / 长篇 AI 写作系统 库
repo: eshabalaji/AI-Based-Story-Book-Generator
stars: 1
url: https://github.com/eshabalaji/ai-based-story-book-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2c36e61eace6938c
  - methods/最强写作方法论_全球最强综合版.md
---

# eshabalaji/AI-Based-Story-Book-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/eshabalaji/ai-based-story-book-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：This project details an AI-powered storybook generator. It utilizes Claude 3 Haiku for dynamic story creation and a Stable Diffusion model for generating corresponding images based on any user-provided theme or prompt. A robust system compiles these AI-generated stories and images into downloadable PDF storybooks.
- **本地描述**：This project details an AI-powered storybook generator. It utilizes Claude 3 Haiku for dynamic story creation and a Stable Diffusion model for generating corresponding images based on any user-provided theme or prompt. A robust system compiles these AI-generated stories and images into downloadable PDF storybooks.
- **拉取时间**：2026-07-23 23:07:01

---

# 📖 AI Storybook Generator

## Overview

This project develops an interactive AI-powered storybook generator, built with Streamlit, that allows users to create unique, illustrated storybooks from any text prompt. It seamlessly integrates state-of-the-art AI models for both narrative creation and image generation, then compiles the complete storybook into a downloadable PDF.

## Features

* **Prompt-to-Story Generation:** Uses **Claude 3 Haiku** (via OpenRouter) to generate engaging and creative stories based on user input.
* **Contextual Image Generation:** Leverages **BART-large-CNN** for intelligent summarization to create image prompts, which are then used by **SDXL-Turbo** to generate relevant illustrations for each story chunk.
* **Interactive Web UI:** Built with **Streamlit** for an easy-to-use and responsive user experience.
* **Downloadable PDF Output:** Compiles the generated story text and images into a professionally formatted PDF, ready for download, using **FPDF**.
* **Efficient Caching:** Utilizes Streamlit's caching mechanisms (`@st.cache_data`, `@st.cache_resource`) for optimized performance.

## How It Works

The application orchestrates a multi-step AI pipeline like:

1.  **User Input:** The user provides a story theme or prompt via the Streamlit interface.
2.  **Story Generation:** The prompt is sent to the **Claude 3 Haiku** model (accessed via OpenRouter API) to generate the full story text.
3.  **Content Segmentation & Summarization:** The generated story is split into readable chunks. **BART-large-CNN** then summarizes these chunks to create concise, effective prompts for image generation.
4.  **Image Generation:** The summarized prompts are fed into the **SDXL-Turbo** model to create corresponding illustrations. Images are saved locally.
5.  **Interactive Display:** The generated story text and images are displayed within the Streamlit web application.
6.  **PDF Compilation:** All story segments and their respective images are compiled into a single PDF document using **FPDF**, with automatic page breaks and formatting.
7.  **Download:** The user can download the complete storybook as a PDF directly from the Streamlit app.

## Technologies Used

* **Frontend:** Streamlit
* **Backend/Logic:** Python
* **AI Models:**
    * **Claude 3 Haiku** (via OpenRouter API) - *for story generation*
    * **BART-large-CNN** - *for summarizing story chunks into image prompts*
    * **SDXL-Turbo** - *for generating images from text prompts*
* **Python Libraries:**
    * `streamlit`
    * `requests` (for API calls)
    * `json`
    * `re` (regex for text processing)
    * `os` (file system operations)
    * `PIL (Pillow)` (image handling)
    * `io` (byte stream handling)
    * `fpdf` (PDF generation)
    * `torch` (PyTorch for GPU acceleration with Diffusers)
    * `transformers` (Hugging Face Transformers for BART-large-CNN)
    * `diffusers` (Hugging Face Diffusers for SDXL-Turbo)
    * `accelerate`, `safetensors` (for Diffusers pipeline optimization)
* **Execution Environment:** Google Colab (with `pyngrok` and `localtunnel` for public access)

## Setup and Running in Google Colab

This application is designed to be easily run within a Google Colab environment.

1.  **Open a new Google Colab notebook.**

2.  **Install Dependencies:** Run the following cells to install all required Python packages.

    ```python
    !pip install streamlit fpdf transformers diffusers accelerate safetensors pyngrok
    # The next line is often included for Streamlit, but might not be strictly necessary if already installed above
    !pip install streamlit -q
    ```

3.  **Set Your API Key:** **Replace `"YOUR_API_KEY"`** with your actual API key for OpenRouter.

    ```python
    # ========== CONFIGURATION ==========
    API_KEY = "YOUR_API_KEY"  # <related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- IMPORTANT: Replace with your actual API key for OpenRouter
    MODEL = "anthropic/claude-3-haiku"
    IMG_MODEL = "stabilityai/sdxl-turbo"
    ```

4.  **Paste the Application Code:** Copy and paste the entire Streamlit application code (`import streamlit as st` down to `st.download_button(...)`) into a new cell in your Colab notebook.

5.  **Save as `app.py`:** After pasting, right-click on the cell and select "File" -> "Save as..." and name the file `app.py`. (Or use `%%writefile app.py` at the top of the cell).

    ```python
    %%writefile app.py
    import streamlit as st
    # ... rest of your code ...
    ```

6.  **Run the Streamlit App:** Execute the following commands in a new Colab cell to start the Streamlit app and expose it publicly via `localtunnel`.

    ```python
    !wget -q -O - ipv4.icanhazip.com
    !streamlit run app.py & npx localtunnel --port 8501
    ```
    * The `!wget` command will show you your Colab's public IP address.
    * `npx localtunnel --port 8501` will provide a public URL (e.g., `https://xxxx-your-colab-ip.loca.lt`) that you can open in your browser to access the Streamlit application.
