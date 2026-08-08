---
id: tool-00344
type: tool
area: 库
status: active
tags: [Claude插件, HTML, 协议未明, 本地优先, 英文文档, 本地写作]
title: copilot-with-react
summary: Claude Code 插件式写作流
source: https://github.com/raghu04/copilot-with-react
created: 2026-07-18
updated: 2026-07-18
no: 344
category: 二、网文 / 长篇 AI 写作系统 库
repo: raghu04/copilot-with-react
stars: 0
url: https://github.com/raghu04/copilot-with-react
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 36a5199bed0e7e14
  - methods/最强写作方法论_全球最强综合版.md
---

# raghu04/copilot-with-react

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/raghu04/copilot-with-react
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：This project is a **React.js web application** designed to explore and understand **GitHub Copilot's capabilities** in writing efficient, structured, and scalable code. It covers component creation, API integration, state management, and UI enhancements with AI-assisted coding.  
- **本地描述**：This project is a **React.js web application** designed to explore and understand **GitHub Copilot's capabilities** in writing efficient, structured, and scalable code. It covers component creation, API integration, state management, and UI enhancements with AI-assisted coding.
- **拉取时间**：2026-07-23 22:49:07

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default tseslint.config({
  extends: [
    // Remove ...tseslint.configs.recommended and replace with this
    ...tseslint.configs.recommendedTypeChecked,
    // Alternatively, use this for stricter rules
    ...tseslint.configs.strictTypeChecked,
    // Optionally, add this for stylistic rules
    ...tseslint.configs.stylisticTypeChecked,
  ],
  languageOptions: {
    // other options...
    parserOptions: {
      project: ['./tsconfig.node.json', './tsconfig.app.json'],
      tsconfigRootDir: import.meta.dirname,
    },
  },
})
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default tseslint.config({
  plugins: {
    // Add the react-x and react-dom plugins
    'react-x': reactX,
    'react-dom': reactDom,
  },
  rules: {
    // other rules...
    // Enable its recommended typescript rules
    ...reactX.configs['recommended-typescript'].rules,
    ...reactDom.configs.recommended.rules,
  },
})
```
