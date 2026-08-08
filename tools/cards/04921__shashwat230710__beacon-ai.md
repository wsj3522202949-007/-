---
id: tool-04921
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: beacon-ai
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/shashwat230710/beacon-ai
created: 2026-07-18
updated: 2026-07-18
no: 4921
category: 一、去 AI 味 / Humanizer 库
repo: shashwat230710/beacon-ai
stars: 0
url: https://github.com/shashwat230710/beacon-ai
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 470b4a34b8d7a000
  - methods/改稿润色指令库.md
---

# shashwat230710/beacon-ai

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/shashwat230710/beacon-ai
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Becon AI — Fake News Detector A full-stack, multi-modal misinformation-analysis web app: paste text, upload an image or video, or drop in a URL, and get a verdict with an explainable evidence report. Built from the "Investigative Noir" implementation plan — dark, dossier/stamp/glitch visual language, three tabs (Analyze / Browse Viral / Dashboard).
- **本地描述**：Becon AI — Fake News Detector A full-stack, multi-modal misinformation-analysis web app: paste text, upload an image or video, or drop in a URL, and get a verdict with an explainable evidence report. Built from the "Investigative Noir" implementation plan — dark, dossier/stamp/glitch visual language, three tabs (Analyze / Browse Viral / Dashboard).
- **拉取时间**：2026-07-25 17:59:27

---

# Becon AI — Fake News Detector

A full-stack, multi-modal misinformation-analysis web app: paste text, upload an
image or video, or drop in a URL, and get a verdict with an explainable
evidence report. Built from the "Investigative Noir" implementation plan —
dark, dossier/stamp/glitch visual language, three tabs (Analyze / Browse
Viral / Dashboard).

**This is a real, working, end-to-end application** — the Flask API, the
trained text model, the classical image-forensics engine, the video frame
pipeline, and the full noir frontend all run today with no external services
required. Read **"What's real vs. what's a stand-in"** below before treating
any of it as more capable than it is.

---

## Quickstart

```bash
cd backend
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

# System dependency for OCR (image text extraction):
#   Ubuntu/Debian: sudo apt install tesseract-ocr
#   macOS:          brew install tesseract
# Optional, for the audio-transcription step of video analysis:
#   Ubuntu/Debian: sudo apt install ffmpeg

# Train the bundled demo text model (takes a few seconds):
python -m ml.generate_dataset
python -m ml.text_model_trainer

# Run the app:
python app.py
# → open http://localhost:5000
```

Or with Docker:
```bash
docker compose up --build
# → open http://localhost:5000
```

Run the test suite:
```bash
cd backend && pytest tests/ -v
```

---

## What's real vs. what's a stand-in

The original implementation plan assumes resources that aren't available in
every environment: an 85,000-article labeled news corpus, ~20,000 labeled
real/manipulated images (CASIA/DFDC/NIST MFC), outbound network access to
video platforms and Whisper's model host, and live RSS access to fact-check
sites. Rather than fake competence the app doesn't have, here's the honest
breakdown — and this same list is shown in-app on the **Dashboard tab**:

| Component | Status | Notes |
|---|---|---|
| **Text classifier** | ✅ Real, trained | TF-IDF(1,2) + `CalibratedClassifierCV(LinearSVC)`, genuinely fits and generalizes. Trained on `ml/generate_dataset.py`'s **synthetic/templated** dataset (encodes known misinformation style markers), not a real news corpus. Detects *writing style*, not factual accuracy — a calm, well-attributed hoax ("NASA scientists announced the Moon will glow green due to a planetary alignment…") can still fool it, since nothing about the sentence structure looks stylistically "fake." The dataset includes sober-toned hoax templates (`SOBER_HOAX_*` in `generate_dataset.py`) to narrow this gap, with a regression test in `tests/test_text_model.py`, but style analysis alone can never fully replace fact-checking against real sources. Swap in a real corpus (LIAR, FakeNewsNet, Kaggle Fake-and-real-news) by replacing `data/raw/dataset.csv` — `text_model_trainer.py` needs no changes. |
| **Suspicious-phrase highlighter** | ✅ Real | Transparent keyword/pattern matcher (`nlp/highlighter.py`), independent of the ML model. |
| **Feature-importance chart** | ✅ Real | Computed live from the trained model's actual coefficients for each specific input (`TextPredictor.top_features`) — not fabricated. |
| **Image analysis** | ✅ Real, but classical (not a CNN) | Error Level Analysis + noise-consistency analysis (`ml/image_forensics.py`) — legitimate, explainable forensic techniques, computed live, no training data needed. The plan's CNN architecture would need ~20k labeled images we don't have; see below for how to add one. |
| **OCR (image text extraction)** | ✅ Real | Tesseract via `pytesseract`, degrades gracefully if the binary isn't installed. |
| **Video — frame extraction & visual analysis** | ✅ Real | OpenCV-based frame sampling + the same forensics engine per frame. |
| **Video — audio transcription (Whisper)** | ⚠️ Wired up, best-effort | `media/audio_transcriber.py` calls `openai-whisper` if installed; it needs to download ~74MB of model weights from OpenAI's CDN on first use. Works out of the box with normal internet access; degrades gracefully (skips audio, keeps visual analysis) if that download isn't reachable. |
| **Video-by-URL (YouTube etc.)** | ⚠️ Scaffolded, disabled by default | `/api/predict/video-url` returns HTTP 501 unless `yt-dlp` is installed — see `media/video_downloader.py`-equivalent hook in `app.py`. Uploading a video file always works. |
| **Viral feed — live RSS** | ⚠️ Real code, needs network | `feed/feed_aggregator.py` really parses RSS from Snopes/PolitiFact/Full Fact/FactCheck.org/AFP via `feedparser`. If those domains aren't reachable it fails per-source (logged) and falls back to... |
| **Viral feed — curated seed data** | ✅ Real, clearly labeled | `data/viral_feed/seed_data.json` — exactly the plan's own "Tier 2" MVP strategy. Every item is marked `is_sample_data: true` and does **not** attribute real verdicts to real organizations (to avoid manufacturing fake fact-checks). |
| **URL/article extraction** | ✅ Real | `requests` + BeautifulSoup, heuristic paragraph extraction (lighter/more maintainable than `newspaper3k`). |
| **Summarizer** | ✅ Real | Lightweight frequency-based extractive summarizer — no model download required. |

