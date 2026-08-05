---
id: tool-01550
type: tool
area: 库
status: active
tags: [Rust, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: allux-agent
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/marvinquevedo/allux-agent
created: 2026-07-18
updated: 2026-07-18
no: 1550
category: 二、网文 / 长篇 AI 写作系统 库
repo: MarvinQuevedo/allux-agent
stars: 0
url: https://github.com/marvinquevedo/allux-agent
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# MarvinQuevedo/allux-agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/marvinquevedo/allux-agent
- **Stars**：0
- **语言**：Rust
- **License**：NOASSERTION
- **Topics**：ollama, ollama-api, ollama-client, ollama-gui
- **GitHub 描述**：Allux is a local AI-powered code agent built in Rust. It connects to Ollama for local LLM inference and provides an interactive terminal UI (via Ratatui) with built-in developer tools — file search, code reading/writing, bash execution, and more — acting as a privacy-first, locally-run alternative to cloud-based coding assistants.
- **本地描述**：Allux is a local AI-powered code agent built in Rust. It connects to Ollama for local LLM inference and provides an interactive terminal UI (via Ratatui) with built-in developer tools — file search, code reading/writing, bash execution, and more — acting as a privacy-first, locally-run alternative to cloud-based coding assistants.
- **拉取时间**：2026-07-23 23:24:18

---

# Allux Agent 🚀

> **Note:** This README and parts of this project were created by **Allux**, an AI agent, using the **Allux** tool itself.

## 🚀 Introduction
Allux is a local code agent built with Rust, designed to assist in software development tasks by integrating with Ollama. This project combines asynchronous processing, file manipulation, and modular extensibility to offer an efficient and powerful development experience.

---

## 📋 Table of Contents
1. [📌 Overview](#overview)
2. [🔧 Architecture and Technologies](#architecture-and-technologies)
3. [📂 Project Structure](#project-structure)
4. [🛠 Tools and Dependencies](#tools-and-dependencies)
5. [🚀 Installation and Setup](#installation-and-setup)
6. [🧪 Basic Usage](#basic-usage)
7. [🔧 Extensibility with Skills](#extensibility-with-skills)
8. [📝 Contributions](#contributions)
9. [📄 Additional Documentation](#additional-documentation)
10. [📋 Licenses](#licenses)

---

## 📌 Overview
Allux is built on:
- **Tokio** for asynchronous operations.
- **Rust** for performance and security.
- **Ollama** for language model integration.

The project allows exploring, modifying, and executing code locally with advanced file processing and pattern matching capabilities.

---

## 🔧 Architecture and Technologies

### 🔄 Architecture
- **Modular**: Each functionality is encapsulated in independent modules.
- **Asynchronous**: Designed to handle multiple tasks simultaneously.
- **Extensible**: Skill system for adding specific functionalities.

### 🛠 Key Technologies
| Technology      | Purpose                                                                 |
|-----------------|-------------------------------------------------------------------------|
| Rust            | Main language for performance and security.                             |
| Tokio           | Asynchronous runtime for I/O handling.                                  |
| Reqwest         | HTTP client with streaming support.                                     |
| Serde           | JSON serialization/deserialization.                                     |
| Crossterm       | Terminal input/output handling.                                         |
| Glob            | File pattern searching.                                                 |
| Regex           | Text pattern processing.                                                |
| Pulldown-cmark  | Markdown processing.                                                    |
| Indicatif       | Progress bars and load indicators.                                      |

---

## 📂 Project Structure
```
allux-agent/
├── Cargo.toml          # Project dependencies and configuration.
├── README.md           # Main documentation.
├── LICENSE             # Project license.
├── docs/               # Technical documentation and guides.
├── scripts/            # Utility scripts.
├── src/                # Main source code.
│   ├── main.rs         # Program entry and REPL.
│   ├── ollama/         # Ollama client and types.
│   ├── tools/          # Built-in tools (bash, grep, edit, etc.).
│   └── ...             # Other modules (config, session, etc.).
├── tests/              # Integration and unit tests.
├── validation/         # Test prompts and validation data.
└── skills-lock.json    # Skills dependencies.
```

---

## 🛠 Tools and Dependencies

### 📦 Main Dependencies
| Dependency   | Version | Purpose                                  |
|--------------|---------|------------------------------------------|
| reqwest      | 0.12    | HTTP client with streaming.              |
| tokio        | 1.0     | Asynchronous runtime.                    |
| serde        | 1.0     | JSON serialization.                     |
| crossterm    | 0.28    | Terminal input/output.                  |
| glob         | 0.3     | File searching.                         |
| regex        | 1.0     | Pattern processing.                     |
| pulldown-cmark| 0.12    | Markdown processing.                    |
| indicatif    | 0.17    | Progress bars.                          |

---

## 🚀 Installation and Setup

### 📦 Prerequisites
1. **Rust**: Install Rust toolchain from [rustup.rs](https://rustup.rs).
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```

2. **Ollama**: Install Ollama for language model integration.
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

### 🛠 Project Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/usuario/allux-agent.git
   cd allux-agent
   ```

2. Build the project:
   ```bash
   cargo build
   ```

3. Run the agent:
   ```bash
   cargo run --bin allux
   ```

---

## 🧪 Basic Usage

### 📌 Main Capabilities
| Command/Tool       | Description                                  |
|-----------------------|----------------------------------------------|
| `bash`                | Execute shell commands.                      |
| `grep <pattern>`      | Search patterns in files.                  |
| `read_file <path>`    | Read file contents.                         |
| `write_file <path>`   | Write/Overwrite files.                      |
| `edit_file <path>`    | Edit specific strings in files.             |
| `tree <path>`         | Display directory structure.                |

---

## 🔧 Extensibility with Skills
Allux allows adding specific functionalities using the skill system. Each skill is an independent module that can add new capabilities to the agent.

### 📦 Installing Skills
1. **Install a skill**:
   ```bash
   npx --yes skills add <owner/repo> --skill <name> -y
   ```

---

## 📝 Contributions
1. **Clone the repository**.
2. **Create a branch** for your feature.
3. **Write tests** to ensure stability.
4. **Submit a Pull Request**.

---

## 📄 Additional Documentation
- **`[Architecture Docs](docs/architecture/overview.md)`**: Detailed technical design.
- **`[Guides](docs/guides/index.md)`**: How to use and configure Allux.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📋 Licenses
This project is licensed under the `[GPL-3.0-or-later](LICENSE)`.
