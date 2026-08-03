---
id: tool-03144
type: tool
area: 库
status: active
tags: [多Agent, TTS, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: Agentic-Image-Audio-Generation
summary: 多 Agent 协作自动产文
source: https://github.com/m01ali/agentic-image-audio-generation
created: 2026-07-18
updated: 2026-07-18
no: 3144
category: 六、多 Agent 小说生产 / 叙事引擎 库
repo: m01ali/Agentic-Image-Audio-Generation
stars: 0
url: https://github.com/m01ali/agentic-image-audio-generation
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
---

# m01ali/Agentic-Image-Audio-Generation

- **分类**：六、多 Agent 小说生产 / 叙事引擎 库
- **链接**：https://github.com/m01ali/agentic-image-audio-generation
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：autogen, elevenlabs, multi-agent-systems, python, stable-diffusion
- **GitHub 描述**：A multi-agent framework utilizing AutoGen, reading children's stories and calling agents for text-to-speech (ElevenLabs) and text-to-image (Stable Diffusion) for generating synchronized audio-visual content.
- **本地描述**：A multi-agent framework utilizing AutoGen, reading children's stories and calling agents for text-to-speech (ElevenLabs) and text-to-image (Stable Diffusion) for generating synchronized audio-visual content.
- **拉取时间**：2026-07-23 23:50:51

---

# Agents Image and Audio Generation

This project consists of three main components: `audio_agent.py`, `image_agent.py`, and `orchestrator.py`. Each component has its own specific functionality and dependencies.

## Requirements

The project dependencies are listed in the `requirements.txt` file. To install them, run:

```bash
pip install -r requirements.txt
````
# Project Components

## Audio Agent
**File**: `audio_agent.py`

### Imports:
- **pydub**: For audio processing
- **requests**: For making HTTP requests
- **json**: For JSON manipulation
- **os**: For operating system interactions
- **base64**: For encoding and decoding
- **requests.adapters.HTTPAdapter** and **urllib3.util.retry.Retry**: For HTTP request retries

### Description:
The `audio_agent.py` script uses **Eleven Labs** for audio generation. It processes audio files, makes HTTP requests to the Eleven Labs API, and handles retries for robust communication.

---

## Image Agent
**File**: `image_agent.py`

### Imports:
- **autogen**: For automation
- **diffusers.StableDiffusionPipeline**: For image generation
- **torch**: For deep learning operations
- **os**: For operating system interactions
- **json**: For JSON manipulation
- **subprocess**: For running subprocesses

### Description:
The `image_agent.py` script uses the **"CompVis/stable-diffusion-v1-4"** model for image generation. It leverages the **Stable Diffusion Pipeline** to create images based on given prompts.

---

## Orchestrator
**File**: `orchestrator.py`

### Imports:
- **json**: For JSON manipulation
- **os**: For operating system interactions
- **groq**: For Groq operations
- **subprocess**: For running subprocesses
- **autogen**: For automation

### Description:
The `orchestrator.py` script uses the **"llama-3.2-90b-vision-preview"** model to analyze children's stories. It follows a specific prompt to extract:
- Major characters
- Scenes
- Character dialogues
- Background scenery

related:
  - methods/网文写作最强SOP.md
---
# Usage
1. **Install Dependencies**  
   Ensure all required dependencies are installed by running:  
   ```bash
   pip install -r requirements.txt
   ```
## License
This project is licensed under the MIT License. 
