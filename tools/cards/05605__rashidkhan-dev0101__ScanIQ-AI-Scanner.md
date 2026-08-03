---
id: tool-05605
type: tool
area: 库
status: active
tags: [TTS, Dart, 协议未明, 本地优先, 英文文档, 本地写作]
title: ScanIQ-AI-Scanner
summary: 小说转语音/有声书
source: https://github.com/rashidkhan-dev0101/scaniq-ai-scanner
created: 2026-07-18
updated: 2026-07-18
no: 5605
category: 一、去 AI 味 / Humanizer 库
repo: rashidkhan-dev0101/ScanIQ-AI-Scanner
stars: 1
url: https://github.com/rashidkhan-dev0101/scaniq-ai-scanner
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# rashidkhan-dev0101/ScanIQ-AI-Scanner

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rashidkhan-dev0101/scaniq-ai-scanner
- **Stars**：1
- **语言**：Dart
- **License**：None
- **Topics**：—
- **GitHub 描述**：-------------------------------- |   Smart AI Scanner           | |------------------------------| | 📷 Scan Text                 | | 😊 Face Analyzer             | | 🌍 Language Detector         | | 🎤 Voice Notes               | |------------------------------| | 📁 Recent Scans              | --------------------------------
- **本地描述**：-------------------------------- （   Smart AI Scanner           （ （------------------------------（ （ 📷 Scan Text                 （ （ 😊 Face Analyzer             （ （ 🌍 Language Detector         （ （ 🎤 Voice Notes               （ （------------------------------（ （ 📁 Recent Scans              （ --------------------------------
- **拉取时间**：2026-07-25 18:24:54

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# LumaScan AI (Flutter + Provider + MVVM)

A production-style starter for your **Smart AI Scanner** UI with 5 screens:

1. Home (dark)
2. Camera Scan (dark)
3. Text Result (light)
4. Face Detection (dark)
5. Language Detection (light)

## Best App Name

✅ **LumaScan AI**

Why this name:
- **Luma** = light/vision (perfect for camera + OCR + detection)
- **Scan** = clear core action
- **AI** = direct value proposition for hiring market

## Route Map

- `/` → Home
- `/camera-scan` → Camera Scan
- `/text-result` → Text Result
- `/face-detection` → Face Detection
- `/language-detection` → Language Detection

## Color System (best fit for your mockup)

- Primary Neon: `#4ADE80`
- Primary Dark: `#16A34A`
- Accent Blue: `#3B82F6`
- Accent Amber: `#F59E0B`
- Accent Violet: `#8B5CF6`
- Dark BG: `#07090F`
- Dark Card: `#11141B`
- Light BG: `#F4F7FA`

## MVVM + Provider Structure

```text
lib/
  core/
    constants/app_colors.dart
    routing/app_router.dart
    theme/app_theme.dart
  features/
    home/
      model/
      view/
      view_model/
    camera_scan/
      model/
      view/
      view_model/
    text_result/
      model/
      view/
      view_model/
    face_detection/
      model/
      view/
      view_model/
    language_detection/
      model/
      view/
      view_model/
  shared/widgets/
  main.dart
```

## Step-by-step setup

1. Create Flutter app.
2. Add `provider` in `pubspec.yaml`.
3. Add centralized colors in `app_colors.dart`.
4. Add theme tokens in `app_theme.dart`.
5. Add named routes in `app_router.dart`.
6. Register all ViewModels in `MultiProvider` (`main.dart`).
7. Build each screen UI under `view/`.
8. Move data/state/actions into `view_model/`.
9. Keep DTOs/config in `model/`.
10. Reuse UI shells/chips/cards via `shared/widgets/`.

## Next integration steps

- Hook camera package for real feed (`camera`) on Camera screen.
- Hook OCR (`google_mlkit_text_recognition`) for Text Result.
- Hook face detection (`google_mlkit_face_detection`) for Face screen.
- Hook language detect + translation (Gemini/OpenAI backend).
- Add repository/data layer for API and local cache.
