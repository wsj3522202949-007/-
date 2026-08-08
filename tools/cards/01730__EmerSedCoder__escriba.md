---
id: tool-01730
type: tool
area: 库
status: active
tags: [Java, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: escriba
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/emersedcoder/escriba
created: 2026-07-18
updated: 2026-07-18
no: 1730
category: 二、网文 / 长篇 AI 写作系统 库
repo: EmerSedCoder/escriba
stars: 0
url: https://github.com/emersedcoder/escriba
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 37884144a65c9c4d
  - methods/最强写作方法论_全球最强综合版.md
---

# EmerSedCoder/escriba

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/emersedcoder/escriba
- **Stars**：0
- **语言**：Java
- **License**：None
- **Topics**：—
- **GitHub 描述**：Escriba is a complete and lightweight text editor software to story makers, novel writers and writing enthusiasts express their criativity through computer screen and then export it in any format wanted to publish it online or print in in a book.
- **本地描述**：Escriba is a complete and lightweight text editor software to story makers, novel writers and writing enthusiasts express their criativity through computer screen and then export it in any format wanted to publish it online or print in in a book.
- **拉取时间**：2026-07-23 23:29:28

---

# ✍️ Escriba

> A modern writing environment for authors, novelists, and world builders.

![Java](https://img.shields.io/badge/Java-21-orange)
![JavaFX](https://img.shields.io/badge/JavaFX-UI-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

---

## 📖 About

Escriba is a desktop writing application designed for fiction authors.

Inspired by tools such as **Scrivener**, **Obsidian**, and **Campfire**, Escriba aims to provide everything a writer needs inside a single application.

The goal is to create a distraction-free environment for planning, organizing, writing, and exporting complete novels.

---

## ✨ Features

### Writing

- Rich text editor
- Multiple chapters
- Scene management
- Word count
- Character count
- Estimated reading time
- Undo / Redo

### Project Management

- Multiple writing projects
- Chapter organization
- Project tree
- Automatic saving
- JSON project storage

### World Building

- Characters
- Locations
- Timeline
- Notes
- Goals
- Items

### Export

- Save projects
- Load projects
- JSON serialization

---

## 🚀 Planned Features

- RichTextFX editor
- Markdown support
- DOCX export
- PDF export
- EPUB export
- AI writing assistant
- Local AI integration (LM Studio)
- Grammar suggestions
- Writing statistics
- Daily writing goals
- Full-screen focus mode
- Themes
- Plugin system
- Cloud synchronization
- Version history
- Custom dictionaries

---

## 🛠️ Technologies

- Java 21
- Java Swing
- Jackson JSON
- Maven
- Git

Future:

- JavaFX
- RichTextFX
- SQLite
- Local LLM Integration

---

## 📂 Project Structure

```
src
├── app
├── model
├── service
├── storage
├── ui
└── export
```

---

## 🏗️ Architecture

Escriba follows a modular architecture.

```
Main
    │
    ▼
ProjectService
    │
    ▼
Book
    │
    ▼
Chapter
    │
    ▼
Scene
```

Persistence is isolated inside the storage layer.

```
UI
 │
 ▼
Services
 │
 ▼
Storage
 │
 ▼
JSON
```

This separation keeps the application maintainable and easy to extend.

---

## 🎯 Project Vision

Escriba is not just another text editor.

The long-term vision is to become a complete creative writing platform combining:

- Writing
- World building
- Research
- Timeline management
- AI assistance
- Professional publishing

All inside one application.

---

## 📸 Screenshots

*(Coming soon)*

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/escriba.git
```

Open the project in IntelliJ IDEA or VS Code.

Run:

```bash
mvn clean package
```

or

```bash
mvn javafx:run
```

---

## 🤝 Contributing

Contributions, ideas and suggestions are welcome.

Feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

**EmerSedCoder**

Passionate about software engineering, artificial intelligence and creative writing.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

> *"Every great story deserves a great writing tool."*
