---
id: tool-05697
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 去AI味]
title: CipherSentinel-Secret-API-Key-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/loganthp/ciphersentinel-secret-api-key-detector
created: 2026-07-18
updated: 2026-07-18
no: 5697
category: 一、去 AI 味 / Humanizer 库
repo: LoganthP/CipherSentinel-Secret-API-Key-Detector
stars: 1
url: https://github.com/loganthp/ciphersentinel-secret-api-key-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5c31322af79c7909
  - methods/改稿润色指令库.md
---

# LoganthP/CipherSentinel-Secret-API-Key-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/loganthp/ciphersentinel-secret-api-key-detector
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：ai-security, api-key-detector, code-security, credential-leak-detection, cybersecurity, devsecops, secret-detection, secure-development, security-scanner, sensitive-data-detection
- **GitHub 描述**：It is an AI-powered security analysis tool that scans code, logs, and text inputs to detect exposed API keys, tokens, and sensitive credentials, helping developers prevent secret leaks, enhance secure coding practices, and strengthen overall application security.
- **本地描述**：It is an AI-powered security analysis tool that scans code, logs, and text inputs to detect exposed API keys, tokens, and sensitive credentials, helping developers prevent secret leaks, enhance secure coding practices, and strengthen overall application security.
- **拉取时间**：2026-07-25 18:28:15

---

# 🌌 CipherSentinel - Advanced Secret & API Key Detector

<p align="center">
  <img src="https://img.shields.io/badge/DevSecOps-Cyber%20Security-black?style=for-the-badge&logo=shield" />
  <img src="https://img.shields.io/badge/React-19-blue?style=for-the-badge&logo=react" />
  <img src="https://img.shields.io/badge/TypeScript-Strict-blue?style=for-the-badge&logo=typescript" />
  <img src="https://img.shields.io/badge/Express-Backend-green?style=for-the-badge&logo=express" />
  <img src="https://img.shields.io/badge/Database-SimpleDB-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Design-Cyberpunk%20UI-purple?style=for-the-badge" />
</p>

<p align="center">
  <b>🔐 A futuristic DevSecOps platform designed to detect API keys, 
  hardcoded secrets, tokens, and configuration leaks with a stunning 
  cyberpunk command-center UI.</b>
</p>

------------------------------------------------------------------------

# ✨ Key Highlights

-   🔑 Advanced Secret & API Key Detection Engine\
-   🧠 Heuristic + Signature-Based Scanning\
-   🌌 Futuristic Cyberpunk Dashboard UI\
-   🗄️ Lightweight SimpleDB (JSON-based storage)\
-   📊 Interactive Risk Analytics & Visualization\
-   🔒 Privacy Mode & Secret Masking\
-   ⚡ Fast, Modular & Git-Friendly Architecture

------------------------------------------------------------------------
# 🚀 Overview

CipherSentinel is a next-generation Secret & Vulnerability Detection
platform built for developers, security researchers, and DevSecOps
teams.\
It scans files, code snippets, and configuration data to proactively
identify exposed credentials before they become real-world security
risks.

------------------------------------------------------------------------

# 🧠 System Block Diagram

``` mermaid
flowchart TD
    A[User Uploads File / Pastes Code] --> B[React Frontend]
    B --> C[Validation Layer]
    C --> D[REST API Call]
    D --> E[Express Backend]
    E --> F[Input Sanitization]
    F --> G[Heuristic Detection Engine]
    G --> H[Signature Library]
    G --> I[Entropy & Pattern Analysis]
    H --> J{Secrets Found?}
    I --> J
    J -->|Yes| K[Risk Scoring Engine]
    J -->|No| L[Safe Result Response]
    K --> M[Severity Classification]
    M --> N[Store Scan Metadata]
    N --> O[(SimpleDB JSON Database)]
    E --> P[Return Structured JSON Report]
    P --> Q[Frontend Visualization]
    Q --> R[Monaco Highlight]
    Q --> S[Risk Gauge & Charts]
```

