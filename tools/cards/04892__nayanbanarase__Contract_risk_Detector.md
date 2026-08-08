---
id: tool-04892
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Contract_risk_Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/nayanbanarase/contract_risk_detector
created: 2026-07-18
updated: 2026-07-18
no: 4892
category: 一、去 AI 味 / Humanizer 库
repo: nayanbanarase/Contract_risk_Detector
stars: 0
url: https://github.com/nayanbanarase/contract_risk_detector
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
content_hash: 91717260c8f40655
  - methods/改稿润色指令库.md
---

# nayanbanarase/Contract_risk_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/nayanbanarase/contract_risk_detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Contract Risk Detector is an AI-powered web application that analyzes legal contracts to identify potential risks and generate intelligent summaries. The system extracts text from PDF and scanned documents using PyPDF2 and Tesseract OCR, detects key clauses through NLP and a rule-based risk engine, and stores analysis results in SQLite. 
- **本地描述**：Contract Risk Detector is an AI-powered web application that analyzes legal contracts to identify potential risks and generate intelligent summaries. The system extracts text from PDF and scanned documents using PyPDF2 and Tesseract OCR, detects key clauses through NLP and a rule-based risk engine, and stores analysis results in SQLite.
- **拉取时间**：2026-07-25 17:58:19

---

# Contract Risk Detector

> **An AI-Powered Contract Analysis System Using FastAPI, React.js, SQLite, OCR, NLP, and Ollama LLM**

---

# Abstract

The Contract Risk Detector is an intelligent web application designed to automate the analysis of legal contracts and identify potential risks. The system extracts text from PDF documents and scanned images using PyPDF2 and Tesseract OCR, processes the extracted content using Natural Language Processing (NLP), detects risky clauses through a rule-based risk engine, and generates AI-powered summaries using Ollama Large Language Models (Phi-4/Llama 3). It also calculates an overall risk score and stores analysis results in an SQLite database. Developed using Python, FastAPI, React.js, SQLite, spaCy, OCR, and Ollama, the system reduces manual effort, improves accuracy, and provides users with a fast and reliable contract analysis solution.

**Keywords:** Artificial Intelligence, Contract Analysis, FastAPI, React.js, SQLite, OCR, NLP, Ollama, Risk Detection, PDF Processing.

---

# 1. Introduction

Legal contracts often contain lengthy and complex language that makes manual review difficult and time-consuming. Missing important clauses such as penalties, liabilities, indemnity, or termination conditions can lead to financial and legal consequences.

The AI Contract Risk Detector automates this process by extracting text from contracts, identifying risky clauses, assigning a numerical risk score, and generating an AI-powered summary. The system combines Artificial Intelligence, Optical Character Recognition (OCR), Natural Language Processing (NLP), and modern web technologies to provide an efficient contract analysis platform.

---

# 2. Literature Review

Traditional contract review relies heavily on manual analysis performed by legal professionals. Although effective, manual review requires significant time and effort.

Recent advancements in Artificial Intelligence and Natural Language Processing have enabled automatic analysis of legal documents. OCR technologies such as Tesseract can extract text from scanned contracts, while NLP libraries such as spaCy improve text understanding. FastAPI simplifies backend development with high performance, React.js enables responsive user interfaces, and Large Language Models (LLMs) such as Ollama provide intelligent summaries and explanations. This project combines these technologies into a single application for automated contract risk detection.

---

# 3. Methodology

The system follows the workflow below:

1. User uploads a contract (PDF/Image).
2. FastAPI receives the uploaded file.
3. PDF text is extracted using PyPDF2.
4. Image text is extracted using Tesseract OCR.
5. spaCy processes the extracted text.
6. Rule-based risk detection identifies important clauses.
7. Risk score is calculated.
8. Ollama LLM generates an AI summary.
9. Results are stored in SQLite.
10. React Dashboard displays analysis results.

---

# 4. System Architecture

```
                User
                  │
                  ▼
          React.js Frontend
                  │
                  ▼
           FastAPI Backend
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
 PDF Reader           OCR Reader
 (PyPDF2)            (Tesseract)
        │                   │
        └─────────┬─────────┘
                  ▼
          Text Extraction
                  │
                  ▼
          NLP Processing
               (spaCy)
                  │
                  ▼
        Rule-Based Risk Engine
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Risk Score         AI Summary
                     (Ollama LLM)
        │                   │
        └─────────┬─────────┘
                  ▼
           SQLite Database
                  │
                  ▼
            Result Dashboard
```

---

# 5. Project Structure

