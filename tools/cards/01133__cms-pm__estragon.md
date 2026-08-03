---
id: tool-01133
type: tool
area: 库
status: active
tags: [Claude插件, JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: estragon
summary: Claude Code 插件式写作流
source: https://github.com/cms-pm/estragon
created: 2026-07-18
updated: 2026-07-18
no: 1133
category: 二、网文 / 长篇 AI 写作系统 库
repo: cms-pm/estragon
stars: 0
url: https://github.com/cms-pm/estragon
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# cms-pm/estragon

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/cms-pm/estragon
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：godot4, llm-tools, mcp-server
- **GitHub 描述**：Estragon is an initial implementation of the MCP protocol for Godot 4, enabling seamless communication between your game and AI assistants. Whether you're building a text-based adventure, a collaborative writing tool, or any other AI-powered experience, Estragon makes it easy to connect your Godot project with AI assistants like Claude.
- **本地描述**：Estragon is an initial implementation of the MCP protocol for Godot 4, enabling seamless communication between your game and AI assistants. Whether you're building a text-based adventure, a collaborative writing tool, or any other AI-powered experience, Estragon makes it easy to connect your Godot project with AI assistants like Claude.
- **拉取时间**：2026-07-23 23:12:04

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 🌿 Estragon - Godot 4 MCP Protocol

A fresh take on LLM collaboration, built with 🍀 and 🌟

## 🚀 Overview

Estragon is an initial implementation of the MCP protocol for Godot 4, enabling seamless communication between your game and AI assistants. Whether you're building a text-based adventure, a collaborative writing tool, or any other AI-powered experience, Estragon makes it easy to connect your Godot project with AI assistants like Claude.

## 📱 Use Cases

- 🎮 Text-based adventures with AI companions
- 📝 Collaborative writing tools
- 🎮 AI-powered game assistants
- 🤖 Custom AI integrations

## 📦 Project Structure

```
📦 estragon/
├── 📁 src/             # Core implementation
├── 📁 godot-plugin/    # Godot plugin
└── 📁 docs/           # Documentation
```

## 🌱 Current Features

- 🎮 Complete Godot 4 editor integration
- 🔌 Full MCP protocol communication
- 🌐 WebSocket-based real-time communication
- 🔄 **Graceful shutdown system** - No stale daemons when Claude Desktop quits
- 🛠️ 8 comprehensive scene manipulation tools
- 📚 Extensive documentation and testing

## 🧪 Recent Research & Development

**🕷️ Web Research Complete** - May 27, 2025
- 🔍 **Collision Shape Assignment:** Research validated Godot 4 patterns for programmatic shape creation
- 🗑️ **Node Deletion System:** Discovered performance optimizations and safety patterns
- 📋 **Implementation Ready:** Production-grade solutions documented in [TODO_ENHANCEMENTS.md](docs/TODO_ENHANCEMENTS.md)

## 🎯 Next Priority Features

- 🟢 **Priority 1:** Collision shape assignment (CircleShape2D, RectangleShape2D, etc.)
- 🟡 **Priority 2:** Node deletion system (safe deletion with performance optimization)
- 🔵 **Priority 3:** Enhanced property type conversion (better MCP protocol handling)

## 🛠️ Setup

For detailed setup instructions, check out:
- [Godot Setup](docs/GODOT_SETUP.md)
- [Client Setup](docs/CLIENT_SETUP.md) - Setup instructions for popular clients (Claude Desktop, MUSHclient, TinyFugue, zMUD, and web clients)
- [Claude Setup](docs/SETUP_CLAUDE.md)
- [Graceful Shutdown](GRACEFUL_SHUTDOWN.md) - **NEW**: Signal-based cascade shutdown system

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues and pull requests.

## 📜 License

MIT License - feel free to use this project however you like!
## 📚 Documentation

### Setup Guides
- [Godot Setup](docs/GODOT_SETUP.md) - Plugin installation and configuration
- [Client Setup](docs/CLIENT_SETUP.md) - Setup for Claude Desktop and other MCP clients  
- [Claude Setup](docs/SETUP_CLAUDE.md) - Claude Desktop configuration

### Architecture & Development
- [Multi-Client Design](docs/MULTICLIENT_DESIGN.md) - WebSocket architecture for multiple connections
- [QA Worklog](docs/QA_WORKLOG_FINAL.md) - Comprehensive testing and validation results
- [Enhancement TODO](docs/TODO_ENHANCEMENTS.md) - **NEW**: Research-validated feature roadmap

### System Documentation  
- [Graceful Shutdown](GRACEFUL_SHUTDOWN.md) - Multi-method process lifecycle management
- [Final Worklog](docs/FINAL_WORKLOG_COMPLETE.md) - Complete development history and achievements

## 🤝 Contributing

We welcome contributions! Check out [TODO_ENHANCEMENTS.md](docs/TODO_ENHANCEMENTS.md) for research-validated enhancement opportunities.

## 📜 License

MIT License - feel free to use this project however you like!
