---
id: tool-04806
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: prompt-injection-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/seokkeon/prompt-injection-detector
created: 2026-07-18
updated: 2026-07-18
$11960
category: 一、去 AI 味 / Humanizer 库
repo: seokkeon/prompt-injection-detector
stars: 0
language: Python
license: null
url: https://github.com/seokkeon/prompt-injection-detector
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
content_hash: b6c789347694c749
  - methods/改稿润色指令库.md
---

# Prompt Injection Detector

Detects hidden prompt injections in text, images, emails, web pages, and multi-turn conversations that could cause AI systems to leak data to attackers.

---

## Features

- **Text detection** — Rule-based patterns + fine-tuned ML classifier (DistilBERT / DeBERTa)
- **Image analysis** — 6-pass OCR, steganography, QR/barcode scanning, EXIF metadata, adversarial text, white-on-white invisible text
- **Email scanning** — Full `.eml` parsing: headers, plain text, HTML, hidden CSS elements, image attachments
- **Indirect injection** — Scans URLs, HTML, and documents for injections hidden in content an AI is asked to read
- **Conversation analysis** — Detects gradual jailbreaks, role drift, delayed triggers, persona anchoring across multi-turn chats
- **Explainability** — Attention rollout + keyword highlighting shows why a text was flagged
- **REST API** — FastAPI with batch (parallel), indirect, conversation, and explainability endpoints
- **React dashboard** — 3-tab UI: Unified (text + URL + HTML + document + conversation), Image, Email

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Full Project Structure

```
prompt-injection-detector/
│
├── api/
│   ├── __init__.py
│   └── main.py                  ← FastAPI app — all 9 endpoints
│                                   • Batch: parallel via asyncio.gather + run_in_executor
│                                   • URL: async httpx, non-blocking
│                                   • Thread-safe stats counter (threading.Lock)
│                                   • SSRF protection on /analyze/indirect/url
│                                   • CORS restricted via CORS_ORIGIN env var
│                                   • Rate limiting via slowapi (pip install slowapi)
│                                   • Startup config validation with warnings
│
├── src/
│   ├── detectors/
│   │   ├── unified_detector.py  ← Single entry point for ALL text-based detection:
│   │   │                           • Rule-based injection patterns (25 patterns, 7 categories)
│   │   │                           • Mega-regex fast path — one pass before running individual patterns
│   │   │                           • ML classifier (DistilBERT / DeBERTa) with LRU cache
│   │   │                           • Indirect injection — URL (async httpx), HTML, document
│   │   │                           • Conversation analysis — gradual jailbreak, role drift,
│   │   │                             delayed triggers, persona anchoring
│   │   │                           • Explainability — attention rollout or keyword highlighting
│   │   │                           • Batch detection
│   │   ├── image_detector.py    ← ALL image detection in one class:
│   │   │                           • 6-pass OCR (was 51+): baseline, inverted, adaptive threshold,
│   │   │                             near-white isolation, high-contrast enhancement, blue channel
│   │   │                           • Steganography: LSB, chi-square, entropy, noise analysis
│   │   │                           • QR code and barcode scanning (pyzbar)
│   │   │                           • EXIF metadata scanning (O(1) set lookup)
│   │   │                           • Adversarial text detection (Tesseract vs EasyOCR divergence)
│   │   │                           • Homoglyph detection (Unicode lookalike characters)
│   │   │                           • QR text analyzed independently, scores combined with max()
│   │   └── email_detector.py    ← Full .eml parsing:
│   │                     
