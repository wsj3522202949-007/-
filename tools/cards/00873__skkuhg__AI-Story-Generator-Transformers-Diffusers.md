---
id: tool-00873
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Story-Generator-Transformers-Diffusers
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/skkuhg/ai-story-generator-transformers-diffusers
created: 2026-07-18
updated: 2026-07-18
no: 873
category: 二、网文 / 长篇 AI 写作系统 库
repo: skkuhg/AI-Story-Generator-Transformers-Diffusers
stars: 1
url: https://github.com/skkuhg/ai-story-generator-transformers-diffusers
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# skkuhg/AI-Story-Generator-Transformers-Diffusers

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/skkuhg/ai-story-generator-transformers-diffusers
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI Story Generator using Hugging Face Transformers and Diffusers for text and image generation
- **本地描述**：AI Story Generator using Hugging Face Transformers and Diffusers for text and image generation
- **拉取时间**：2026-07-23 23:04:27

---

# 📚 AI Story Generator with Transformers and Diffusers

An interactive AI-powered story generator that creates compelling narratives with corresponding AI-generated images using Hugging Face's transformers and diffusers libraries.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Transformers](https://img.shields.io/badge/🤗%20Transformers-Latest-orange)
![Diffusers](https://img.shields.io/badge/🤗%20Diffusers-Latest-red)

## ✨ Features

- **AI Text Generation**: Uses GPT-2 for creative story writing
- **AI Image Generation**: Uses Stable Diffusion for scene visualization
- **Interactive Interface**: Jupyter widget-based GUI for easy use
- **Multi-Chapter Stories**: Generate complete stories with multiple chapters
- **Customizable Settings**: Adjust creativity, length, art styles
- **Scene Detection**: Automatically extracts visual scenes from text
- **Multiple Art Styles**: Fantasy, realistic, anime, watercolor, and more

## 🚀 Quick Start

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/skkuhg/AI-Story-Generator-Transformers-Diffusers.git
cd ai-story-generator-transformers-diffusers
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Usage Options

#### 1. Interactive Jupyter App (Recommended)
```bash
python main.py --interactive
```

#### 2. Command Line Interface
```bash
# Generate a single chapter
python main.py --generate "Once upon a time in a magical kingdom"

# Generate a complete 3-chapter story
python main.py --complete "In a mystical forest" --chapters 3

# Text-only generation (faster)
python main.py --generate "Space adventure" --no-images
```

#### 3. Jupyter Notebook
```bash
jupyter notebook story_generator_notebook.ipynb
```

### Example Usage

```python
from src import StoryGeneratorApp

# Create and launch the app
app = StoryGeneratorApp()
app.display_app()

# Or generate programmatically
story_data = app.generate_complete_story(
    "In a cyberpunk city where AI and humans coexist",
    num_chapters=3,
    chapter_length=150,
    art_style="digital art, cyberpunk, neon"
)
```

## 🎮 Interactive Controls

- **Story Prompt**: Enter your story beginning
- **Chapter Length**: Control text length (50-300 tokens)
- **Creativity**: Adjust randomness (0.1-1.5)
- **Art Style**: Choose from 6 visual styles
- **Generate Chapter**: Create single chapter with images
- **Continue Story**: Add more chapters
- **New Story**: Reset and start fresh

## 🎨 Available Art Styles

- **Fantasy Art**: Magical, mystical scenes
- **Realistic**: Photographic quality images
- **Anime Style**: Colorful, animated look
- **Watercolor**: Artistic, painted effect
- **Digital Art**: Modern, vibrant style
- **Oil Painting**: Classical, detailed artwork

## 📊 System Requirements

### Minimum Requirements
- **Python**: 3.8+
- **Memory**: 8GB RAM
- **Storage**: 5GB free space (for models)
- **OS**: Windows, macOS, or Linux

### Recommended for Best Performance
- **GPU**: CUDA-compatible GPU with 6GB+ VRAM
- **Memory**: 16GB RAM
- **CPU**: Multi-core processor

## 🔧 Configuration

### Command Line Options

```bash
python main.py [OPTIONS]

Options:
  -i, --interactive          Launch interactive widget app
  -g, --generate TEXT        Generate single chapter from prompt
  -c, --complete TEXT        Generate complete story from prompt
  -n, --chapters INT         Number of chapters (default: 3)
  -l, --length INT           Chapter length in tokens (default: 150)
  -t, --creativity FLOAT     Creativity/temperature (0.1-1.5, default: 0.8)
  -s, --style TEXT           Art style for images
  --no-images               Skip image generation (text only)
  --samples                 Show sample story prompts
  --tips                    Show usage tips
```

### Environment Variables

```bash
export HF_HUB_DOWNLOAD_TIMEOUT=300    # Download timeout
export TOKENIZERS_PARALLELISM=false   # Avoid warnings
```

## 📁 Project Structure

```
ai-story-generator-transformers-diffusers/
├── src/
│   ├── __init__.py              # Package initialization
│   ├── story_generator.py       # Text generation module
│   ├── image_generator.py       # Image generation module
│   ├── story_app.py            # Interactive app interface
│   └── utils.py                # Utility functions
├── examples/                   # Example scripts
├── tests/                     # Unit tests
├── docs/                      # Documentation
├── assets/                    # Static assets
├── main.py                    # CLI entry point
├── story_generator_notebook.ipynb  # Demonstration notebook
├── requirements.txt           # Dependencies
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

## 🎭 Example Story Prompts

1. "In a mystical forest where ancient trees whispered secrets"
2. "On a distant planet where two moons cast silver light"
3. "In a steampunk city where gears and magic coexisted"
4. "Deep in the ocean where mermaids guarded ancient treasures"
5. "In a floating castle above the clouds where wizards studied"
6. "In a cyberpunk city where AI and humans coexist"
7. "On a space station orbiting a dying star"
8. "In a magical school hidden in the mountains"
9. "During the last day on Earth before evacuation"
10. "In a world where books come to life"

## 🚨 Troubleshooting

### Common Issues

**1. Out of Memory Errors**
- Reduce chapter length or switch to CPU mode
- Use `--no-images` flag for text-only generation
- Close other applications to free RAM

**2. Slow Performance**
- First run downloads ~4GB of models
- GPU acceleration significantly speeds up generation
- Use shorter chapters for faster results

**3. Model Download Fails**
- Check internet connection
- Try running again (downloads resume automatically)
- Use VPN if in restricted region

**4. Poor Quality Output**
- Adjust creativity settings (0.7-0.9 works well)
- Try different art styles
- Make prompts more descriptive

### Performance Tips

- **GPU Users**: Automatic GPU acceleration when available
- **CPU Users**: Use shorter chapters and fewer inference steps
- **Memory**: Close unused applications during generation
- **Storage**: Ensure 5GB free space for model downloads

## 🔬 Technical Details

### Models Used
- **Text Generation**: GPT-2 Medium (~350M parameters)
- **Image Generation**: Stable Diffusion v1.5 (~860M parameters)
- **Total Download Size**: ~4-5GB on first run

### Architecture
- **Framework**: PyTorch, Transformers, Diffusers
- **Interface**: Jupyter Widgets, IPython
- **Image Processing**: PIL, Matplotlib
- **Networking**: Requests with retry logic

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/skkuhg/AI-Story-Generator-Transformers-Diffusers/blob/main/LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚖️ Legal and Ethical Considerations

- Generated content is for personal/educational use
- Be mindful of content guidelines when sharing
- Models may reflect biases from training data
- Always review generated content before public sharing
- Respect copyright and intellectual property rights

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for transformers and diffusers libraries
- [OpenAI](https://openai.com/) for GPT-2 model
- [Stability AI](https://stability.ai/) for Stable Diffusion
- The open-source AI community for their contributions

## 📞 Support

If you encounter any issues or have questions:

1. Check the [troubleshooting section](#-troubleshooting)
2. Look through existing [GitHub issues](https://github.com/yourusername/ai-story-generator-transformers-diffusers/issues)
3. Create a new issue with detailed information about your problem
4. Include system information, error messages, and steps to reproduce

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**🎉 Happy story generating! 📚✨**
