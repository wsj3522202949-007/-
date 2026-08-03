---
id: tool-05418
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/usausernob/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5418
category: 一、去 AI 味 / Humanizer 库
repo: usausernob/ai-slop-detector
stars: 0
url: https://github.com/usausernob/ai-slop-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# usausernob/ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/usausernob/ai-slop-detector
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：usausernob/ai-slop-detector
- **拉取时间**：2026-07-25 18:17:52

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Slop Detector Extension

AI Slop Detector adalah ekstensi peramban ringan yang dirancang untuk mendeteksi apakah suatu media di internet merupakan file asli atau hasil rekayasa kecerdasan buatan (AI). 

Ekstensi ini mendukung tiga mode media utama: Gambar, Audio, dan Video. Untuk menjaga kinerja peramban tetap optimal, seluruh proses deteksi didelegasikan ke server backend terpisah.

## Fitur Utama

- **Dukungan Multi-Media:** Mampu mendeteksi rekayasa AI pada file Gambar, Audio, maupun Video.
- **Metode Pemindaian Fleksibel:**
  - **Klik Kanan (Context Menu):** Pindai media secara instan melalui menu klik kanan pada peramban.
  - **Tombol Injeksi:** Tombol pemindaian yang terintegrasi otomatis pada media yang sedang dilihat di halaman web.
  - **Unggah Manual:** Fasilitas untuk mengunggah file media langsung melalui halaman pengaturan (Options page) ekstensi.
- **Ringan & Aman:** Beban kerja dilakukan di server terpisah yang sudah dilengkapi perlindungan dari beban berlebih.

## Teknologi Utama

- **Frontend:** WXT Framework (TypeScript)
- **Backend:** FastAPI (Python) dan Model AI
