---
id: tool-00161
type: tool
area: 库
status: active
tags: [大纲规划, Python, 协议宽松, 本地优先, 英文文档, 人物设定, RAG, 本地写作]
title: plot-weaver-desktop-app
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/zhengzhengli39/plot-weaver-desktop-app
created: 2026-07-18
updated: 2026-07-18
no: 161
category: 二、网文 / 长篇 AI 写作系统 库
repo: Zhengzhengli39/plot-weaver-desktop-app
stars: 0
url: https://github.com/zhengzhengli39/plot-weaver-desktop-app
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Zhengzhengli39/plot-weaver-desktop-app

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/zhengzhengli39/plot-weaver-desktop-app
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A Python-based desktop tool for writers to generate story frameworks, characters, and plots quickly.
- **本地描述**：A Python-based desktop tool for writers to generate story frameworks, characters, and plots quickly.
- **拉取时间**：2026-07-23 22:43:43

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Plot Weaver Desktop App

https://img.shields.io/badge/Python-3.7%252B-blue
https://img.shields.io/badge/License-MIT-green
https://img.shields.io/badge/GUI-Tkinter-orange

An intelligent scriptwriting desktop application built with Python, featuring character creation, plot generation, and knowledge base management to help writers and screenwriters quickly build story frameworks.

## ✨ Features

- **Character Creation System**: Generate detailed character profiles based on zodiac signs, Chinese zodiac, occupations, and other attributes

- **Plot Generation Engine**: Support for multiple story structures (Three-Act, Five-Act, Hero's Journey)

- **Knowledge Base Integration**: Built-in knowledge elements from history, geography, humanities, and other fields

- **GUI Interface**: User-friendly interface built with Tkinter

- **Smart Recommendations**: Automatically suggest suitable plot elements based on character attributes

- **Export Functionality**: Support for multiple export formats (TXT, HTML, Markdown)

## 🚀 Installation & Setup

### Prerequisites

- Python 3.7 or higher

- pip (Python package manager)

### Installation Steps

1. Clone or download this project

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
   Or install using setup.py:
   
   ```bash
   python setup.py install
   ```
3. Run the application:

   ```bash
   python main.py
   ```

### Development Setup

For development or running tests, install development dependencies:

   ```bash
   pip install -r test_requirements.txt
   ```

## 📖 Usage Guide

### Main Interface

The application features three main tabs:

1. **Knowledge Base Selection**: Browse and select knowledge domains to include in your story

2. **Character Settings**: Create and customize story characters

3. **Plot Generation**: Generate story outlines based on characters and knowledge elements

### Creating Characters

In the "Character Settings" tab, you can set the following character attributes:

- Nationality, gender, birth year

- Zodiac sign and Chinese zodiac

- Occupation and family background

The system automatically generates character personalities and backstories based on these attributes.

### Generating Plots

In the "Plot Generation" tab, select the following elements:

- Story genre (Drama, Action, Romance, Sci-Fi, etc.)

- Setting (Modern, Historical, Futuristic, Fantasy)

- Conflict type (Person vs. Person, Person vs. Nature, Person vs. Society, Person vs. Self)

- Story structure (Three-Act, Five-Act, Hero's Journey)

Click the "Generate Outline" button to create a complete story outline based on your selections.

## 🏗 Project Structure

```text
PLOT-WEAVER-DESKTOP-APP/
│
├── main.py                 # Main application entry point
├── character_creator.py    # Character creation logic
├── database_manager.py     # Database management
├── plot_generator.py       # Plot generation engine
├── run_tests.py           # Test runner
├── setup.py               # Package installation configuration
├── test_requirements.txt  # Test dependencies
├── test_plot_generator.py # Plot generator tests
│
├── plot_generator/        # Plot generator module
│   ├── analyzers.py       # Script analysis tools
│   ├── cache.py           # Cache management
│   ├── cli.py             # Command-line interface
│   ├── config.py          # Configuration management
│   ├── exceptions.py      # Custom exceptions
│   ├── exporters.py       # Export functionality
│   ├── knowledge.py       # Knowledge management
│   ├── logger.py          # Log management
│   ├── performance.py     # Performance monitoring
│   ├── utils.py           # Utility functions
│   │
│   └── knowledge/         # Knowledge data files
│       ├── characters.json
│       ├── config.json
│       ├── conflicts.json
│       └── ...(other JSON files)
│
└── tests/                 # Test directory
    ├── test_analyzers.py
    ├── test_cache_performance.py
    ├── test_exporters.py
    └── test_knowledge.py
```

## 🧪 Running Tests

The project includes a comprehensive test suite. Run tests using:

   ```bash
   python run_tests.py
   ```

   Or using pytest:

   ```bash
   pytest -v
   ```

Test coverage reports will be generated in the `coverage_report/` directory.

## 🤝 Contributing

We welcome contributions of all kinds! Please follow these steps:

1. Fork the repository

2. Create a feature branch (git checkout -b feature/AmazingFeature)

3. Commit your changes (git commit -m 'Add some AmazingFeature')

4. Push to the branch (git push origin feature/AmazingFeature)

5. Open a Pull Request

### Code Style

Please follow PEP 8 style guidelines and run code formatting tools before submitting.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by traditional narrative structures and modern AI technology

- Built with Python and Tkinter

**Development Note**： This project was developed with the assistance of AI tools for code generation, boilerplate setup, and documentation. The overall architecture, design decisions, prompt engineering, and final implementation were guided and curated by a human developer.





