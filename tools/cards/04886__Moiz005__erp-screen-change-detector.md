---
id: tool-04886
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: erp-screen-change-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/moiz005/erp-screen-change-detector
created: 2026-07-18
updated: 2026-07-18
no: 4886
category: 一、去 AI 味 / Humanizer 库
repo: Moiz005/erp-screen-change-detector
stars: 0
url: https://github.com/moiz005/erp-screen-change-detector
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
content_hash: 925221e460523f04
  - methods/改稿润色指令库.md
---

# Moiz005/erp-screen-change-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/moiz005/erp-screen-change-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI-powered computer vision tool that detects meaningful screen changes in ERP demo recordings, captures key screenshots, extracts OCR text, and generates structured JSON, CSV, and HTML outputs for automated SOP and business process documentation.
- **本地描述**：An AI-powered computer vision tool that detects meaningful screen changes in ERP demo recordings, captures key screenshots, extracts OCR text, and generates structured JSON, CSV, and HTML outputs for automated SOP and business process documentation.
- **拉取时间**：2026-07-25 17:58:06

---

# ERP Screen Change Detector

Detects and captures meaningful screen changes in ERP demo recordings (e.g. Microsoft Teams sessions with an ERP app). Automatically identifies the Teams layout state (chat open, people open, or normal) so that the right portion of the screen is compared.

## Quick Start (Windows)

```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
python src\main.py --video path\to\demo.mp4
```

Outputs are written to a run-based folder: `output/{run_id}/`.

---

## How It Works

### Pipeline

```
Video Frame
  │
  ├── Layout Detection ──────────────────────────┐
  │     OCR on sidebar ROI                       │
  │     ↓                                        │
  │     "meeting chat" found → chat_open         │
  │     "people" / "participants" → people_open  │
  │     otherwise → normal                       │
  │                                              │
  ├── ERP Crop (per layout)                      │
  │     normal:   frame[250:1030, 100:1600]      │
  │     chat:     frame[350:1030, 100:1400]      │
  │     people:   frame[350:1030, 100:1400]      │
  │     ↓ resize to 1280×720                     │
  │                                              │
  ├── Change Detection                           │
  │     SSIM + ORB + Debounce                    │
  │     against last accepted frame              │
  │     ↓ if change confirmed                    │
  │                                              │
  ├── Duplicate Filter (pHash)                   │
  │     ↓ if not a duplicate                     │
  │                                              │
  └── Save screenshot + Full-frame OCR           │
       (text extracted from entire image)        │
```

### Layout Detection

The detector only inspects the **right sidebar** of the Teams window (configured as `sidebar_roi` in `config.yaml`). It runs OCR once on that region and checks for keywords:

| Layout | Trigger Keywords |
|---|---|
| `chat_open` | "meeting chat", "type a message", "joined the conversation" |
| `people_open` | "people", "participants", "invite", "search participants" |
| `normal` | (none matched — sidebar is empty or closed) |

### Change Detection

Each frame is compared against the last accepted frame through a three-stage process:

1. **SSIM** — Structural similarity (range 0–1). If SSIM < threshold, the frame is considered different.
2. **ORB** — Feature matching similarity (range 0–1). If ORB < threshold, further confirms difference.
3. **Debounce** — A candidate change must remain stable for N consecutive frames before being accepted (filters out transient spinners, popups, animations).

A **pHash duplicate filter** then compares the new frame against the last saved screenshot — if the perceptual hash distance is below the threshold, it's skipped as a near-identical duplicate.

---

## CLI Arguments

| Argument | Type | Default | Description |
|---|---|---|---|
| `--video` | str | **(required)** | Path to the input video file |
| `--run-id` | str | auto-generated | Run ID for the detection run (e.g. `RUN_20260625_223000`) |
| `--config` | str | `configs/config.yaml` | Path to the YAML configuration file |
| `--output` | str | `output` | Base output directory; results go to `{output}/{run_id}/` |
| `--sampling-rate` | int | `1` | Seconds between sampled frames |
| `--ssim-threshold` | float | `0.85` | SSIM threshold (0–1); higher = less sensitive |
| `--phash-threshold` | int | `10` | Max pHash distance to consider frames similar; lower = stricter |
| `--debounce-frames` | int | `2` | Consecutive stable frames required to confirm a change |
| `--duplicate-threshold` | int | `5` | Max pHash distance to consider a change a duplicate of the last saved screenshot |

All parameters can also be set in `configs/config.yaml`.

---

## Configuration

Edit `configs/config.yaml` to adjust:

- **`layouts`** — Per-layout crop coordinates that define the ERP content area (excluding Teams sidebars). Three layouts: `normal`, `chat_open`, `people_open`.
- **`layout_detection.sidebar_roi`** — The right-sidebar region OCR'd to determine the layout state.
- **`ignore_regions`** — Rectangles to mask out before comparison (e.g. taskbars, footers).
- **Detection thresholds** — SSIM, ORB, pHash, debounce, duplicate.

---

## Outputs

Results are written to `output/{run_id}/`:

| File / Directory | Description |
|---|---|
| `screenshots/` | Captured change frames as PNG images |
| `changes.json` | Full metadata per change (run ID, timestamp, OCR text, layout type, SSIM/ORB scores, classification, review flags) |
| `changes.csv` | Same metadata in tabular format |
| `review.html` | Visual review page rendered from `templates/review.html.j2` |

### Classification Values

Each detected change is classified into one of these controlled values:

| Classification | Description |
|---|---|
| `first_frame` | The very first frame captured from the video |
| `erp_change` | A standard ERP process step change |
| `erp_dialog` | A dialog or popup appeared (OCR contains dialog-related keywords) |
| `erp_tab_change` | A tab navigation occurred (OCR contains tab-related keywords) |
| `non_process_ui_change` | A UI change that is not part of the ERP workflow (e.g. Teams chat/people panel open) |
| `unclear` | Could not be determined |

When the layout is `chat_open` or `people_open`, the change is automatically classified as `non_process_ui_change` with `needs_review = true` and a review reason explaining that a Teams panel was detected.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Visualising Layout ROIs

Use the included test utility to verify that the crop rectangles align with your screen recording:

```powershell
python tests\test_erp_section.py output\screenshots\0001_00-00-00.png
```

This draws a semi-transparent overlay for each layout's ERP crop area and saves the visualisations to `output\tests\`.
