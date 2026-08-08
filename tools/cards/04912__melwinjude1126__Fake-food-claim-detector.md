---
id: tool-04912
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 去AI味]
title: Fake-food-claim-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/melwinjude1126/fake-food-claim-detector
created: 2026-07-18
updated: 2026-07-18
no: 4912
category: 一、去 AI 味 / Humanizer 库
repo: melwinjude1126/Fake-food-claim-detector
stars: 0
url: https://github.com/melwinjude1126/fake-food-claim-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1c2fead284d08419
  - methods/改稿润色指令库.md
---

# melwinjude1126/Fake-food-claim-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/melwinjude1126/fake-food-claim-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI-powered tool using FastAPI, Tesseract OCR, and Google Gemini to analyze food labels. It extracts text from packaging to verify marketing claims against actual ingredients and nutritional data, providing consumers with a health risk score.
- **本地描述**：An AI-powered tool using FastAPI, Tesseract OCR, and Google Gemini to analyze food labels. It extracts text from packaging to verify marketing claims against actual ingredients and nutritional data, providing consumers with a health risk score.
- **拉取时间**：2026-07-25 17:59:05

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Fake Food Claim Detector

Fake Food Claim Detector is a smart, AI-powered tool designed to help consumers uncover the truth behind food packaging. By simply uploading images of a product's front and back labels, this application uses Optical Character Recognition (OCR) and Google's Gemini Large Language Model (LLM) to cross-reference bold marketing claims against actual ingredients and nutritional data.

## Features

- **Marketing Claim Extraction**: Uses AI to identify claims like "100% Natural", "No Added Sugar", or "Low Fat" from the front packaging.
- **Ingredient Simplification**: Reconstructs noisy OCR ingredient lists, translates complex chemical names into simple English, and assigns a health risk level (Low, Moderate, High) to each.
- **Nutritional Analysis**: Extracts standard nutritional values from the back label table.
- **Claim Verification**: Automatically verifies if the marketing claims made on the front are actually supported by the ingredients and nutrition facts on the back.
- **Regulatory Compliance Check**: Evaluates the product against FSSAI and WHO guidelines.
- **Overall Risk Score**: Calculates a final risk score summarizing the healthiness and honesty of the product.

## Technology Stack

- **Backend framework**: FastAPI
- **LLM Integration**: Google Gemini (gemini-2.5-flash)
- **OCR Engine**: Tesseract OCR (via `pytesseract`), OpenCV, Pillow
- **Frontend**: Vanilla HTML, CSS, and JavaScript (Served statically by FastAPI)
- **Data Validation**: Pydantic

## Installation & Setup

### Prerequisites

1. **Python 3.8+** installed.
2. **Tesseract OCR** installed on your system. 
   - *Windows*: Download the installer from the [UB-Mannheim repository](https://github.com/UB-Mannheim/tesseract/wiki).
   - *Mac*: `brew install tesseract`
   - *Linux*: `sudo apt-get install tesseract-ocr`
3. A **Google Gemini API Key**. You can get one from Google AI Studio.

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd fake-food-claim-detector-final-yr-project
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   - Copy `.env.example` to a new file named `.env`.
   - Open `.env` and add your Gemini API Key:
     ```env
     GEMINI_API_KEY=your_actual_api_key_here
     ```

5. **Run the application:**
   ```bash
   python main.py
   ```
   *Alternatively, you can run:* `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`

6. **Access the application:**
   Open your browser and navigate to [http://localhost:8000](http://localhost:8000). You will see the web interface where you can upload product images.

## Project Structure

- `main.py`: The main FastAPI application, handling routes and orchestrating the analysis pipeline.
- `services/ocr_service.py`: Handles text extraction from images using Tesseract.
- `services/llm_service.py`: Prompts the Gemini API to extract claims, ingredients, and nutrition facts.
- `services/verification_service.py`: Contains the logic for verifying claims, checking compliance, and scoring risk.
- `models.py`: Pydantic models for request and response data validation.
- `frontend/`: Contains the static files (`index.html`, `style.css`, `script.js`) for the web user interface.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
