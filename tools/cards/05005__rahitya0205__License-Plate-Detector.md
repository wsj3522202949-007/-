---
id: tool-05005
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: License-Plate-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/rahitya0205/license-plate-detector
created: 2026-07-18
updated: 2026-07-18
no: 5005
category: 一、去 AI 味 / Humanizer 库
repo: rahitya0205/License-Plate-Detector
stars: 0
url: https://github.com/rahitya0205/license-plate-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# rahitya0205/License-Plate-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rahitya0205/license-plate-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered License Plate Recognition (ALPR) system built with YOLOv11 and EasyOCR. Features automated data logging to CSV with high-precision vehicle localization and text extraction.
- **本地描述**：AI-powered License Plate Recognition (ALPR) system built with YOLOv11 and EasyOCR. Features automated data logging to CSV with high-precision vehicle localization and text extraction.
- **拉取时间**：2026-07-25 18:02:39

---

# 🚗 Automated License Plate Recognition (ALPR)

An end-to-end **Automatic License Plate Recognition** system that detects vehicles in images, localizes their license plates using **YOLOv11**, and extracts alphanumeric text via **EasyOCR** — all logged to a structured CSV database.

---

## 🌟 Features

- **Real-time plate localization** — YOLOv11 detects vehicles and isolates license plate regions with high precision
- **OCR text extraction** — EasyOCR transcribes plate characters into clean alphanumeric strings
- **Automatic data logging** — detected plates and timestamps are appended to `plate_log.csv` for downstream use
- **Apple Silicon optimized** — leverages MPS (Metal Performance Shaders) for GPU-accelerated inference on MacBook Air

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.11+ |
| Object Detection | YOLOv11 (Ultralytics) |
| OCR | EasyOCR |
| Image Processing | OpenCV |
| Hardware Acceleration | Apple MPS (Metal) |
| Dev Environment | VS Code, Git |

---

## 📂 Project Structure

```
License-Plate-Detector/
├── main.py              # Core detection + OCR pipeline
├── test.jpg             # Sample test image
├── plate_log.csv        # Auto-generated detection log (created at runtime)
├── requirements.txt     # Python dependencies
└── .gitignore           # Excludes model weights and virtual environments
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/rahitya0205/License-Plate-Detector.git
cd License-Plate-Detector

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

Detected plates are printed to the console and saved to `plate_log.csv` with a timestamp.

---

## 📊 Output Format

`plate_log.csv` captures each detection in the following structure:

| timestamp | plate_text | confidence |
|---|---|---|
| 2024-11-01 14:32:01 | KA03MF1234 | 0.91 |

---

## ⚙️ Configuration

| Parameter | Location | Description |
|---|---|---|
| Input image path | `main.py` | Path to the image file for detection |
| Confidence threshold | `main.py` | Minimum detection confidence (default: 0.5) |
| Device (`cpu` / `mps`) | `main.py` | Inference hardware target |

---

## 🧠 How It Works

```
Input Image
    │
    ▼
YOLOv11 Detection ──► Bounding Box around license plate region
    │
    ▼
Crop & Preprocess ──► Isolated plate image
    │
    ▼
EasyOCR ──► Raw text string (e.g. "KA03MF1234")
    │
    ▼
plate_log.csv ──► Timestamped record saved
```

---

## 📦 Dependencies

```
ultralytics
easyocr
opencv-python
```

Install all with:

```bash
pip install -r requirements.txt
```

> **macOS note:** SSL certificates are handled automatically for model downloads. No manual intervention needed.

---

## 🔭 Roadmap

- [ ] Video stream / webcam support
- [ ] Multi-language plate recognition
- [ ] REST API endpoint (FastAPI)
- [ ] Web dashboard for viewing detection history

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🙋 Author

**Rahitya** — BCA Final Year, Seshadripuram Degree College  
[GitHub](https://github.com/rahitya0205) · [LinkedIn](https://www.linkedin.com/in/rahitya-a9542b328/)
