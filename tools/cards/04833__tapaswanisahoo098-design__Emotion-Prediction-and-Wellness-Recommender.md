---
id: tool-04833
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 去AI味]
title: Emotion-Prediction-and-Wellness-Recommender
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/tapaswanisahoo098-design/emotion-prediction-and-wellness-recommender
created: 2026-07-18
updated: 2026-07-18
no: 4833
category: 一、去 AI 味 / Humanizer 库
repo: tapaswanisahoo098-design/Emotion-Prediction-and-Wellness-Recommender
stars: 0
url: https://github.com/tapaswanisahoo098-design/emotion-prediction-and-wellness-recommender
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 204ceaf6305e0806
  - methods/改稿润色指令库.md
---

# tapaswanisahoo098-design/Emotion-Prediction-and-Wellness-Recommender

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/tapaswanisahoo098-design/emotion-prediction-and-wellness-recommender
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Emotion Detector & Wellness Recommender is an AI-powered web application built with Streamlit that analyzes the emotional tone of a user's text and responds with personalized wellness support.It bridges the gap between emotional awareness and actionable self-care by combining natural language understanding with culturally rich music recommendations
- **本地描述**：Emotion Detector & Wellness Recommender is an AI-powered web application built with Streamlit that analyzes the emotional tone of a user's text and responds with personalized wellness support.It bridges the gap between emotional awareness and actionable self-care by combining natural language understanding with culturally rich music recommendations
- **拉取时间**：2026-07-25 17:56:07

---

# 🎭 Emotion Detector & Wellness Recommender

A Streamlit web application that detects emotions from text input and provides personalized wellness recommendations, activities, motivational quotes, and curated music videos in multiple Indian and English languages.

---

## ✨ Features

- **🧠 Emotion Detection** — Analyzes your text using the `j-hartmann/emotion-english-distilroberta-base` model via Hugging Face Inference API
- **📊 Emotion Breakdown** — Visual progress bars showing confidence scores for all detected emotions
- **🏃 Activity Suggestions** — Personalized activities based on your current emotional state
- **💬 Motivational Quotes** — Curated quotes matching your mood
- **🎵 Music Recommendations** — Curated YouTube video previews in **19 languages**:
  - 🇬🇧 English
  - 🇮🇳 Hindi, Odia, Telugu, Tamil, Bengali, Kannada, Punjabi, Marathi, Gujarati
  - 🇮🇳 Malayalam, Assamese, Bhojpuri, Haryanvi, Kashmiri, Konkani, Maithili, Gondi, Rajasthani

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Emotion Model | `j-hartmann/emotion-english-distilroberta-base` |
| Inference API | Hugging Face `huggingface_hub` |
| Environment Config | `python-dotenv` |

---

## 📁 Project Structure

```
emotion-detector/
│
├── app.py                  # Main Streamlit application
├── .env                    # Environment variables (HF_TOKEN)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/emotion-detector.git
cd emotion-detector
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
HF_TOKEN=your_huggingface_api_token_here
```

> 💡 Get your free API token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### 5. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🎯 Supported Emotions

| Emotion | Message |
|---|---|
| 😄 Joy | Uplifting activities and happy music |
| 😢 Sadness | Comforting suggestions and soothing music |
| 😠 Anger | Calming techniques and relaxing music |
| 😨 Fear | Grounding exercises and supportive music |
| 🤢 Disgust | Refreshing activities and neutral music |
| 😲 Surprise | Adventure-themed suggestions and energetic music |
| 😐 Neutral | Mindfulness activities and peaceful music |

---

## 🌍 Music Languages

The app supports curated video previews and YouTube search for **19 languages**, making it accessible across India and beyond. Each language has emotion-matched playlists, mixes, and direct video thumbnails with watch links.

---

## 📝 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `HF_TOKEN` | Hugging Face API token for inference | ✅ Yes |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🙏 Acknowledgements

- [Hugging Face](https://huggingface.co/) for the emotion classification model
- [Streamlit](https://streamlit.io/) for the web framework
- All regional music artists and YouTube creators featured in recommendations
