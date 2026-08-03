---
id: tool-00003
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: bramble
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/lovemecomputer/bramble
created: 2026-07-18
updated: 2026-07-18
$1348
category: 二、网文 / 长篇 AI 写作系统 库
repo: lovemecomputer/bramble
stars: 43
language: JavaScript
license: MIT
url: https://github.com/lovemecomputer/bramble
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# bramble 🌱

### An interactive fiction or dialog editor

![bramble graph example](https://i.imgur.com/1by9sFs.gif "Bramble Graph Example")

Inspired by [Twine](https://twinery.org/), [Yarn](https://github.com/InfiniteAmmoInc/Yarn), and the like.

---

Heavily in alpha. Approaching a point of testing, feedback, and input if you would like to get involved.

[some progress posted to twitter](https://twitter.com/search?q=bramble%20from%3Aanimalphase&src=typd)

---

A native desktop app running in Electron. Started from this boilerplate: https://github.com/chentsulin/electron-react-boilerplate

---

## Installation

Clone this repository and run `npm install` in the folder.

---

## Usage

#### Running in dev mode:

This starts the renderer process in hot-module-replacement mode and starts a server sends hot updates to the renderer process (seems like this only needs to be run once?):

`$ npm run dev`

Run these two commands simultaneously in different console tabs to initiate dev rendering & hot-swap:

- `$ npm run hot-updates-server`

- `$ npm run start-hot-renderer`

---

## Contribute

### // TODO

 - In `state-return.js`, create an option that returns only relevant properties for rendering SVG arrows.
 - Add HTML export functionality.
 - Reorganize how projects are saved to include local media and other future user-generated assets.
 - Have new patches created in a context-informed location.
 - Add ability to move through link destinations by using arrow keys.
 - Move keypresses to Electron API.
 - Add ability to search patches.
 - Add zooming functionality.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Bramble is brought to you by [Audrey Moon](http://loveme.computer/) aka [animalphase](http://animalphase.com/).

Contact me on [twitter](https://twitter.com/animalphase)
