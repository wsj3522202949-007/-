---
id: tool-05263
type: tool
area: 库
status: active
tags: [TTS, Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: ai-watermark-detector-removel
summary: 小说转语音/有声书
source: https://github.com/osman-haider/ai-watermark-detector-removel
created: 2026-07-18
updated: 2026-07-18
no: 5263
category: 一、去 AI 味 / Humanizer 库
repo: osman-haider/ai-watermark-detector-removel
stars: 3
url: https://github.com/osman-haider/ai-watermark-detector-removel
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# osman-haider/ai-watermark-detector-removel

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/osman-haider/ai-watermark-detector-removel
- **Stars**：3
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：ai-water-management, ai-watermark, ai-watermark-detection, ai-watermark-remover, watermark
- **GitHub 描述**：An end-to-end NLP pipeline for detecting and mitigating AI-generated text watermarks using transformer models from Hugging Face with ML-based ensemble decisions. It transforms text via paraphrasing, back-translation, synonym replacement, and sentence restructuring, then compares detection results before and after processing.
- **本地描述**：An end-to-end NLP pipeline for detecting and mitigating AI-generated text watermarks using transformer models from Hugging Face with ML-based ensemble decisions. It transforms text via paraphrasing, back-translation, synonym replacement, and sentence restructuring, then compares detection results before and after processing.
- **拉取时间**：2026-07-25 18:12:05

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Watermark Detector and Removal Pipeline

A comprehensive pipeline for detecting and removing AI-generated watermarks from text using multiple detection models, paraphrasing, back-translation, and sentence restructuring techniques.

## Features

- **Multi-Model Watermark Detection**: Uses multiple transformer models (T5, GPT-2, Llama-2, Falcon, DeepSeek) to detect watermarks
- **ML-Based Decision Making**: Combines detection results using machine learning for final prediction
- **Text Paraphrasing**: Rewrites text using contextual word embeddings to remove watermarks
- **Synonym Replacement**: Replaces words with synonyms using WordNet for text variation
- **Back-Translation**: Translates text through intermediate languages and back to English for additional transformation
- **Sentence Restructuring**: Restructures sentences by converting between active/passive voice
- **Automatic File Management**: Saves all outputs to the `data/` folder
- **Result Tracking**: Saves detection results before and after processing for comparison

## Project Structure

```
watermark-detector-removel/
├── ai_detector/              # Watermark detection modules
│   ├── base.py              # Core detection logic
│   ├── config.py            # Model configurations
│   ├── cal_perc_model.py    # ML decision model
│   ├── model_building.py    # Feature extraction and model building
│   ├── normalizer.py        # Text normalization utilities
│   ├── homoglyphs.py        # Homoglyph detection and handling
│   ├── ensemble_ai_detector.pkl          # Trained ensemble model
│   └── ensemble_ai_detector_scaler.pkl   # Feature scaler
├── paraphraser/              # Text paraphrasing module
│   └── paraphsing.py
├── translator/               # Back-translation module
│   └── translation.py
├── Sentence_Restructuring/  # Sentence restructuring module
│   └── restructuring.py
├── synonym_replacement/      # Synonym replacement module
│   └── synonym_replacement.py
├── data/                     # Input/output files
│   ├── data.txt             # Input text (required)
│   ├── paraphrase.txt       # Paraphrased output (generated)
│   ├── translated.txt       # Back-translated output (generated)
│   ├── restructured.txt     # Restructured output (generated)
│   └── synonym_replaced.txt # Synonym-replaced output (generated)
├── models/                   # Model files (backup location)
│   ├── ensemble_ai_detector.pkl
│   └── ensemble_ai_detector_scaler.pkl
├── results/                  # Detection results
│   ├── before_detection.json    # Detection results before processing
│   ├── after_detection.json     # Detection results after processing
│   └── comparison_summary.json  # Comparison summary
├── notebooks/                # Jupyter notebooks for development
│   ├── ai_detector.ipynb
│   └── paraphrasing.ipynb
├── test/                     # Test files
│   └── test.py
├── main.py                   # Main execution script
├── setup_nltk.py             # NLTK data setup script (run once before main.py)
└── requirements.txt          # Python dependencies
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/osman-haider/watermark-detector-removel.git
cd watermark-detector-removel
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

**Windows:**
```powershell
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install spaCy language model

```bash
python -m spacy download en_core_web_sm
```

### 5. Download NLTK data

Run the setup script to download all required NLTK data packages:

```bash
python setup_nltk.py
```

This will download:
- `punkt`: Sentence tokenizer
- `punkt_tab`: Updated punkt tokenizer data
- `wordnet`: WordNet lexical database for synonym replacement
- `averaged_perceptron_tagger_eng`: Part-of-speech tagger for English

**Note:** This step is required before running the main application. The script will check if packages are already installed and skip them if found.

## Setup

### Hugging Face Authentication

This project uses gated models (like `meta-llama/Llama-2-7b-hf`) that require authentication. You need to set your Hugging Face token as an environment variable.

#### Getting your Hugging Face Token

1. Go to https://huggingface.co/settings/tokens
2. Create a new token (or use an existing one)
3. Make sure you have access to the gated models you need:
   - Request access at https://huggingface.co/meta-llama/Llama-2-7b-hf

#### Setting the Token (Windows PowerShell)

**Option 1: Set for current session only**
```powershell
$env:HF_TOKEN = "your_token_here"
```

**Option 2: Set permanently (for current user)**
```powershell
[System.Environment]::SetEnvironmentVariable("HF_TOKEN", "your_token_here", "User")
```

**Option 3: Set permanently (system-wide)**
```powershell
[System.Environment]::SetEnvironmentVariable("HF_TOKEN", "your_token_here", "Machine")
```

After setting permanently, restart your terminal/PowerShell.

#### Setting the Token (Windows Command Prompt)

**Option 1: Set for current session only**
```cmd
set HF_TOKEN=your_token_here
```

**Option 2: Set permanently**
```cmd
setx HF_TOKEN "your_token_here"
```

#### Using .env file (Recommended)

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_token_here
```

The code will automatically load the token from the `.env` file using `python-dotenv`.

#### Alternative Environment Variable Names

The code also checks for these environment variable names:
- `HUGGINGFACE_TOKEN`
- `HUGGING_FACE_HUB_TOKEN`

#### Verify Token is Set

```powershell
echo $env:HF_TOKEN
```

## Usage

**Important:** Make sure you've completed all setup steps above, including running `python setup_nltk.py` to download required NLTK data.

### 1. Prepare Input Text

Place your text in `data/data.txt`:

```bash
# Create the file if it doesn't exist
echo "Your text here" > data/data.txt
```

### 2. Run the Pipeline

```bash
python main.py
```

### 3. Check Outputs

After execution, check the following folders:

**`data/` folder:**
- `paraphrase.txt` - Paraphrased version of the input
- `synonym_replaced.txt` - Synonym-replaced version of the input
- `translated.txt` - Back-translated version (English → Intermediate Language → English)
- `restructured.txt` - Sentence-restructured version

**`results/` folder:**
- `before_detection.json` - Watermark detection results before processing
- `after_detection.json` - Watermark detection results after processing
- `comparison_summary.json` - Summary comparing before and after detection results

## Pipeline Steps

The script processes text through the following steps:

1. **Load Input Text** - Reads text from `data/data.txt`
2. **Watermark Detection (Before)** - Detects watermarks using multiple transformer models
3. **ML Decision (Before)** - Computes final decision using ML ensemble model
4. **Save Initial Detection Results** - Saves detection results to `results/before_detection.json`
5. **Paraphrasing** - Rewrites text using contextual word embeddings (BERT-based)
6. **Save Paraphrased Text** - Saves to `data/paraphrase.txt`
7. **Back-Translation** - Translates text through an intermediate language and back to English
8. **Save Translated Text** - Saves to `data/translated.txt`
9. **Synonym Replacement** - Replaces words with synonyms using WordNet
10. **Save Synonym Replaced Text** - Saves to `data/synonym_replaced.txt`
11. **Sentence Restructuring** - Restructures sentences by converting between active/passive voice
12. **Save Restructured Text** - Saves to `data/restructured.txt`
13. **Watermark Detection (After)** - Detects watermarks in the final processed text
14. **ML Decision (After)** - Computes final decision for processed text
15. **Save Final Detection Results** - Saves detection results to `results/after_detection.json`
16. **Comparison Analysis** - Compares before and after detection results
17. **Save Comparison Summary** - Saves comparison to `results/comparison_summary.json`

## Notes

- The translation module processes text sentence-by-sentence to handle long texts efficiently
- All outputs overwrite previous files on each run
- The pipeline includes comprehensive error handling and progress logging
- Make sure you have internet access for downloading models and using translation APIs

## Troubleshooting

### Error: "Cannot access gated repo"
- Make sure your Hugging Face token is set correctly
- Request access to gated models at their respective Hugging Face pages
- Verify token has read permissions

### Error: "spacy model not found"
- Run: `python -m spacy download en_core_web_sm`

### Error: "NLTK data not found" or "LookupError: punkt"
- Run: `python setup_nltk.py` to download all required NLTK data packages
- Make sure you have internet access during the setup

### Translation errors with long text
- The script automatically handles long texts by processing sentence-by-sentence
- If errors persist, check your internet connection and Google Translate API availability
