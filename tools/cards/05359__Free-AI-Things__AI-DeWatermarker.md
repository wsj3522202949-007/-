---
id: tool-05359
type: tool
area: 库
status: active
tags: [TypeScript, 协议传染, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-DeWatermarker
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/free-ai-things/ai-dewatermarker
created: 2026-07-18
updated: 2026-07-18
no: 5359
category: 一、去 AI 味 / Humanizer 库
repo: Free-AI-Things/AI-DeWatermarker
stars: 15
url: https://github.com/free-ai-things/ai-dewatermarker
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Free-AI-Things/AI-DeWatermarker

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/free-ai-things/ai-dewatermarker
- **Stars**：15
- **语言**：TypeScript
- **License**：GPL-3.0
- **Topics**：ai, ai-mark, ai-watermark, ai-watermark-remover, homoglyph-detection, llm, open-source, text-cleaner, text-obfuscation, unicode-detection, zero-width-characters
- **GitHub 描述**：🛡️ AI DeWatermarker — Real-time AI watermark & text obfuscation detector and cleaner. Detects hidden Unicode, invisible characters, and homoglyph attacks — all processed locally in your browser for full privacy.
- **本地描述**：🛡️ AI DeWatermarker — Real-time AI watermark & text obfuscation detector and cleaner. Detects hidden Unicode, invisible characters, and homoglyph attacks — all processed locally in your browser for full privacy.
- **拉取时间**：2026-07-25 18:15:39

---


# 🛡️ AI DeWatermarker

<div align="center">

**Real-time detection and removal of AI watermarks, invisible Unicode, and text obfuscation**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![React](https://img.shields.io/badge/React-18.3.1-61DAFB?logo=react)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8.3-3178C6?logo=typescript)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-5.4.19-646CFF?logo=vite)](https://vitejs.dev/)

[Features](#-features) • [How It Works](#-how-it-works) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

AI DeWatermarker is a free, open-source tool that detects and removes hidden AI watermarks and text obfuscation from text content. All processing happens **locally in your browser** - ensuring complete privacy and security. Just visit to use: https://ai-de-watermarker.vercel.app/.  
<img width="1920" height="922" alt="chrome_tKFFaSJzir" src="https://github.com/user-attachments/assets/f8959eb5-7fbd-489c-a132-9f34f2c94399" />
<img width="1920" height="922" alt="chrome_gybc802wRX" src="https://github.com/user-attachments/assets/e18e6005-0a3b-4f7f-83a9-141b4d6d9cb4" />

## ✨ Features

### 🔍 Comprehensive Detection

- **Zero-Width Characters**: Detects invisible tracking characters like Zero Width Space (U+200B), Zero Width Non-Joiner, and more
- **Invisible Characters**: Finds hidden Unicode like soft hyphens, combining grapheme joiners, and variation selectors
- **Homoglyphs**: Identifies look-alike characters from different scripts (Cyrillic, Greek, Latin)
- **Bidirectional Marks**: Detects direction control characters used for text obfuscation
- **Suspicious Punctuation**: Identifies non-standard quotes, dashes, and ellipsis
- **Special Spaces**: Finds non-breaking spaces, em spaces, and other unusual whitespace
- **Mixed Scripts**: Detects mixing of different writing systems
- **Control Characters**: Identifies C0/C1 control codes and tag characters 

### 🎯 Advanced Analysis

- **Noise Score**: Calculates the percentage of suspicious characters in your text
- **Real-time Highlighting**: Visual indicators show exactly where issues are detected
- **Line Density Analysis**: Identifies heavily obfuscated sections
- **Pattern Detection**: Finds repeating invisible character sequences and unmatched bidi pairs
- **Encoded Data Detection**: Identifies potential Base64 or hex-encoded watermarks 

### 🧹 Intelligent Cleaning

- **Unicode Normalization**: Converts text to NFC (Normal Form Composed)
- **Homoglyph Replacement**: Replaces look-alike characters with standard equivalents
- **Whitespace Normalization**: Collapses multiple spaces and standardizes line endings
- **Control Character Removal**: Strips out harmful control codes
- **Punctuation Standardization**: Converts fancy quotes and dashes to ASCII equivalents

### 🔒 Privacy-First

- **100% Client-Side**: All processing happens in your browser
- **No Data Collection**: Your text never leaves your device
- **No Server Calls**: Works completely offline after initial load
- **Open Source**: Fully transparent and auditable code

## 🚀 How It Works

1. **Paste or type** your suspicious text into the input area
2. **Real-time analysis** detects all types of watermarks and obfuscation
3. **Visual highlights** show exactly where issues are found
4. **Detailed report** breaks down each type of detection
5. **Clean output** provides sanitized text ready to copy

## 💻 Installation

### Prerequisites

- Node.js 18+ and npm/yarn/pnpm

### Steps

```bash
# Clone the repository
git clone https://github.com/maruf009sultan/AI-DeWatermarker.git

# Navigate to the project directory
cd AI-DeWatermarker

# Install dependencies
npm install

# Start the development server
npm run dev

# Build for production
npm run build
```

## 🎮 Usage

### Basic Usage

1. Open the application in your browser
2. Paste text into the "Suspicious Text" area
3. View the real-time detection report on the right
4. Copy the cleaned text from the "Cleaned Output" section

### Understanding the Detection Report

- **Noise Score**: Higher percentages indicate more obfuscation
  - 0-5%: Clean or minimal obfuscation
  - 5-10%: Moderate watermark presence
  - 10%+: High suspicion of AI watermarking

- **Color Coding**:
  - 🔴 Red: Invisible characters and bidi marks
  - 🟡 Amber: Homoglyphs
  - 🔵 Blue: Suspicious punctuation
  - 🟣 Purple: Special spaces 

## 🛠️ Tech Stack

- **Frontend Framework**: React 18.3.1 with TypeScript
- **Build Tool**: Vite 5.4.19
- **UI Components**: shadcn/ui (Radix UI primitives)
- **Styling**: Tailwind CSS with custom animations
- **State Management**: React Query (TanStack Query)
- **Routing**: React Router DOM
- **Form Handling**: React Hook Form with Zod validation
- **Icons**: Lucide React
- **Notifications**: Sonner

## 📁 Project Structure

```
AI-DeWatermarker/
├── src/
│   ├── components/      # Reusable UI components
│   ├── pages/          # Page components
│   ├── utils/          # Detection and cleaning utilities
│   ├── lib/            # Library configurations
│   └── hooks/          # Custom React hooks
├── public/             # Static assets
└── index.html          # Entry HTML file
```

## 🧪 Detection Examples

### Zero-Width Characters
Invisible tracking characters embedded between words or letters to create unique fingerprints.

### Homoglyphs
Using Cyrillic 'а' (U+0430) instead of Latin 'a' (U+0061) to create visually identical but technically different text.

### Bidirectional Marks
RTL/LTR override characters that can hide or obfuscate text content. 

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow the existing code style
- Write clear commit messages
- Add tests for new features
- Update documentation as needed

## 📜 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/Free-AI-Things/AI-DeWatermarker/blob/main/LICENSE) file for details. 

## 🌟 Why AI DeWatermarker?

- **Educational**: Learn about Unicode obfuscation techniques
- **Practical**: Clean text from AI-generated content
- **Transparent**: Open-source and community-driven
- **Fast**: Real-time processing with no server delays
- **Comprehensive**: Detects 14+ types of obfuscation patterns

## 🔗 Links

- [Report a Bug](https://github.com/maruf009sultan/AI-DeWatermarker/issues)
- [Request a Feature](https://github.com/maruf009sultan/AI-DeWatermarker/issues)
- [Contribute](https://github.com/maruf009sultan/AI-DeWatermarker/pulls)

## 💖 Acknowledgments

Made with ❤️ for the open-source community. Special thanks to all contributors and users who make this project better.

---

<div align="center">

**[⬆ Back to Top](#-ai-dewatermarker)**

If you find this project useful, please consider giving it a ⭐ on GitHub!

</div>

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---
