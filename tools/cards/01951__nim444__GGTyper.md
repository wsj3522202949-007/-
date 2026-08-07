---
id: tool-01951
type: tool
area: 库
status: active
tags: [Swift, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: GGTyper
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nim444/ggtyper
created: 2026-07-18
updated: 2026-07-18
no: 1951
category: 二、网文 / 长篇 AI 写作系统 库
repo: nim444/GGTyper
stars: 0
url: https://github.com/nim444/ggtyper
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# nim444/GGTyper

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nim444/ggtyper
- **Stars**：0
- **语言**：Swift
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：AI writing copilot for macOS 27 - standalone Liquid Glass app with OpenRouter models, prompt Characters, green diff view and push-to-talk
- **本地描述**：AI writing copilot for macOS 27 - standalone Liquid Glass app with OpenRouter models, prompt Characters, green diff view and push-to-talk
- **拉取时间**：2026-07-23 23:35:52

---

![Swift](https://img.shields.io/badge/swift-%23FA7343.svg?style=for-the-badge&logo=swift&logoColor=white)
![macOS](https://img.shields.io/badge/mac%20os%2027-000000?style=for-the-badge&logo=apple&logoColor=F0F0F0)
![SwiftUI](https://img.shields.io/badge/SwiftUI-0071e3.svg?style=for-the-badge&logo=swift&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-7C3AED?style=for-the-badge)

# GGTyper

**Your text, fixed. Anywhere.**

![Demo](assets/demo.gif)

GGTyper is an AI writing copilot for macOS, rebuilt from the ground up for macOS 27 with the Liquid Glass design language. Type or speak a messy draft, hit **Let's Process**, and get a clean rewrite with every change highlighted in green - so you see exactly what the AI fixed before you copy it.

One OpenRouter API key unlocks hundreds of models. Reusable prompt presets called **Characters** ("Fix grammar", "Dev talk", "Formal email") decide how your text gets rewritten.

> GGTyper is the successor of [Typer-AI-Mac](https://github.com/nim444/Typer-AI-Mac) and [Typer-AI-Android](https://github.com/nim444/Typer-AI-Android), redesigned as a standalone window app instead of a menu-bar item.

---

## Features

- **Onboarding wizard** - guided first run: pick a provider, verify your API key, favorite your models, create your first Character
- **OpenRouter** - one key, the whole catalog. Searchable model picker fed live from the OpenRouter API, with favorites and a starred default
- **Characters** - named system prompts you switch between per task; full CRUD in Settings, at least one always present
- **Green diff view** - results render as a word-level LCS diff; everything the AI changed is highlighted so nothing slips by
- **Push-to-talk** - WhatsApp-style mic: hold to record, slide up to lock hands-free, quick tap to toggle. Live partial transcription streams into the input while you speak (on-device speech recognition when available)
- **History** - every fix is kept with its original; copy either one back out. Retention by entry count or by days, your choice
- **Liquid Glass UI** - frosted window, glass toolbar capsules, interactive glass mic, no title bar - just a pin, your Character, history, settings, and a close button
- **Pin to screen** - one click keeps GGTyper floating above every other window
- **Keychain-only secrets** - the API key never touches UserDefaults or disk

## Requirements

- macOS 27.0 or later
- An [OpenRouter API key](https://openrouter.ai/keys)
- Xcode 27 (beta) only if building from source

## Download

Grab the latest `GGTyper-x.y.dmg` from [Releases](https://github.com/nim444/GGTyper/releases), open it, and drag **GGTyper** into **Applications**.

The app is not notarized (no paid Apple Developer account), so macOS will warn on first launch. Either right-click the app and choose **Open**, or clear the quarantine flag:

```bash
xattr -dr com.apple.quarantine /Applications/GGTyper.app
```

If macOS still blocks it, approve the app under **System Settings > Privacy & Security > Open Anyway**.

## Build & Run

```bash
git clone https://github.com/nim444/GGTyper.git
cd GGTyper
open GGTyper.xcodeproj
```

Build and run (Cmd+R). The onboarding wizard takes it from there.

## How to use

1. **Onboard once** - select OpenRouter, paste your key (verified live against the API before it is saved to the Keychain), checkmark the models you want, star a default, and keep or edit the prefilled "Fix grammar" Character.
2. **Type or talk** - write into the input box, or use the mic:

   | Gesture | Action |
   |---|---|
   | Hold | Record while pressed, stop on release |
   | Hold + slide up | Lock recording hands-free |
   | Quick tap | Toggle recording on |
   | Tap while recording | Stop |

3. **Let's Process** (or Cmd+Return) - your active Character's prompt steers the model; the rewrite appears below with changes in green.
4. **Copy** the result, or open **History** later to copy the fixed or the original text of any past run.

## Tech

| Component | Technology |
|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Language / UI | Swift, SwiftUI, Liquid Glass (glassEffect, glass button styles) |
| AI | OpenRouter chat completions (OpenAI-compatible), live model catalog |
| Speech | AVAudioEngine + SFSpeechRecognizer, partial results, on-device preferred |
| Diff | Word-level longest common subsequence with green highlights |
| Storage | Keychain (API key), UserDefaults (settings), JSON in Application Support (history) |
| Icon | Icon Composer (.icon) with glass layers |
| Sandbox | Enabled - outgoing network + microphone only |

```text
GGTyper/
├── GGTyperApp.swift            # WindowGroup (hidden title bar) + Settings scene
├── Models/                     # GGCharacter, HistoryEntry, OpenRouter DTOs
├── Services/
│   ├── AppStore.swift          # observable app state + persistence
│   ├── OpenRouterClient.swift  # verify key, list models, chat completions
│   ├── SpeechRecorder.swift    # push-to-talk capture + live transcription
│   ├── WordDiff.swift          # LCS diff -> green-highlighted AttributedString
│   ├── HistoryStore.swift      # JSON history + retention pruning
│   └── KeychainHelper.swift    # generic-password storage
└── Views/
    ├── Onboarding/             # welcome, provider, API key, models, character
    ├── MainView.swift          # compact glass window
    ├── MicButton.swift         # hold / slide-to-lock / tap gestures
    ├── HistoryView.swift       # history popover
    └── Settings/               # Provider, Characters, History tabs
```

## Roadmap

- LM Studio and Ollama as local providers (cards already in onboarding)
- Migrate dictation to the macOS 27 SpeechAnalyzer API
- Global hotkey to summon the window from any app
- Optional menu-bar companion mode
- Streaming responses

## License

**PolyForm Noncommercial License 1.0.0** - free for personal, academic, and non-profit use; commercial use is prohibited. See [LICENSE](https://github.com/nim444/GGTyper/blob/main/LICENSE).
