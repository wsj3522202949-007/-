---
id: tool-05611
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Based-Skin-Disease-Classification-System-
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ffightik/ai-based-skin-disease-classification-system-
created: 2026-07-18
updated: 2026-07-18
no: 5611
category: 一、去 AI 味 / Humanizer 库
repo: Ffightik/AI-Based-Skin-Disease-Classification-System-
stars: 1
url: https://github.com/ffightik/ai-based-skin-disease-classification-system-
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 9cc0ce96b96aed0f
  - methods/改稿润色指令库.md
---

# Ffightik/AI-Based-Skin-Disease-Classification-System-

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ffightik/ai-based-skin-disease-classification-system-
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：cuda, deep-learning, efficientnet, grad-cam, gradio, skin-cancer-classification, skin-cancer-detection
- **GitHub 描述**：AI-powered skin lesion classifier: EfficientNet-B4 trained on HAM10000 (7 classes), MobileNetV3 skin detector, Grad-CAM visual explanations, GPT-4o-mini diagnosis text, Gradio web UI. Bachelor's thesis in Biomedical Engineering.
- **本地描述**：AI-powered skin lesion classifier: EfficientNet-B4 trained on HAM10000 (7 classes), MobileNetV3 skin detector, Grad-CAM visual explanations, GPT-4o-mini diagnosis text, Gradio web UI. Bachelor's thesis in Biomedical Engineering.
- **拉取时间**：2026-07-25 18:25:06

---

# 🔬 DermAI Detector

<div align="center">

