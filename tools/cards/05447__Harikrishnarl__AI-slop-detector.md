---
id: tool-05447
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/harikrishnarl/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5447
category: 一、去 AI 味 / Humanizer 库
repo: Harikrishnarl/AI-slop-detector
stars: 0
url: https://github.com/harikrishnarl/ai-slop-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 086599656a47d667
  - methods/改稿润色指令库.md
---

# Harikrishnarl/AI-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/harikrishnarl/ai-slop-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Harikrishnarl/AI-slop-detector
- **拉取时间**：2026-07-25 18:19:01

---

# AI Slop Detector 🤖

A production-ready, privacy-first **Dual-Tier AI Text & Cliché Detection Pipeline**. This project combines rapid statistical stylometric rules with a local deep learning transformer core to filter low-variance, repetitive machine-generated text ("AI Slop") without sacrificing data privacy or incurring costly cloud API overhead.

---

## 🚀 Key Features

*   **Dual-Tier Routing Engine**: 
    *   **Tier 1 (Fast Statistical Rules)**: Instantly intercepts highly predictable or cliché-dense text using lightweight mathematical distributions, avoiding expensive model inference.
    *   **Tier 2 (Local Transformer Core)**: Routes high-risk, complex text payloads to an offline Hugging Face sequence classification model for deep structural fingerprinting.
*   **Stylometric Profile Analysis**: Computes real-time sentence-length variance (**Burstiness**), unique vocabulary distributions (**Type-Token Ratio**), and AI keyword saturation (**Cliché Density**).
*   **Interactive Streamlit Dashboard**: A modern, responsive workspace layout complete with live visual metric blocks, confidence scales, and automated regex-driven inline keyword highlighting.
*   **100% Data Privacy**: Runs completely locally on your hardware with zero data exfiltration to external third-party servers.

---

## 🛠️ Architecture Blueprint

```
[ Text Payload Input ]
          │
          ▼
┌────────────────────────────────────────┐
│  TIER 1: Fast Statistical Analyzer     │
│  (Computes Burstiness & Token Ratios)  │
└───────────────────┬────────────────────┘
                    │
       Does Cliché Density Pass Threshold?
          ┌─────────┴─────────┐
         YES                  NO
          │                    │
          ▼                    ▼
┌──────────────────┐ ┌────────────────────────────────┐
│  Instant Flag    │ │ TIER 2: Local Transformer Core │
│  (Deterministic) │ │ (Hugging Face Deep Attention)  │
└──────────────────┘ └────────────────────────────────┘
```

---

## 🗂️ Project Structure

```text
ai-slop-detector/
│
├── app.py             # Streamlit Interactive Front-End UI Dashboard
├── pipeline.py        # Core Dual-Tier Routing Engine & Math Logic
├── requirements.txt   # Pinpoint Project Dependencies
└── README.md          # Project Technical Documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone & Navigate to Project Directory
```bash
git clone https://github.com/yourusername/ai-slop-detector.git
cd ai-slop-detector
```

### 2. Configure Virtual Environment
**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*Note: If you run into Windows OS errors regarding `fbgemm.dll`, ensure you have the official [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe) installed or force install a clean PyTorch build using `pip install torch --index-url https://download.pytorch.org/whl/cpu`.*

---

## 🖥️ Running the Application

Launch the localized dashboard directly through your terminal:
```bash
streamlit run app.py
```
A browser tab will automatically open at `http://localhost:8501`.

---

## 📊 Understanding the Analytics Metric Suite

*   **Burstiness (Sentence Length Variance)**: Measures how dynamically sentence structure changes throughout the text body. Human writers inherently cluster highly variable sentence patterns (High Burstiness), whereas LLMs yield flat, uniform cadences (Low Burstiness).
*   **Cliché Density**: The mathematical percentage of text dedicated exclusively to common algorithmic corporate buzzwords (e.g., *"delve"*, *"tapestry"*, *"synergy"*, *"paramount"*).
*   **Unique Token Ratio (Type-Token Ratio)**: Measures lexical richness. Lower relative values pinpoint high repetition and predictable vocabulary profiles typical of baseline generative completions.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🔮 Future Roadmap Upgrades
*   **INT8 Model Quantization**: Compile the local Hugging Face transformer core to ONNX or INT8 formats to slash CPU inference cycles.
*   **Batch Parallel Uploads**: Integrate `joblib` multi-core mapping engines to support heavy-duty file uploads (.pdf, .docx, .csv) across massive operational folder structures.
*   **Custom Vector Fine-Tuning**: Swap baseline classifications with dedicated generative detectors like `roberta-base-openai-detector`.
