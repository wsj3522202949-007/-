---
id: tool-01186
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-CV-Generator-Automation
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/farhan3376/ai-cv-generator-automation
created: 2026-07-18
updated: 2026-07-18
no: 1186
category: 二、网文 / 长篇 AI 写作系统 库
repo: Farhan3376/AI-CV-Generator-Automation
stars: 0
url: https://github.com/farhan3376/ai-cv-generator-automation
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 7247ea86cee58a9f
  - methods/最强写作方法论_全球最强综合版.md
---

# Farhan3376/AI-CV-Generator-Automation

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/farhan3376/ai-cv-generator-automation
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：An end-to-end professional pipeline designed to help job seekers bypass Applicant Tracking Systems (ATS). This project demonstrates high-performance engineering by combining a FastAPI backend with Google Gemini AI for intelligent re-writing, alongside a premium React dashboard and n8n workflow orchestrations for production-grade automation
- **本地描述**：An end-to-end professional pipeline designed to help job seekers bypass Applicant Tracking Systems (ATS). This project demonstrates high-performance engineering by combining a FastAPI backend with Google Gemini AI for intelligent re-writing, alongside a premium React dashboard and n8n workflow orchestrations for production-grade automation
- **拉取时间**：2026-07-23 23:13:37

---

# A I - C V - G e n e r a t o r - A u t o m a t i o n 

## 🚀 AI Resume Tailoring Engine

An end-to-end AI automation pipeline that re-engineers your resume for specific job descriptions using **Google Gemini AI**. This project demonstrates full-stack proficiency by combining a high-performance **FastAPI** backend with professional **n8n** workflow orchestrations for seamless document automation.

---

## ✨ Features

- **🧠 Gemini AI Rewriting**: High-impact alignment of your experience with target Job Descriptions.
- **📊 ATS Intelligence**: Real-time keyword matching and similarity scoring.
- **📄 PDF Upload Support**: Built-in extraction of text from your existing PDF resumes.
- **🎨 Premium React UI**: High-fidelity Glassmorphism dashboard for an effortless user experience.
- **📝 LaTeX Rendering**: Professional templates for pixel-perfect document generation.
- **🔄 Multi-Mode Engine**: Toggle between `Aggressive`, `Conservative`, or `Research-Focused`.
- **🧩 n8n Automation**: Pre-built workflow JSON for seamless external integration.

---

## 📖 About the Project

The **AI Resume Tailoring Engine** is a professional-grade automation tool designed to bridge the gap between skilled candidates and Applicant Tracking Systems (ATS). By combining the reasoning capabilities of **Google Gemini AI** with a modular **FastAPI** backend and a reactive **React** frontend, the system provides a seamless experience for transforming a generic resume into a job-aligned masterpiece.

This project showcases several advanced engineering patterns:
- **Scalable Document Processing**: Real-time PDF text extraction and LaTeX rendering.
- **AI-Driven Orchestration**: Complex system prompts for Gemini for structured JSON outputs.
- **Low-Code Extensibility**: Pre-built **n8n** integration for enterprise workflows.

---

## 🏗️ Architecture

- **FastAPI Backend**: Python-powered pipeline with Gemini integration and PDF extraction.
- **React Frontend**: Vite-based dashboard with real-time feedback.
- **LaTeX Engine**: Dynamic Jinja2 templating for automated CV formatting.

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.10+
- Node.js & npm
- Gemini API Key ([Get it here](https://aistudio.google.com/))

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```
*Don't forget to configure your `.env` with your `GEMINI_API_KEY`!*

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---

## 📡 API & Usage
Open **[http://localhost:5173/](http://localhost:5173/)** (or your Vite port) to use the interactive dashboard.

### Endpoint: `POST /api/v1/resume/generate`
Accepts `multipart/form-data`:
- `job_description`: (text)
- `resume_file`: (PDF file)
- `mode`: (`aggressive`, `conservative`, or `research-focused`)

---

## 🧩 n8n Integration
1. Open your n8n instance and create a new workflow.
2. Import the provided `n8n/workflow.json` file.
3. Configure the HTTP Request nodes to point to your FastAPI endpoint (use Ngrok if n8n is in the cloud).
4. The workflow handles the end-to-end trigger, extraction, and delivery logic.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📄 License
MIT