------------------------------------------------------------------------

# 🏗️ Project File Architecture

    CipherSentinel-Secret-API-Key-Detector/
    │
    ├── client/                         # React Cyberpunk Frontend
    │   ├── src/
    │   │   ├── components/
    │   │   ├── pages/
    │   │   ├── hooks/
    │   │   ├── utils/
    │   │   ├── animations/
    │   │   └── styles/
    │   └── package.json
    │
    ├── server/                         # Express Backend
    │   ├── controllers/
    │   ├── routes/
    │   ├── services/
    │   ├── detectors/
    │   ├── simpledb/
    │   └── utils/
    │
    ├── simpledb-data/                  # JSON Database Storage
    │   ├── scans.json
    │   └── settings.json
    │
    ├── test-files/
    ├── public/
    ├── README.md
    └── package.json

------------------------------------------------------------------------

# 🔍 Core Features Breakdown

## 1️⃣ Heuristic Scanner Engine

-   Detects AWS Keys, JWT Tokens, Stripe Secrets, Google API Keys,
    Private Keys (.pem), Slack Tokens
-   Regex + Heuristic Analysis
-   Drag & Drop File Scanning
-   Paste Code Instant Analysis

## 2️⃣ Command Center Dashboard

-   Total Scans Overview
-   Critical Threat Counter
-   Risk Trend Graphs (Recharts)
-   Recent Scan Activity Panel

## 3️⃣ Vulnerability Lab (Results Page)

-   🎯 Dynamic Risk Score (0--100 Gauge)
-   🔴 Highlighted Secrets in Monaco Editor
-   🧾 Detailed Detection Metadata (File, Line, Type)
-   🔒 Secret Masking Toggle (\*\*\*\* Protection)

## 4️⃣ Scan Archive (History)

-   Stored securely using SimpleDB JSON
-   Search & Filter Past Scans
-   Two-Step Secure Deletion Flow

## 5️⃣ Settings & DevSecOps Controls

-   Deep Scan Mode
-   Sensitivity Slider
-   Privacy Mode (No File Storage)
-   Detection Signature Toggles
-   SimpleDB Data Management

------------------------------------------------------------------------

# ⚙️ Running the Fully Functional Project

## 📦 1️⃣ Install All Dependencies (Client + Server)

From the root directory, run:

```bash
npm run install:all
```

------------------------------------------------------------------------

## 🚀 2️⃣ Start the Full Development Environment

``` bash
npm run dev
```

Frontend Dashboard:

    http://localhost:5173
Backend API:

    http://localhost:5000

------------------------------------------------------------------------

# 🗄️ SimpleDB Schema Example

``` json
{
  "scanId": "uuid",
  "fileName": "sample.env",
  "secretsDetected": [],
  "severity": "Critical",
  "riskScore": 87,
  "createdAt": "timestamp"
}
```

------------------------------------------------------------------------

# 🛠️ Tech Stack

| Layer         | Technologies                                      |
|---------------|---------------------------------------------------|
| Frontend      | React 19, TypeScript, TailwindCSS 4, Framer Motion|
| Backend       | Node.js, Express 5, Multer                        |
| Database      | SimpleDB (JSON File-Based)                        |
| Visualization | Recharts, Monaco Editor                           |
| UI Design     | Cyberpunk Glassmorphism + Neon UI                 |
| Icons         | Material Symbols                                  |

------------------------------------------------------------------------

# 🎨 UI/UX Philosophy

-   Cyberpunk Command Center Theme\
-   Glassmorphism + Neon Glow\
-   Interactive Risk Intelligence\
-   Beginner-Friendly but Enterprise-Level Feel

---------------------------------------------------------------------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# 🔒 Security Notice

CipherSentinel is designed for internal auditing and research purposes.\
Ensure `simpledb-data/` is excluded from public repositories if
containing sensitive results.

*Built as a DevSecOps Vulnerability Research Platform.*
