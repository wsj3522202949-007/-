---
id: tool-01464
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: storyboard-app
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/acharyaparth/storyboard-app
created: 2026-07-18
updated: 2026-07-18
no: 1464
category: 二、网文 / 长篇 AI 写作系统 库
repo: acharyaparth/storyboard-app
stars: 1
url: https://github.com/acharyaparth/storyboard-app
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 989e7c03346a5e6d
  - methods/最强写作方法论_全球最强综合版.md
---

# acharyaparth/storyboard-app

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/acharyaparth/storyboard-app
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered storyboard generator for macOS - Transform scripts into professional storyboards using FLUX.1-dev model
- **本地描述**：AI-powered storyboard generator for macOS - Transform scripts into professional storyboards using FLUX.1-dev model
- **拉取时间**：2026-07-23 23:21:46

---

# Offline Storyboard Generator for macOS

An offline macOS application that generates storyboard illustrations from scripts using AI. Built with Electron and Python, featuring the FLUX.1-dev model with a specialized LoRA adapter for storyboard generation.

## Features

- **Offline Operation**: All processing happens locally on your Mac
- **One-Click Setup**: Automatic model download and installation
- **Simple Script Parsing**: Paste your script and generate storyboards
- **Export Options**: Save storyboards as PNG or PDF
- **Privacy-First**: No data sent to external servers

## System Requirements

- **macOS**: 12.0+ (Monterey or later)
- **Processor**: Apple Silicon (M1/M2/M3) recommended for best performance
- **RAM**: 32GB minimum (FLUX.1-dev requires significant memory)
- **Storage**: 50GB free disk space for models
- **Internet**: Required only for initial model download

## Quick Start

### Option 1: Download Pre-built App (Recommended)

1. Download the latest `.dmg` file from [GitHub Releases](https://github.com/yourusername/storyboard-app/releases)
2. Double-click the `.dmg` file to mount it
3. Drag the Storyboard App to your Applications folder
4. Launch the app from Applications or Spotlight

### Option 2: Build from Source

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/storyboard-app.git
   cd storyboard-app
   ```

2. Run the build script:
   ```bash
   ./build.sh
   ```

3. Install the generated `.dmg` file from the `dist/` directory

## First-Time Setup

1. When you first launch the app, you'll see a setup screen
2. Click "Download Models" to install the required AI models (~25GB)
3. Wait for the download to complete (this may take 30-60 minutes depending on your internet speed)
4. The app will automatically restart once installation is complete

## Usage

### 1. Enter Your Script

Paste your script in the text area. The app works best with scripts that have clear scene breaks:

```
Scene 1: A young woman walks into a coffee shop

Scene 2: She orders a latte and sits by the window

Scene 3: An old man approaches her table
```

### 2. Parse Your Script

Click "Parse Script" to extract individual scenes. The app will:
- Identify scene breaks automatically
- Extract scene descriptions
- Validate the script structure
- Show you a preview of parsed scenes

### 3. Generate Storyboard

Click "Generate Storyboard" and wait for the AI to create illustrations. Each scene takes 30-60 seconds to generate.

### 4. Export Your Storyboard

Save your storyboard as:
- **PNG Images**: Individual files for each scene
- **PDF Document**: Single document with all scenes

## Development

### Building from Source

1. **Prerequisites:**
   - Node.js 18+ and npm
   - Python 3.8+ and pip
   - macOS 12.0+ with Xcode Command Line Tools

2. **Install Dependencies:**
   ```bash
   # Python dependencies
   cd python-backend
   pip3 install -r requirements.txt
   cd ..
   
   # Node.js dependencies
   cd electron-app
   npm install
   cd ..
   ```

3. **Build the App:**
   ```bash
   ./build.sh
   ```

4. **Development Mode:**
   ```bash
   cd electron-app
   npm run dev
   ```

## License

This project uses the FLUX.1-dev model which is licensed under the [flux-1-dev-non-commercial-license](https://huggingface.co/black-forest-labs/FLUX.1-dev). Please review the license terms before using this software commercially.

## Credits

- **AI Model**: [FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) by Black Forest Labs
- **LoRA Adapter**: [storyboard-scene-generation-model-flux-v3-FLH](https://huggingface.co/jwywoo/storyboard-scene-generation-model-flux-v3-FLH) by jwywoo
- **Built with**: Electron, React, Python, Flask, Diffusers, and PyTorch

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Made with ❤️ for storytellers and filmmakers**
