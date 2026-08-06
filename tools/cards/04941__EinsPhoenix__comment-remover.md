---
id: tool-04941
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: comment-remover
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/einsphoenix/comment-remover
created: 2026-07-18
updated: 2026-07-18
no: 4941
category: 一、去 AI 味 / Humanizer 库
repo: EinsPhoenix/comment-remover
stars: 0
url: https://github.com/einsphoenix/comment-remover
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# EinsPhoenix/comment-remover

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/einsphoenix/comment-remover
- **Stars**：0
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Clean up AI-generated code directly inside VS Code. Less slop, more ship. And no more 1 line code, 1 line comment.
- **本地描述**：Clean up AI-generated code directly inside VS Code. Less slop, more ship. And no more 1 line code, 1 line comment.
- **拉取时间**：2026-07-25 18:00:15

---

<div align="center">

# 🧹 Comment Remover

### Clean up your code by removing comments with a single click!

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/EinsPhoenix/comment-remover)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://buymeacoffee.com/einsphoenix)

---

</div>

## 📖 What is Comment Remover?

**Comment Remover** is a powerful VS Code extension that helps you clean up your codebase by removing comments from your files and folders with ease. Whether you're preparing code for production, creating clean examples, or just want a comment-free view of your code, this extension has you covered!

### Key Features

- **Remove comments from single files or entire folders**
- **Undo functionality** - Made a mistake? No problem!
- **Smart comment detection** - Handles line comments (`//`, `#`) and block comments (`/* */`)
- **Preserve special comments** - Keep JSDoc, TODOs, or custom-prefixed comments
- **Flexible ignore patterns** - Skip specific files, folders, or patterns
- **Highly configurable** - Customize the behavior to fit your needs
- **Multi-language support** - Works with JavaScript, TypeScript, Python, Java, C++, and more!

---

## 🚀 How to Use

### Remove Comments from a Single File

Right-click on any file in the Explorer and select **"Remove Comments"**:

![Remove Comments from File](https://raw.githubusercontent.com/EinsPhoenix/comment-remover/refs/heads/main/images/remove-comments-file.png)

### Remove Comments from an Entire Folder

Right-click on any folder in the Explorer and select **"Remove Comments from Folder"**:

![Remove Comments from Folder](https://raw.githubusercontent.com/EinsPhoenix/comment-remover/refs/heads/main/images/remove-comments-folder.png)

### Made a mistake?

No worries! After removing comments, all changes are clearly displayed. You can review changes individually and easily undo any modifications if needed:
![View removed comments](https://raw.githubusercontent.com/EinsPhoenix/comment-remover/refs/heads/main/images/RemovedComments.png)

With the **Keep** or **Undo** buttons, you decide which files to keep or restore:
![Keep or Undo](https://raw.githubusercontent.com/EinsPhoenix/comment-remover/refs/heads/main/images/Keep.png)

### Command Palette

You can also access all commands through the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`):

- `Comment Remover: Remove Comments` - Remove comments from current file
- `Comment Remover: Remove Comments from Folder` - Remove comments from selected folder
- `Comment Remover: Undo Last Comment Removal` - Undo the last operation
- `Comment Remover: Add Ignore Pattern` - Add files/patterns to ignore
- `Comment Remover: Add Preserve Comment Prefix` - Preserve comments with specific prefixes
- `Comment Remover: Show All Settings` - View current configuration

---

## Configuration

Customize the extension's behavior in your VS Code settings:

![Settings](https://raw.githubusercontent.com/EinsPhoenix/comment-remover/refs/heads/main/images/Settings.png)

---

## Examples

### Before
```javascript
// This is a line comment
function calculateSum(a, b) {
    /* This is a block comment
       that spans multiple lines */
    return a + b;
}

// TODO: This will be preserved if configured
const result = calculateSum(5, 3);
```

### After (with default settings)
```javascript
function calculateSum(a, b) {
    return a + b;
}

const result = calculateSum(5, 3);
```

---

## Use Cases

- **Production Deployment** - Remove comments before deploying to reduce file size
- **Code Sharing** - Share clean code snippets without internal comments
- **Documentation** - Create clean code examples for documentation
- **Learning** - Study code structure without comment distractions
- **Code Review** - Focus on the actual code implementation

---

## Support & Feedback

### Thank You!

Thank you so much for using **Comment Remover**! I hope this extension makes your coding life a little easier and your codebase a little cleaner. Your support and feedback mean the world to me!

If you encounter any issues or have suggestions for improvements, please feel free to:
- 🐛 [Report bugs on GitHub](https://github.com/EinsPhoenix/comment-remover/issues)
- 💡 [Request features](https://github.com/EinsPhoenix/comment-remover/issues)
- ⭐ [Star the repository](https://github.com/EinsPhoenix/comment-remover)

### Buy Me a Coffee ☕

If you find this extension helpful and want to support its development, consider buying me a coffee! Your support helps me maintain and improve this extension, but it's completely optional - the extension will always be free to use.

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-☕%20Support%20Development-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://buymeacoffee.com/einsphoenix)

Every coffee keeps the code flowing! ☕✨

---

## License

This extension is released under the MIT License. See the [LICENSE](https://github.com/EinsPhoenix/comment-remover/blob/main/LICENSE) file for details.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<div align="center">

**Made with ❤️ by [einsphoenix](https://buymeacoffee.com/einsphoenix)**

*Happy Coding! 🚀*

</div>
