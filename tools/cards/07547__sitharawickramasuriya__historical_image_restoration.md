---
id: tool-07547
type: tool
area: 库
status: active
tags: [Python, 协议传染, 本地优先, 英文文档, 本地写作]
title: historical_image_restoration
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/sitharawickramasuriya/historical_image_restoration
created: 2026-07-18
updated: 2026-07-18
no: 7547
category: 画龙补充 / 扩容入库 — 补充源
repo: sitharawickramasuriya/historical_image_restoration
stars: 0
url: https://github.com/sitharawickramasuriya/historical_image_restoration
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/QUICK_START.md
---

# sitharawickramasuriya/historical_image_restoration

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/sitharawickramasuriya/historical_image_restoration
- **Stars**：0
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：historical_image_restoration
- **拉取时间**：2026-07-25 19:25:16

related:
  - methods/QUICK_START.md
---

# 🖼️ Historical Image Restoration GUI
A powerful Python-based GUI tool to restore historical images, such as wall paintings, using a combination of manual masking, traditional OpenCV inpainting, and AI-based Stable Diffusion. The tool offers HSV-based mask generation, brush painting, inpainting options, and image quality assessment via SSIM.

# ✨ Features
🎨 Manual Painting: Mark damaged regions using a brush tool.

🌈 HSV Masking: Automatically generate masks by adjusting Hue, Saturation, and Value sliders.

🔧 Restoration Methods:

  Stable Diffusion (ML) – High-quality AI-based inpainting.

  Telea (Fast) – Fast OpenCV inpainting for quick fixes.

  NS (Native / Navier-Stokes) – Quality-focused OpenCV inpainting.

🔍 Quality Assessment: Uses SSIM (Structural Similarity Index) to evaluate restoration results.

🛠️ Enhancement Tools:

  Denoising (FastNLMeans)

  Sharpness Boost

💾 Save Results: Export restored and enhanced images.

# 🖥️ How It Works
Load Image
Upload a damaged historical image (e.g., mural, wall painting).

Mark Damage
  Use the brush or HSV sliders to highlight areas for inpainting.

Choose Method
  Select one of the three inpainting methods:

ML (Stable Diffusion) – Uses machine learning for photorealistic restoration.

Fast (Telea) – Faster, edge-aware OpenCV algorithm.

Quality (NS) – Navier-Stokes based method for smoother fills.

Apply Inpainting
  Hit "Apply Inpainting" to restore the selected regions.

Enhance & Save
  Improve image quality via denoising and sharpness adjustments. Save final output.

Evaluate
  Use the "Check Image Quality" button to calculate SSIM score vs. original image.

# 📷 GUI Layout
Left Panel: Tool controls (HSV sliders, brush settings, method selection, enhancement).

Right Panel: Interactive canvas to view and edit the image.

# 🧠 Tech Stack
Python

CustomTkinter – for modern GUI

OpenCV – inpainting & HSV masking

Stable Diffusion – ML-based inpainting (optional setup)

scikit-image – SSIM evaluation

Pillow – image processing

