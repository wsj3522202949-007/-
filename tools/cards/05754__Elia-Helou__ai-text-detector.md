---
id: tool-05754
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/elia-helou/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5754
category: 一、去 AI 味 / Humanizer 库
repo: Elia-Helou/ai-text-detector
stars: 0
url: https://github.com/elia-helou/ai-text-detector
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
content_hash: 630c88bf3119ce42
  - methods/改稿润色指令库.md
---

# Elia-Helou/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/elia-helou/ai-text-detector
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Elia-Helou/ai-text-detector
- **拉取时间**：2026-07-25 18:30:41

---

# AI Project: Text Detection and Recognition

This repository contains a complete AI-powered text detection and recognition system. The system uses YOLOv8 for text detection, paired with a robust OCR for text extraction. The project is divided into three main components:

1. **Backend**: A Flask-based backend serving the AI model and providing API endpoints.
2. **Frontend**: A React web application to interact with the backend.
3. **Mobile App**: A React Native mobile application for seamless interaction on the go.

---

## Project Structure


---

## Features

### **Backend**
- Built with Flask.
- Serves the YOLOv8-trained model for text detection and OCR processing.
- Dockerized for easy deployment and scalability.

### **Frontend**
- Built with React.
- Provides a user-friendly web interface to upload images and view results.
- Dockerized for simplified deployment.

### **Mobile App**
- Built with React Native.
- Allows users to capture images, send them to the backend for processing, and view detection results.
- Optimized for both Android and iOS.

---

## Installation and Setup

### Prerequisites
- [Docker](https://www.docker.com/) installed on your system.
- Node.js and npm installed (for mobile development).

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

### **Backend Setup**
1. Navigate to the `backend/` directory:
   ```bash
   cd backend
