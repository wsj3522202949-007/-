---
id: tool-00270
type: tool
area: 库
status: active
tags: [TTS, Python, 协议宽松, 需API密钥, 英文文档]
title: storyteller
summary: 小说转语音/有声书
source: https://github.com/prkshverma09/storyteller
created: 2026-07-18
updated: 2026-07-18
no: 270
category: 二、网文 / 长篇 AI 写作系统 库
repo: prkshverma09/storyteller
stars: 4
url: https://github.com/prkshverma09/storyteller
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# prkshverma09/storyteller

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/prkshverma09/storyteller
- **Stars**：4
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI Audio Drama Generator - Transform text scripts into immersive audio dramas using Deepgram TTS
- **本地描述**：AI Audio Drama Generator - Transform text scripts into immersive audio dramas using Deepgram TTS
- **拉取时间**：2026-07-23 22:46:57

---

# 🎭 StoryTeller - AI Audio Drama Generator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Deepgram](https://img.shields.io/badge/Powered%20by-Deepgram-purple.svg)](https://deepgram.com)

**StoryTeller** is a Python application that transforms text scripts into immersive audio dramas using AI-powered text-to-speech technology. Create professional-quality audio content with different character voices, perfect for podcasts, audiobooks, or interactive storytelling.

## ✨ Features

