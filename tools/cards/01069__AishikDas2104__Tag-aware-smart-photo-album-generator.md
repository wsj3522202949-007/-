---
id: tool-01069
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Tag-aware-smart-photo-album-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/aishikdas2104/tag-aware-smart-photo-album-generator
created: 2026-07-18
updated: 2026-07-18
no: 1069
category: 二、网文 / 长篇 AI 写作系统 库
repo: AishikDas2104/Tag-aware-smart-photo-album-generator
stars: 2
url: https://github.com/aishikdas2104/tag-aware-smart-photo-album-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AishikDas2104/Tag-aware-smart-photo-album-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/aishikdas2104/tag-aware-smart-photo-album-generator
- **Stars**：2
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-powered photo story generator using CLIP models and intelligent sequencing algorithms
- **本地描述**：AI-powered photo story generator using CLIP models and intelligent sequencing algorithms
- **拉取时间**：2026-07-23 23:10:10

---

# Tag-Aware Smart Photo Album Generator

> Transform your photo collection into a cinematic story using AI-powered semantic analysis and intelligent sequencing algorithms

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

An end-to-end AI system that automatically organizes large photo collections (1,000-50,000+ images) into coherent photo stories. Using OpenAI's CLIP for semantic understanding and custom "Battle of Heuristics" algorithms for optimal image pairing and sequencing, this tool creates narrative-driven photo albums that maximize visual flow and storytelling impact.

## Key Features

### AI-Powered Analysis
- **CLIP Vision Models**: Supports both ViT-B-32 (fast, 512-dim) and ViT-L-14 (high-quality, 768-dim)
- **Zero-Shot Tagging**: Automatic semantic tag extraction from 200+ predefined categories
- **Metadata Extraction**: EXIF, GPS coordinates, timestamps, and perceptual hashing

### Intelligent Pairing
- **Battle of Heuristics Algorithm**: Pairs portrait images to maximize semantic richness
- **Three Pairing Strategies**: Tag-based, embedding-based, or hybrid approach
- **Smart Slide Construction**: Single landscape slides + paired portrait slides

### Advanced Indexing
- **Inverted Tag Index**: Fast retrieval of semantically related images
- **FAISS Vector Search**: Sub-linear approximate nearest neighbor search
- **Auto-Dimension Detection**: Works seamlessly with different CLIP models

### Story Sequencing
- **Two-Stage Optimization**:
  1. Greedy construction with candidate selection
  2. Local refinement via window-based swaps
- **Multi-Factor Scoring**: Combines tag continuity, visual similarity, and temporal proximity
- **Configurable Weights**: Fine-tune the balance between semantic and visual coherence

### Multi-Format Output
- **JSON Export**: Complete slide sequence with metadata
- **CSV Export**: Spreadsheet-friendly format
- **Video Generation**: Automated slideshow with crossfade transitions (requires FFmpeg)

### Interactive Web UI
- **Gradio Interface**: User-friendly drag-and-drop workflow
- **Model Selection**: Switch between ViT-B-32 and ViT-L-14
- **Real-Time Progress**: Live status updates during processing
- **Download Results**: One-click download of all outputs

## Quick Start

### Prerequisites
- Python 3.10 or higher
- 4GB+ RAM recommended
- (Optional) GPU with CUDA for faster processing
- (Optional) FFmpeg for video generation

### Installation

```bash
# Clone the repository
git clone https://github.com/AishikDas2104/tag-aware-smart-photo-album-generator.git
cd tag-aware-smart-photo-album-generator

# Install dependencies
pip install -r requirements.txt
```

### Running the Web App

```bash
# Start the web interface
.\start_app.bat

# Or manually:
python src/web_ui/app.py
```

Then open http://127.0.0.1:7860 in your browser.

## Usage Guide

### Step-by-Step

1. **Launch the app** using `start_app.bat`
2. **Enter input path**: Point to your image folder
3. **Select AI model**:
   - **ViT-B-32**: Faster processing, 600MB model
   - **ViT-L-14**: Higher quality, 1.7GB model
4. **Configure settings** (optional):
   - Pairing strategy: hybrid (recommended), tag, or embedding
   - Adjust weights for tags, visual similarity, and time
5. **Click "Generate Story"**
6. **Download outputs**: JSON, CSV, and video files

### Output Files

- `story.json`: Complete slide sequence with all metadata
- `story.csv`: Human-readable spreadsheet format
- `story.mp4`: Automated slideshow (if FFmpeg installed)

## Architecture

```
┌─────────────────┐
│ Input Processor │──► Loads images, extracts EXIF metadata
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ CLIP Extractor  │──► Generates embeddings + semantic tags
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Slide Builder   │──► Pairs images using Battle of Heuristics
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Indexing Layer  │──► Tag index + FAISS vector index
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Sequencer       │──► 2-stage optimization (Greedy + Refinement)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Output Gen      │──► JSON, CSV, Video
└─────────────────┘
```

