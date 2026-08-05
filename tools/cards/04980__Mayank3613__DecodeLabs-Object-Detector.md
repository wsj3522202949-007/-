---
id: tool-04980
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: DecodeLabs-Object-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/mayank3613/decodelabs-object-detector
created: 2026-07-18
updated: 2026-07-18
no: 4980
category: 一、去 AI 味 / Humanizer 库
repo: Mayank3613/DecodeLabs-Object-Detector
stars: 0
url: https://github.com/mayank3613/decodelabs-object-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Mayank3613/DecodeLabs-Object-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mayank3613/decodelabs-object-detector
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：mplement a basic image or text recognition task using existing pre-trained AI libraries
- **本地描述**：mplement a basic image or text recognition task using existing pre-trained AI libraries
- **拉取时间**：2026-07-25 18:01:44

---

# 👁️ DecodeLabs Object Detector

**Building the Machine's Optic Nerve** — A Python-based object detection pipeline using OpenCV's DNN module with a pre-trained MobileNet-SSD model. The system ingests raw images, applies a multi-stage pre-processing pipeline, runs forward inference through a deep neural network, and outputs annotated images with labeled bounding boxes for detected objects.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-green?logo=opencv&logoColor=white)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](test_detector.py)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Pipeline Architecture](#pipeline-architecture)
- [Pre-Processing Pipeline](#pre-processing-pipeline)
- [Model Architecture](#model-architecture)
- [Detectable Object Classes](#detectable-object-classes)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Technical Concepts](#technical-concepts)
- [Contributing](#contributing)
- [License](#license)

---

## 🔭 Overview

This project implements **Path 2: Object Detection** from the DecodeLabs curriculum — transitioning from structured data to **unstructured visual data**. It demonstrates:

- **Transfer Learning**: Loading a pre-trained MobileNet-SSD Caffe model trained on the PASCAL VOC dataset.
- **Image Pre-Processing**: Grayscale conversion, Gaussian blur, and Otsu's adaptive thresholding.
- **4D Blob Construction**: Transforming raw images into DNN-compatible tensors via `cv2.dnn.blobFromImage()`.
- **Confidence Gating**: An 80% threshold that filters out false positive detections.
- **Bounding Box Visualization**: Annotated output images with labeled rectangles and confidence scores.

---

## 🏗️ Pipeline Architecture

```
                        ┌──────────────────────┐
                        │    Raw Input Image    │
                        └──────────┬───────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   Pre-Processing Pipeline    │
                    │  ┌────────────────────────┐  │
                    │  │  1. Grayscale Convert   │  │
                    │  │  2. Gaussian Blur (5x5) │  │
                    │  │  3. Otsu's Threshold    │  │
                    │  └────────────────────────┘  │
                    └──────────────┬───────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   4D Blob Construction       │
                    │   cv2.dnn.blobFromImage()    │
                    │   300x300 | Scale: 0.007843  │
                    │   Mean Subtraction: 127.5    │
                    └──────────────┬───────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   MobileNet-SSD Forward Pass │
                    │   (Caffe DNN Inference)       │
                    └──────────────┬───────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   Confidence Gate (≥ 80%)     │
                    │   Filter false positives      │
                    └──────────────┬───────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   Bounding Box Extraction     │
                    │   Scale to original dims      │
                    │   Clamp to image bounds       │
                    └──────────────┬───────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   Annotated Output Image      │
                    │   Labeled boxes + confidence   │
                    └──────────────────────────────┘
```

---

## 🔬 Pre-Processing Pipeline

The pre-processing pipeline transforms raw visual data through three stages to demonstrate image manipulation fundamentals:

| Stage | Operation | Purpose |
|-------|-----------|---------|
| **1** | Grayscale Conversion | Collapse 3-channel BGR matrix to single-channel intensity values |
| **2** | Gaussian Blur (5×5) | Eliminate high-frequency noise using a weighted kernel convolution |
| **3** | Otsu's Thresholding | Automatically compute optimal threshold to create binary contrast |

> **Note**: While the DNN model operates on the original BGR image (via blob construction), the pre-processing pipeline is implemented separately to demonstrate classical computer vision techniques and can be visualized independently using the `preprocess` command.

---

## 🧠 Model Architecture

**MobileNet-SSD** combines two powerful architectures:

- **MobileNet**: A lightweight, efficient feature extractor using depthwise separable convolutions. Designed for mobile and embedded vision applications.
- **SSD (Single Shot MultiBox Detector)**: A detection framework that predicts bounding boxes and class scores in a single forward pass — no region proposal step needed.

The model was pre-trained on the **PASCAL VOC dataset** and loaded via OpenCV's `cv2.dnn.readNetFromCaffe()` for transfer learning.

---

## 🏷️ Detectable Object Classes

The MobileNet-SSD model is trained on 20 object categories from the PASCAL VOC dataset:

| Category | Classes |
|----------|---------|
| **Vehicles** | Aeroplane, Bicycle, Boat, Bus, Car, Motorbike, Train |
| **Animals** | Bird, Cat, Cow, Dog, Horse, Sheep |
| **People** | Person |
| **Indoor** | Bottle, Chair, Dining Table, Potted Plant, Sofa, TV/Monitor |

---

## 📁 Project Structure

```
DecodeLabs-Object-Detector/
├── detector.py              # Core detection engine (ObjectDetector class)
├── main.py                  # Interactive CLI entry point
├── test_detector.py         # Pytest suite (4 milestone validations)
├── requirements.txt         # Python dependencies
├── models/
│   ├── deploy.prototxt      # MobileNet-SSD network architecture
│   └── mobilenet_iter_73000.caffemodel  # Pre-trained weights
├── images/
│   ├── sample_test.jpg      # Sample test image
│   └── empty_scene.jpg      # Edge case: empty scene
├── output/                  # Annotated output images (auto-created)
├── LICENSE                  # MIT License
├── CODE_OF_CONDUCT.md       # Community guidelines
├── CONTRIBUTING.md          # Contribution guidelines
├── SECURITY.md              # Security policy
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Steps

```bash
# Clone the repository
git clone https://github.com/Mayank3613/DecodeLabs-Object-Detector.git
cd DecodeLabs-Object-Detector

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

> **Note**: The pre-trained model files (`models/deploy.prototxt` and `models/mobilenet_iter_73000.caffemodel`) are included in the repository and downloaded automatically during setup.

---

## 🚀 Usage

### Interactive Mode

```bash
python main.py
```

This launches an interactive CLI where you can:
- Enter an image path to detect objects
- Use `preprocess <path>` to view pre-processing pipeline output
- Type `exit` or `quit` to end the session

### Example Session

```
  ╔══════════════════════════════════════════╗
  ║    Object Detection AI Pipeline 👁️       ║
  ║    Model: MobileNet-SSD (Caffe)          ║
  ║    Confidence Gate: ≥ 80%                ║
  ╚══════════════════════════════════════════╝

  Image path (or command) > images/sample_test.jpg

  Processing: images/sample_test.jpg (640x480 px)

  🎯 Detected 2 Object(s):
  ────────────────────────────────────────────────────────
  #    Class              Confidence     Bounding Box (X,Y,W,H)
  ────────────────────────────────────────────────────────
  1    person             92.34%         (95, 78, 110, 325)
  2    car                87.12%         (345, 235, 240, 150)
  ────────────────────────────────────────────────────────

  Annotated output saved: output/sample_test_detected.jpg
```

### Direct Module Usage

```python
from detector import ObjectDetector
import cv2

detector = ObjectDetector(confidence_threshold=0.80)
detector.load_model()

image = cv2.imread("your_image.jpg")
detections = detector.detect(image)

for det in detections:
    print(f"{det['label']}: {det['confidence']:.2%} at {det['bbox']}")

annotated = detector.annotate_image(image, detections)
cv2.imwrite("output.jpg", annotated)
```

---

## 🧪 Testing

The test suite validates all four project milestones:

```bash
# Run full test suite
pytest test_detector.py -v
```

### Test Categories

| Milestone | Category | Tests | Description |
|-----------|----------|-------|-------------|
| **1** | Library Integration | 5 | Model loads, files exist, error handling |
| **2** | Pre-Processing Integrity | 6 | Grayscale, blur, threshold output validation |
| **3** | Accuracy Benchmarking | 5 | Confidence gate, label validity, result structure |
| **4** | Visual Confirmation | 5 | Bounding box bounds, annotation integrity |

---

## 📖 Technical Concepts

### Transfer Learning
Instead of training a model from scratch (requiring massive datasets and compute), we load a pre-trained MobileNet-SSD model. This is called **transfer learning** — reusing knowledge learned from one task (VOC object detection) and applying it to new images.

### 4D Blob Construction
`cv2.dnn.blobFromImage()` converts an image into a 4-dimensional tensor `[batch, channels, height, width]` suitable for neural network input. The function handles resizing (300×300), mean subtraction (127.5), and scaling (0.007843).

### Confidence Gating
Raw neural network outputs include many low-confidence "ghost" detections. The **80% confidence threshold** acts as a quality gate, ensuring only reliable detections pass through to the output.

### Otsu's Thresholding
A histogram-based method that automatically determines the optimal threshold value by minimizing intra-class variance. This produces clean binary segmentation without manual tuning.

---

## 🤝 Contributing

Contributions are welcome! Please read the [Contributing Guide](CONTRIBUTING.md) for details on the process for submitting pull requests.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 👤 Author

- **Mayank3613** — [GitHub Profile](https://github.com/Mayank3613)
