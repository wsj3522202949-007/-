---
id: tool-07334
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 本地写作]
title: genai_poetry
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/jgarnicaa/genai_poetry
created: 2026-07-18
updated: 2026-07-18
no: 7334
category: 画龙补充 / 扩容入库 — 补充源
repo: jgarnicaa/genai_poetry
stars: 0
url: https://github.com/jgarnicaa/genai_poetry
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: b2f5a14a191a5d89
  - methods/QUICK_START.md
---

# jgarnicaa/genai_poetry

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/jgarnicaa/genai_poetry
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：GenAI NLP for poetry in Spanish and English. Deployment in webapp through AWS:
- **本地描述**：genai_poetry
- **拉取时间**：2026-07-25 19:18:13

related:
  - methods/QUICK_START.md
---

# GenAI Poetry - AI-Powered Poetry Generator

## 📌 Project Overview
GenAI Poetry is an AI-powered poetry generator capable of creating poems in **English and Spanish**. The model was fine-tuned from **GPT-2** to specialize in poetry generation, ensuring coherent and creative outputs. The application consists of a **backend** (FastAPI) handling the model inference and a **frontend** (Streamlit) providing an interactive web interface.

## 🚀 Project Structure
The repository contains the following directories:

- **`webapp/backend/`** - Contains the FastAPI backend, including model inference logic and API endpoints.
- **`webapp/frontend/`** - Contains the Streamlit web interface for user interaction.
- **`webapp/`** - Main folder for deployment, containing backend, frontend, and Docker configuration.
- **`webapp/backend/model/`** - Stores the fine-tuned GPT-2 model (must be downloaded separately).
- **`data/`** - Includes datasets used for training the model.
- **`docs/`** - Documentation and architecture diagrams.
- **`src/`** - Files of EDA and Training model

## 🛠️ Running the Project Locally
### **Prerequisites**
Ensure you have the following installed:
- **Python 3.8+**
- **Docker & Docker Compose**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/jgarnicaa/GenAI_Poetry.git
cd GenAI_Poetry
```

### **2️⃣ Download the Model**
Download the fine-tuned GPT-2 model and place it in `webapp/backend/model/`:
```bash
wget -P webapp/backend/ https://genaipoetry-bucket.s3.eu-west-3.amazonaws.com/model/
```

### **3️⃣ Run the Application**
Start the application using Docker Compose:
```bash
cd webapp
docker-compose up --build -d
```

### **4️⃣ Access the Web Interface**
Once running, access the poetry generator at:
```bash
http://0.0.0.0:8501
```

## 🌍 Accessing the Live Version on AWS EC2
If deployed on an AWS EC2 instance, access the application using the public IP:
```bash
http://13.39.47.61:8501
```

Ensure that the EC2 security group allows inbound traffic on port **8501**.

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it!

## 🤝 Contributing
Contributions are welcome! Fork the repo and submit a pull request with improvements.

## 📧 Contact
For questions or collaborations, contact **Eduardo Garnica** via GitHub.


