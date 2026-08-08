---
id: tool-00833
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: CUSTOM
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/pariksith/custom
created: 2026-07-18
updated: 2026-07-18
no: 833
category: 二、网文 / 长篇 AI 写作系统 库
repo: pariksith/CUSTOM
stars: 1
url: https://github.com/pariksith/custom
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2b7e272eb3841098
  - methods/最强写作方法论_全球最强综合版.md
---

# pariksith/CUSTOM

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/pariksith/custom
- **Stars**：1
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：creative-writing, gradio, huggingface, poem-generator, python, qwen, rizz-generator, story-generator, transformers
- **GitHub 描述**：Custom Story Generator is a cinematic local AI writing app built with Gradio, Hugging Face Transformers, and PyTorch. It turns a short prompt into one of three output styles such as Story, Poem and Rizz
- **本地描述**：Custom Story Generator is a cinematic local AI writing app built with Gradio, Hugging Face Transformers, and PyTorch. It turns a short prompt into one of three output styles such as Story, Poem and Rizz
- **拉取时间**：2026-07-23 23:03:19

---



<div align="center">

# Custom Story Generator

### Turn a single prompt into a cinematic **Story**, **Poem**, or **Rizz** line.

A local AI writing app built with **Gradio**, **Hugging Face Transformers**, and **PyTorch**. It wraps a polished cinematic interface around a configurable text-generation model, so you can draft creative writing from your own machine without building a frontend or calling a hosted API.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-5.9.1-F97316?logo=gradio&logoColor=white)](https://www.gradio.app/)
[![Transformers](https://img.shields.io/badge/Transformers-Hugging%20Face-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/docs/transformers)
[![PyTorch](https://img.shields.io/badge/PyTorch-CPU%2FGPU-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License: All Rights Reserved](https://img.shields.io/badge/License-All%20Rights%20Reserved-red.svg)](LICENSE)

<img src="captures/screenshots/01-desktop-home.png" alt="Custom Story Generator hero screen" width="900">

</div>

---

## ✨ Why this is different

Most small text-generation demos stop at a plain textbox. **Custom Story Generator** focuses on the full writing moment: a cinematic landing view, mode selection, tuned prompt templates, length control, and a dedicated reading surface for the generated result.

- 🎭 **Three creative modes** - Story, Poem, and Rizz each use different system prompts and generation settings.
- 🖥️ **Local-first workflow** - runs as a Gradio app on your machine, with the model selected through environment variables.
- 🎬 **Cinematic UI** - full-screen hero art, animated particles, warm glass panels, and a dramatic compose/read flow.
- ⚙️ **Configurable model backend** - supports causal and seq2seq Transformer models.
- 📱 **Responsive captures included** - desktop, full-page, mobile, compose, footer, and generated-output screenshots are included.

---

## 🚀 Features

| Feature | Description |
|---|---|
| **Story mode** | Generates structured short fiction with a beginning, middle, and ending |
| **Poem mode** | Produces expressive verse with line breaks and an emotional arc |
| **Rizz mode** | Creates short, playful, respectful pickup lines |
| **Length control** | Slider from `0` to `1000` tokens, with sensible per-mode limits |
| **Prompt cleaning** | Normalizes model artifacts and spacing before showing the final text |
| **Model selection** | Set `TEXT_MODEL_NAME` and `TEXT_MODEL_KIND` without changing UI code |
| **Gradio interface** | One Python command launches the full web app |
| **Demo automation** | Playwright script captures screenshots and video; FFmpeg produces the MP4/GIF demo |

---

## 🖼️ Screenshots & Demo

<div align="center">
  <img src="demo_video/story-generator-demo.gif" alt="Custom Story Generator working demo" width="760"><br>
  <em>End-to-end flow: hero → compose → choose a mode → enter a prompt → create → read.</em>
</div>

<br>

| Hero | Compose |
|---|---|
| <img src="captures/screenshots/01-desktop-home.png" width="430" alt="Hero screen"> | <img src="captures/screenshots/04-desktop-prompt-poem.png" width="430" alt="Compose screen with prompt"> |
| **Generated output** | **How it works** |
| <img src="captures/screenshots/10-desktop-read-output.png" width="430" alt="Read output screen"> | <img src="captures/screenshots/06-desktop-how-it-works.png" width="430" alt="How it works footer"> |
| **Mobile hero** | **Mobile compose** |
| <img src="captures/screenshots/07-mobile-home.png" width="260" alt="Mobile hero screen"> | <img src="captures/screenshots/08-mobile-compose.png" width="260" alt="Mobile compose screen"> |


## 🧩 How It Works

```text
User prompt + selected mode
      |
      v
Mode-specific instruction template
  |-- Story: fiction structure, vivid details, natural pacing
  |-- Poem: imagery, rhythm, intentional line breaks
  |-- Rizz: concise, charming, respectful pickup line
      |
      v
Tokenizer + Transformer model
      |
      v
Text generation
  |-- temperature
  |-- top_p
  |-- repetition penalty
  |-- max_new_tokens
      |
      v
Cleanup
  |-- remove assistant/model markers
  |-- normalize spacing
  |-- mode-specific formatting
      |
      v
Gradio output textbox
```

---

## 🛠️ Tech Stack

- **UI:** Gradio Blocks, custom CSS, responsive HTML sections
- **Model runtime:** Hugging Face Transformers, PyTorch, Accelerate
- **Default model:** `Qwen/Qwen2.5-1.5B-Instruct`
- **Automation:** Playwright for screenshots/video capture
- **Media:** FFmpeg for MP4 and GIF generation
- **Deployment target:** Hugging Face Spaces or any local Python environment

---

## ⚙️ Model Configuration

The generator defaults to a causal language model:

```bash
TEXT_MODEL_NAME=Qwen/Qwen2.5-1.5B-Instruct
TEXT_MODEL_KIND=causal
```

You can swap in another compatible model:

```bash
# PowerShell
$env:TEXT_MODEL_NAME="distilgpt2"
$env:TEXT_MODEL_KIND="causal"
python run_app.py
```

For seq2seq models:

```bash
$env:TEXT_MODEL_NAME="google/flan-t5-base"
$env:TEXT_MODEL_KIND="seq2seq"
python run_app.py
```

---

## 📸 Regenerate Screenshots & Video

Start the app first:

```bash
python run_app.py
```

Then run the Playwright capture script in another terminal:

```bash
python tools/capture_app.py
```

Outputs:

```text
captures/screenshots/
captures/videos/story-generator-flow.mp4
captures/videos/*.webm
```

To rebuild the README GIF from the MP4:

```bash
ffmpeg -y -i captures/videos/story-generator-flow.mp4 -vf "fps=12,scale=900:-1:flags=lanczos,palettegen" demo_video/palette.png
ffmpeg -y -i captures/videos/story-generator-flow.mp4 -i demo_video/palette.png -lavfi "fps=12,scale=900:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=3" demo_video/story-generator-demo.gif
```

---

## 📂 Project Structure

```text
StoryGenerator-main/
├── app/
│   ├── Story_Generator.py   # model loading, prompt building, generation, cleanup
│   ├── ui.py                # Gradio Blocks UI and custom CSS
│   ├── hero_bg.png          # cinematic hero background
│   └── __init__.py
├── captures/
│   ├── screenshots/         # generated README screenshots
│   └── videos/              # Playwright webm + FFmpeg mp4 demo
├── demo_video/
│   └── story-generator-demo.gif
├── tools/
│   └── capture_app.py       # Playwright screenshot/video automation
├── requirements.txt
├── run_app.py
└── README.md
```

---

## ✅ Verification

Captured locally with:

- Playwright browser automation
- FFmpeg MP4 conversion
- A successful generated-output screenshot using Rizz mode

Latest captured output:

> Underneath that starlit sky, it's like a book just for you.

---

## 🚧 Limitations

- First generation can take time while the model loads into memory.
- Large models may require significant RAM or a GPU for comfortable speed.
- If the model is not cached locally, Transformers may download it on first run.
- Output quality depends on the selected model and available compute.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📜 License

[All Rights Reserved](https://github.com/pariksith/CUSTOM/blob/main/LICENSE) - this project may not be used, copied, modified, redistributed, published, or deployed without prior written permission from the owner. Unauthorized use may result in legal action.

<div align="center">

**Built with Gradio + Transformers + PyTorch.**

</div>
