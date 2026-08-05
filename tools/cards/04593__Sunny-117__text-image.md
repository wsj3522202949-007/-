---
id: tool-04593
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 中文友好, 本地写作]
title: text-image
summary: 本地优先、隐私可控的写作工作台
source: https://github.com/sunny-117/text-image
created: 2026-07-18
updated: 2026-07-18
no: 4593
category: 五、写作 IDE / 本地优先工作台 库
repo: Sunny-117/text-image
stars: 4
url: https://github.com/sunny-117/text-image
tier: "B"
use_case: "本地优先、隐私可控的写作工作台"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# Sunny-117/text-image

- **分类**：五、写作 IDE / 本地优先工作台 库
- **链接**：https://github.com/sunny-117/text-image
- **Stars**：4
- **语言**：JavaScript
- **License**：None
- **Topics**：ai, code-formatter, detector, formatter, plugin
- **GitHub 描述**：🐛🐛🐛 Text image can "textify" text, images, and videos, and can be used with simple configuration 它可以将文字、图片、视频进行「文本化」 只需要通过简单的配置即可使用
- **本地描述**：🐛🐛🐛 Text image can "textify" text, images, and videos, and can be used with simple configuration 它可以将文字、图片、视频进行「文本化」 只需要通过简单的配置即可使用
- **拉取时间**：2026-07-25 17:49:41

related:
  - methods/QUICK_START.md
---

# text-image

![](./logo.png)

English|`[简体中文](./README-zh.md)`

🐛🐛🐛 `text-image` can "textify" text, images, and videos, and can be used with simple configuration


## Website

https://sunny-117.github.io/text-image/

## Install

```bash
npm i @sunny-117/text-image
```

## Usage

```js
import { createTextImage } from '@sunny-117/text-image'
```

### Draw text

```js
import { createTextImage } from '@sunny-117/text-image'
createTextImage({
  // Required, configure the canvas element, and complete the final drawing on it
  canvas: document.querySelector('canvas'),
  // Optional, configure the text for drawing, default to '6'
  replaceText: '6',
  // Optional, configure drawing radius, the larger the value, the sparser it will be, default to 10
  raduis: 10,
  // Optional, configure whether to grayscale. If grayscale is enabled, colors will be lost, default to false
  isGray: false,
  // Required, configure drawing content
  source: {
    // Required, configure what text to draw
    text: 'Text Image',
    // Optional, configure the font used for text, CSS format, default to Microsoft Yahei
    fontFamily: 'Microsoft YaHei',
    // Optional, configure text size, default to 200
    fontSize: 200
  },
})
```

### Draw image

```js
import { createTextImage } from '@sunny-117/text-image'
createTextImage({
  // Required, configure the canvas element, and complete the final drawing on it
  canvas: document.querySelector('canvas'),
  // Optional, configure the text for drawing, default to '6'
  replaceText: '6',
  // Optional, configure drawing radius, the larger the value, the sparser it will be, default to 10
  raduis: 10,
  // Optional, configure whether to grayscale. If grayscale is enabled, colors will be lost, default to false
  isGray: false,
  // Required, configure drawing content
  source: {
    // Required, configure the image path for drawing
    img: 'path',
    // Optional, configure image width, default to the width of the image itself
    width: 500,
    // Optional, configure image height, default to the height of the image itself
    height: 300
  },
})
```



## Draw a video

```js
import { createTextImage } from '@sunny-117/text-image'
createTextImage({
  // Required, configure the canvas element, and complete the final drawing on it
  canvas: document.querySelector('canvas'),
  // Optional, configure the text for drawing, default to '6'
  replaceText: '6',
  // Optional, configure drawing radius, the larger the value, the sparser it will be, default to 10
  raduis: 10,
  // Optional, configure whether to grayscale. If grayscale is enabled, colors will be lost, default to false
  isGray: false,
  // Required, configure drawing content
  source: {
    // Required, configure the video path for drawing
    video: 'path',
    // Optional, configure video width, default to the width of the video itself
    width: 500,
    // Optional, configure video height, default to the height of the video itself
    height: 300
  },
})
```


# License

Released under the MIT License. Refer to the LICENSE file for more information."