```
contract-risk-detector/
│
├── backend/
│   ├── app.py
│   ├── pdf_reader.py
│   ├── risk_engine.py
│   ├── database.py
│   ├── show_data.py
│   ├── ocr_reader.py
│   ├── contracts.db
│   └── uploads/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── requirements.txt
├── README.md
└── venv/
```

---

# 6. Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| React.js | Frontend Framework |
| SQLite | Database |
| PyPDF2 | PDF Text Extraction |
| Tesseract OCR | Image Text Extraction |
| Pillow | Image Processing |
| spaCy | Natural Language Processing |
| Ollama (Phi-4/Llama 3) | AI Summary Generation |
| Axios | API Communication |
| VS Code | Development Environment |

---

# 7. Implementation

## Frontend

The frontend is developed using React.js and provides an interactive interface for uploading contracts, viewing detected risks, AI-generated summaries, and contract scores.

### Features

- Contract Upload
- Risk Dashboard
- AI Summary Display
- Risk Score Visualization

---

## Backend

The backend is developed using FastAPI and handles all server-side operations including:

- File Upload
- PDF Processing
- OCR Processing
- Risk Detection
- AI Summary Generation
- Database Operations

---

## PDF Processing

PyPDF2 extracts text from PDF contracts.

---

## OCR Module

Tesseract OCR extracts text from scanned contracts and images.

---

## NLP Processing

spaCy is used to preprocess extracted text before analysis.

---

## Risk Detection Engine

The system detects keywords such as:

- Penalty
- Liability
- Termination
- Indemnity
- Lawsuit
- Hidden Fees
- Service Charges
- Processing Fees

Each detected keyword contributes to the overall risk score.

---

## AI Summary Generation

Ollama LLM (Phi-4/Llama 3) generates a concise summary of the uploaded contract, highlighting important clauses and risks.

---

## Database

SQLite stores:

- Contract Name
- Upload Date
- Risk Score
- AI Summary

---

# 8. Software Requirements

- Python 3.10+
- Node.js
- React.js
- FastAPI
- SQLite
- PyPDF2
- spaCy
- Pillow
- pytesseract
- Ollama
- VS Code

---

# 9. Hardware Requirements

## Minimum

- Intel Core i3
- 4 GB RAM
- 10 GB Storage

## Recommended

- Intel Core i5/i7
- 8 GB RAM
- SSD Storage

---

# 10. Features

- PDF Contract Upload
- OCR Support for Scanned Contracts
- Automatic Text Extraction
- AI-Powered Contract Summary
- Clause Detection
- Hidden Fee Detection
- Risk Score Calculation
- SQLite Database Storage
- FastAPI REST API
- React Dashboard

---

# 11. Advantages

- Automates contract analysis
- Saves review time
- Detects risky clauses
- Generates AI summaries
- Supports scanned contracts
- Easy-to-use interface
- Uses free and open-source technologies

---

# 12. Limitations

- Current risk detection primarily uses predefined rules.
- OCR accuracy depends on image quality.
- AI summary quality depends on the selected language model.
- SQLite is suitable for small to medium-scale applications.

---

# 13. Future Scope

Future enhancements include:

- Machine Learning-based risk prediction
- Multilingual contract analysis
- Cloud deployment (AWS/Azure)
- User Authentication
- Digital Signature Verification
- Email Notifications
- Contract Comparison
- AI Chatbot for Question Answering
- Retrieval-Augmented Generation (RAG)
- Vector Database Integration
- Real-time Collaboration
- Enterprise Contract Management Integration

---

# 14. Conclusion

The Contract Risk Detector demonstrates how Artificial Intelligence, Natural Language Processing, OCR, and modern web technologies can be integrated to automate legal contract analysis. The application successfully extracts contract text, identifies risky clauses, calculates a risk score, generates AI-powered summaries, and stores analysis results efficiently. The project reduces manual effort while improving the speed and accuracy of contract review, making it suitable for educational purposes and future real-world applications.

---

# References

[1] FastAPI Documentation. https://fastapi.tiangolo.com/

[2] React Documentation. https://react.dev/

[3] SQLite Documentation. https://www.sqlite.org/

[4] PyPDF2 Documentation. https://pypdf2.readthedocs.io/

[5] spaCy Documentation. https://spacy.io/

[6] Tesseract OCR Documentation. https://tesseract-ocr.github.io/

[7] Ollama Documentation. https://ollama.com/

[8] Python Software Foundation. https://www.python.org/

[9] Pillow Documentation. https://pillow.readthedocs.io/

[10] Jurafsky, D., & Martin, J. H., *Speech and Language Processing*, Pearson Education.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Author

**Nayan Shankar Banarase**

Master of Computer Applications (MCA)

Project: Contract Risk Detector

Year: 2026
