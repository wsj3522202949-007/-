---
id: tool-05140
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 需API密钥, 英文文档]
title: humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/sriman676/humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5140
category: 一、去 AI 味 / Humanizer 库
repo: sriman676/humanizer
stars: 0
url: https://github.com/sriman676/humanizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8d8f8eb3f46649ff
  - methods/改稿润色指令库.md
---

# sriman676/humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sriman676/humanizer
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Local-first Python tool that rewrites long-form text into natural prose via a local Ollama LLM pipeline — supports PDF/DOCX/TXT input, CLI and Flask web UI.
- **本地描述**：Local-first Python tool that rewrites long-form text into natural prose via a local Ollama LLM pipeline — supports PDF/DOCX/TXT input, CLI and Flask web UI.
- **拉取时间**：2026-07-25 18:07:36

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Humanizer

Humanizer is a local Python tool that rewrites long-form text using a 3-stage pipeline:

1. LLM structural rewrite
2. LLM humanization rewrite
3. Python post-processing

It supports both CLI and a Flask web interface.

## Features

- Local-first workflow via Ollama (no external API key required)
- File input support: PDF, DOCX, TXT, MD
- Paste-text input support in web UI
- Chunked processing for longer documents
- Configurable writing style and target page count

## Project Structure

- `humanizer.py`: CLI tool and rewrite pipeline
- `humanizer_app.py`: Flask web app
- `humanizer_uploads/`: temporary uploaded and output files

## Requirements

- Python 3.10+
- Ollama running locally
- A pulled Ollama model (default: `llama3.1:8b`)

Python packages:

- `requests`
- `flask`
- `PyMuPDF`
- `python-docx`

## Setup

1. Install Python dependencies:

```bash
pip install requests flask PyMuPDF python-docx
```

2. Start Ollama:

```bash
ollama serve
```

3. Pull the default model:

```bash
ollama pull llama3.1:8b
```

4. Quick health check:

```bash
python - << 'EOF'
from humanizer import check_ollama, DEFAULT_MODEL
print("OLLAMA_READY=", check_ollama(DEFAULT_MODEL))
EOF
```

Expected output:

- `OLLAMA_READY= True`

## CLI Usage

Interactive mode:

```bash
python humanizer.py
```

File mode:

```bash
python humanizer.py --file paper.pdf --pages 18 --style research
python humanizer.py --file essay.docx --pages 2 --style academic --output out.txt
```

### CLI Arguments

- `--file`, `-f`: input file path
- `--pages`, `-p`: target page count
- `--style`, `-s`: style key
- `--output`, `-o`: output text file path
- `--model`, `-m`: Ollama model name

Available styles:

- `academic`
- `business`
- `legal`
- `journalistic`
- `general`
- `essay`
- `research`

## Web App Usage

Run:

```bash
python humanizer_app.py
```

Open:

- `http://localhost:5050`

Web app supports:

- Uploading supported files
- Pasting text directly
- Choosing style and target pages
- Viewing output or downloading `.txt`

## Large Documents (Up To 20 Pages And Beyond)

The pipeline is chunk-based and can process long documents, including 20-page inputs, if:

- Ollama is running
- Sufficient CPU/RAM is available
- You allow enough processing time

The app uses a default estimate of `400 words = 1 page`.

## Equations And Algorithms

- Text containing equations and algorithms can be processed.
- Equation-like segments and math symbols are now protected with placeholders during rewriting and restored afterward, so notation is preserved exactly in normal cases.
- For highest fidelity, validate output against source when mathematical notation or pseudocode must remain exact.

## Supported File Types

- `.pdf`
- `.docx`
- `.txt`
- `.md`

Note on `.doc`:

- Legacy binary `.doc` files are less reliable with `python-docx`.
- Convert `.doc` to `.docx` before processing for best results.

## Troubleshooting

### `OLLAMA_READY=False`

Ensure both are true:

1. Ollama server is running (`ollama serve`)
2. Selected model is pulled (`ollama pull <model>`)

### `Model '<name>' not found`

Pull it first:

```bash
ollama pull <name>
```

### `Cannot connect to Ollama`

- Verify Ollama is installed and running on `http://localhost:11434`
- Check local firewall or container networking rules

### Empty Extraction Result

- Some PDFs are scanned images and may require OCR before processing.

## Security And Privacy

- Processing is local to your machine/environment.
- Uploaded files are written to `humanizer_uploads/`.
- Old job artifacts are periodically cleaned up by the app.
