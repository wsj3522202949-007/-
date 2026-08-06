---
id: tool-01049
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: story-prompt-helper
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/iqbal-rashed/story-prompt-helper
created: 2026-07-18
updated: 2026-07-18
no: 1049
category: 二、网文 / 长篇 AI 写作系统 库
repo: iqbal-rashed/story-prompt-helper
stars: 0
url: https://github.com/iqbal-rashed/story-prompt-helper
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# iqbal-rashed/story-prompt-helper

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/iqbal-rashed/story-prompt-helper
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：ai, creative-writing, llm, openai, prompt-generator, story, writing
- **GitHub 描述**：Quickly generate story prompts and auto-insert them into ChatGPT and Gemini for faster story writing.
- **本地描述**：Quickly generate story prompts and auto-insert them into ChatGPT and Gemini for faster story writing.
- **拉取时间**：2026-07-23 23:09:35

---

<p align="center">
  <img src="public/icons/icon-128.png" alt="Story Prompt Helper Logo" width="128" height="128">
</p>

<h1 align="center">Story Prompt Helper for ChatGPT & Gemini</h1>

<p align="center">
  <strong>🚀 Generate professional story prompts and auto-insert them into ChatGPT or Gemini with one click!</strong>
</p>

<p align="center">
  <a href="https://chromewebstore.google.com/detail/kmdmhfblcaconcihgbddmhimafifpjib?utm_source=item-share-cb">
    <img src="https://img.shields.io/chrome-web-store/v/kmdmhfblcaconcihgbddmhimafifpjib?style=for-the-badge&logo=googlechrome&logoColor=white&label=Chrome%20Web%20Store" alt="Chrome Web Store">
  </a>
  <img src="https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=white" alt="React 19">
  <img src="https://img.shields.io/badge/TypeScript-5.9-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Vite-7-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite">
  <img src="https://img.shields.io/badge/Manifest-V3-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Manifest V3">
</p>

---

## ✨ Features

- 🎯 **One-Click Prompt Injection** — Generate and send prompts directly to ChatGPT or Gemini without copy-pasting
- 🎭 **Rich Customization** — Fine-tune genre, tone, language, audience, pacing, and more
- 📝 **Smart Prompt Engineering** — Automatically crafts professional-grade prompts using best practices
- 🌍 **Multi-Language Support** — Write stories in English, Bengali, Hindi, Spanish, French, or German
- ⌨️ **Keyboard Shortcut** — Quick access with `Ctrl+Shift+Y` (Windows) or `Cmd+Shift+Y` (Mac)
- 🌙 **Beautiful Dark UI** — Modern, sleek interface that matches your workflow
- 🔒 **Privacy First** — No API calls, no data collection — everything runs locally

---

## 📥 Installation

### From Chrome Web Store (Recommended)

<p align="center">
  <a href="https://chromewebstore.google.com/detail/kmdmhfblcaconcihgbddmhimafifpjib?utm_source=item-share-cb">
    <img src="https://developer.chrome.com/static/docs/webstore/branding/image/YT2Grfi9vEBa2wAPzhWa.png" alt="Available in the Chrome Web Store" width="248">
  </a>
</p>

