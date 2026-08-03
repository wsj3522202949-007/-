---
id: tool-01147
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Bedtime-Story-Generator-with-Illustrations
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/dhanesvaran/bedtime-story-generator-with-illustrations
created: 2026-07-18
updated: 2026-07-18
no: 1147
category: 二、网文 / 长篇 AI 写作系统 库
repo: DHANESVARAN/Bedtime-Story-Generator-with-Illustrations
stars: 0
url: https://github.com/dhanesvaran/bedtime-story-generator-with-illustrations
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# DHANESVARAN/Bedtime-Story-Generator-with-Illustrations

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dhanesvaran/bedtime-story-generator-with-illustrations
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：The MD Industries Story Engine is a fully offline orchestration framework for generating illustrated storyboards. It integrates Local LLMs (Ollama) and Latent Diffusion Models (SDXL Turbo) to automate narrative generation, prompt extraction, and sequential image synthesis.
- **本地描述**：The MD Industries Story Engine is a fully offline orchestration framework for generating illustrated storyboards. It integrates Local LLMs (Ollama) and Latent Diffusion Models (SDXL Turbo) to automate narrative generation, prompt extraction, and sequential image synthesis.
- **拉取时间**：2026-07-23 23:12:29

---

# 📖 MD Industries: AI Story Engine
**An Asynchronous, Hardware-Governed Local AI Multimodal Generation Pipeline**

![Version](https://img.shields.io/badge/Version-16.0-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![Python](https://img.shields.io/badge/Python-3.10%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)

## 📌 Overview
The **MD Industries Story Engine** is an advanced, fully offline orchestration framework designed to generate highly cohesive, multi-page illustrated children's books and storyboards. By seamlessly bridging Local Large Language Models (via Ollama) and Latent Diffusion Models (SDXL Turbo), the engine automates the entire creative pipeline—from narrative generation to prompt extraction and sequential image synthesis.

Developed to run on consumer-grade edge hardware (e.g., 6GB VRAM GPUs), the engine's defining feature is its **Active Resource Governance** architecture, which actively prevents VRAM saturation and thermal throttling through Just-In-Time (JIT) model unloading and dynamic CPU offloading.

### 👥 Developers
* **M. Dhanesvaran**
* **Sri Ram. G**
* *SRM Institute of Science and Technology - Trichy*

---

## 🚀 Key Technical Features

* **Thread Synchronization & Sequential Execution:** Utilizes Python `threading` and `.join()` gates to guarantee strict sequential handoffs between text and image generation phases, preventing cross-model resource collisions.
* **Active Resource Governance (ARG):** Actively manages physical hardware states. Automatically purges the LLM from VRAM (`ollama stop`) immediately after Phase 1, before loading SDXL into memory.
* **Dynamic VRAM Offloading:** Implements `enable_model_cpu_offload()` to juggle massive diffusion models between system RAM and GPU VRAM, allowing 6GB NVIDIA cards to run SDXL Turbo without triggering `CUDA Out of Memory` crashes.
* **Context-Aware Prompt Extraction:** Automatically parses LLM text outputs to isolate specific illustration instructions, enforcing strict character and stylistic continuity across multiple pages.
* **Asynchronous Hardware Telemetry:** A persistent, non-blocking UI dashboard that tracks CPU load, RAM usage, GPU utilization, and thermals in real-time alongside a cinematic generation animation.
* **Hierarchical Data Serialization:** Automatically constructs time-stamped, organized directory trees, separating the raw text assets from the final rendered images in dedicated `illustrations/` subfolders.
* **SDXL Anti-Pattern Parameters:** Uses optimized inference steps and guidance scaling to enforce cohesive, subject-focused image generation and eliminate pattern hallucinations.

---

## ⚙️ System Requirements & Installation

### Prerequisites
* **OS:** Windows 10/11 or Linux
* **GPU:** NVIDIA GPU (Minimum 6GB VRAM recommended)
* **LLM Engine:** [Ollama](https://ollama.com/) (Installed with at least one model, e.g., `codellama` or `mistral`)
* **Diffusion Model:** `sd_xl_turbo_1.0_fp16.safetensors` (Downloaded and placed in the root directory)

### Setup Instructions

**1. Clone the Repository:**
```bash
git clone [https://github.com/YourUsername/MD_Story_Engine.git](https://github.com/YourUsername/MD_Story_Engine.git)
cd MD_Story_Engine
```

**2. Create and Activate a Virtual Environment:**
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux:
source venv/bin/activate
```

**3. Install Core AI Dependencies:**
*Install PyTorch for CUDA (adjust the index-url based on your specific CUDA version):*
```bash
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu118](https://download.pytorch.org/whl/cu118)
```
*Install Orchestration Libraries:*
```bash
pip install diffusers transformers accelerate psutil
```

---

## 💻 Usage

To provide a seamless user experience, the system includes a `START_ENGINE.bat` launcher that automatically activates the environment and boots the Python core.

1. Double-click `START_ENGINE.bat` (or run `python md_story_v16_final.py` from your active terminal).
2. Select your installed Ollama text core from the detected models list.
3. Configure the story parameters (Page Count, Theme, Tone, Art Style, Character Name, Visual Description).
4. **Phase 1:** The engine will generate the narrative text and safely unload the LLM.
5. **Phase 2:** SDXL Turbo will initialize, offload to CPU/VRAM, and sequentially generate the pages into the `/illustrations` subfolder.
6. Press `[ENTER]` to reboot the loop for a new story.

---

## 🏗️ System Architecture Pipeline

1. **Input Acquisition:** User configures narrative constraints.
2. **Phase 1 (LLM Worker):** Subprocess boots Ollama -> Injects Context -> Serializes Text -> Terminates Process (`ollama stop`).
3. **Data Extraction:** Parses `.txt` for `**Illustration Prompt:**` anchors.
4. **Phase 2 (SDXL Worker):** Boots SDXL Turbo -> Triggers `enable_model_cpu_offload()` -> Loops Inference -> Serializes PNGs -> Flushes VRAM (`torch.cuda.empty_cache()`).
5. **Completion:** Thread joins Main loop -> Telemetry waits for manual restart.

---

## 🔮 Future Roadmap
* *Dynamic prompt enhancement using secondary LLM passes.*
* *GUI/Web-UI integration for non-terminal users.*
* *[Add your future improvement ideas here!]*

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
*Created for the B.Tech 6th Semester Main Project Curriculum at SRM Institute of Science and Technology.(2023-27)*