## Configuration

Edit `src/config.py` to customize:

```python
# Model Selection
CLIP_MODEL_NAME = "ViT-L-14"  # or "ViT-B-32"

# Pairing Strategy
PAIRING_STRATEGY = "hybrid"  # "tag", "embedding", or "hybrid"

# Sequencing Weights
W_TAGS = 1.0        # Tag similarity weight
W_EMBEDDING = 2.0   # Visual similarity weight
W_TEMPORAL = 0.5    # Temporal proximity weight

# Video Settings
VIDEO_ENABLED = True
SLIDE_DURATION = 3.0  # seconds per slide
```

## Troubleshooting

### Video Not Generated
**Issue**: Video generation fails silently  
**Solution**: Install FFmpeg
- Download: https://www.gyan.dev/ffmpeg/builds/
- Add to system PATH
- Or disable: `VIDEO_ENABLED = False` in config.py

### First Run is Slow
**Issue**: Model downloads on first use  
**Solution**: This is normal. ViT-B-32 (600MB) or ViT-L-14 (1.7GB) downloads once and caches locally.

### Out of Memory
**Issue**: Large image collections cause OOM  
**Solution**: 
- Use ViT-B-32 (lighter model)
- Reduce `BATCH_SIZE` in config.py
- Process fewer images at once

## Performance

| Dataset Size | Model     | Processing Time | Memory Usage |
|-------------|-----------|-----------------|--------------|
| 100 images  | ViT-B-32  | ~2 minutes      | 2-3 GB       |
| 100 images  | ViT-L-14  | ~3 minutes      | 3-4 GB       |
| 1000 images | ViT-B-32  | ~15 minutes     | 4-5 GB       |
| 1000 images | ViT-L-14  | ~25 minutes     | 6-8 GB       |

*Times measured on CPU (Intel i7). GPU acceleration significantly faster.*

## Tech Stack

- **AI Models**: OpenCLIP (ViT-B-32, ViT-L-14)
- **Vector Search**: FAISS
- **Image Processing**: Pillow, OpenCV
- **Video Generation**: MoviePy, FFmpeg
- **Web UI**: Gradio
- **Core**: Python 3.10+, NumPy, PyTorch

## Use Cases

- **Photographers**: Organize event photos into coherent albums
- **Travelers**: Create narrative-driven travel photo stories
- **Families**: Build chronological family albums
- **Designers**: Sort large image libraries by visual similarity
- **Researchers**: Analyze and cluster image datasets

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/AishikDas2104/Tag-aware-smart-photo-album-generator/blob/main/LICENSE) file for details.

## Acknowledgments

- OpenAI CLIP team for the vision models
- LAION for the pretrained weights
- Battle of Heuristics algorithm inspiration

## Contact