1. Click the badge above or visit the [Chrome Web Store](https://chromewebstore.google.com/detail/kmdmhfblcaconcihgbddmhimafifpjib?utm_source=item-share-cb)
2. Click **"Add to Chrome"**
3. Pin the extension to your toolbar for quick access

### Manual Installation (Developer Mode)

1. Clone this repository:
   ```bash
   git clone https://github.com/iqbal-rashed/story-prompt-helper.git
   cd story-prompt-helper
   ```

2. Install dependencies and build:
   ```bash
   yarn install
   yarn build
   ```

3. Load the extension in Chrome:
   - Navigate to `chrome://extensions/`
   - Enable **Developer mode** (toggle in top-right)
   - Click **"Load unpacked"**
   - Select the `dist` folder

---

## 🎮 Usage

1. **Open ChatGPT or Gemini** in your browser
2. **Click the extension icon** or press `Ctrl+Shift+Y` (`Cmd+Shift+Y` on Mac)
3. **Describe your story idea** — just 1-3 sentences is enough!
4. **Customize settings** — adjust genre, tone, length, and other options
5. **Click "Send to Chat"** — the prompt is automatically inserted and ready to go!

> 💡 **Tip:** The extension doesn't call any AI APIs itself. It crafts professional prompts and injects them directly into the chat interface, giving you full control.

---

## ⚙️ Customization Options

| Category | Options |
|----------|---------|
| **Genre** | Sci-Fi, Fantasy, Drama, Comedy, Horror, Romance, Mystery |
| **Tone** | Dramatic, Upbeat, Mysterious, Humorous, Dark, Romantic |
| **Language** | English, Bengali, Hindi, Spanish, French, German |
| **Audience** | General, Kids, Teens, Adults, Family |
| **Pacing** | Slow, Moderate, Fast, Dynamic |
| **POV** | First-person, Third-person limited, Third-person omniscient |
| **Time Period** | Present day, Near future, Far future, Historical, Unspecified |
| **Ending Type** | Happy, Sad, Bittersweet, Open-ended, Twist, No preference |
| **Writing Style** | Simple & clear, Poetic & descriptive, Fast-paced & punchy, Light & humorous |
| **Content Rating** | No limits, PG, PG-13, R |
| **Story Length** | 50 - 500 words |
| **Characters** | 1 - 10 main characters |

### Additional Controls

- ✅ **Include Narration** — Rich, descriptive narration
- ✅ **Include Dialogue** — Natural, character-revealing dialogue
- ✅ **Include Plot Twist** — Add surprising but believable plot twists
- 📌 **Must Include** — Specify elements that must appear in the story
- 🚫 **Avoid** — Specify themes or elements to exclude

---

## 🛠️ Development

### Prerequisites

- Node.js 18+
- Yarn or npm

### Setup

```bash
# Clone the repository
git clone https://github.com/iqbal-rashed/story-prompt-helper.git
cd story-prompt-helper

# Install dependencies
yarn install

# Start development server
yarn dev

# Build for production
yarn build

# Run linting
yarn lint
```

### Tech Stack

| Technology | Purpose |
|------------|---------|
| **React 19** | UI framework |
| **TypeScript 5.9** | Type-safe JavaScript |
| **Vite 7** | Build tool & dev server |
| **Tailwind CSS 4** | Styling |
| **Radix UI** | Accessible UI primitives |
| **React Hook Form** | Form state management |
| **Lucide React** | Icon library |

### Project Structure

```
story-prompt-helper/
├── public/
│   ├── background.js       # Service worker for message handling
│   ├── content-script.js   # Injects prompts into ChatGPT/Gemini
│   ├── manifest.json       # Chrome extension manifest (V3)
│   └── icons/              # Extension icons
├── src/
│   ├── App.tsx             # Main popup component
│   ├── components/         # Reusable UI components
│   ├── hooks/              # Custom React hooks
│   ├── lib/                # Utility functions
│   └── index.css           # Global styles
├── dist/                   # Built extension (load this in Chrome)
└── docs/                   # Documentation
```

---

## 🌐 Supported Platforms

| Platform | Status |
|----------|--------|
| ChatGPT (`chatgpt.com`) | ✅ Fully Supported |
| ChatGPT Legacy (`chat.openai.com`) | ✅ Fully Supported |
| Google Gemini (`gemini.google.com`) | ✅ Fully Supported |

---

## 🔒 Privacy & Security

- **No API calls** — The extension never sends your data anywhere
- **No tracking** — Zero analytics or telemetry
- **Local processing** — All prompt generation happens in your browser
- **Minimal permissions** — Only requires `activeTab` to inject prompts
- **Open source** — Fully auditable code

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](https://github.com/iqbal-rashed/story-prompt-helper/blob/main/LICENSE).

---

## 💬 Feedback & Support

- 🐛 **Report bugs** — [Open an issue](https://github.com/iqbal-rashed/story-prompt-helper/issues)
- 💡 **Feature requests** — [Start a discussion](https://github.com/iqbal-rashed/story-prompt-helper/discussions)
- ⭐ **Like this project?** — Give it a star on [GitHub](https://github.com/iqbal-rashed/story-prompt-helper)!

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<p align="center">
  Made with ❤️ for storytellers and AI enthusiasts
</p>
