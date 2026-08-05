---
id: tool-00247
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: christmas-story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/tommasofacchin/christmas-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 247
category: 二、网文 / 长篇 AI 写作系统 库
repo: tommasofacchin/christmas-story-generator
stars: 1
url: https://github.com/tommasofacchin/christmas-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# tommasofacchin/christmas-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/tommasofacchin/christmas-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：groq-api, huggingface, pytorch, stable-diffusion, streamlit
- **GitHub 描述**：Streamlit web app built for the Datapizza AI Christmas Challenge. It uses a Groq‑backed Datapizza client for text generation, PyTorch + diffusers (SDXL) for images
- **本地描述**：Streamlit web app built for the Datapizza AI Christmas Challenge. It uses a Groq‑backed Datapizza client for text generation, PyTorch + diffusers (SDXL) for images
- **拉取时间**：2026-07-23 22:46:18

---

Christmas Story Generator 🎄
============================

Christmas Story Generator is a Streamlit web app built for the **Datapizza AI Christmas Challenge**. It creates short, cozy Christmas stories for kids and generates one illustration per scene using **Groq + Datapizza AI** for text and **PyTorch + diffusers (SDXL)** for images.

The goal is to explore an end‑to‑end storybook pipeline: prompt engineering for safe, kid‑friendly stories, automatic scene splitting, image‑prompt generation, and a simple web UI for running everything locally.

***

## Tech stack

- Frontend / UI: Streamlit.
- LLM client: Datapizza OpenAI-style client (Groq backend).
- Image generation: PyTorch + `diffusers` with Stable Diffusion XL base 1.0.
- PDF / images: Pillow, ReportLab.
- Environment: Python 3.10-3.12 in a dedicated virtual environment (avoid 3.13 for now due a libs support).

***

## Features

- Input:
  - Child name and age.
  - Themes / keywords, with a button to sample 3 random themes from a predefined pool.
- Story generation:
  - A Datapizza `Agent` writes a short Christmas story split into scenes, each ending with `[SCENE_BREAK]`.
  - A safety tool sanitizes edgy keywords into kid‑friendly Christmas concepts (e.g. “gun” → “snowball blaster”).
- Character description:
  - A second `Agent` generates a single, detailed visual description of the main character, optimized for inclusion in SDXL prompts.
- Image generation:
  - For each scene, a Stable Diffusion prompt is created by combining the scene text, the character description, and a fixed “storybook” style preset.
  - SDXL renders one illustration per scene.
- UI / UX:
  - Main page: Story settings, character description, full story, and a responsive HTML grid of all illustrated scenes.
  - History page: Browse previous storybooks, reload their text and images, and view them with the same HTML layout.

***

## Project structure

```text
.
├─ app.py                 # Streamlit UI entrypoint
├─ core/
│   ├─ __init__.py        # Re-exports build_clients, build_pipeline, generate_storybook
│   ├─ config.py          # Constants: OUT_DIR, STEPS, WIDTH/HEIGHT, STYLE_PRESET, NEGATIVE, THEME_POOL
│   ├─ clients.py         # Datapizza / Groq Agents, sanitize_keywords tool
│   ├─ pipeline.py        # SDXL pipeline construction (GPU/CPU)
│   ├─ story.py           # Story, character description, image-prompt generation
│   ├─ images.py          # generate_ai_illustration using SDXL
│   ├─ export.py          # PDF export (ReportLab)
│   └─ storybook.py       # Orchestrator: generate_storybook, save PNGs + story.json + PDF
├─ pages/
│   └─ 01_Stories_history.py  # Streamlit multipage: browse past stories
├─ outputs/
│   └─ <story_id>/
│       ├─ 01.png, 02.png, ...
│       ├─ story.json
│       └─ <ild>_christmas_storybook.pdf
├─ requirements.txt       # Python dependencies
└─ README.md              # This file
```

Each story is fully self‑contained in `outputs/<story_id>/`, including all images, metadata (`story.json`), and the exported PDF.

***

## Requirements

- Python: 3.10.x-3.12.x (recommended for PyTorch + diffusers).
- OS: developed on Windows; should work similarly on Linux/macOS with the same Python version.
- Hardware:
  - GPU (CUDA) strongly recommended for SDXL (large model, faster inference).
  - CPU‑only works but is slower; you may want to reduce:
    - `STEPS` (e.g. ~12–20).
    - `WIDTH` / `HEIGHT` (e.g. 512×512 or smaller).

---

## Installation & setup (Windows / PowerShell)

```powershell
# Clone the repository
git clone https://github.com/tommasofacchin/christmas-story-generator.git
cd christmas-story-generator

# Create a virtual environment (Python 3.10–3.12)
py -3.12 -m venv .venv

# Activate the venv
.\.venv\Scripts\Activate.ps1

python --version  # should show 3.10–3.12

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Deactivate when finished
deactivate
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Configuration: API keys and tokens

### GROQ API key (required)

The app uses a Datapizza client that talks to the **Groq** OpenAI‑compatible API.

- Start the app with `streamlit run app.py`.
- In the **sidebar**, paste your **GROQ API key** into the `GROQ API key` field.
- The key is only used at runtime and is not committed to the repo.

Each user can provide their own key when running the app locally or on their own deployment.

### Hugging Face token (optional)

- Used to authenticate, if needed, when downloading **Stable Diffusion XL base 1.0** from Hugging Face.
- If you don’t have a token or the model is accessible anonymously, you can leave this empty.

***

## SDXL pipeline: CPU vs GPU

In `core/pipeline.py`, the SDXL pipeline is built with a simple device check:

- If `torch.cuda.is_available()` is `True`, SDXL loads on **GPU** with half precision (`torch.float16`).
- Otherwise, it falls back to **CPU** in full precision (`torch.float32`).

On CPU you might want to tune parameters in `core/config.py`:

- `STEPS`: reduce for faster generation (e.g. 12–20).
- `WIDTH` / `HEIGHT`: smaller resolutions to fit memory and speed requirements.
- Optionally, fewer scenes (`MIN_SCENES`, `MAX_SCENES`) for lighter runs.

***


!`[Streamlit home](img/streamlit_home.png)`

## How it works (high level)

1. The user fills in child name, age, and themes (or clicks the 🎲 button to sample 3 random themes from `THEME_POOL`).  
2. `build_clients` creates two Datapizza Agents:
   - Story agent (writes the story with `[SCENE_BREAK]` separators).
   - Prompt agent (writes SDXL‑friendly visual/scene prompts).
3. `generate_storybook`:
   - Sanitizes keywords.
   - Generates the full story and splits it into scenes.
   - Generates a character description.
   - For each scene, generates a diffusion prompt and calls the SDXL pipeline to render an image.
   - Saves images and metadata under `outputs/<story_id>/`.
4. `app.py`:
   - Shows story info, character, and full story.
   - Renders all scenes in a responsive HTML grid (both for the live run and in the history page).
