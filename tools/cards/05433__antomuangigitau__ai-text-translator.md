---
id: tool-05433
type: tool
area: 库
status: active
tags: [Claude插件, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: ai-text-translator
summary: Claude Code 插件式写作流
source: https://github.com/antomuangigitau/ai-text-translator
created: 2026-07-18
updated: 2026-07-18
no: 5433
category: 一、去 AI 味 / Humanizer 库
repo: antomuangigitau/ai-text-translator
stars: 0
url: https://github.com/antomuangigitau/ai-text-translator
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 3d34977a5d7e0d22
  - methods/改稿润色指令库.md
---

# antomuangigitau/ai-text-translator

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/antomuangigitau/ai-text-translator
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Text-Translator-Language-Detector
- **本地描述**：Text-Translator-Language-Detector
- **拉取时间**：2026-07-25 18:18:28

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default tseslint.config({
  languageOptions: {
    // other options...
    parserOptions: {
      project: ['./tsconfig.node.json', './tsconfig.app.json'],
      tsconfigRootDir: import.meta.dirname,
    },
  },
})
```

- Replace `tseslint.configs.recommended` to `tseslint.configs.recommendedTypeChecked` or `tseslint.configs.strictTypeChecked`
- Optionally add `...tseslint.configs.stylisticTypeChecked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and update the config:

```js
// eslint.config.js
import react from 'eslint-plugin-react'

export default tseslint.config({
  // Set the react version
  settings: { react: { version: '18.3' } },
  plugins: {
    // Add the react plugin
    react,
  },
  rules: {
    // other rules...
    // Enable its recommended rules
    ...react.configs.recommended.rules,
    ...react.configs['jsx-runtime'].rules,
  },
})
```
