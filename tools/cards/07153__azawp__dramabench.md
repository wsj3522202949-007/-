---
id: tool-07153
type: tool
area: 库
status: active
tags: [协议宽松, 需API密钥, 英文文档]
title: dramabench
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/azawp/dramabench
created: 2026-07-18
updated: 2026-07-18
no: 7153
category: 画龙补充 / 扩容入库 — 补充源
repo: azawp/dramabench
stars: 0
url: https://github.com/azawp/dramabench
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/QUICK_START.md
---

# azawp/dramabench

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/azawp/dramabench
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A six-dimensional evaluation framework for drama script continuation with interactive leaderboard and case studies
- **本地描述**：dramabench
- **拉取时间**：2026-07-25 19:12:28

---

# DramaBench

<div align="center">

![DramaBench Cover](assets/DramaBench_cover.png)

**A Six-Dimensional Evaluation Framework for Drama Script Continuation**

[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()
[![License](https://img.shields.io/badge/License-MIT-blue)]()
[![Paper](https://img.shields.io/badge/Paper-arXiv-red)](https://arxiv.org/abs/2512.19012)

[🌐 Website](https://dramabench.pages.dev/) • [✨ Interactive Demo](https://dramabench.pages.dev/web/demo.html) • [📊 Leaderboard](https://dramabench.pages.dev/web/leaderboard.html) • [🤗 Dataset](https://huggingface.co/datasets/FutureMa/DramaBench)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Project Components](#project-components)
- [Web Demo](#web-demo)
- [Dataset](#dataset)
- [Evaluation Framework](#evaluation-framework)
- [Leaderboard](#leaderboard)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

---

<a id="overview"></a>
## 🎯 Overview

**DramaBench** is a comprehensive benchmark for evaluating drama script continuation capabilities of large language models. It provides:

### Core Components

- 🌐 **Project Website** - Interactive showcase with evaluation results and case studies
- ✨ **Interactive Demo** - Try script continuation with multiple LLM models (user-provided API key)
- 💾 **Large-Scale Dataset** - 1,103 drama scripts with human annotations
- 📊 **Evaluation Framework** - 6 independent dimensions with rigorous metrics
- 🏆 **Model Leaderboard** - Compare 8 SOTA language models
- 📝 **Case Studies** - 24 curated examples with detailed analysis

### Six Evaluation Dimensions

1. **Format Standards** (Rule-based) - Screenplay format compliance
2. **Narrative Efficiency** (LLM-labeled) - Story progression effectiveness
3. **Character Consistency** (LLM-labeled) - Character voice and behavior
4. **Emotional Depth** (LLM-labeled) - Emotional arc development
5. **Logic Consistency** (LLM-labeled) - Factual coherence and continuity
6. **Conflict Handling** (LLM-labeled) - Conflict development quality

### Key Statistics

- **1,103** unique drama scripts
- **8,824** total evaluations (1,103 scripts × 8 models)
- **8** state-of-the-art language models
- **6** independent evaluation dimensions
- **252** statistical significance tests (65.9% significant)
- **24** curated case studies

---

<a id="quick-start"></a>
## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Web browser (Chrome, Safari, Firefox, or Edge)

### Launch Web Demo

**Method 1: One-Click Start (Easiest)**

```bash
cd DramaBench
./start_demo.sh
```

This will automatically:
- ✅ Start a local HTTP server on port 8000
- ✅ Open the demo in your default browser
- ✅ Navigate to http://localhost:8000

**Method 2: Manual Server Start**

```bash
cd DramaBench

# Using uv (if available)
uv run python -m http.server 8000

# Or using Python 3 directly
python3 -m http.server 8000

# Then open http://localhost:8000 in your browser
```

### ⚠️ Important Note

Due to browser CORS restrictions, you **must** use a local HTTP server to view the demo. Opening HTML files directly (`file://` protocol) will cause data loading errors.

---

<a id="project-components"></a>
## 🧩 Project Components

### 1. Project Website & Interactive Demo

An interactive, Apple-inspired web interface for exploring evaluation results and trying script continuation.

**Website Features:**
- 📊 Interactive leaderboard with dimension filters
- 📝 Case studies explorer with 24 examples
- 🎨 Premium dark gradient design
- 📱 Fully responsive (mobile/tablet/desktop)
- ⚡ Pure HTML/CSS/JavaScript (no frameworks)

**Interactive Demo Features:**
- ✨ Try script continuation with 4 SOTA models (GPT-5.2, Gemini 3, GLM-4.7, MiniMax M2.1)
- 🔑 User-provided OpenRouter API key (stored locally)
- 📜 100 drama scripts from DramaBench dataset
- 🎭 Official prompt template for generation
- 📊 Compare AI-generated vs ground truth continuations
- 🎨 Matching Apple-style design

**Pages:**
- `index.html` - Main landing page
- `web/leaderboard.html` - Model rankings
- `web/cases.html` - Case studies browser
- `web/demo.html` - Interactive script continuation demo

[→ View Live Website](https://dramabench.pages.dev/) | [→ Try Interactive Demo](https://dramabench.pages.dev/web/demo.html)

### 2. Dataset

**🎉 Now Available on Hugging Face!**

The DramaBench dataset is being released progressively to ensure quality and gather community feedback.

**Current Release (v1.0):**
- ✅ **100 Drama Scripts** - Available now on Hugging Face
- 📥 **Download**: [FutureMa/DramaBench](https://huggingface.co/datasets/FutureMa/DramaBench)
- 📄 **Format**: JSONL with structured metadata
- 🔓 **License**: MIT License
- 📊 **Usage**: Load with `datasets` library

**Quick Start:**
```python
from datasets import load_dataset

# Load dataset
dataset = load_dataset("FutureMa/DramaBench", split="train")

# Access samples
sample = dataset[0]
print(sample['title'])
print(sample['context'])
print(sample['continuation'])
```

**Release Roadmap:**
| Version | Samples | Status | Expected Release |
|---------|---------|--------|------------------|
| v1.0 | 100 | ✅ Available | 2025-12-23 |
| v2.0 | 500 | 🔄 Coming Soon | Q1 2026 |
| v3.0 (Full) | 1,103 | 📋 Planned | Q2 2026 |

**Full Dataset Contents (v3.0):**
- 1,103 drama script contexts and continuations
- Model-generated continuations (8 SOTA models)
- Human annotations and quality assessments
- Multi-dimensional evaluation metrics
- Error taxonomy and classification

### 3. Evaluation Code

**Coming Soon**: Full evaluation pipeline including:

- Six-dimensional evaluation framework
- LLM-based labeling prompts and scripts
- Statistical analysis tools
- Visualization generation
- Reproducibility scripts

---

<a id="web-demo"></a>
## 🌐 Website & Interactive Demo

### Live Website

Visit [dramabench.pages.dev](https://dramabench.pages.dev) to explore:

- **Homepage** - Project overview and statistics
- **Leaderboard** - Compare 8 SOTA models across 6 dimensions
- **Case Studies** - Browse 24 curated examples with detailed analysis
- **Interactive Demo** - Try script continuation yourself

### Interactive Demo

**Try it now:** [dramabench.pages.dev/web/demo.html](https://dramabench.pages.dev/web/demo.html)

Experience drama script continuation with state-of-the-art language models:

**Features:**
- 🎭 **100 Drama Scripts** - Select from DramaBench v1.0 dataset
- 🤖 **4 SOTA Models** - GPT-5.2, Gemini 3 Flash, GLM-4.7, MiniMax M2.1
- 🔑 **Your API Key** - Uses OpenRouter API (bring your own key)
- 📊 **Compare Results** - View AI-generated vs ground truth side-by-side
- 🎨 **Apple Design** - Beautiful, responsive interface

**How to Use:**
1. Get your free API key from [OpenRouter](https://openrouter.ai/keys)
2. Visit the [demo page](https://dramabench.pages.dev/web/demo.html)
3. Enter your API key (stored locally in your browser)
4. Select a script from 100 options
5. Choose your preferred model
6. Generate and compare continuations

**Cost:** Pay-as-you-go through OpenRouter (typically $0.01-0.10 per generation)

### Website Features

**Interactive Leaderboard**
- Filter by dimension (overall + 6 dimensions)
- Expandable model details with per-dimension scores
- Rank badges (gold/silver/bronze)
- Real-time filtering and sorting

**Case Studies Explorer**
- 24 curated success/failure examples
- Filter by dimension and type
- Script excerpts with metrics
- Analysis insights and takeaways

**Design**
- Apple-inspired UI with premium dark gradients
- SF Pro font family (system fonts)
- Glassmorphism effects
- Smooth animations and transitions
- Fully responsive layout

### Technologies

- Pure HTML/CSS/JavaScript (no frameworks)
- Apple Design Language principles
- CSS Grid & Flexbox layouts
- Backdrop filters for glassmorphism
- CSS animations for smooth transitions

### Local Development

Regenerate web demo data from source:

```bash
cd DramaBench
uv run python web/scripts/process_data.py
```

This processes:
- 6 dimension metrics CSV files (8,824 evaluations)
- 24 case studies with detailed analysis
- Generates web-friendly JSON in `web/data/`

---

<a id="dataset"></a>
## 💾 Dataset

### Dataset Access

**🤗 Hugging Face Dataset**: [FutureMa/DramaBench](https://huggingface.co/datasets/FutureMa/DramaBench)

**Current Release: v1.0 (100 samples)** - Available Now!

### Quick Start

**Load with Datasets Library:**
```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("FutureMa/DramaBench", split="train")

# Access a sample
sample = dataset[0]
print(f"Title: {sample['title']}")
print(f"Context: {sample['context'][:200]}...")
print(f"Continuation: {sample['continuation'][:200]}...")
print(f"Stats: {sample['stats']}")
```

**Analyze Dataset:**
```bash
cd DramaBench
python scripts/load_dataset.py
```

### Dataset Overview

**Current Release (v1.0 - 100 samples):**
- 100 high-quality drama scripts with context-continuation pairs
- Average context length: ~1,601 characters (~400 tokens)
- Average continuation length: ~1,600 characters (~400 tokens)
- Split types: 73% scene boundary, 27% middle
- Format: Fountain screenplay format (industry standard)
- Fields: `id`, `title`, `description`, `context`, `continuation`, `stats`

**Release Roadmap:**
| Version | Samples | Status | Release Date |
|---------|---------|--------|--------------|
| **v1.0** | **100** | **✅ Available** | **2025-12-23** |
| v2.0 | 500 | 🔄 Coming Soon | Q1 2026 |
| v3.0 (Full) | 1,103 | 📋 Planned | Q2 2026 |

**Full Benchmark (v3.0 - Planned):**
- 1,103 complete drama scripts
- Model-generated continuations from 8 SOTA models
- Human annotations and quality assessments
- Multi-dimensional evaluation metrics (8,824 evaluations)
- Error taxonomy and classification
- Statistical significance test results

**Format:** JSONL with structured metadata

**License:** MIT License

---

<a id="evaluation-framework"></a>
## 📊 Evaluation Framework

### Methodology

DramaBench uses a **hybrid evaluation system**:

1. **Rule-Based Analysis** (Format Standards)
   - 100% reproducible
   - Zero cost
   - Fountain syntax validation

2. **LLM-Based Labeling** (5 content dimensions)
   - Structured feature extraction
   - Statistical metric calculation
   - Not direct scoring

### Six Dimensions

| Dimension | Type | Key Metrics | Description |
|-----------|------|-------------|-------------|
| **Format Standards** | Rule-based | Format Error Rate, Novelization Index, Dialogue-Action Ratio | Screenplay format compliance |
| **Narrative Efficiency** | LLM-labeled | Effective Narrative Rate (ENR), Beats Per Page | Story progression effectiveness |
| **Character Consistency** | LLM-labeled | Out-of-Character Rate, Voice Distinctiveness | Character voice and behavior consistency |
| **Emotional Depth** | LLM-labeled | Arc Score, Complexity Ratio | Emotional arc development |
| **Logic Consistency** | LLM-labeled | Logic Break Rate, Context Coherence | Factual coherence and logical continuity |
| **Conflict Handling** | LLM-labeled | Conflict Score, Drop Rate | Conflict development and resolution |

### Validation

**Statistical Significance:**
- 252 Mann-Whitney U tests performed
- 166/252 comparisons significant (65.9% with FDR correction)
- Beats Per Page: Most differentiating (26/28 significant)

**Dimension Independence:**
- Mean absolute correlation: |r| = 0.020 (extremely low)
- Max correlation: |r| = 0.068 (Format ↔ Narrative)
- All dimensions capture distinct quality aspects

**Human-LLM Agreement:**
- Strong agreement on 3/5 dimensions
- Logic: r=0.48*** (Pearson correlation)
- Emotional Depth: κ=0.53 (Cohen's Kappa)
- Conflict: κ=0.42 (Cohen's Kappa)

---

<a id="leaderboard"></a>
## 🏆 Leaderboard

### Top 8 Models Evaluated

| Rank | Model | Provider | Overall Score |
|------|-------|----------|---------------|
| 🥇 1 | **GPT-5.2** | OpenAI | 0.960 |
| 🥈 2 | **GLM-4.6** | Zhipu AI | 0.930 |
| 🥉 3 | **Qwen3-Max** | Alibaba Cloud | 0.917 |
| 4 | **Claude Opus 4.5** | Anthropic | 0.888 |
| 5 | **MiniMax M2** | MiniMax | 0.869 |
| 6 | **DeepSeek V3.2** | DeepSeek | 0.856 |
| 7 | **Gemini 3 Pro** | Google DeepMind | 0.843 |
| 8 | **Kimi K2 Thinking** | Moonshot AI | 0.815 |

**Note:** Rankings may vary by dimension. See [web demo](web/leaderboard.html) for detailed per-dimension scores.

---

<a id="documentation"></a>
## 📚 Documentation

### Project Structure

```
DramaBench/
├── index.html                    # Main landing page
├── README.md                     # This file
├── start_demo.sh                 # One-click demo launcher
├── assets/
│   └── DramaBench_cover.png     # Project cover image
├── web/                          # Web application
│   ├── leaderboard.html         # Model rankings page
│   ├── cases.html               # Case studies page
│   ├── demo.html                # Interactive script continuation demo
│   ├── css/
│   │   └── apple-style.css      # Apple-inspired CSS framework
│   ├── data/                    # Data files
│   │   ├── leaderboard.json     # Model rankings (14KB)
│   │   ├── case_studies.json    # 24 case studies (262KB)
│   │   ├── statistics.json      # Overall statistics (3KB)
│   │   └── demo/                # Demo-specific data
│   │       ├── dramabench_continuation_100.jsonl  # 100 scripts dataset
│   │       └── drama_continuation_prompt_template.txt  # Official prompt
│   └── scripts/
│       ├── process_data.py      # Data processing script
│       └── demo.js              # Interactive demo logic
├── dataset/                      # [Coming Soon] Dataset files
├── evaluation/                   # [Coming Soon] Evaluation code
└── docs/                         # [Coming Soon] Additional documentation
```

### Browser Compatibility

Tested and optimized for:
- ✅ Chrome 90+
- ✅ Safari 14+
- ✅ Firefox 88+
- ✅ Edge 90+

### Common Issues

**Issue: "Error loading data"**

- **Cause**: Opening HTML files directly without HTTP server
- **Solution**: Use `./start_demo.sh` or `python3 -m http.server 8000`

**Issue: "Port 8000 already in use"**

- **Cause**: Another process is using port 8000
- **Solution**: Use a different port: `python3 -m http.server 8001`

---

<a id="contributing"></a>
## 🤝 Contributing

We welcome contributions to DramaBench! Areas for contribution:

- 🐛 Bug reports and fixes
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- 📊 New visualizations
- 🔧 Evaluation tools
- 💾 Dataset improvements

**How to Contribute:**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

<a id="citation"></a>
## 📖 Citation

If you use DramaBench in your research, please cite our paper:

```bibtex
@misc{ma2025dramabenchsixdimensionalevaluationframework,
  title={DramaBench: A Six-Dimensional Evaluation Framework for Drama Script Continuation},
  author={Shijian Ma and Yunqi Huang and Yan Lin},
  year={2025},
  eprint={2512.19012},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2512.19012}
}
```

---

<a id="license"></a>
## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Apple Design Team** - Design inspiration
- **ACL Community** - Research support
- **Model Providers** - OpenAI, Anthropic, Google DeepMind, Alibaba Cloud, DeepSeek, MiniMax, Moonshot AI, Zhipu AI

---

## 📧 Contact

For questions, feedback, or collaboration opportunities:

- **Issues**: [GitHub Issues](https://github.com/IIIIQIIII/DramaBench/issues)
- **Email**: mas8069@foxmail.com
- **Twitter**: @mashijiann

related:
  - methods/QUICK_START.md
---

<div align="center">

**Last Updated**: 2025-12-20 • **Version**: 1.0.0 • **Status**: ✅ Active

Made with ❤️ by the DramaBench Team

</div>
