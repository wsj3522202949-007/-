---
id: tool-01658
type: tool
area: 库
status: active
tags: [Svelte, 协议传染, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: book-editor
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/jeasoncc/book-editor
created: 2026-07-18
updated: 2026-07-18
no: 1658
category: 二、网文 / 长篇 AI 写作系统 库
repo: jeasoncc/book-editor
stars: 36
url: https://github.com/jeasoncc/book-editor
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 66caa26db0635f8d
  - methods/最强写作方法论_全球最强综合版.md
---

# jeasoncc/book-editor

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jeasoncc/book-editor
- **Stars**：36
- **语言**：Svelte
- **License**：GPL-3.0
- **Topics**：book, editor, novel, writer
- **GitHub 描述**：Secret Writing is a  next-generation plain text editor engineered for  creative writing,this software that help you to write your novel, in a simple way.
- **本地描述**：Secret Writing is a  next-generation plain text editor engineered for  creative writing,this software that help you to write your novel, in a simple way.
- **拉取时间**：2026-07-23 23:27:24

---


                 ______________________________________________________________________
                /     ___       ____              __      ______    ___ __             \
                |    /   |     / __ )____  ____  / /__   / ____/___/ (_) /_____  _____ |
                |   / /| |    / __  / __ \/ __ \/ //_/  / __/ / __  / / __/ __ \/ ___/ |
                |  / ___ |   / /_/ / /_/ / /_/ / ,<    / /___/ /_/ / / /_/ /_/ / /     |
                | /_/  |_|  /_____/\____/\____/_/|_|  /_____/\__,_/_/\__/\____/_/      |
                \                                                                      /
                 ----------------------------------------------------------------------

