---
id: tool-05136
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/tranhoainam197/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5136
category: 一、去 AI 味 / Humanizer 库
repo: Tranhoainam197/ai-text-detector
stars: 0
url: https://github.com/tranhoainam197/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Tranhoainam197/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/tranhoainam197/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Hệ thống phát hiện văn bản AI
- **本地描述**：Hệ thống phát hiện văn bản AI
- **拉取时间**：2026-07-25 18:07:28

---

# 🤖 AI Text Detector
### Hệ thống phát hiện văn bản do Trí tuệ nhân tạo (AI) tạo ra bằng phương pháp Stacking Ensemble

## 📖 Giới thiệu

AI Text Detector là một hệ thống hỗ trợ phát hiện và ước tính xác suất một văn bản được viết bởi **con người** hay được **tạo bởi các mô hình Trí tuệ nhân tạo (Large Language Models - LLMs)**.

Hệ thống được xây dựng dựa trên phương pháp **Stacking Ensemble Learning**, kết hợp nhiều tín hiệu ngôn ngữ khác nhau nhằm nâng cao độ chính xác trong quá trình phân loại.

Người dùng có thể:

- ✍️ Nhập trực tiếp văn bản cần kiểm tra.
- 📄 Tải lên các tài liệu:
  - TXT
  - DOCX
  - PDF
- 📊 Nhận kết quả dự đoán dưới dạng xác suất văn bản do AI hoặc con người tạo ra.
- 💡 Xem giải thích về kết quả dự đoán dựa trên các đặc trưng ngôn ngữ.

---

# 🚀 Tổng quan hệ thống

Hệ thống gồm hai thành phần chính:

## Backend

Được xây dựng bằng **FastAPI**.

Chức năng:

- Trích xuất nội dung từ văn bản hoặc tài liệu.
- Tính toán Perplexity bằng GPT-2.
- Trích xuất các Stylometric Features.
- Dự đoán bằng Gradient Boosting Classifier.
- Kết hợp kết quả bằng Logistic Regression (Stacking Ensemble).
- Trả kết quả thông qua REST API.

---

## Frontend

Được xây dựng bằng **React + Vite**.

Chức năng:

- Giao diện nhập văn bản.
- Upload tài liệu.
- Hiển thị kết quả dự đoán.
- Hiển thị giải thích kết quả.

---

# 🧠 Phương pháp sử dụng

Hệ thống áp dụng mô hình **Stacking Ensemble** gồm hai tầng.

### 1. Perplexity (GPT-2)

Đánh giá mức độ "bối rối" của mô hình GPT-2 khi đọc văn bản.

- Perplexity thấp → văn bản có xu hướng do AI tạo.
- Perplexity cao → văn bản có xu hướng do con người viết.

---

### 2. Stylometric Features

Trích xuất các đặc trưng phong cách viết như:

- Vocabulary Diversity
- Function Word Ratio
- Sentence Length Variance
- Average Sentence Length
- Average Word Length
- Punctuation Density
- Lexical Density

---

### 3. Gradient Boosting Classifier

Huấn luyện mô hình học máy dựa trên các đặc trưng Stylometric.

---

### 4. Logistic Regression Meta-Learner

Kết hợp:

- Perplexity
- Burstiness
- Xác suất từ Gradient Boosting

để đưa ra kết quả cuối cùng.

---

### 5. Explainable AI

Sinh lời giải thích giúp người dùng hiểu lý do hệ thống đưa ra kết quả dự đoán.

---

# 📁 Cấu trúc dự án

```text
AI-TEXT-DETECTOR/
│
├── backend/
│   ├── data/
│   │   ├── build_dataset.py
│   │   └── dataset.csv
│   │
│   ├── detector/
│   │   ├── classifier.py
│   │   ├── ensemble.py
│   │   ├── explainer.py
│   │   ├── extractors.py
│   │   ├── features.py
│   │   ├── perplexity.py
│   │   ├── train_classifier.py
│   │   └── train_ensemble.py
│   │
│   ├── models/
│   │   ├── classifier.pkl
│   │   └── ensemble.pkl
│   │
│   └── main.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# ⚙️ Yêu cầu hệ thống

### Backend

- Python 3.10 hoặc mới hơn

### Frontend

- Node.js 18 hoặc mới hơn
- npm

---

# 🛠 Cài đặt dự án

## 1. Clone repository

```bash
git clone https://github.com/Tranhoainam197/ai-text-detector.git

cd ai-text-detector
```

---

## 2. Cài đặt Backend

Di chuyển vào thư mục backend

```bash
cd backend
```

Tạo môi trường ảo

```bash
python -m venv venv
```

Kích hoạt môi trường

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Cài đặt thư viện

```bash
pip install -r ../requirements.txt
```

---

## 3. Cài đặt NLTK

Chỉ cần thực hiện một lần

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
```

---

# 🧠 Huấn luyện mô hình

Nếu chưa có các file mô hình (`classifier.pkl`, `ensemble.pkl`), hãy thực hiện:

Huấn luyện Gradient Boosting

```bash
python detector/train_classifier.py
```

Huấn luyện Stacking Ensemble

```bash
python detector/train_ensemble.py
```

Sau khi hoàn thành sẽ sinh ra:

```
backend/models/classifier.pkl

backend/models/ensemble.pkl
```

---

# ▶️ Chạy Backend

Từ thư mục **backend**

```bash
uvicorn main:app --reload 
```

Server sẽ chạy tại:

```
http://localhost:8000
```

Swagger API:

```
http://localhost:8000/docs
```

---

# 🌐 Chạy Frontend

Mở một Terminal mới.

Di chuyển vào thư mục frontend

```bash
cd frontend
```

Cài đặt các package

```bash
npm install
```

Khởi chạy ứng dụng

```bash
npm run dev
```

Frontend sẽ chạy tại:

```
http://localhost:5173
```

---

# 🛠 Công nghệ sử dụng

## Backend

- Python
- FastAPI
- Transformers (GPT-2)
- PyTorch
- Scikit-learn
- NLTK
- Joblib

## Frontend

- React
- Vite
- JavaScript
- HTML
- CSS

---

# 📌 Lưu ý

- Lần đầu chạy, mô hình GPT-2 sẽ được tải về nên có thể mất vài phút.
- Hiệu suất xử lý sẽ nhanh hơn khi sử dụng GPU.
- Hệ thống chỉ đưa ra xác suất dự đoán và không đảm bảo độ chính xác tuyệt đối đối với mọi loại văn bản.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# 👨‍💻 Tác giả

**Trần Hoài Nam**

GitHub: https://github.com/Tranhoainam197

Link: https://github.com/Tranhoainam197/ai-text-detector
