---
id: tool-07367
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: comicgeneration
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/kummethayaswanth/comicgeneration
created: 2026-07-18
updated: 2026-07-18
no: 7367
category: 画龙补充 / 扩容入库 — 补充源
repo: kummethayaswanth/comicgeneration
stars: 3
url: https://github.com/kummethayaswanth/comicgeneration
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# kummethayaswanth/comicgeneration

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/kummethayaswanth/comicgeneration
- **Stars**：3
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：comicgeneration
- **拉取时间**：2026-07-25 19:19:44

---

# ComfyUI Comic Generation System

An automated system for generating 6-panel comics using ComfyUI workflows with character consistency maintained through the Flux-Kontext AI model.

## 🎨 What This Does

Transform any character image into a 6-panel comic story while maintaining character consistency across all panels. Perfect for creating:
- Character story arcs
- Educational comics  
- Narrative sequences
- Animation references

## 🚀 Quick Start

1. **Install Requirements**: Ensure you have ComfyUI with Flux-Kontext model
2. **Prepare Character**: Place your character image in ComfyUI's input folder
3. **Create Story**: Write your 6-panel story prompts in JSON format
4. **Generate Workflow**: Use the Python script to create ComfyUI workflow
5. **Run in ComfyUI**: Execute the workflow to generate your comic

### Example Usage
```bash
python comic_generator.py hogwarts_sorting.json default_character.png my_comic
```

## 📁 Repository Structure

```
├── workflows/                          # ComfyUI workflow templates
│   ├── 6panel_comic_example.json      # Main 6-panel comic template
│   └── tpose_gen_api.json              # T-pose generation template
├── 6panel prompt files/               # Story prompt JSON files
│   └── hogwarts_sorting.json          # Example: Hogwarts sorting ceremony
├── generated workflows/               # Generated ComfyUI workflows
│   └── hogwarts_comic_fixed.json     # Example generated workflow
├── comic_generator.py                 # Main Python script
├── generate_comic.bat                 # Windows batch file for easy use
├── Comic_Generation_README.md         # Detailed usage instructions
├── T-Pose_Generation_Workflow_Documentation.md  # T-pose workflow guide
└── README.md                          # This file
```

## 🎯 Features

- **Character Consistency**: Maintains character appearance across all panels
- **Flexible Storytelling**: Easy-to-edit JSON prompt system
- **Professional Quality**: Serious comic book art style (not anime/cartoon)
- **Automated Layout**: Generates 3x2 panel grid automatically
- **Batch Processing**: Generate multiple comics from different prompt files
- **ComfyUI Integration**: Seamless workflow generation for ComfyUI

## 📖 Documentation

- **`[Comic Generation Guide](Comic_Generation_README.md)`**: Comprehensive usage instructions
- **`[T-Pose Workflow Guide](T-Pose_Generation_Workflow_Documentation.md)`**: Understanding the T-pose generation system

## 🛠️ Technical Requirements

### Required Models
- `flux1-kontext-dev.safetensors` - Main AI model for character consistency
- `clip_l.safetensors` - Text encoder
- `t5xxl_fp16.safetensors` - Additional text encoder  
- `ae.safetensors` - VAE decoder

### Hardware Recommendations
- **GPU**: 8GB+ VRAM
- **RAM**: 16GB+ system memory
- **Storage**: ~20GB for model files

## 🎭 Example: Hogwarts Sorting Comic

The included example creates a story where a character goes through the Hogwarts sorting ceremony:

1. Standing nervously in the Great Hall
2. Walking to the front when called
3. Sitting with the Sorting Hat
4. Hat deliberating the choice
5. Joy as "GRYFFINDOR!" is announced
6. Walking proudly to the house table

## 🔧 How It Works

1. **Input Processing**: Takes your character image and creates a T-pose reference
2. **Prompt Processing**: Reads your story JSON and extracts panel descriptions
3. **Workflow Generation**: Creates a complete ComfyUI workflow with all settings
4. **Character Consistency**: Uses Flux-Kontext's reference system to maintain appearance
5. **Panel Assembly**: Automatically stitches individual panels into final comic grid

## 🤝 Contributing

Feel free to:
- Add new story prompt examples
- Improve the Python script
- Create alternative panel layouts
- Share your generated comics

## 📜 License

This project is open source. Please credit when using or modifying.

## 🏗️ Built With

- **ComfyUI**: Node-based AI image generation interface
- **Flux-Kontext**: Character-consistent AI model by Black Forest Labs
- **Python**: Automation and workflow generation
- **JSON**: Configuration and prompt management

related:
  - methods/QUICK_START.md
---

*Create consistent, professional comic stories with the power of AI!* 
