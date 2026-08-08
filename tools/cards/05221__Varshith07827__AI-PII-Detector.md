---
id: tool-05221
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-PII-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/varshith07827/ai-pii-detector
created: 2026-07-18
updated: 2026-07-18
no: 5221
category: 一、去 AI 味 / Humanizer 库
repo: Varshith07827/AI-PII-Detector
stars: 1
url: https://github.com/varshith07827/ai-pii-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: e5b7a653f4c6e415
  - methods/改稿润色指令库.md
---

# Varshith07827/AI-PII-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/varshith07827/ai-pii-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Developers accidentally push spreadsheets with passport numbers or patient data to GitHub every day. Drop any file or text in and get an instant heat-map of every personal identifier plus one-click masking—turning a potential breach into a 30-second fix
- **本地描述**：Developers accidentally push spreadsheets with passport numbers or patient data to GitHub every day. Drop any file or text in and get an instant heat-map of every personal identifier plus one-click masking—turning a potential breach into a 30-second fix
- **拉取时间**：2026-07-25 18:10:33

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# PII Detector –(CLI + GUI) AI Privacy Protection Tool

Offline-first Flask app that detects, scores, highlights, and masks PII in pasted text or uploaded files (PDF, DOCX, CSV, XLSX, TXT). Hybrid regex + optional spaCy mode, plus a CLI for offline/batch use.

## Quick start

1. Create/activate a virtualenv (already configured at `.venv` if you used the setup tools).
2. Install base deps:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Install NLP extras for spaCy:
   ```bash
   pip install -r requirements-nlp.txt
   python -m spacy download en_core_web_md || python -m spacy download en_core_web_sm
   ```
4. Run the app:
   ```bash
   flask --app app run --reload
   ```
5. Open http://127.0.0.1:5000 and test.

## CLI Usage

You can use the CLI tool to process text or files directly from the command line.

```bash
# Process text string
python cli.py "My email is test@example.com"

# Process a file
python cli.py path/to/document.txt

# Process PDF/DOCX/CSV/XLSX/TXT with auto extraction
python cli.py path/to/document.pdf

# Save masked output to a file
python cli.py input.txt --output masked.txt

# Generate JSON report
python cli.py input.txt --json report.json

# Specify detection and masking modes
python cli.py input.txt --mode regex --mask-mode partial

# Filter by confidence threshold
python cli.py input.txt --min-confidence 0.7

# Batch process directory recursively
python cli.py path/to/documents/ --batch --json batch_report.json
```

## Features

- Multi-format ingest with in-memory parsing; 10 MB max; no data stored.
- Regex detection for Aadhaar, PAN, Passport (IN), credit/debit cards (Luhn), phone/email/IP/DOB, bank accounts with IFSC cues, placeholder/fake data.
- Optional spaCy hybrid mode for names, addresses, dates; falls back to regex-only if unavailable.
- Risk scoring with compliance hints (GDPR/DPDP/HIPAA), heat-map highlighting, and masking modes (partial, full, synthetic). Placeholders can be flagged or masked (opt-in).
- Masking can target a single detected type (e.g., only emails) or all types.
- Offline-only: no external API calls.
- CLI supports text or file inputs, detection/masking mode selection, and JSON reporting.
- CLI auto-extracts PDF, DOCX, CSV, XLSX, and TXT with the same size limits as the API.
- CLI batch mode processes entire directories with aggregated reports and per-file risk summaries.
- Confidence threshold filtering (`--min-confidence`) reduces noise by excluding low-confidence detections.

## API (draft)

- `POST /api/detect` (multipart or JSON): `text` or `file`, `mode` (`regex|hybrid`). Returns entities and risk.
- `POST /api/mask` (JSON or form): `text`, `mode`, `masking` (`partial|full|synthetic`), `includePlaceholders` (bool). Returns masked text.
- `GET /health`: liveness.

## Tests

```bash
pytest
```

## Notes

- Placeholder stripping/replacement is opt-in; defaults to flagging only.
- For best NLP accuracy, prefer `en_core_web_md` if available; auto-fallback to small model.
- Python 3.12 virtualenv provided at `.venv312` (recommended for spaCy compatibility); base `.venv` is 3.13.