Created by [Aishik Das](https://github.com/AishikDas2104)

---

Star this repo if you find it useful!

> Transform your photo collection into a cinematic story using AI-powered semantic analysis and intelligent sequencing algorithms

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Overview

An end-to-end AI system that automatically organizes large photo collections (1,000-50,000+ images) into coherent photo stories. Using OpenAI's CLIP for semantic understanding and custom "Battle of Heuristics" algorithms for optimal image pairing and sequencing, this tool creates narrative-driven photo albums that maximize visual flow and storytelling impact.

## ✨ Key Features

### 🤖 AI-Powered Analysis
- **CLIP Vision Models**: Supports both ViT-B-32 (fast, 512-dim) and ViT-L-14 (high-quality, 768-dim)
- **Zero-Shot Tagging**: Automatic semantic tag extraction from 200+ predefined categories
- **Metadata Extraction**: EXIF, GPS coordinates, timestamps, and perceptual hashing

### 🎨 Intelligent Pairing
- **Battle of Heuristics Algorithm**: Pairs portrait images to maximize semantic richness
- **Three Pairing Strategies**: Tag-based, embedding-based, or hybrid approach
- **Smart Slide Construction**: Single landscape slides + paired portrait slides

### 🔍 Advanced Indexing
- **Inverted Tag Index**: Fast retrieval of semantically related images
- **FAISS Vector Search**: Sub-linear approximate nearest neighbor search
- **Auto-Dimension Detection**: Works seamlessly with different CLIP models

### 📖 Story Sequencing
- **Two-Stage Optimization**:
  1. Greedy construction with candidate selection
  2. Local refinement via window-based swaps
- **Multi-Factor Scoring**: Combines tag continuity, visual similarity, and temporal proximity
- **Configurable Weights**: Fine-tune the balance between semantic and visual coherence

### 📤 Multi-Format Output
- **JSON Export**: Complete slide sequence with metadata
- **CSV Export**: Spreadsheet-friendly format
- **Video Generation**: Automated slideshow with crossfade transitions (requires FFmpeg)

### 🖥️ Interactive Web UI
- **Gradio Interface**: User-friendly drag-and-drop workflow
- **Model Selection**: Switch between ViT-B-32 and ViT-L-14
- **Real-Time Progress**: Live status updates during processing
- **Download Results**: One-click download of all outputs

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- 4GB+ RAM recommended
- (Optional) GPU with CUDA for faster processing
- (Optional) FFmpeg for video generation

### Installation

```bash
# Clone the repository
git clone https://github.com/AishikDas2104/tag-aware-smart-photo-album-generator.git
cd tag-aware-smart-photo-album-generator

# Install dependencies
pip install -r requirements.txt
```

### Running the Web App

```bash
# Start the web interface
.\start_app.bat

# Or manually:
python src/web_ui/app.py
```

Then open http://127.0.0.1:7860 in your browser.

## 📋 Usage Guide

### Step-by-Step

1. **Launch the app** using `start_app.bat`
2. **Enter input path**: Point to your image folder
3. **Select AI model**:
   - **ViT-B-32**: Faster processing, 600MB model
   - **ViT-L-14**: Higher quality, 1.7GB model
4. **Configure settings** (optional):
   - Pairing strategy: hybrid (recommended), tag, or embedding
   - Adjust weights for tags, visual similarity, and time
5. **Click "Generate Story"**
6. **Download outputs**: JSON, CSV, and video files

### Output Files

- `story.json`: Complete slide sequence with all metadata
- `story.csv`: Human-readable spreadsheet format
- `story.mp4`: Automated slideshow (if FFmpeg installed)

## 🏗️ Architecture

```
┌─────────────────┐
│ Input Processor │──► Loads images, extracts EXIF metadata
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ CLIP Extractor  │──► Generates embeddings + semantic tags
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Slide Builder   │──► Pairs images using Battle of Heuristics
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Indexing Layer  │──► Tag index + FAISS vector index
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Sequencer       │──► 2-stage optimization (Greedy + Refinement)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Output Gen      │──► JSON, CSV, Video
└─────────────────┘
```

## ⚙️ Configuration

Edit `src/config.py` to customize:

```python
# Model Selection
CLIP_MODEL_NAME = "ViT-L-14"  # or "ViT-B-32"

# Pairing Strategy
PAIRING_STRATEGY = "hybrid"  # "tag", "embedding", or "hybrid"

# Sequencing Weights
W_TAGS = 1.0        # Tag similarity weight
W_EMBEDDING = 2.0   # Visual similarity weight
W_TEMPORAL = 0.5    # Temporal proximity weight

# Video Settings
VIDEO_ENABLED = True
SLIDE_DURATION = 3.0  # seconds per slide
```

## 🐛 Troubleshooting

### Video Not Generated
**Issue**: Video generation fails silently  
**Solution**: Install FFmpeg
- Download: https://www.gyan.dev/ffmpeg/builds/
- Add to system PATH
- Or disable: `VIDEO_ENABLED = False` in config.py

### First Run is Slow
**Issue**: Model downloads on first use  
**Solution**: This is normal. ViT-B-32 (600MB) or ViT-L-14 (1.7GB) downloads once and caches locally.

### Out of Memory
**Issue**: Large image collections cause OOM  
**Solution**: 
- Use ViT-B-32 (lighter model)
- Reduce `BATCH_SIZE` in config.py
- Process fewer images at once

## 📊 Performance

| Dataset Size | Model     | Processing Time | Memory Usage |
|-------------|-----------|-----------------|--------------|
| 100 images  | ViT-B-32  | ~2 minutes      | 2-3 GB       |
| 100 images  | ViT-L-14  | ~3 minutes      | 3-4 GB       |
| 1000 images | ViT-B-32  | ~15 minutes     | 4-5 GB       |
| 1000 images | ViT-L-14  | ~25 minutes     | 6-8 GB       |

*Times measured on CPU (Intel i7). GPU acceleration significantly faster.*

## 🛠️ Tech Stack

- **AI Models**: OpenCLIP (ViT-B-32, ViT-L-14)
- **Vector Search**: FAISS
- **Image Processing**: Pillow, OpenCV
- **Video Generation**: MoviePy, FFmpeg
- **Web UI**: Gradio
- **Core**: Python 3.10+, NumPy, PyTorch

## 🎯 Use Cases

- 📷 **Photographers**: Organize event photos into coherent albums
- 🏖️ **Travelers**: Create narrative-driven travel photo stories
- 👨‍👩‍👧 **Families**: Build chronological family albums
- 🎨 **Designers**: Sort large image libraries by visual similarity
- 📊 **Researchers**: Analyze and cluster image datasets

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/AishikDas2104/Tag-aware-smart-photo-album-generator/blob/main/LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI CLIP team for the vision models
- LAION for the pretrained weights
- Battle of Heuristics algorithm inspiration

## 📧 Contact

Created by [Aishik Das](https://github.com/AishikDas2104)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

⭐ Star this repo if you find it useful!