**Bottom line:** every endpoint does real work on real input; the two honest
gaps are (1) the text model's *training data* is synthetic, and (2) the image
"AI" is classical forensics rather than a trained CNN, both because the
underlying labeled datasets aren't available here. Everything is structured
so plugging in real data later requires no architecture changes.

### Upgrading to production
- **Real news corpus:** replace `backend/data/raw/dataset.csv` (columns:
  `text,label,topic`) with a real labeled dataset, then re-run
  `python -m ml.text_model_trainer`.
- **Trained CNN for images:** `ml/image_preprocessor.py` already has
  `preprocess_for_model()` (224×224×3, normalized) ready for a Keras/TF model;
  wire a `predict()` call into `ml/image_predictor.py` alongside (or instead
  of) the forensics score once you have labeled training images.
- **Whisper:** `pip install openai-whisper` and ensure outbound network
  access to OpenAI's model host — no code changes needed.
- **yt-dlp:** `pip install yt-dlp` and implement the download step in
  `/api/predict/video-url` in `app.py` (the endpoint already detects and
  reports whether `yt-dlp` is present).
- **Live fact-check feeds:** ensure outbound network access to the domains in
  `data/viral_feed/sources.json`; `feed_aggregator.py` needs no changes.

---

## Project structure

```
becon-ai/
├── backend/
│   ├── app.py                  # Flask entry point, all API routes
│   ├── config.py
│   ├── requirements.txt
│   ├── ml/                     # text + image + video ML pipelines
│   ├── nlp/                    # highlighter, summarizer, URL extraction, OCR
│   ├── media/                  # frame extraction, audio transcription
│   ├── feed/                   # viral feed aggregation, caching, curation
│   ├── utils/                  # logging, helpers, validators
│   ├── data/                   # models/, raw/, viral_feed/, feedback/
│   └── tests/                  # pytest suite (40 tests)
├── frontend/
│   ├── index.html
│   ├── css/                    # theme tokens, animations, components, responsive
│   └── js/                     # api, ui, charts, feed, media-upload, app
├── Dockerfile
├── docker-compose.yml
└── README.md   ← you are here
```

## API reference

| Method | Endpoint | Purpose |
|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| GET | `/api` | Health check |
| POST | `/api/predict/text` | `{text}` → verdict + evidence report |
| POST | `/api/predict/image` | multipart `file` → verdict + heatmap + OCR |
| POST | `/api/predict/video` | multipart `file` → frame-by-frame + audio analysis |
| POST | `/api/predict/video-url` | `{url}` → 501 unless `yt-dlp` installed |
| POST | `/api/predict/url` | `{url}` → extracts article, then analyzes |
| POST | `/api/summarize` | `{text}` → extractive summary |
| GET | `/api/feed` | Viral feed, filterable/paginated |
| GET | `/api/feed/stats` | Aggregate feed stats |
| POST | `/api/feed/refresh` | Force a feed refresh |
| GET | `/api/feed/sources` | List of fact-check sources + fetch status |
| GET | `/api/model/info` | Text-model metadata (accuracy, training size, etc.) |
| GET | `/api/suspicious-phrases` | The tracked phrase dictionary |
| POST | `/api/feedback` | `{correct, input_mode, predicted_label, notes}` |

Every endpoint returns `{"success": true/false, ...}` with matching HTTP
status codes (400/422/429/500/501 as appropriate).

## Notes on the demo dataset & seed feed data

- `ml/generate_dataset.py` synthesizes labeled examples from templates
  encoding known misinformation *style* markers (sensationalism, vague
  authority, urgency) vs. measured reporting style — see the module
  docstring for the full rationale.
- `data/viral_feed/seed_data.json` contains illustrative example items only
  (`is_sample_data: true`), not real fact-checks — see the file's own `note`
  field.

## License

Demo/reference implementation — adapt freely for your own use.
