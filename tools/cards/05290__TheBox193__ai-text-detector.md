---
id: tool-05290
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/thebox193/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5290
category: 一、去 AI 味 / Humanizer 库
repo: TheBox193/ai-text-detector
stars: 5
url: https://github.com/thebox193/ai-text-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1034e092e52f326d
  - methods/改稿润色指令库.md
---

# TheBox193/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/thebox193/ai-text-detector
- **Stars**：5
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Detect and highlight any text that looks AI-generated!
- **本地描述**：Detect and highlight any text that looks AI-generated!
- **拉取时间**：2026-07-25 18:13:06

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

This is a [Plasmo extension](https://docs.plasmo.com/) project bootstrapped with [`plasmo init`](https://www.npmjs.com/package/plasmo).

## Getting Started

First, run the development server:

```bash
pnpm dev
# or
npm run dev
```

Open your browser and load the appropriate development build. For example, if you are developing for the chrome browser, using manifest v3, use: `build/chrome-mv3-dev`.

You can start editing the popup by modifying `popup.tsx`. It should auto-update as you make changes. To add an options page, simply add a `options.tsx` file to the root of the project, with a react component default exported. Likewise to add a content page, add a `content.ts` file to the root of the project, importing some module and do some logic, then reload the extension on your browser.

For further guidance, [visit our Documentation](https://docs.plasmo.com/)

## Making production build

Run the following:

```bash
pnpm build
# or
npm run build
```

This should create a production bundle for your extension, ready to be zipped and published to the stores.

## Safari build (framework-native)

Run the Safari target build:

```bash
yarn build:safari
```

This creates `build/safari-mv3-prod` and `build/safari-mv3-prod.zip`. To ship for Safari, run Apple's
`safari-web-extension-converter` on the build output to generate an Xcode project for signing and distribution.

## Submit to the webstores

The easiest way to deploy your Plasmo extension is to use the built-in [bpp](https://bpp.browser.market) GitHub action. Prior to using this action however, make sure to build your extension and upload the first version to the store to establish the basic credentials. Then, simply follow [this setup instruction](https://docs.plasmo.com/framework/workflows/submit) and you should be on your way for automated submission!
