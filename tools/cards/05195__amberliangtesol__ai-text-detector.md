---
id: tool-05195
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/amberliangtesol/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5195
category: 一、去 AI 味 / Humanizer 库
repo: amberliangtesol/ai-text-detector
stars: 0
url: https://github.com/amberliangtesol/ai-text-detector
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
content_hash: a21d8362e5597f96
  - methods/改稿润色指令库.md
---

# amberliangtesol/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/amberliangtesol/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：人工智慧資訊安全hw5
- **本地描述**：人工智慧資訊安全hw5
- **拉取时间**：2026-07-25 18:09:37

---

# AI Text Detector 🔍

## 📌 部署資訊

**🌐 部署網址：** https://ai-text-detect.streamlit.app/

**🤖 使用模型：** [AICodexLab/answerdotai-ModernBERT-base-ai-detector](https://huggingface.co/AICodexLab/answerdotai-ModernBERT-base-ai-detector)

**✨ 模型特點：**
- 基底是 ModernBERT-base，算是輕量版 BERT，跑起來不會太重
- 任務：判斷文字是 AI 寫的還是人寫的（二元分類）
  - Label 1 → AI-generated text
  - Label 0 → Human-written text

**📊 辨識報告說明：**
- **AI Detector Report（AI 檢測報告）**：顯示整體分析結果標題
- **Overall AI Percentage（整體 AI 比例）**：圓環圖顯示文本中 AI 生成內容的百分比
- **Detection Result（檢測結果）**：根據 AI 比例判斷文本為「AI Generated」或「Human Written」
- **Text Analysis Breakdown（文本分析細項）**：
  - 將文本分段分析，每段獨立評分
  - 顯示各段落的 AI 可能性（0-100%）
  - 使用紅色標示高 AI 可能性段落
- **Content Classification（內容分類）**：
  - **Identical**：完全相同的 AI 生成內容
  - **Minor Changes**：稍作修改的 AI 內容
  - **Paraphrased**：改寫過的 AI 內容  
  - **Unique**：獨特的人類撰寫內容
- **View Highlighted Text（檢視標註文本）**：顯示原文並用不同顏色標註可疑段落
- **Recommendations（建議）**：根據檢測結果提供改進建議

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

A modern web application that detects AI-generated content using the ModernBERT model from Hugging Face.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-text-detector.streamlit.app)

## 🌟 Features

- **AI Detection**: Uses state-of-the-art ModernBERT model to identify AI-generated text
- **Visual Analytics**: Interactive donut charts and segment analysis
- **Content Classification**: Categorizes text into 4 levels (Identical, Minor Changes, Paraphrased, Unique)
- **Real-time Analysis**: Instant feedback with confidence scores
- **Modern UI**: Clean, responsive design with animated elements
- **Sample Text**: Built-in example for quick testing

## 🚀 Live Demo

Visit the live app: [AI Text Detector](https://ai-text-detector.streamlit.app)

## 💻 Local Installation

```bash
# Clone the repository
git clone https://github.com/amberliangtesol/ai-text-detector.git
cd ai-text-detector

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📦 Requirements

- Python 3.8+
- streamlit==1.29.0
- transformers==4.36.0
- torch==2.1.0
- plotly==5.18.0
- numpy==1.24.3
- Pillow==10.1.0

## 📁 Project Structure

```
ai-text-detector/
├── app.py              # Main application
├── requirements.txt    # Package dependencies
├── assets/            # Resource folder
│   ├── logo.png       # Logo image
│   └── bg.png        # Background image
├── styles/            # Style folder
│   └── custom.css     # Custom CSS styles
├── .streamlit/        # Streamlit configuration
│   └── config.toml    # Theme and server settings
└── README.md          # Project documentation
```

## 🎯 How It Works

1. **Input Text**: Paste or type the text you want to analyze
2. **Click Detect**: The AI model analyzes your text
3. **View Results**: 
   - Overall AI percentage in a donut chart
   - Segment-by-segment analysis
   - Content classification breakdown
   - Detection verdict (AI Generated or Human Written)

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: AICodexLab/answerdotai-ModernBERT-base-ai-detector
- **Visualization**: Plotly
- **Styling**: Custom CSS with modern design

## 👤 Author

**amberliangtesol**

- GitHub: [@amberliangtesol](https://github.com/amberliangtesol)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