![圖片說明](https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_1638,h_920/https://dashboard.snapcraft.io/site_media/appmedia/2022/01/2022-01-08_21-50-45%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE3.jpeg)

![圖片說明2](https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_1638,h_920/https://dashboard.snapcraft.io/site_media/appmedia/2022/01/2022-01-08_21-57-55%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

# 🪶 EpicCraft — The Ultimate Writing Tool for Epic Storytellers

> *“Write boldly. Edit wisely. Dream endlessly.”*

**EpicCraft** (a.k.a. *Book Editor*) is a cross-platform desktop writing tool built for novelists, storytellers, and creative writers.  
It provides a smooth, distraction-free environment with powerful editing blocks, offline data storage, and modern UI — all wrapped in a single elegant app.

---

## ✨ Key Features

- 🧠 **Block-based Writing** — powered by [Editor.js](https://editorjs.io/), offering flexible paragraph, quote, list, and custom writing tools.
- 🎨 **Modern UI** — written in [Svelte](https://svelte.dev/) for smooth performance and simplicity.
- ⚡ **Cross-Platform Desktop App** — built with [Electron](https://www.electronjs.org/), supports Linux, Windows, and macOS.
- 💾 **Offline Local Storage** — built on `localforage` and `SQLite` concepts for fully local writing.
- 🔍 **Fast Search** — `lunr.js`-based full-text search for your entire project.
- 🧩 **Extensible Tools** — supports custom Editor.js plugins such as marker, quote, underline, alerts, and more.
- 📚 **Story Management** — organize chapters, outlines, and notes easily.
- 🧭 **Export Ready** — build distributable packages for all major OS targets.
- 🧱 **Developer Friendly** — includes Storybook, ESLint, Jest, and Prettier setup out of the box.

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend Framework** | [Svelte 3](https://svelte.dev/) |
| **Editor Core** | [Editor.js](https://editorjs.io/) with plugins (quote, list, marker, etc.) |
| **Desktop Runtime** | [Electron 11+](https://www.electronjs.org/) |
| **Data Layer** | LocalForage + RxJS |
| **Build System** | Webpack 5 |
| **UI & Animation** | Animate.css · Anime.js · Tippy.js |
| **Testing** | Jest + @testing-library/svelte |
| **Styling** | SCSS + Prettier + ESLint |
| **Packaging** | electron-builder · electron-packager |

---

## 🧩 Project Structure

```

book-editor/
├── src/
│   ├── electron.js        # Electron main process entry
│   ├── components/        # Svelte UI components
│   ├── editor/            # Editor.js setup & tools
│   ├── assets/            # Static assets
│   ├── styles/            # SCSS stylesheets
│   └── licenses.json
├── build/                 # App icons and packaging configs
├── dist*/                 # Build outputs
├── package.json
└── README.md

````

---

## ⚙️ Installation & Development

### 🧰 Prerequisites
Make sure the following are installed:
- Node.js ≥ 18
- npm or pnpm
- Electron (installed automatically)
- Linux / Windows / macOS environment

### 🏗️ Install dependencies

```bash
npm install
# or
pnpm install
````

### 🧪 Run in Development Mode

```bash
npm run dev
```

### 🧱 Build for Production

```bash
npm run build
```

### 💻 Launch Electron App

```bash
npm run electron
```

---

## 🧳 Packaging & Distribution

You can create platform-specific builds easily:

```bash
# Linux (AppImage / DEB / RPM)
npm run pack:linux
npm run pack:deb

# Windows
npm run pack:win
npm run pack:wininstaller

# macOS
npm run dist
```

Or build all at once:

```bash
npm run dist
```

---

## 🧪 Testing

Run unit tests and integration tests using Jest:

```bash
npm test
```

---

## 🧼 Code Quality

Format and lint automatically:

```bash
npm run prettier
npm run lint
```

---

## 🧱 Storybook (UI Component Playground)

Launch Storybook for Svelte component development:

```bash
npm run storybook
```

Build static Storybook site:

```bash
npm run build-storybook
```

---

## 🧩 Scripts Summary

| Command              | Description                                |
| -------------------- | ------------------------------------------ |
| `npm run dev`        | Start development server with Webpack      |
| `npm run build`      | Build production bundle                    |
| `npm run electron`   | Run Electron app locally                   |
| `npm run lint`       | Fix code style issues                      |
| `npm run prettier`   | Format codebase                            |
| `npm run storybook`  | Run Storybook                              |
| `npm test`           | Run Jest test suite                        |
| `npm run dist`       | Build distributable executables for all OS |
| `npm run pack:linux` | Package Linux AppImage                     |
| `npm run pack:win`   | Package Windows executable                 |

---

## 🪪 License

This project is licensed under the **Apache License 2.0**.
You are free to use, modify, and distribute it, provided that you retain this license and notice.

See the [LICENSE](https://github.com/jeasoncc/book-editor/blob/main/LICENSE) file for details.

---

## 👤 Author

**Martin (jeasoncc)**
📧 `xiaomiquan@aliyun.com`
🌍 [GitHub Profile](https://github.com/jeasoncc)

---

## 🌟 Contributing

We welcome contributions from the community!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m "Add awesome feature"`)
4. Push the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request 🚀

---

## 🧭 Roadmap

* [x] Core writing editor
* [x] Electron desktop integration
* [ ] Multi-tab support
* [ ] Export as Markdown / PDF
* [ ] Cloud sync (Appwrite planned)
* [ ] Theme customization
* [ ] Plugin ecosystem

---

## 💬 Community

If you like this project, please **⭐ star it** on GitHub!
You can also file issues or suggestions via [GitHub Issues](https://github.com/jeasoncc/book-editor/issues).

> 🪶 *EpicCraft — A writing tool made by storytellers, for storytellers.*




![GitHub](https://img.shields.io/github/license/jeasoncc/Secret-writing)   ![GitHub repo size](https://img.shields.io:/github/repo-size/jeasoncc/Secret-writing)   ![GitHub language count](https://img.shields.io:/github/languages/count/jeasoncc/Secret-writing)   ![GitHub Repo stars](https://img.shields.io:/github/stars/jeasoncc/Secret-writing?style=social)


[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/xiaomiquan)
[![安裝軟體敬請移駕 Snap Store](https://snapcraft.io/static/images/badges/tw/snap-store-black.svg)](https://snapcraft.io/xiaomiquan)

```
    +----------+     +------------+     +------------+
    | Electron | --> |            | <-- | Typescript |
    +----------+     | BookEditor |     +------------+
                     |            |     +------------+
                     |            | <-- | LocalForge |
                     +------------+     +------------+
                       ^
                       |
                       |
                     +------------+
                     |  Sevelte   |
                     +---------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---+


```
