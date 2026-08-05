---
id: tool-07147
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 本地写作]
title: layout-recognition-yolov8
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/ashishraj97/layout-recognition-yolov8
created: 2026-07-18
updated: 2026-07-18
no: 7147
category: 画龙补充 / 扩容入库 — 补充源
repo: ashishraj97/layout-recognition-yolov8
stars: 2
url: https://github.com/ashishraj97/layout-recognition-yolov8
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
  - methods/QUICK_START.md
---

# ashishraj97/layout-recognition-yolov8

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/ashishraj97/layout-recognition-yolov8
- **Stars**：2
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：layout-recognition-yolov8
- **拉取时间**：2026-07-25 19:12:17

---

## 📝 YOLOv8 Layout Recognition for Historical Documents  

This project is part of the RenAIssance Test I (Layout Organization Recognition). The goal is to develop a model that detects and segments the main text regions in scanned early modern printed sources, while ignoring embellishments like marginalia and decorations.
This project utilizes **YOLOv8** for **Layout Organization Recognition** in **historical scanned documents**.  
The model detects **text regions**, including **headings, main text, authors, and drop caps**, while ignoring embellishments. 

---

### 🚀 Features  

✔ **Dataset:** Custom dataset of historical document images, manually annotated for text regions.  
✔ **Model:** **YOLOv8m**, fine-tuned with custom **augmentation** & **hyperparameters**.  
✔ **Training:** **180 epochs**, optimized learning rate, batch size, and augmentation techniques.  
✔ **Evaluation:** Precision, Recall, **mAP@0.5**, **mAP@0.5:0.95**, and **training loss analysis**, IoU, and F1-score.  
✔ **Inference:** Predicts layouts on **new document images** and **saves** structured outputs.  
✔ **Visualization:** Training loss, **mAP trends, Precision-Recall curves, and Confusion Matrix**.  

---

### 📜 Dataset & Preprocessing

- Dataset: The dataset consists of 6 scanned early modern printed sources.
- Preprocessing: The PDFs were converted to images and annotated in Roboflow to label only the main text regions. The dataset was then exported in YOLOv8 format for training.
- Challenges: Variability in text layout, marginalia, and embellishments required precise annotation.

