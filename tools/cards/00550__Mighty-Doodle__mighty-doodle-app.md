---
id: tool-00550
type: tool
area: 库
status: active
tags: [C#, 协议传染, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: mighty-doodle-app
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/mighty-doodle/mighty-doodle-app
created: 2026-07-18
updated: 2026-07-18
no: 550
category: 二、网文 / 长篇 AI 写作系统 库
repo: Mighty-Doodle/mighty-doodle-app
stars: 0
url: https://github.com/mighty-doodle/mighty-doodle-app
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 96e0ea6248346db0
  - methods/最强写作方法论_全球最强综合版.md
---

# Mighty-Doodle/mighty-doodle-app

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mighty-doodle/mighty-doodle-app
- **Stars**：0
- **语言**：C#
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：Open-source Unity app for Mighty Doodle®, a playful literacy platform that helps children build reading and writing skills through interactive mini-games. Designed for scalability, multisensory learning, and real-time progress tracking.
- **本地描述**：Open-source Unity app for Mighty Doodle®, a playful literacy platform that helps children build reading and writing skills through interactive mini-games. Designed for scalability, multisensory learning, and real-time progress tracking.
- **拉取时间**：2026-07-23 22:55:05

---

# 🧠 Mighty Doodle

### A Kids' Learning & Education App — Completely Open Source
 
**Mighty Doodle** is a mobile application built to help children develop reading, writing, and vocabulary skills through interactive lessons, handwriting practice, and voice-based learning.
 
It runs natively on **iOS** and **Android**, and is now **fully open source** — meaning anyone is free to use, modify, and build upon this project however they see fit.

---

## 📖 Overview
 
Mighty Doodle is a structured, immersive learning experience designed for children. It combines handwriting recognition, speech processing, and vocabulary modules into a single cross-platform mobile app.
 
The project is built using **Unity 6 LTS** and is architected for **modularity**, **performance**, and **real-world production deployment**. Whether you're a developer, educator, or researcher — this codebase is yours to explore and build on.
 
**Core technologies integrated:**
 
| Technology | Purpose |
|---|---|
| ✍️ Google ML Kit | Digital ink & handwriting recognition |
| 🎙️ Microsoft Speech Services | Voice recognition via backend |
| 📱 Unity 6 LTS | Cross-platform mobile engine |
| 💾 MemoryPack | High-performance serialization |
| 💰 RevenueCat + Unity IAP | Subscription & purchase management |
 
---
 
## ✨ Features
 
| Feature | Description |
|---|---|
| 📖 Interactive Reading Lessons | Structured stories and comprehension exercises tailored for children |
| ✍️ Handwriting Recognition | Real-time digital ink recognition powered by Google ML Kit |
| 🎙️ Speech-Based Learning | Pronunciation feedback and voice validation through the backend |
| 🔤 Vocabulary Builder | Word and language learning modules designed for young learners |
| 🎮 Gamified Reward System | Extensible mini-game reward pipeline to keep children engaged |
| 📱 Cross-Platform | Runs natively on both iOS and Android |
| ⚡ Mobile Optimized | Lightweight, performance-focused build for a wide range of devices |
 
---
 
## 🏗️ Project Specifications
 
| Category | Details |
|---|---|
| Engine | Unity 6.3 LTS (6000.3.6f1) |
| Target Platforms | iOS, Android |
| Handwriting Recognition | Google ML Kit (Digital Ink Recognition) |
| Speech Recognition | Microsoft Speech Services (Backend) |
| Serialization | MemoryPack (MIT) |
| Subscription Management | RevenueCat (Android) |
| In-App Purchases | Unity IAP |
 
---
 
## 🌐 Backend Server Setup
 
> ⚠️ **The backend server is required to run Mighty Doodle.** Without it, authentication, speech recognition, email verification, IAP validation, and user data will not function.
 
### Step 1 — Clone the Backend Repository
 
```bash
git clone https://github.com/Mighty-Doodle/AppService.git
```
 
### Step 2 — Follow the Backend README
 
The backend repository contains its own setup instructions. Follow them carefully to configure and launch all services.
 
### What the Backend Powers
 
| Service | Role |
|---|---|
| 🔐 Auth System | Account creation, login, and session management |
| 🎙️ Speech API | Voice recording processing and validation |
| 📧 Email Service | Account verification email flow |
| 💰 IAP Validation | Receipt validation and subscription logic |
| 📊 User Data | Progression tracking and persistent storage |
 
Once your backend server is up and running, all systems in the app will function as intended.
 
---

## 🚀 Getting Started
 
### 1. Clone This Repository
 
```bash
git clone https://github.com/Mighty-Doodle/mighty-doodle-app.git
```
 
---
 
### 2. Open in Unity
 
- Launch **Unity Hub**
- Open the project using **Unity 6.3 LTS (6000.3.6f1)**
 
> Make sure you have the correct Unity version installed. Using a different version may cause compatibility issues.
 
---
 
### 3. Resolve Dependencies
 
Unity's **External Dependency Manager (Jar Resolver)** will automatically handle the following on startup:
 
- Downloading required Android and iOS native dependencies
- Configuring Google ML Kit bindings
- Resolving native plugin references
 
> 💡 If the resolver does not run automatically, trigger it manually:
> **Assets → External Dependency Manager → Android Resolver → Force Resolve**
 
---
 
### 4. Configure the Backend
 
- Set up and run your backend server (see [Backend Server Setup](#-backend-server-setup))
- Update your API base URLs in `APIEndpoints.cs` (see [API Endpoint Configuration](#-api-endpoint-configuration))

---

## ⚠️ Important Development Notes
 
### ✍️ Digital Ink Recognition — Editor Limitation
 
Handwriting recognition relies on **native mobile APIs** from Google ML Kit and is not available inside the Unity Editor.
 
| Environment | Status |
|---|---|
| Unity Editor | ❌ Not supported |
| Physical iOS / Android Device | ✅ Required for testing |
 
Always test handwriting features on a real device.
 
---
 
### 🎙️ Speech Recognition System
 
Speech recognition in Mighty Doodle is powered entirely by **Microsoft Speech Services** running on the backend server. The Unity client sends voice recordings to the backend via API and receives the recognition result — there is no on-device speech processing.
 
All related implementation lives in the **backend server codebase**.
 
---
 
### 🔐 Account Verification Flow
 
| Environment | Behavior |
|---|---|
| Unity Editor | Bypass verification using the **"Next"** button |
| Device Build | Requires a fully configured backend that handles verification links |
 
---

## ⚙️ Required Configuration
 
### 💰 In-App Purchases (IAP) Setup
 
Mighty Doodle uses a **hybrid IAP system** that combines three layers:
 
- **Unity IAP** — Handles the client-side purchase flow
- **RevenueCat** — Manages Android subscription syncing and entitlement validation
- **Backend Server** — Performs final receipt validation and assigns subscription state
 
---
 
### 🧪 Development Mode — Disable Subscriptions
 
During development, you can bypass the subscription requirement entirely:
 
```csharp
RequireSubscription = false;
```
 
> 📍 This flag is located in the **Core Prefab** inside your main scene.
 
---

### 🍎 iOS IAP Setup
 
#### 1. App Store Connect Configuration
 
- Create your app project in **App Store Connect**
- Create the following subscription products:
  - Weekly
  - Monthly
  - Yearly
 
#### 2. Assign Product IDs
 
Once your subscriptions are created in App Store Connect, retrieve their **Product IDs** and add them to:
 
```
Assets/ScriptableObjects/Resources/Subscriptions.asset
```
 
For each subscription entry in this asset, assign the corresponding **iOS Product ID**.
 
---
 
### 🤖 Android IAP Setup
 
#### 1. Google Play Console
 
- Create your app in the **Google Play Console**
- Configure the following subscription products:
  - Weekly
  - Monthly
  - Yearly
 
#### 2. Google Cloud Setup
 
- Create a **Google Cloud Project**
- Enable the required Google Play APIs
- Link your Google Cloud Project with the Google Play Console
 
#### 3. Assign Product IDs
 
Retrieve the Product IDs from the Google Play Console and add them to:
 
```
Assets/ScriptableObjects/Resources/Subscriptions.asset
```
 
---

### 🔗 RevenueCat Setup (Android)
 
RevenueCat is required for Android subscription management. Follow these steps carefully.
 
#### 1. Create a RevenueCat Project
 
- Log in to [RevenueCat](https://www.revenuecat.com/)
- Create a new project and add your app
- Connect it with the **Google Play Store**
 
#### 2. Service Account Setup
 
- In **Google Cloud**, create a **Service Account**
- Download the generated `service.json` file
- Grant the service account the required permissions
- Invite the service account in the **Google Play Console** with the appropriate access level
 
#### 3. Permissions Propagation
 
> ⏱️ Google permissions can take **up to 24 hours** to fully propagate. IAP will **not function correctly** until this process is complete. Plan accordingly during testing.
 
#### 4. Entitlements & Offers
 
- Create **Entitlements** in RevenueCat to represent subscription access
- Map each subscription product to the correct entitlement
- Configure **Offers** as needed for your monetization model
 
---

### 🌐 Backend IAP Requirements
 
Both iOS and Android purchase flows depend on a fully operational backend server. The backend must support:
 
- **Receipt validation** — verifying Apple and Google receipts
- **Subscription state management** — tracking active, expired, and cancelled subscriptions
- **RevenueCat Webhook integration** — receiving real-time subscription events from RevenueCat (Android)
 
---
 
### 🔄 Purchase Flow
 
#### iOS Purchase Flow
 
```
User initiates purchase (Unity IAP)
    ↓
Apple returns a receipt
    ↓
Receipt sent to Backend Server
    ↓
Backend validates the receipt with Apple
    ↓
Subscription assigned to the user account
```
 
#### Android Purchase Flow
 
```
User initiates purchase (Unity IAP)
    ↓
Google returns a receipt
    ↓
Receipt sent to RevenueCat
    ↓
RevenueCat validates & syncs the purchase
    ↓
Backend receives subscription event
    ↓
Backend fetches latest subscription state from RevenueCat
    ↓
Subscription assigned to the user account
```
 
---

### 🔗 App URL Configuration
 
Several URLs within the app point to external pages such as your Privacy Policy, Terms of Service, and parent portal. These must be updated before publishing.
 
**File location:**
 
```
Assets/Scripts/MightyDoodle/Constants/URLs.cs
```
 
Open the file and replace the placeholder values with your own:
 
| Constant | Description |
|---|---|
| `AppStoreAppId` | Your App Store app ID — format: `idXXXXXXXXXX` |
| `PrivacyPolicy` | Full URL to your Privacy Policy page |
| `TermsOfUse` | Full URL to your Terms of Service page |
| `ContactUs` | Full URL to your Contact page |
| `GrownupsPortal` | Full URL to your web admin or parent portal |
 
**Example:**
 
```csharp
private const string AppStoreAppId = "id1234567890";
 
public const string PrivacyPolicy   = "https://yourdomain.com/privacy-policy";
public const string TermsOfUse      = "https://yourdomain.com/terms-of-service";
public const string ContactUs       = "https://yourdomain.com/contact-us";
public const string GrownupsPortal  = "https://admin.yourdomain.com";
```
 
> 💡 `FTCGov` is hardcoded to `https://www.ftc.gov` and does not need to be changed.
 
---

### 🌐 API Endpoint Configuration
 
Once your backend server is deployed, update the base URLs in `APIEndpoints.cs` to point to your own environments.
 
**File location:**
 
```
Assets/Scripts/MightyDoodle/Services/APIEndpoints.cs
```
 
Locate the `ConfigureBaseUrl()` method and update the URL for each environment:
 
```csharp
case Environment.Development:
    _baseUrl = "https://your-dev-server.com/api/v1";
    break;
case Environment.QA:
    _baseUrl = "https://your-qa-server.com/api/v1";
    break;
case Environment.Production:
    _baseUrl = "https://your-production-server.com/api/v1";
    break;
```
 
> ⚠️ Ensure your backend server is fully deployed and accessible before switching to **Production**. Every API call in the app — including authentication, speech recognition, IAP validation, and lesson data — routes through this base URL.
 
---

### 🏗️ iOS Build Setup
 
Before building for iOS, update the following constants in `PostProcessBuildScript.cs`:
 
| Field | Description |
|---|---|
| `APP_NAME` | The display name of your app |
| `APP_IDENTIFIER` | Your app's bundle identifier (e.g. `com.yourcompany.mightydoodle`) |
 
---

## 🎨 Asset Restoration Guide
 
To comply with third-party licensing requirements, several proprietary assets have been removed from this repository. The following guide explains how to restore the full experience using your own assets.
 
---
 
### 🎭 Shaders & Visuals
 
The original toon-style shaders have been replaced with Unity's standard **Unlit Shader** as a placeholder.
 
To restore visual quality:
 
1. Purchase and install **MK Toon Shader** from the Unity Asset Store
2. Reassign the shader to materials used on:
   - Characters
   - Environment assets
 
---
 
### 🌄 Backgrounds
 
#### Step 1 — Add Background Textures
 
Place your background image textures in:
 
```
Assets/ScriptableObjects/Resources
```
 
#### Step 2 — Assign Materials
 
Assign the textures to the materials located at:
 
```
Assets/Materials/Background/Texture Materials
```
 
#### Step 3 — Re-enable Background Transitions
 
Open `PanelAnimator.cs` and **uncomment** the following methods:
 
- `ShowNextPanel`
- `ShowPreviousPanel`
 
#### Step 4 — Fix Affected Prefabs
 
There are 1–2 prefabs that reference background transitions directly. Update these manually to restore correct behaviour.
 
---
 
### 🔊 Audio
 
All original music and sound effects have been removed. To restore audio:
 
1. Add your own audio files to the project
2. Re-link audio references in the relevant scripts and prefabs
 
---
 
### 🎮 Reward Mini-Games
 
The reward mini-games were removed due to licensing. The underlying reward system remains intact and supports **scene-based reward loading**, so replacing them is straightforward.
 
To add your own mini-games:
 
1. Create new Unity scenes for each mini-game
2. Hook each scene into the existing reward trigger logic
 
---

## 🔑 iOS Keychain — Removed Asset

### What It Was Used For
 
The app used a paid Unity Asset Store plugin — [iOS Keychain Plugin](https://assetstore.unity.com/packages/3d/characters/ios-keychain-plugin-43083#description) — to manage the **7-day free trial offer visibility** on the subscription screen.
 
On iOS, there is no native way to determine whether a user has previously subscribed or used the app under a given Apple ID. To ensure the free trial offer is shown only to genuinely new users, the app wrote a permanent flag to the device's iOS Keychain upon the user's first purchase. On subsequent launches — even after reinstalling the app — this Keychain entry persists, and the free trial UI is suppressed for that Apple ID.
 
On Android, the equivalent logic is handled automatically via **RevenueCat**, which tracks entitlement and purchase history natively.
 
### Current Behaviour (Asset Removed)
 
Because the iOS Keychain plugin has been removed due to licensing restrictions, the relevant methods in `PlayerPrefsManager.cs` are currently stubbed out:
 
- `SetSubscribedFromDevice()` — does nothing
- `HasSubscribedFromDevice()` — always returns `true`
 
As a result, **the 7-day free trial UI will always appear on the subscription screen on iOS**, regardless of whether the user has previously subscribed.
 
### How to Restore This Functionality
 
1. Purchase and import the [iOS Keychain Plugin](https://assetstore.unity.com/packages/3d/characters/ios-keychain-plugin-43083#description) from the Unity Asset Store, or find a suitable free alternative that provides iOS Keychain read/write access.
2. Open `PlayerPrefsManager.cs` and update the two stubbed methods with the commented-out Keychain logic:
 
```csharp
public static void SetSubscribedFromDevice()
{
    Keychain.SetValue(SubscribedFromDeviceKey, "true");
}
 
public static bool HasSubscribedFromDevice()
{
    var subscribed = Keychain.GetValue(SubscribedFromDeviceKey);
    return !string.IsNullOrEmpty(subscribed) && subscribed == "true";
}
```
 
Once restored, the system will work exactly as before — the free trial offer will only be shown to users who have never purchased a subscription under their Apple ID.
 
---

## License & Usage
 
This project is open-source under the GPL-3.0 License.
 
**Important:**
- "Mighty Doodle®" name, logo, and branding are trademarks of Mighty Doodle, Inc.
- Included assets and content are for use within this project only and may not be reused independently without permission.
 
### Third-Party Libraries
 
| Library | License |
|---|---|
| MemoryPack | MIT |
| Google ML Kit (Digital Ink Recognition) | Apache 2.0 |
| IOSNativeAlerts | MIT |
| EasingFunctions — C.J. Kimberlin | MIT |
| UnityWav / WavUtility | MIT |
 
---
 
## 📌 Quick Reference
 
A summary of the most important things to take care of before shipping.
 
| Item | Notes |
|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| 🖥️ Handwriting Recognition | Does not work in the Unity Editor — always test on a physical device |
| 🌐 Backend Server | Mandatory for all production features to function |
| ⏱️ RevenueCat Permissions | Google permissions can take up to 24 hours to propagate |
| 🔗 URLs.cs | Update all public-facing URLs before publishing |
| 🌐 APIEndpoints.cs | Update base URLs after deploying your backend server |
| 🎨 Assets | Proprietary assets have been removed — restoration required for the full experience |
| 🧪 Dev Mode | Set `RequireSubscription = false` in the Core Prefab to skip subscriptions during development |
