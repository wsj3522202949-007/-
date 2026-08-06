---
id: tool-07490
type: tool
area: 库
status: active
tags: [文风迁移, Python, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: handoc-orderocr
summary: 风格微调/文风迁移
source: https://github.com/polo-marco/handoc-orderocr
created: 2026-07-18
updated: 2026-07-18
no: 7490
category: 画龙补充 / 扩容入库 — 补充源
repo: polo-marco/handoc-orderocr
stars: 4
url: https://github.com/polo-marco/handoc-orderocr
tier: "B"
use_case: "风格微调/文风迁移"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# polo-marco/handoc-orderocr

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/polo-marco/handoc-orderocr
- **Stars**：4
- **语言**：Python
- **License**：None
- **Topics**：chinese, historical-documents, ocr
- **GitHub 描述**：This project offers an advanced Optical Character Recognition (OCR) solution specialized for Chinese historical documents, uniquely addressing complex layouts and reading orders. 
- **本地描述**：handoc-orderocr
- **拉取时间**：2026-07-25 19:23:29

---

# OCR System for Chinese Historical Documents with Image-Based Reading Order Detection

**Author:** Hsing-Yuan Ma
**Affiliation:** National Chengchi University
**Contact:** [hsingyuanma@gmail.com](mailto:hsingyuanma@gmail.com)

---

## 🚀 Project Overview [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Pzalb0VztHhWkvbc0xuCZ-4PQDJT7-Dt?usp=sharing)

This project offers an advanced Optical Character Recognition (OCR) solution specialized for **Chinese historical documents**, uniquely addressing complex layouts and reading orders. It employs state-of-the-art methods for text detection and recognition and introduces an innovative approach for image-based reading order detection, significantly improving the accuracy and usability of digitized historical texts. You can try it with google Colab!

## 🚀 System Demo

To see the system in action, check out the [demo video](https://www.youtube.com/watch?v=RWgGDymY2Bc) and screenshot below!


![sys_demo](https://github.com/polo-marco/handoc-orderocr/blob/main/assets/system_demo.png)


## 🖼️ Sample Output

Input image:

![input](https://github.com/polo-marco/handoc-orderocr/blob/main/assets/example_1.jpg)

Output with detected text, recognition results, and reading order:

![output](https://github.com/polo-marco/handoc-orderocr/blob/main/assets/example_1_result.png)
---

## 🏆 Key Features

* **Text Detection:** Leveraging Differential Binarization++ (DB++)
* **Text Recognition:** High accuracy with SVTR Net
* **Reading Order Detection:** CNN-based approach combining visual and spatial information, utilizing the "First Decide then Decode" (FDTD) algorithm
* **Visualized Outputs:** Interactive annotations with bounding boxes, recognized texts, and reading order indicators
* **Dockerized Deployment:** Easily deployable using Docker and accessible via a modern Gradio interface

---

## 📚 System Pipeline

1. **Input:** Upload historical document images.
2. **Text Detection:** Segments text regions using DB++.
3. **Text Recognition:** Identifies text content using SVTR Net.
4. **Reading Order Detection:** Determines reading sequence using multimodal CNN model.
5. **Output:** Structured digital text with annotated visualizations.

---

## 🧑‍🔬 Model Training

* **Datasets:** MTHv2 (Tripitaka Koreana in Han, Multiple Tripitaka in Han; \~3,199 images)
* **Performance Metrics:**

  * **Text Detection:** F1 score = 0.95
  * **Text Recognition:** Accuracy = 0.83
  * **Reading Order Detection:** Page Error Rate of 5%, meaning that only 5% of pages contain any order prediction errors (i.e., at least one text box is placed in an incorrect sequence).

---

## 🛠️ Getting Started

### 📌 Requirements

* Docker
* CUDA-enabled GPU

### 🐳 Deployment Using Docker

#### 1. **Clone Repository**

```bash
git clone https://github.com/Polo-Marco/HanDoc-OrderOCR.git
cd HanDoc-OrderOCR
```

#### 2. **Build Docker Image**

```bash
docker build -t chinese-historical-ocr .
```

#### 3. **Run Docker Container**

```bash
docker run --gpus all --shm-size 4g -p 9999:9999 chinese-historical-ocr
```

### 🌐 Access the Application

* Open your browser at: `http://localhost:9999`

---

## 🏗️ Project Structure

```
.
├── app/                 # Main application code (main.py, pipeline, utils)
├── configs/             # Configuration files
├── scripts/             # Utility scripts
├── assets/              # Demo result
├── output/              # Output files and temporary data
├── VORO/                # Reading order detection module
├── dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
└── README.md
```

`models/` and `PaddleOCR/` directories are created automatically during setup.

---

## 📖 References

* **Paper:** [Reading between the Lines: Image-Based Order Detection in OCR for Chinese Historical Documents](https://ojs.aaai.org/index.php/AAAI/article/view/30572) *(Ma, Huang, Liu - AAAI 2024)*
* **Methods and Algorithms:**

  * DB++ *(Liao et al., 2022)*
  * SVTR Net *(Du et al., 2022)*
  * FDTD algorithm *(Quiros & Vidal, 2022)*

---

## 🙏 Acknowledgements

Supported by National Chengchi University and Academia Sinica. Thanks to the open-source OCR community.

---

## 📢 License

Copyright © 2024
Association for the Advancement of Artificial Intelligence (AAAI)
Open-source for academic and research use.

---

## ✨ Contact

For collaboration, deployment assistance, or inquiries, contact [hsingyuanma@gmail.com](mailto:hsingyuanma@gmail.com).

related:
  - methods/QUICK_START.md
---

*This project helps preserve and unlock the cultural heritage of Chinese manuscripts, making historical documents accessible for research and exploration.*
