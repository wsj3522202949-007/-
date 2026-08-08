---
id: tool-01030
type: tool
area: 库
status: active
tags: [Dart, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: writing-app
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/uobirek/writing-app
created: 2026-07-18
updated: 2026-07-18
no: 1030
category: 二、网文 / 长篇 AI 写作系统 库
repo: uobirek/writing-app
stars: 0
url: https://github.com/uobirek/writing-app
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
content_hash: 38d76dac55666bb6
  - methods/最强写作方法论_全球最强综合版.md
---

# uobirek/writing-app

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/uobirek/writing-app
- **Stars**：0
- **语言**：Dart
- **License**：None
- **Topics**：—
- **GitHub 描述**：All-in-one tool designed to help writers plan, organize, and write their novels in a single, structured space.
- **本地描述**：All-in-one tool designed to help writers plan, organize, and write their novels in a single, structured space.
- **拉取时间**：2026-07-23 23:09:02

---

![Frame 1](https://github.com/user-attachments/assets/ce372aac-1c44-4edc-8de7-38e3b3bf6efc)


# ✍️🔮 Fantasies

**Fantasies** is a powerful, all-in-one tool designed to help writers plan, organize, and write their novels in a single, structured space. With built-in features for character development, worldbuilding, outlining, and drafting, this app ensures that every detail of your story stays organized while you focus on writing.

## 🚀 Features  
- **Project Dashboard**: Manage multiple writing projects.  
- **Text Editor**: Draft your novel with basic and advanced formatting.  
- **Notes System**: Organize characters, worldbuilding, and story outlines.  
- **Drag-and-Drop Notes**: Reorder notes easily.  
- **Cloud Image Upload**: Store images for characters, settings, and notes.  
- **Multi-Platform**: Works on **Android** and **Desktop**.  

---

## 🛠️ Tech Stack  
- **Flutter** (Cross-platform development)  
- **Firebase** (Auth, Firestore for data storage)  
- **Cloudinary** (Image storage)  

---

## 🔑 Environment Setup  

Create a `.env` file in the root of your project and add:  

```ini
# Firebase API Keys
FIREBASE_API_KEY=your_api_key_here
FIREBASE_APP_ID=your_app_id_here
FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id_here
FIREBASE_PROJECT_ID=your_project_id_here
FIREBASE_STORAGE_BUCKET=your_storage_bucket_here

# Cloudinary API Keys
CLOUDINARY_CLOUD_NAME=your_cloud_name_here
CLOUDINARY_UPLOAD_PRESET=your_upload_preset_here
```
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📦 Installation
### 1️⃣ Clone the repository
```
git clone https://github.com/your-username/writing-app.git
cd writing-app
```
### 2️⃣ Install dependencies

```
flutter pub get
```
### 3️⃣ Run the app
```
flutter run
```

