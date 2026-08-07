---
id: tool-05116
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: Same_file_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/huzaifaaidev/same_file_detector
created: 2026-07-18
updated: 2026-07-18
no: 5116
category: 一、去 AI 味 / Humanizer 库
repo: HuzaifaAIDev/Same_file_detector
stars: 1
url: https://github.com/huzaifaaidev/same_file_detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# HuzaifaAIDev/Same_file_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/huzaifaaidev/same_file_detector
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：ai, docker, document-analysis, document-processing, duplicate-detection, fastapi, file-comparison, jwt, ocr, pdf-processing, python, rest-api, tesseract, text-similarity
- **GitHub 描述**：AI-powered document similarity and duplicate file detection system using FastAPI, OCR, and fuzzy text matching.
- **本地描述**：AI-powered document similarity and duplicate file detection system using FastAPI, OCR, and fuzzy text matching.
- **拉取时间**：2026-07-25 18:06:43

---

# 🔍 Same File Detector

![Same File Detector Banner](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/banner.png)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![OCR](https://img.shields.io/badge/OCR-Tesseract-orange)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)
![Database](https://img.shields.io/badge/Database-SQLite%20%7C%20PostgreSQL-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)
![GitHub Stars](https://img.shields.io/github/stars/HuzaifaAIDev/Same_file_detector?style=social)

# 📄 Document Similarity & Duplicate File Detection System

**Same File Detector** is a document comparison platform designed to identify duplicate and similar documents using OCR extraction, text processing, and fuzzy similarity analysis.

The system allows users to upload:

* **BASE Files** → Reference documents
* **COMPARE Files** → Documents to analyze

and automatically classifies comparison results into:

* ✅ **EXACT** — Documents contain identical content
* ⚠️ **SIMILAR** — Documents contain highly matching content
* ❌ **DIFFERENT** — Documents have low similarity

The system supports multiple file formats:

* PDF
* DOCX
* XLSX
* PPTX
* TXT
* CSV
* JSON
* Images (OCR supported)

---

# ⭐ Support This Project

If you find this project useful, consider giving it a ⭐ star on GitHub.

Your support helps improve the project and motivates future development.

⭐ Star the repository:

https://github.com/HuzaifaAIDev/Same_file_detector

---

# ✨ Key Features

## 📂 Document Comparison Engine

* Upload multiple BASE and COMPARE documents
* Extract text from different file formats
* Compare document content automatically
* Generate similarity scores
* Classify documents as EXACT / SIMILAR / DIFFERENT
* Maintain comparison history

---

## 🔎 Intelligent Document Processing

The system provides:

* OCR extraction from images and scanned PDFs
* Text extraction from supported formats
* Fuzzy text similarity matching
* Content-based duplicate detection
* Automated document classification

---

# 🔐 Authentication & Security

Implemented security features:

* JWT authentication
* Secure password hashing using bcrypt
* Email OTP verification
* Password reset workflow
* Role-based access control
* Security headers middleware
* Rate limiting protection
* Input validation
* File upload validation
* Safe file handling

---

# 👨‍💼 Admin Features

Admin users can:

* Access admin dashboard
* Manage users
* Activate or suspend accounts
* Monitor user activity
* Access protected admin APIs

---

# 📸 Application Screenshots

## 🔐 Authentication

### Sign In

![Sign In](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/sign_in.jpg)

### Create Account

![Create Account](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/create_account.jpg)

### Email OTP Verification

![Verify Email](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/verify_email.jpg)

### Password Reset

![Reset Password](assets/reset_password.jpg)

---

# 👤 User Dashboard

### User Dashboard

![User Dashboard](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/user_dashboard_empty.jpg)

### Select Files For Comparison

![Selected Files](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/user_files_selected.jpg)

### Comparison Results

![Comparison Results](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/comparison_results.jpg)

---

# 👨‍💼 Admin Panel

### Admin Dashboard

![Admin Dashboard](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/admin_dashboard.jpg)

### User Management Light Theme

![Light Theme](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/admin_user_management_light.jpg)

### User Management Dark Theme

![Dark Theme](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/admin_user_management_dark.jpg)

---

# 📚 API Documentation

Built with FastAPI Swagger documentation.

### Swagger Overview

![Swagger Overview](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/api_docs_overview.jpg)

### Authentication, Admin & Compare APIs

![Auth Admin Compare](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/api_docs_auth_admin_compare.jpg)

### Compare API Interface

![Compare API](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/api_docs_admin_compare_ui.jpg)

### API Schemas

![Schemas](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/api_docs_schemas.jpg)

![Extended Schemas](https://github.com/HuzaifaAIDev/Same_file_detector/blob/main/assets/api_docs_schemas_extended.jpg)

---

# 🏗️ System Architecture

```
Same_file_detector/

│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── auth.py
│   │   │       ├── admin.py
│   │   │       ├── compare.py
│   │   │       ├── health.py
│   │   │       └── router.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   ├── validators.py
│   │   │   ├── exceptions.py
│   │   │   ├── logging_config.py
│   │   │   └── seed.py
│   │   │
│   │   ├── database/
│   │   │   └── session.py
│   │   │
│   │   ├── middleware/
│   │   │   ├── security_headers.py
│   │   │   └── rate_limit.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── otp.py
│   │   │   └── comparison.py
│   │   │
│   │   ├── repositories/
│   │   │   ├── user_repository.py
│   │   │   ├── otp_repository.py
│   │   │   └── comparison_repository.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   └── compare.py
│   │   │
│   │   ├── services/
│   │   │   ├── extraction_service.py
│   │   │   ├── comparison_service.py
│   │   │   ├── otp_service.py
│   │   │   └── email_service.py
│   │   │
│   │   ├── utils/
│   │   │   └── file_validation.py
│   │   │
│   │   └── main.py
│   │
│   ├── tests/
│   ├── uploads/
│   ├── logs/
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   └── .env.example
│
├── frontend/
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       │
│       └── js/
│           └── app.js
│
├── assets/
│   ├── banner.png
│   └── screenshots
│
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 🛠️ Technology Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication
* bcrypt

## Document Processing

* PyMuPDF
* Tesseract OCR
* Pillow
* RapidFuzz

## Frontend

* Jinja2 Templates
* HTML5
* CSS3
* JavaScript

## Database & Deployment

* SQLite
* PostgreSQL
* Docker
* Docker Compose

---

# 📋 Requirements

Before running:

* Python 3.10+
* Tesseract OCR
* Docker (optional)
* PostgreSQL (production)

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/HuzaifaAIDev/Same_file_detector.git

cd Same_file_detector
```

---

# Backend Setup

```bash
cd backend

python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment file:

```bash
copy .env.example .env
```

Run application:

```bash
python main.py
```

Application URL:

```
http://localhost:20285
```

---

# 🧪 Testing

Run:

```bash
pytest -q
```

---

# 🐳 Docker Deployment

Run:

```bash
docker compose up --build
```

Docker setup provides:

* FastAPI application
* Database service
* Production-ready configuration

---

# 📖 API Documentation

Swagger:

```
http://localhost:20285/api/docs
```

Redoc:

```
http://localhost:20285/api/redoc
```

---

# 🔌 Main API Endpoints

| Method | Endpoint                       | Description           |
| ------ | ------------------------------ | --------------------- |
| POST   | `/api/v1/auth/register`        | Register user         |
| POST   | `/api/v1/auth/login`           | User login            |
| POST   | `/api/v1/auth/change-password` | Change password       |
| POST   | `/api/v1/auth/reset-password`  | Reset password        |
| POST   | `/api/v1/compare`              | Compare documents     |
| GET    | `/api/v1/compare/history`      | Comparison history    |
| GET    | `/api/v1/admin/users`          | Admin user management |
| GET    | `/api/v1/health`               | Health check          |

---

# 📁 Supported Formats

| Format | Support |
| ------ | ------- |
| PDF    | ✅       |
| DOCX   | ✅       |
| XLSX   | ✅       |
| PPTX   | ✅       |
| TXT    | ✅       |
| CSV    | ✅       |
| JSON   | ✅       |
| Images | ✅ OCR   |

---

# 🔮 Future Improvements

Planned features:

* Semantic similarity using AI embeddings
* Advanced document understanding
* Cloud deployment
* Analytics dashboard
* Large-scale document processing
* Additional file formats

---

# 🤝 Contributing

Contributions and suggestions are welcome.

Steps:

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Submit a pull request

---

# 👨‍💻 Author

**HuzaifaAIDev**

GitHub:

https://github.com/HuzaifaAIDev

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# 📄 License

This project is licensed under the MIT License.
