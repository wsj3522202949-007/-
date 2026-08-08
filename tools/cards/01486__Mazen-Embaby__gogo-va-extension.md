---
id: tool-01486
type: tool
area: 库
status: active
tags: [TypeScript, 协议传染, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: gogo-va-extension
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/mazen-embaby/gogo-va-extension
created: 2026-07-18
updated: 2026-07-18
no: 1486
category: 二、网文 / 长篇 AI 写作系统 库
repo: Mazen-Embaby/gogo-va-extension
stars: 1
url: https://github.com/mazen-embaby/gogo-va-extension
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 13e25398bbd86317
  - methods/最强写作方法论_全球最强综合版.md
---

# Mazen-Embaby/gogo-va-extension

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mazen-embaby/gogo-va-extension
- **Stars**：1
- **语言**：TypeScript
- **License**：GPL-3.0
- **Topics**：angular, chatbot, chrome-ai, chrome-extension, custom-components, custom-elements, gemini-api, gemini-chat, gemini-nano, summarize, tailwindcss, translate
- **GitHub 描述**：🚀 GoGo VA is a chrome-extension born out of the need for a tool that simplifies writing tasks while offering the power of advanced AI models. We wanted to create an AI assistant that works entirely offline, giving users privacy and efficiency, all without the need for an internet connection.
- **本地描述**：🚀 GoGo VA is a chrome-extension born out of the need for a tool that simplifies writing tasks while offering the power of advanced AI models. We wanted to create an AI assistant that works entirely offline, giving users privacy and efficiency, all without the need for an internet connection.
- **拉取时间**：2026-07-23 23:22:25

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# GogoVA Chrome Extension 🚀



Check out this [YouTube video](https://www.youtube.com/watch?v=LS5fnL6I3X4).



**prompt-chat**

![Chat with](https://raw.githubusercontent.com/Mazen-Embaby/gogo-va-extension/refs/heads/main/screenshots/Screenshot%20from%202025-01-22%2009-44-35.png)



**Chat History**

![](https://raw.githubusercontent.com/Mazen-Embaby/gogo-va-extension/refs/heads/main/screenshots/Screenshot%20from%202025-01-22%2009-45-55.png)



**Start to write Paragraph, Email, Comment, or Message**

![](https://raw.githubusercontent.com/Mazen-Embaby/gogo-va-extension/refs/heads/main/screenshots/Screenshot%20from%202025-01-22%2009-46-05.png)



**Start to summarize web content**

![](https://raw.githubusercontent.com/Mazen-Embaby/gogo-va-extension/refs/heads/main/screenshots/Screenshot%20from%202025-01-22%2009-46-27.png)



**Simultaneous translation**

![](https://raw.githubusercontent.com/Mazen-Embaby/gogo-va-extension/refs/heads/main/screenshots/Screenshot%20from%202025-01-22%2009-46-41.png)



**Writing Assistance**

![](https://raw.githubusercontent.com/Mazen-Embaby/gogo-va-extension/refs/heads/main/screenshots/Screenshot%20from%202025-01-22%2009-47-25.png)



## Inspiration

GoGo VA is a chrome-extension was born out of the need for a tool that simplifies writing tasks while offering the power of advanced AI models. We wanted to create an AI assistant that works entirely offline, giving users privacy and efficiency, all without the need for an internet connection.

## What it does

GoGo VA revolutionizes the writing experience by offering powerful tools for prompt generation, translation, summarization, and more. Whether you're brainstorming ideas, translating text, or summarizing long documents, GoGo VA is designed to help you get your work done faster and more effectively—all from the comfort of your own device.

## Key Features
- 🛠️ **Vite**: for lightning-fast development and hot module replacement.

- 🧰 **TypeScript**: for type safety and enhanced productivity.

- ⚛️ **angular**: for building dynamic and interactive UI components.

- 📦 **CRX**: custom element

- 🎨 **Tailwind CSS**: for hassle-free styling, including seamless integration in content scripts.

  🎨 **Angular Material**: for hassle-free styling, including seamless integration in content scripts.


## Requirements

🚍 Google Chrome Canary

🔧 Enable & Download built-in chrome AI API [ prompt, summarize,  ]

## Usage Instructions

1. 📥 Clone the repository.
2. 🔧 Install dependencies with `npm install`.
3. 🚀 build the extension with `npm run build:extension`.
4. 🏗️ In chrome select manage extension then load unpacked then the directory build.

## Development & Contribution

#### Inject component Angular 18

1. To inject an angular component register it first as a web component in `main.ts`

     ```typescript
     createApplication()
       .then((app) => {
         const component = createCustomElement(SimpleComponent, {
           injector: app.injector,
         });
         customElements.define('app-simple', component);
       })
       .catch((err) => console.error(err));
     
     bootstrapApplication(AppComponent, appConfig).catch((err) =>
       console.error(err),
     );
     ```

     

2. Inject the registered component through the code below 

     ```typescript
       const webComponentTag = 'app-simple';
     
       let componentElement = document.querySelector(webComponentTag);
     
       if (!componentElement) {
         componentElement = document.createElement(webComponentTag);
         componentElement.id = 'angular-chrome-app';
         document.body.appendChild(componentElement);
     
         // Load Angular's compiled scripts & Inject the Angular main.js script
         const angularScript = document.createElement('script');
         angularScript.type = 'module'; // Ensure it's treated as an ES module
         const moduleUrl = chrome.runtime.getURL('main.js');
         angularScript.src = moduleUrl;
         document.body.appendChild(angularScript);
       }
     ```

## Enhancement To Do
- [ ] custom webpack build on watch to serve
- [ ] text-checker:
  - [ ] sync the scroll of textarea to text-checker
  - [ ] click to the propose (suggestion) visible the cursor