**AI-powered skin lesion classification — EfficientNet-B4 · Grad-CAM · GPT-4o-mini**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org)
[![Gradio](https://img.shields.io/badge/Gradio-4.x-FF7C00?style=flat)](https://gradio.app)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat)](LICENSE)

> ⚠️ **Not a medical device.** For research and educational purposes only.  
> Always consult a qualified dermatologist for any skin condition.

</div>

---
# Overview

This project presents a deep learning–based system for automatic skin lesion analysis using dermatoscopic images. The primary objective of the work is early skin cancer detection through artificial intelligence methods and explainable deep learning techniques.

The system was developed as a bachelor research project in Biomedical Engineering and focuses on automated classification of skin lesions using convolutional neural networks. The proposed pipeline combines image preprocessing, lesion classification, explainable AI visualization, and natural language explanation generation.

The project uses dermatoscopic images from the HAM10000 dataset and implements a two-stage diagnostic pipeline consisting of:

1. Skin region detection  
2. Multi-class skin lesion classification

The system also integrates Grad-CAM visualization and GPT-generated explanations to improve interpretability and usability in medical applications.

---

# System Architecture

The developed pipeline consists of several sequential stages:

```text
Input Image
     ↓
Skin Detection (MobileNetV3)
     ↓
Lesion Classification (EfficientNet-B4)
     ↓
Grad-CAM Visualization
     ↓
GPT-based Explanation
     ↓
Interactive Gradio Interface
```

---

# Dataset

The project uses the HAM10000 dermatoscopic image dataset.

### Dataset Information

| Property | Value |
|---|---|
| Dataset | HAM10000 |
| Images | 10,015 |
| Classes | 7 |
| Image Type | Dermatoscopic |
| Task | Multi-class classification |

### Diagnostic Classes

- Melanoma (mel)
- Melanocytic nevus (nv)
- Basal cell carcinoma (bcc)
- Benign keratosis (bkl)
- Actinic keratosis (akiec)
- Dermatofibroma (df)
- Vascular lesion (vasc)

---

# Deep Learning Models

## MobileNetV3-Small

MobileNetV3 was used as a lightweight binary classifier for detecting whether the uploaded image contains a valid skin region.

Advantages:
- Fast inference
- Low computational cost
- Suitable for real-time preprocessing

---

## EfficientNet-B4

EfficientNet-B4 was used as the primary multi-class classifier for skin lesion diagnosis.

The architecture was selected because of:
- High classification accuracy
- Efficient compound scaling
- Strong performance on medical imaging tasks

Training strategy:
- Transfer learning from ImageNet
- Fine-tuning with weighted loss
- Aggressive image augmentation

---

# Data Augmentation

To improve generalization and reduce overfitting, multiple augmentation techniques were applied:

- RandomResizedCrop
- Horizontal and vertical flips
- Random rotation
- Color jitter
- Affine transformations
- Random grayscale conversion

These transformations simulate real-world variability in dermatoscopic imaging conditions.

---

## Class Imbalance Handling

HAM10000 contains a strong class imbalance problem.

To address this issue, two balancing strategies were used simultaneously:

- WeightedRandomSampler
- Class-weighted CrossEntropyLoss

# Class Distribution 
![CL](https://github.com/Ffightik/AI-Based-Skin-Disease-Classification-System-/blob/main/Distr.png)


# Class Imbalance
![Imb](https://github.com/Ffightik/AI-Based-Skin-Disease-Classification-System-/blob/main/DataDisbalance.png)


This significantly improved minority class recognition performance.

---

# Explainable AI — Grad-CAM

Medical AI systems require interpretability.

To improve model transparency, Grad-CAM visualization was implemented. The method generates heatmaps showing which image regions most influenced the neural network decision.

This allows:
- Better understanding of model behavior
- Increased trust in predictions
- Visual verification of lesion focus regions

---

# GPT Integration

The system additionally integrates GPT-4o-mini to generate natural language explanations for classification results.

This functionality transforms raw predictions into more understandable descriptions for users and non-technical audiences.

---

# Interactive Interface

A web-based interface was developed using Gradio.

Features:
- Image upload
- Click-based ROI selection
- Real-time prediction
- Grad-CAM visualization
- AI-generated explanations

# Interface:
![Int](https://github.com/Ffightik/AI-Based-Skin-Disease-Classification-System-/blob/main/InterFace.png)


The interface was designed for ease of use and rapid interaction.

---

# Training Configuration

| Parameter | Value |
|---|---|
| Framework | PyTorch 2.0 |
| Python | 3.11 |
| GPU | NVIDIA RTX 4060 |
| Batch Size | 32 |
| Optimizer | AdamW |
| Learning Rate | 1e-4 |
| Scheduler | CosineAnnealingLR |
| Epochs | 15 |

---

# Results
# Confusion Metrics EfficientNet-B4
![Conf](https://github.com/Ffightik/AI-Based-Skin-Disease-Classification-System-/blob/main/Confusion.png)

# F1 Score Metrics 
![f1](https://github.com/Ffightik/AI-Based-Skin-Disease-Classification-System-/blob/main/F1Score.png)

The trained EfficientNet-B4 classifier achieved strong performance on HAM10000.

### Key Observations

- Highest performance achieved for the nevus class
- Strong ROC-AUC values across multiple categories
- Good robustness to noisy dermatoscopic images
- Stable validation performance without severe overfitting

---


# Repository Structure

```text
src/
    train_classifier.py
    train_skin_detector.py
    gradcam.py
    inference.py
    app.py

models/
    efficientnet_b4.pth
    mobilenet_skin_detector.pth

notebooks/
    experiments.ipynb

results/
    confusion_matrix.png
    roc_curve.png
    gradcam_examples/

dataset/
    HAM10000/
```

---


# Research Contribution

This project demonstrates the practical application of deep learning and explainable AI for medical image analysis.

The proposed system:
- Automates preliminary skin lesion screening
- Reduces dependence on manual inspection
- Improves interpretability of AI decisions
- Provides an accessible user interface for interaction

The work highlights the potential of AI-assisted diagnostic systems in dermatology and computational medicine.

---

## Tech stack

| Layer | Technology |
|-------|-----------|
| Deep learning | PyTorch 2.0 |
| Model zoo | timm (EfficientNet-B4, MobileNetV3-Small) |
| Explainability | Grad-CAM via PyTorch autograd hooks |
| Web UI | Gradio 4.x |
| LLM | OpenAI GPT-4o-mini |
| Image processing | OpenCV, Pillow |
| ML utilities | scikit-learn, numpy, pandas |

---

# Future Improvements

Potential future directions include:

- Larger clinical datasets
- Better melanoma sensitivity
- Ensemble architectures
- Segmentation-based preprocessing
- Vision Transformers
- Clinical metadata integration
- Mobile deployment

---
## References

1. Tschandl P. et al. — [HAM10000 dataset](https://doi.org/10.1038/sdata.2018.161), *Scientific Data*, 2018
2. Tan M., Le Q.V. — [EfficientNet: Rethinking Model Scaling](https://proceedings.mlr.press/v97/tan19a.html), *ICML*, 2019
3. Selvaraju R.R. et al. — [Grad-CAM](https://doi.org/10.1109/ICCV.2017.74), *ICCV*, 2017
4. Howard A. et al. — [Searching for MobileNetV3](https://doi.org/10.1109/ICCV.2019.00140), *ICCV*, 2019
5. Esteva A. et al. — [Dermatologist-level classification](https://doi.org/10.1038/nature21056), *Nature*, 2017

---
# Authors

| Name | Role | Contact |
|---|---|---|
| Nataliia Nechyporenko | Biomedical Engineering Student | [LinkedIn](https://www.linkedin.com/in/nataliia-nechyporenko-b05351362/) |
| Dr. Agata Sage | Supervisor | [LinkedIn](https://www.linkedin.com/in/agata-sage-260a8b264/) |
| MSc. Anna Slian | Research Support | [LinkedIn](https://www.linkedin.com/in/anna-slian/) |
| Prof. Dmitriy Losikhin | Scientific Supervisor | [ORCID](https://orcid.org/0000-0002-6325-7263) |

---

## License

MIT License — free for research and educational use.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<div align="center">
<sub>Bachelor's thesis · Biomedical Engineering · 2025</sub>
</div>
