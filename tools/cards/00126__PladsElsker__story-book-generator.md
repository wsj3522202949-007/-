---
id: tool-00126
type: tool
area: 库
status: active
tags: [TTS, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: story-book-generator
summary: 小说转语音/有声书
source: https://github.com/pladselsker/story-book-generator
created: 2026-07-18
updated: 2026-07-18
no: 126
category: 二、网文 / 长篇 AI 写作系统 库
repo: PladsElsker/story-book-generator
stars: 4
url: https://github.com/pladselsker/story-book-generator
tier: "B"
use_case: "小说转语音/有声书"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# PladsElsker/story-book-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/pladselsker/story-book-generator
- **Stars**：4
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Generate a story book narated and depicted by AI from written novels
- **本地描述**：Generate a story book narated and depicted by AI from written novels
- **拉取时间**：2026-07-23 22:42:38

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# story-book-generator
Generate a story book narated and depicted by AI from written novels

## Roadmap

### Light novel scraper

- Chrome extension
- Python + headless browser
- Should easily be able to scrape different web sites, and click on the "next chapter" link automatically

`Input` A web url of a light novel.  
`Output` A uniquely named folder containing a novel.json file of this format:  
```json
{
  "title": "Mushoko tenser",
  "first_chapter_url": "https://www.webnovel.com/fsdjfjsf/chapter-1",
  "last_scraped_url": "https://www.webnovel.com/fsdjfjsf/chapter-118",
  "chapters": [
    {
      "title": "title",
      "content": "content\ncontent"
    }
  ]
}
```

### Paragraph splitter

To make sure both the audio and the image are in sync, the chapters must be split into visually similar paragraphs and then those splits must be reused for both the audio and visual pipelines.  

`Input` A scraped light novel JSON file.  
`Output` A sequence of scenes containing a consistent context over a few lines (visual context).  
```json
{
  "title": "Mushoko tenser",
  "first_chapter_url": "https://www.webnovel.com/fsdjfjsf/chapter-1",
  "last_scraped_url": "https://www.webnovel.com/fsdjfjsf/chapter-118",
  "chapters": [
    {
      "title": "title",
      "content": "- Content!\n- No, you content!",
      "scenes": [
        "- Content!",
        "- No, you content!"
      ]
    }
  ],
}
```

### Light novel to audio
- https://huggingface.co/metavoiceio/metavoice-1B-v0.1
- https://huggingface.co/Pendrokar/xvapitch_nvidia
- https://huggingface.co/spaces/coqui/xtts
- https://github.com/yl4579/StyleTTS2
- https://huggingface.co/ShoukanLabs/Vokan
- [rvc](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)?
- Maybe something else?
- Selecting the right voice actor for the right dialog

`Input` A scene in text.  
`Output` `scene-<i>.wav` located in the folder `assets/chapter-<j>/`.  

### Light novel to sequence of images

- Stable diffusion transformer model?
- LLM to fetch previous images from database for consistency?
- Basic natural language analysis and embbeding database?
- Split characters and background?
- Use Trellis to generate 3D models of the characters for consistent image generation. 
- A repository of previously generated images and associated annotations. An annotation is a text associated to a generated image, could be the original light novel text or a reasoning about the image. Annotations are optimized to be searched when generating the next image.

`Input` A scene in text.  
`Output` `scene-<i>.png` located in the folder `assets/chapter-<j>/`.  

### Mobile consumption

- Consume the audio and video easily from a cellphone while traveling.  
- Offline generation and save generated story on a mobile app.  

`Input` A processed novel folder.  
`Output` Mobile app playback.  
