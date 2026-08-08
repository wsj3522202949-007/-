---
id: tool-01777
type: tool
area: 库
status: active
tags: [Dart, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: kids-story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/pasindusandamal/kids-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1777
category: 二、网文 / 长篇 AI 写作系统 库
repo: pasindusandamal/kids-story-generator
stars: 2
url: https://github.com/pasindusandamal/kids-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d0490e284ac7643c
  - methods/最强写作方法论_全球最强综合版.md
---

# pasindusandamal/kids-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/pasindusandamal/kids-story-generator
- **Stars**：2
- **语言**：Dart
- **License**：None
- **Topics**：—
- **GitHub 描述**：Kids Story Generator is an educational Flutter application that generates child-friendly stories using Ollama AI. The app creates unique, engaging stories based on user prompts while keeping the content appropriate and educational for children.
- **本地描述**：Kids Story Generator is an educational Flutter application that generates child-friendly stories using Ollama AI. The app creates unique, engaging stories based on user prompts while keeping the content appropriate and educational for children.
- **拉取时间**：2026-07-23 23:30:51

---

# 🎨 Kids Story Generator

> 📚 An educational Flutter application that generates child-friendly stories using Ollama AI. The app creates unique, engaging stories based on user prompts while keeping the content appropriate and educational for children.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 AI Stories | Generate unique stories using Ollama AI |
| 👶 Kid-Friendly | Safe and educational content for children |
| 🎯 Simple UI | Intuitive and easy-to-use interface |
| 🛡️ Error Handling | Robust error management and loading states |


## 🚀 Prerequisites

Before you begin, ensure you have the following installed:
* 📱 Flutter SDK
* 🤖 Ollama AI (running locally)
* 📦 Required packages:
  * `http` for API calls
  * `provider` for state management

## 💻 Installation

1. **Clone the repository:**
```bash
git clone [your-repository-url]
```

2. **Install dependencies:**
```bash
flutter pub get
```

3. **Verify Ollama is running locally** on port 11434

4. **Launch the application:**
```bash
flutter run
```

## 📁 Project Structure

```
lib/
├── 🎮 controller/
│   └── story_controller.dart
├── 📊 model/
│   └── story_model.dart
├── 🛠️ services/
│   └── ollama_service.dart
├── 🎨 view/
│   ├── widgets/
│   │   ├── input_prompt.dart
│   │   └── story_display.dart
│   └── story_generator.dart
└── 🚀 main.dart
```

## 🔄 How It Works

1. 📝 User enters a story prompt
2. 🤖 App connects to local Ollama AI
3. ✨ AI generates kid-friendly story
4. 📱 Story displays in scrollable container

## 🛠️ Technical Details

### Architecture
* 🏗️ MVC pattern implementation
* 📊 Provider state management
* 🤖 Ollama AI integration
* ⚡ Async operations handling

### Key Components

```dart
// Story Controller
class StoryController extends ChangeNotifier {
  final TextEditingController promptController = TextEditingController();
  final OllamaService _ollamaService = OllamaService();
  // ...
}

// API Service
class OllamaService {
  Future<String> generateStory(String prompt) async {
    // AI integration logic
  }
}
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/pasindusandamal/kids-story-generator/blob/main/LICENSE.md) file for details.

## 🙏 Acknowledgments

* 💙 Flutter Team
* 🤖 Ollama AI
* 📦 Provider Package

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

