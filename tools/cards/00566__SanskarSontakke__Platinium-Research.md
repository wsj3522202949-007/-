---
id: tool-00566
type: tool
area: 库
status: active
tags: [TTS, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: Platinium-Research
summary: 小说转语音/有声书
source: https://github.com/sanskarsontakke/platinium-research
created: 2026-07-18
updated: 2026-07-18
no: 566
category: 二、网文 / 长篇 AI 写作系统 库
repo: SanskarSontakke/Platinium-Research
stars: 0
url: https://github.com/sanskarsontakke/platinium-research
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 73a576a2ebd9def1
  - methods/最强写作方法论_全球最强综合版.md
---

# SanskarSontakke/Platinium-Research

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sanskarsontakke/platinium-research
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：An advanced AI-powered research assistant and writing tool featuring deep reasoning, web grounding, real-time voice brainstorming, and image analysis.
- **本地描述**：An advanced AI-powered research assistant and writing tool featuring deep reasoning, web grounding, real-time voice brainstorming, and image analysis.
- **拉取时间**：2026-07-23 22:55:33

---


# Platinium Research

**Platinium Research** is an advanced, "Local-First" AI Research Agent designed for deep reasoning, academic writing, and complex project management. It integrates Google Gemini 2.5/3.0 models with a spatial canvas, spreadsheet engine, and live web research capabilities.

## 🌟 Features

*   **Deep Reasoning:** Uses `gemini-3-pro-preview` for logic puzzles, argumentation, and outlining.
*   **Web Grounding:** Real-time web search and citation generation using `gemini-2.5-flash`.
*   **Prompt Engineering:** Generates high-fidelity image prompts for Midjourney/DALL-E instead of generating low-res images.
*   **Spatial Canvas:** Mind-map and organize thoughts visually using React Flow logic.
*   **Data Analysis:** Built-in spreadsheet editor with chart visualization.
*   **Live Voice Mode:** Real-time brainstorming via the Gemini Live API (WebSockets).

---

## 🚀 Getting Started (Web)

1.  **Clone the repository.**
2.  **Install dependencies:**
    ```bash
    npm install
    ```
3.  **Run locally:**
    ```bash
    npm start
    ```

### Authentication
The app uses **Google Drive** as its backend database (NoSQL via JSON files).
1.  On first load, you will be asked for an **OAuth Access Token**.
2.  Go to the [Google OAuth Playground](https://developers.google.com/oauthplayground/).
3.  Select the **Drive API v3** scopes (`drive.file`, `drive.readonly`).
4.  Exchange the code for a token and paste it into the app.

---

## 📱 Porting to Flutter (Mobile & Windows)

You can convert Platinium Research into a native-feeling app for Android, iOS, and Windows using Flutter.

### Strategy 1: The Wrapper (Recommended for Speed)
This method wraps the existing highly-optimized React code in a WebView, adding native bridge capabilities.

**1. Create Flutter Project:**
```bash
flutter create platinium_mobile
cd platinium_mobile
flutter pub add flutter_inappwebview permission_handler
```

**2. Update `lib/main.dart`:**
```dart
import 'package:flutter/material.dart';
import 'package:flutter_inappwebview/flutter_inappwebview.dart';
import 'package:permission_handler/permission_handler.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Permission.microphone.request(); // For Live Mode
  runApp(const MaterialApp(home: WebViewApp()));
}

class WebViewApp extends StatelessWidget {
  const WebViewApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: InAppWebView(
          initialUrlRequest: URLRequest(
            url: WebUri("https://your-firebase-app-url.web.app")
          ),
          initialSettings: InAppWebViewSettings(
            mediaPlaybackRequiresUserGesture: false,
            allowsInlineMediaPlayback: true,
            userAgent: "PlatiniumNative/1.0",
          ),
          onPermissionRequest: (controller, request) async {
            return PermissionResponse(
              resources: request.resources,
              action: PermissionResponseAction.GRANT
            );
          },
        ),
      ),
    );
  }
}
```

**3. Build for Windows:**
```bash
flutter config --enable-windows-desktop
flutter build windows
```

### Strategy 2: Native Port (Advanced)
To rewrite the app purely in Dart/Flutter:
1.  Use `google_generative_ai` package for Gemini API calls.
2.  Use `googleapis` package for Drive integration.
3.  Replace the React Canvas with `interactive_viewer` and `CustomPainter`.
4.  Replace the Markdown editor with `flutter_markdown`.

---

## 🔥 Firebase & GCP Integration (Free Tier)

Platinium is designed to be hosted on **Firebase Hosting** (Google Cloud Platform) using the free tier.

### 1. Prerequisites
*   Install Firebase CLI: `npm install -g firebase-tools`
*   Login: `firebase login`

### 2. Initialize Project
Run the following in the project root:
```bash
firebase init
```
*   Select **Hosting**.
*   Select **Create a new project** (or use existing).
*   Public directory: `build` (or `dist` depending on your bundler).
*   Configure as single-page app? **Yes**.
*   Automatic builds with GitHub? **Optional**.

### 3. Build & Deploy
```bash
npm run build
firebase deploy
```

### 4. Enabling Google Auth (Optional Replacement for Manual Token)
To replace the manual "Paste Token" workflow with real "Sign In with Google":

1.  In Firebase Console -> **Authentication** -> **Sign-in method**, enable **Google**.
2.  In `components/DrivePicker.tsx`, import Firebase Auth:
    ```typescript
    import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
    
    // Replace handleConnect with:
    const handleConnect = async () => {
       const provider = new GoogleAuthProvider();
       provider.addScope('https://www.googleapis.com/auth/drive.file');
       const result = await signInWithPopup(auth, provider);
       const credential = GoogleAuthProvider.credentialFromResult(result);
       const token = credential?.accessToken;
       // ... store token
    };
    ```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🛠 Project Architecture

*   **`services/agent`**: Contains the AI Orchestrator. It uses a "Reasoning Loop" to call tools (`searchWeb`, `deepReason`) before answering.
*   **`services/driveService.ts`**: Handles all storage. Platinium is "Serverless" in the sense that it talks directly from the Browser to Google Drive APIs.
*   **`components/CanvasBoard.tsx`**: A custom-built SVG/HTML hybrid engine for the infinite whiteboard.
*   **`components/LiveBrainstorm.tsx`**: Manages WebSockets for the Gemini Live API (Audio I/O).