- 🎙️ **Multi-Character Voice Generation**: Assign unique AI voices to different characters
- 🎵 **Automatic Audio Combination**: Programmatically combines individual audio segments
- 🔧 **Easy Configuration**: Simple character-to-voice mapping
- 📝 **Script Processing**: Automatically cleans emotional cues and stage directions
- 🎯 **Professional Output**: Generates high-quality WAV audio files
- 🛠️ **Standalone Tools**: Includes utility scripts for audio processing
- 🤖 **AI Story Conversion**: Convert any story text into drama script format using Google Gemini

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Deepgram API key ([Get one here](https://console.deepgram.com/))
- Google API key ([Get one here](https://makersuite.google.com/app/apikey)) - for story conversion feature

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/storyteller.git
   cd storyteller
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env and add your Deepgram API key
   ```

5. **Run the audio drama generator**
   ```bash
   python src/storyteller/example.py
   ```

## 📖 Usage

### Basic Usage

1. **Configure your script** in `src/storyteller/example.py`:
   ```python
   DRAMA_SCRIPT = [
       {"character": "NARRATOR", "line": "Once upon a time..."},
       {"character": "HERO", "line": "I will save the day!"},
       {"character": "VILLAIN", "line": "Not if I can help it!"},
   ]
   ```

2. **Map characters to voices**:
   ```python
   VOICE_MAP = {
       "NARRATOR": "aura-asteria-en",
       "HERO": "aura-luna-en",
       "VILLAIN": "aura-asteria-en",
   }
   ```

3. **Run the generator**:
   ```bash
   python src/storyteller/example.py
   ```

### Available Voice Models

StoryTeller supports Deepgram's Aura voice models:

- `aura-asteria-en` - Clear, professional narrator voice
- `aura-luna-en` - Warm, engaging character voice
- `aura-stella-en` - Energetic, dynamic voice
- `aura-athena-en` - Authoritative, commanding voice
- `aura-hera-en` - Sophisticated, elegant voice
- `aura-orion-en` - Deep, resonant voice
- `aura-arcas-en` - Friendly, approachable voice
- `aura-perseus-en` - Strong, heroic voice
- `aura-angus-en` - Warm, fatherly voice
- `aura-orpheus-en` - Melodic, artistic voice
- `aura-helios-en` - Bright, optimistic voice
- `aura-zeus-en` - Powerful, authoritative voice

*Note: Voice availability depends on your Deepgram plan.*

### Advanced Usage

#### Using the Standalone Audio Combiner

```bash
# Combine specific audio files
python scripts/combine_audio.py output.wav file1.wav file2.wav file3.wav

# Combine all files in a directory
python scripts/combine_audio.py final_drama.wav audio_segments/*.wav
```

#### Custom Script Processing

The `clean_text()` function automatically removes stage directions:
```python
# Input: "(Sad voice) I guess I'll just go home."
# Output: "I guess I'll just go home."
```

### AI Story Conversion

The new story conversion feature allows you to convert any story text into a drama script format using Google Gemini.

#### Using the Story Converter

```python
from storyteller.example import convert_story_to_drama_script

# Your story text
story = """
Sarah was walking through the forest when she heard a strange noise behind her.
She turned around quickly, but there was nothing there. The wind rustled the leaves
above her head. "Hello?" she called out nervously. A voice replied from somewhere
in the trees: "Don't be afraid, Sarah. I've been waiting for you."
"""

# Convert to drama script
drama_script = convert_story_to_drama_script(story)

# The result will be a list of dictionaries like:
# [
#     {"character": "NARRATOR", "line": "Sarah was walking through the forest..."},
#     {"character": "SARAH", "line": "(nervously) Hello?"},
#     {"character": "MYSTERIOUS VOICE", "line": "Don't be afraid, Sarah..."}
# ]
```

#### Testing the Story Converter

Run the test script to try the conversion feature:

```bash
python test_story_conversion.py
```

This will:
1. Test the conversion with a sample story
2. Allow you to input your own story for conversion
3. Display the generated drama script

#### Integration with Audio Generation

Once you have a converted drama script, you can use it with the audio generation:

```python
# Convert your story
drama_script = convert_story_to_drama_script(your_story)

# Replace the DRAMA_SCRIPT in example.py with your converted script
# Then run the audio generation
build_audio_drama()
```

## 🏗️ Project Structure

```
StoryTeller/
├── src/
│   ├── storyteller/           # Main package
│   │   ├── __init__.py
│   │   ├── main.py           # Application entry point
│   │   ├── config.py         # Configuration management
│   │   ├── example.py        # Audio drama generator
│   │   ├── models/           # Data models
│   │   ├── services/         # Business logic
│   │   ├── api/              # API endpoints
│   │   └── utils/            # Utility functions
│   └── tests/                # Test files
├── scripts/                  # Utility scripts
│   ├── dev_server.py        # Development server
│   └── combine_audio.py      # Audio file combiner
├── docs/                     # Documentation
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development dependencies
├── env.example              # Environment variables template
└── README.md                # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# Required
DEEPGRAM_API_KEY=your_deepgram_api_key_here

# Optional
DEBUG=True
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

### Voice Configuration

Customize character voices by modifying the `VOICE_MAP`:

```python
VOICE_MAP = {
    "NARRATOR": "aura-asteria-en",
    "CHARACTER1": "aura-luna-en",
    "CHARACTER2": "aura-orion-en",
    # Add more characters as needed
}
```

## 🧪 Development

### Setting up Development Environment

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest

# Run linting
black src/
isort src/
flake8 src/
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/storyteller

# Run specific test file
pytest src/tests/test_main.py
```

## 📚 API Reference

### Core Functions

#### `build_audio_drama()`
Main function that generates audio for all script lines and combines them.

#### `combine_audio_files(input_files, output_file)`
Combines multiple WAV files into a single audio file.

#### `clean_text(text)`
Removes stage directions and emotional cues from dialogue.

#### `convert_story_to_drama_script(story_text)`
Converts any story text into a drama script format using Google Gemini.

**Parameters:**
- `story_text` (str): The input story text to convert

**Returns:**
- `List[Dict[str, str]]`: A list of dictionaries with 'character' and 'line' keys

**Example:**
```python
story = "Once upon a time, Alice found a magical book..."
script = convert_story_to_drama_script(story)
# Returns: [{"character": "NARRATOR", "line": "Once upon a time..."}, ...]
```

### Configuration Functions

#### `load_config()`
Loads configuration from environment variables and `.env` file.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](https://github.com/prkshverma09/storyteller/blob/main/CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/prkshverma09/storyteller/blob/main/LICENSE) file for details.

## 🙏 Acknowledgments

- [Deepgram](https://deepgram.com) for providing excellent text-to-speech API
- The Python community for amazing audio processing libraries
- Contributors and users who help improve StoryTeller

## 📞 Support

- 📖 [Documentation](https://github.com/prkshverma09/storyteller/tree/main/docs/)
- 🐛 [Report Issues](https://github.com/yourusername/storyteller/issues)
- 💬 [Discussions](https://github.com/yourusername/storyteller/discussions)
- 📧 [Contact](mailto:your.email@example.com)

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/storyteller&type=Date)](https://star-history.com/#yourusername/storyteller&Date)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Made with ❤️ for storytellers everywhere**
