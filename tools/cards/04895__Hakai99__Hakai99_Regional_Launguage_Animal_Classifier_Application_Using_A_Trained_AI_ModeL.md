---
id: tool-04895
type: tool
area: 库
status: active
tags: [TTS, Kotlin, 协议未明, 本地优先, 英文文档, 本地写作]
title: Hakai99_Regional_Launguage_Animal_Classifier_Application_Using_A_Trained_AI_ModeL
summary: 小说转语音/有声书
source: https://github.com/hakai99/hakai99_regional_launguage_animal_classifier_application_using_a_trained_ai_model
created: 2026-07-18
updated: 2026-07-18
no: 4895
category: 一、去 AI 味 / Humanizer 库
repo: Hakai99/Hakai99_Regional_Launguage_Animal_Classifier_Application_Using_A_Trained_AI_ModeL
stars: 0
url: https://github.com/hakai99/hakai99_regional_launguage_animal_classifier_application_using_a_trained_ai_model
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: d32bbf8232f6f573
  - methods/改稿润色指令库.md
---

# Hakai99/Hakai99_Regional_Launguage_Animal_Classifier_Application_Using_A_Trained_AI_ModeL

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/hakai99/hakai99_regional_launguage_animal_classifier_application_using_a_trained_ai_model
- **Stars**：0
- **语言**：Kotlin
- **License**：None
- **Topics**：—
- **GitHub 描述**：Assamese Animal Detector - Real-time animal detection Android app using TensorFlow Lite & YOLOv8. Detects 11 Assamese animals via camera with text-to-speech pronunciation. Offline, fast, and kid-friendly. Perfect for learning animals in native Assamese language. No internet required. Built with Kotlin & AndroidX.
- **本地描述**：Assamese Animal Detector - Real-time animal detection Android app using TensorFlow Lite & YOLOv8. Detects 11 Assamese animals via camera with text-to-speech pronunciation. Offline, fast, and kid-friendly. Perfect for learning animals in native Assamese language. No internet required. Built with Kotlin & AndroidX.
- **拉取时间**：2026-07-25 17:58:26

---

#  Assamese Animal Detector - Android App

An intelligent, real-time animal detection Android application built with TensorFlow Lite and YOLOv8, featuring Assamese language support and text-to-speech functionality for educational purposes.

##Features

- Real-Time Animal Detection**: Uses a custom-trained YOLOv8 nano model to detect 11 different Assamese animals in real-time through your device's camera
- Assamese Language Support**: Complete Assamese interface with all text, labels, and speech output in Assamese script
- Text-to-Speech Integration**: Automatic pronunciation of detected animals in Assamese using Android's built-in TTS engine
- Offline Functionality**: Works completely offline - no internet connection required for detection
- Lightweight & Fast**: Optimized TensorFlow Lite model ensures smooth performance even on budget devices
- Kid-Friendly Interface**: Colorful, intuitive UI designed specifically for children to explore and learn about animals

## Supported Animals

The app detects 11 Assamese animals:
1. হাঁহ (Duck)
2. মেকুৰী (Parrot)
3. গৰু (Cow)
4. কুকুৰ (Dog)
5. হাঁহ (Duck)
6. হাতী (Elephant)
7. লগনিয়া (Monkey/Langur)
8. পাৰ চৰাই (Bird)
9. ম'হ (Bufallow)
10. কাছ (Turtle)

## Technology Stack

- **Language**: Kotlin
- **Framework**: Android SDK (API 21+)
- **ML Model**: YOLOv8 Nano (Custom Trained)
- **ML Framework**: TensorFlow Lite
- **UI**: AndroidX with Material Design
- **Libraries**: CameraX, Coroutines, OkHttp

## Requirements

- Android 5.0 (API 21) or higher
- Camera permission
- Internet permission (for Wikipedia integration)
- Minimum 100MB storage

## How It Works

1. Launch the app and grant camera permissions
2. Point your device at an animal
3. The model detects the animal in real-time
4. App displays the animal name in Assamese
5. Text-to-Speech pronounces the name
6. Users can explore more information via Wikipedia search

## Model Performance

- Training Data: 873 images across 11 animal classes
- Validation Accuracy: 87.6% mAP@50
- Inference Speed: 2.5ms per image
- Model Size: 11.7MB (TFLite)

## 📝 License

This project is open-source and available for educational purposes.

## 👨‍💻 Author
Dev Kumar Lahkar has
developed as an educational tool to teach children about animals in their native Assamese language.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork and submit pull requests.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

Learn animals in Assamese. Offline. Real-time. Free.