📥 **Download Dataset & YOLO Results:**  
- 📁 [Dataset (Train, Test, Valid)](https://drive.google.com/drive/folders/1tvZZfsfFHPlLx26hQEDGcEnAJ6h9g0wm?usp=drive_link)  
- 📁 [YOLO Results (Trained Weights & Predictions)](https://drive.google.com/drive/folders/1hjbZ72TodFKLEgVIRXIIpPbUUwb7eqom?usp=drive_link)

---

### 🎯 Model Selection & Training Details

🔹**Why YOLOv8?**
  - YOLOv8 offers high-speed object detection and performs well on small datasets.
  - The model is lightweight yet powerful for text region detection in historical documents.

🔹 **Training Setup:**
  - Model: YOLOv8m
  - Optimizer: AdamW
  - Batch Size: 16
  - Epochs: 180
  - Learning Rate: 0.001
  - Augmentations: Rotation, Contrast Adjustments, Shearing, Perspective Transformations
  - Confidence Threshold & IoU: Tuned for better text region segmentation

🔹 **Model Selection: Why YOLOv8 over Transformers?**
- The RenAIssance Project suggests using convolutional-recurrent, transformer-based, or self-supervised models. While transformer-based models like LayoutLM or Swin Transformer are effective for structured document parsing, they are computationally expensive and require larger datasets.
- Instead, YOLOv8m, a convolutional model, was chosen due to:
    - ✔ Efficient object detection, suitable for layout recognition in small datasets.
    - ✔ Fast inference speed, crucial for historical document processing.
    - ✔ Ability to detect localized text regions without needing OCR integration.
For future iterations, I aim to experiment with Vision Transformer (ViT)-based YOLO variants to improve performance further.

|Model	            |   Speed	 |   Accuracy  	|Computational Cost       |  Text Region Suitability       |
|-------------------|----------|--------------|-------------------------|--------------------------------|
|YOLOv8	            |⚡ Fast	 |✅ High	    |  💰 Low	                |🏆 Best for small datasets      |
|LayoutLM	          |🐢 Slow	 |✅ High	    |💰💰 Expensive	        |👍 Good for structured layouts  |  
|Swin Transformer	  |🐢 Slow	 |🔥 Very High	|💰💰💰 Very Expensive	  |✅ Strong but needs large data  |

---

### 🎯 Model Performance  

📌 **Final Evaluation Metrics:**  

| **Metric**    | **Value**  |
|--------------|-----------|
| Precision    | 85.4%     |
| Recall       | 86.3%     |
| mAP@0.5      | 91.2%     |
| mAP@0.5:0.95 | 75.9%     |
| F1-Score     | 85.8%     |

🔹 **Why These Metrics?**
- Since layout recognition requires precise text region detection while ignoring embellishments, we use Precision, Recall, and F1-score to measure detection accuracy and balance between false positives and false negatives. mAP@0.5 and mAP@0.5:0.95 ensure robustness across different localization overlaps.

📌 **Evaluation Metrics:**
- **Precision (85.4%):** Measures the percentage of correctly detected text regions among all detected regions. A high precision ensures that the model minimizes false positives (incorrectly detecting embellishments or margins as text).
- **Recall (86.3%):** Represents how many actual text regions were correctly detected. A high recall means the model effectively captures most text areas, reducing false negatives (missed text regions).
- **mAP@0.5 (91.2%):** Measures detection accuracy with a 50% IoU threshold, evaluating how well the model identifies text regions. A high score means strong localization performance.
- **mAP@0.5:0.95 (75.9%):** A more stringent metric that averages mAP across multiple IoU thresholds (from 0.5 to 0.95), testing the model’s robustness. A score of 75.9% suggests that the model maintains reliable detection across varying levels of overlap.
- **F1-score (85.8%):** A balance between Precision & Recall, useful for layout recognition where both false positives (wrong elements detected as text) and false negatives (missed text regions) need to be minimized.
- **IoU (Intersection over Union):** Measures how well predicted text regions overlap with ground truth annotations. A higher IoU ensures more accurate text localization.

📊 **Training Loss & mAP Trends Over Epochs:**  

![download](https://github.com/user-attachments/assets/82e2b6ef-e2c8-4684-9735-b0061bd7f2b2)

📈 **Precision-Recall Curve:**  

![download](https://github.com/user-attachments/assets/e3e92478-d896-4f30-a716-0806564cf981)

✅ Successful Layout Recognition:

![d2869d59-2563-4794-80c4-a8d21063e2c1](https://github.com/user-attachments/assets/7aa4ef01-18a2-46fc-96cb-8b542b2b54f2)

📥 To view all graphs and predicted images, check the **Predicted Images and Curves** folder in the repository.

---

### 🚀 Observations  
✔ **Good model convergence** with minimal overfitting.  
✔ **Improved recall & precision**, enhancing layout recognition accuracy.  
✔ **Strong detection** of main text and drop caps, with minor misclassifications in headings and author labels.  
✔ **mAP@0.5 = 91.2%** and **mAP@0.5:0.95 = 75.9%**, indicating reliable detection but scope for layout refinement.  

---

### 🔄 Next Steps for Improvement  
✔ **Expand dataset** (current: 52 images) and add more text variations.  
✔ **Apply stronger augmentations** (rotation, shearing, perspective) to improve generalization.  
✔ **Fine-tune confidence threshold & IoU ** for better text region segmentation.  
✔ **Experiment with YOLOv8L or YOLOv8X** for improved feature extraction.  
✔ **Implement OCR post-processing** to assess text extraction accuracy.  
✔ **Optimize heading recognition & threshold settings** for enhanced classification. 

---

### ⚙️ Requirements  

- **Python 3.7+**
- **GPU (Recommended): A Tesla T4 (used in Colab) or any NVIDIA GPU with at least 8GB VRAM for faster training.**  
- **Ultralytics YOLOv8**  
- **PyTorch, Pandas, Matplotlib, Pillow (PIL)**

---

### 🚀 Installation  

#### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/AshishRaj97/Layout-Recognition-YOLOv8.git
```
#### 2️⃣ Install Required Packages
```bash
pip install ultralytics
pip install torch
pip install pandas matplotlib pillow
```
related:
  - methods/QUICK_START.md
---

### 📜 License  
This project is licensed under the **MIT License**. See the `[LICENSE](LICENSE)` file for details.  

### 👨‍💻 Author  
📌 **Ashish Raj**  
📧 [ar469492@gmail.com] | 🖥️ [Your GitHub](https://github.com/your-username)  

🔹 If you find this project useful, give it a ⭐ on GitHub! 🚀  
