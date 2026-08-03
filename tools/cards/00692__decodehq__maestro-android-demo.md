---
id: tool-00692
type: tool
area: 库
status: active
tags: [Shell, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: maestro-android-demo
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/decodehq/maestro-android-demo
created: 2026-07-18
updated: 2026-07-18
no: 692
category: 二、网文 / 长篇 AI 写作系统 库
repo: decodehq/maestro-android-demo
stars: 1
url: https://github.com/decodehq/maestro-android-demo
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# decodehq/maestro-android-demo

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/decodehq/maestro-android-demo
- **Stars**：1
- **语言**：Shell
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Demo repository showcasing mobile UI test automation using Maestro on the Android Wikipedia app. Includes example tests, workflows, and best practices for writing reliable, maintainable mobile test flows.
- **本地描述**：Demo repository showcasing mobile UI test automation using Maestro on the Android Wikipedia app. Includes example tests, workflows, and best practices for writing reliable, maintainable mobile test flows.
- **拉取时间**：2026-07-23 22:59:12

---

# 🛰️ Maestro Android Demo

A minimal example of running **Maestro** Android flows locally or in CI, with **Allure** reporting baked in.

---

## 📚 Table of Contents
- [🚀 Quick Start (local)](#-quick-start-local)
- [☁️ Running in CI (GitHub Actions + BrowserStack)](#️-running-in-ci-github-actions--browserstack)
- [🧩 Project Structure](#-project-structure)
- [🖼️ Example](#-example)
- [❤️ Credits](#️-credits)

---

## 🚀 Quick Start (local)

### 1️⃣ Setup

```bash
brew install allure     # or choco install allure
curl -Ls https://get.maestro.mobile.dev | bash
git clone https://github.com/decodehq/maestro-android-demo.git
cd maestro-android-demo
```

### 2️⃣ Run Tests

> ⚠️ **Note:** Application needs to be installed on the device before running the tests.

```bash
./local.sh test .                      # run all flows
./local.sh test "Onboarding flow.yaml" # run one flow

maestro test .                         # standalone Maestro (no allure)
maestro test "Onboarding flow.yaml"    # standalone Maestro (no allure)
```

📁 Logs are saved to:  
`artifacts/debug-output/<flow>/maestro.log`

### 3️⃣ Generate Allure Report 

> ⚠️ **Note:** Requires running tests via `./local.sh test` first,  
so Allure JSON files can be generated from Maestro logs.

```bash
./local.sh report    # converts + builds Allure HTML
./local.sh open      # serves artifacts/allure-report
```

Allure output layout:
```
artifacts/
 ├─ debug-output/      # raw Maestro logs
 ├─ allure-results/    # Allure JSON
 └─ allure-report/     # HTML report
```

---

## ☁️ Running in CI (GitHub Actions + BrowserStack)

This repository includes a **fully automated CI workflow** that:
1. Runs Maestro E2E tests on **BrowserStack** devices.  
2. Generates Allure 2 results via  
   `.github/actions/generate-allure-files/maestro_all_to_allure.py`.  
3. Publishes the HTML report to **GitHub Pages** using  
   `.github/actions/publish-allure-to-pages/action.yml`.

To enable CI:
1. Add these secrets in your GitHub repository:
   - `BROWSERSTACK_USERNAME`
   - `BROWSERSTACK_ACCESS_KEY`
   - `SLACK_WEBHOOK_URL` *(optional, for notifications)*  
2. Trigger the workflow manually from **Actions → “Run E2E Test”**.

Example workflow file:  
`.github/workflows/run-e2e-test.yml`

---

### ☁️ How BrowserStack Tests Are Started

The CI workflow (`.github/workflows/run-e2e-test.yml`) runs Maestro flows on BrowserStack devices, converts logs to **Allure**, and publishes results to **GitHub Pages**.

### 🔐 Required Secrets
Add these in **GitHub → Settings → Secrets and variables → Actions**:
- `BROWSERSTACK_USERNAME`
- `BROWSERSTACK_ACCESS_KEY`
- *(optional)* `SLACK_WEBHOOK_URL`

---

### 📦 What Must Be Uploaded to BrowserStack

You need **two things**:

1. **App build** (APK/AAB) → generates an **App ID** (`bs://<app-id>`)  
2. **Maestro Suite** (zip of your flows) → generates a **Suite ID** (`bs://<suite-id>`)

> 💡 If `browserstack_suite_id` is **empty**, the workflow will automatically zip and upload the Maestro workspace for you.

---

### 🧱 Maestro Suite Contents

Include only your test assets:
```
.maestro/                    # (optional) workspace config
subflows/                    # shared subflows
*flow.yaml                   # test flows (e.g. "Onboarding flow.yaml", "Search flow.yaml")
```

**Exclude:** `artifacts/`, `allure-*`, `.git/`, `node_modules/`, and build outputs.

Example zip command:
```bash
zip -r maestro-workspace.zip \
  .maestro subflows \
  "Onboarding flow.yaml" "Search flow.yaml"
```

---

### ⬆️ Getting App and Suite IDs

#### A) From BrowserStack Dashboard
1. Go to **App Automate → Upload** and upload your APK → copy **App ID** (`bs://...`)
2. Go to **Maestro → Upload Suite** → upload `maestro-workspace.zip` → copy **Suite ID** (`bs://...`)

#### B) Via API
```bash
# Upload app → returns {"app_url":"bs://<app-id>"}
curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
  -X POST "https://api-cloud.browserstack.com/app-automate/upload" \
  -F "file=@/path/to/app.apk"

# Upload Maestro Suite → returns {"suite_url":"bs://<suite-id>"}
curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
  -X POST "https://api-cloud.browserstack.com/app-automate/maestro/v2/suites" \
  -F "file=@maestro-workspace.zip"
```

---

### ▶️ Triggering the Workflow

Open **Actions → “Maestro E2E on BrowserStack” → Run workflow**, and provide:

- `browserstack_app_id` — required (`bs://abcd1234...`)
- `browserstack_suite_id` — optional (auto-zip if empty)
- `generate_allure` — `true` to build Allure results
- `send_slack` — `true` if `SLACK_WEBHOOK_URL` is set

**Device matrix:** controlled by environment:
```yaml
env:
  BSTACK_DEVICES: "Google Pixel 7-13.0, Samsung Galaxy S22-12.0, OnePlus 11R-13.0"
```

Format: `"<Device Name>-<OS Version>"`, comma-separated.

---

### 🧪 Workflow Summary

1. Zips & uploads Maestro suite (if needed)
2. Runs tests on all devices via BrowserStack Maestro
3. Downloads logs for each test
4. Converts logs → **Allure JSON** (`generate-allure-files`)
5. Publishes **Allure HTML** to GitHub Pages (`publish-allure-to-pages`)

**Workflow Artifacts**
| Name | Description |
|------|--------------|
| `allure-results-<build-id>` | Allure JSON results (used for HTML generation) |
| `browserstack-build` | Metadata of the BrowserStack build |
| `maestro_flows_zip` | Zipped Maestro workspace uploaded to BrowserStack |

---

## 🧩 Project Structure

```
.github/
 ├─ actions/
 │   ├─ generate-allure-files/
 │   │   ├─ action.yml
 │   │   └─ maestro_all_to_allure.py
 │   └─ publish-allure-to-pages/
 │       └─ action.yml
 │
 └─ workflows/
     └─ run-e2e-test.yml               # CI workflow entrypoint
.maestro/                              # Maestro workspace config
artifacts/                             # Output folder for logs/reports
subflows/                              # Shared Maestro subflows
Onboarding flow.yaml                   # Example flow
Search flow.yaml                       # Example flow
local.sh                               # Main local runner (test + report)
README.md
LICENSE
.gitignore
```

---

## 🖼️ Example

### ✅ GitHub Actions Run

This demo workflow runs Maestro E2E tests across **BrowserStack** devices, converts logs to **Allure**, and publishes the results to **GitHub Pages**.

| Stage | Description |
|--------|--------------|
| 🧪 **maestro-e2e** | Executes Maestro test flows on BrowserStack devices |
| 📊 **generate-allure-results** | Parses BrowserStack logs → generates Allure JSON |
| 🌐 **publish-allure-to-pages** | Builds and deploys Allure HTML report |
| 🔔 **notify** | (Optional) Sends Slack summary with pass/fail stats |

| Github | Allure |
|--------|-----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| <img width="1321" height="710" alt="Screenshot 2025-11-12 at 07 43 37" src="https://github.com/user-attachments/assets/a9d514e3-c530-4509-8b22-be4da8fccc83" /> | <img width="1345" height="817" alt="Screenshot 2025-11-12 at 07 45 40" src="https://github.com/user-attachments/assets/bf734454-05be-4d49-87e7-fb968de082c2" /> |


📍Example run:  
[Maestro E2E on BrowserStack #35](https://github.com/decodehq/maestro-android-demo/actions/runs/19246141804)


## ❤️ Credits

Built with [Maestro](https://maestro.mobile.dev/)  
Allure Reporting powered by [Qameta Allure](https://docs.qameta.io/allure/)  
Maintained by [DECODE Agency](https://decode.agency)
