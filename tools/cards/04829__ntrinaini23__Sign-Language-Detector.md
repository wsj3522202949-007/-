---
id: tool-04829
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 去AI味]
title: Sign-Language-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ntrinaini23/sign-language-detector
created: 2026-07-18
updated: 2026-07-18
no: 4829
category: 一、去 AI 味 / Humanizer 库
repo: ntrinaini23/Sign-Language-Detector
stars: 0
url: https://github.com/ntrinaini23/sign-language-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ntrinaini23/Sign-Language-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ntrinaini23/sign-language-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI-powered Sign Language Predictive Communicator that uses MediaPipe, TensorFlow, OpenCV, Flask, and React to recognize hand gestures in real time, generate predictive text with a Trie-based NLP engine, and convert sentences into speech. Designed to improve accessible communication through intelligent AI and Computer Vision.
- **本地描述**：An AI-powered Sign Language Predictive Communicator that uses MediaPipe, TensorFlow, OpenCV, Flask, and React to recognize hand gestures in real time, generate predictive text with a Trie-based NLP engine, and convert sentences into speech. Designed to improve accessible communication through intelligent AI and Computer Vision.
- **拉取时间**：2026-07-25 17:55:57

---

# Sign Language Predictive Communicator (Assistive AI Lab)

This is a complete, real-time Sign Language Recognition and Predictive Communication Assistant designed for high-accuracy letter/digit input, automatic word prediction utilizing Tries, and speech synthesis output.

The system uses **MediaPipe Hands** landmark coordinate extraction (21 joints, 63 coordinates normalized relative to the wrist joint) instead of brute-force pixel image classifiers, achieving **90%+ prediction accuracy** while completely ignoring complex camera lighting and background interference.

---

## 📂 Project Structure

```text
sign_language_predictive_ai/
├── app.py                      # Core dynamic Flask Web Server & routing API
├── train_landmark_model.py      # Keras MLP training script, early stopping, reports
├── extract_landmarks.py        # Normalizes raw Kaggle images to landmark arrays
├── requirements.txt            # Local Python dependencies requirements
├── README.md                   # Installation & Kaggle system configurations guidance
│
├── dataset/                    # Target directory for your downloaded Kaggle partitions
│   └── (Your ASL sign alphabet/digit folders)
│
├── models/
│   ├── sign_landmark_model.h5  # Best compiled neural network weights
│   └── class_names.npy         # Categories string array mapping
│
├── engine/
│   ├── __init__.py
│   ├── hand_tracker.py         # Handles MediaPipe joint extraction & draws bones
│   ├── gesture_engine.py       # Orchestrates tracker tracks and model inferences
│   └── smoothing.py            # Stabilizes prediction jitter via majority vote
│
├── logic/
│   ├── __init__.py
│   ├── trie.py                 # Core Prefix Trie search index algorithm
│   ├── predictor.py            # Handles sentence building, space, and suggestions list
│   └── dictionary.txt          # Vocabulary weights dictionary
│
└── utils/
    ├── __init__.py
    ├── speech.py               # Background async speech synthesizer using pyttsx3
    └── kaggle_downloader.py    # Downloads/unpacks datasets using your Kaggle APIs
```

---

## ⚙️ Requirements & Local Setup

### 1. Initialize Virtual Environment
Set up an isolated python ecosystem to guarantee dependency compatibility:
```bash
# Create local virtual setup environment
python3 -m venv venv

# Activate active configuration profile
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install Stable Libraries
```bash
pip install -r requirements.txt
```

---

## 🔑 Kaggle Dataset Setup

This project uses standard ASL Alphabet and Digit Kaggle datasets for joint coordinate training.

### A. Place API Credentials
1. Register/Login to [Kaggle](https://www.kaggle.com).
2. Go to your **Account Settings** tab and click **Create New API Token**.
3. Download the generated `kaggle.json` file.
4. Move this file inside your user directory:
   * **Linux/macOS**: `~/.kaggle/kaggle.json`
   * **Windows**: `C:\Users\<YourUsername>\.kaggle\kaggle.json`
5. Apply correct reading permissions:
   * **Linux/macOS**: `chmod 600 ~/.kaggle/kaggle.json`

### B. Trigger Auto-Download
Run the following terminal commands to fetch your target dataset cleanly of choice (replace with your desired Kaggle slug, such as `grassknoted/asl-alphabet` or `mudit007/sign-language-digits-dataset`):
```bash
kaggle datasets download -d DATASET_OWNER/DATASET_NAME -p dataset --unzip
```
*Note: Make sure your target directory unzips folders in either of these standard layouts:*
- `dataset/A-samples/`, `dataset/B-samples/` (the label will automatically extract as `"A"`, `"B"`)
- `dataset/A/`, `dataset/B/`, `dataset/0/` (standard direct mapping label)

---

## 🏋️ Landmark Extraction & Model Training

Once folders are extracted, parse custom 21-joint coordinates and compile your neural classification model:

### 1. Extract Hand Landmarks 
Runs images through MediaPipe to compute normalized 63 feature coordinates (relative to wrist joints):
```bash
python extract_landmarks.py
```
This saves:
- `models/X_landmarks.npy` (Extracted gesture coordinates matrix)
- `models/y_labels.npy` (Category labels)

### 2. Train Deep MLP Keras Classifier
Builds and fits Keras Multi-Layer Perceptron (Dense (256) -> Batch Normalization -> Dropout -> Dense (128) -> Dense (64)) with early stopping callbacks, displaying extensive test-set confusion matrices and precision metrics:
```bash
python train_landmark_model.py
```
This saves:
- `models/sign_landmark_model.h5` (Best compiled neural weights)
- `models/class_names.npy` (String classifier mapping list)

---

## 🚀 Running the Live Dashboard

Boot the local server dashboard which starts live predictions instantly:
```bash
python app.py
```
Visit the following local link inside your standard browser:
`http://127.0.0.1:5000`

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 💡 Key Design Highlights
- **Normalized Joints Approach**: Coordinates are extracted relative to the wrist point, meaning prediction accuracy is robust against background elements, hand size variations, and distance from the camera.
- **Trie-Based Predictive Writing**: As you sign individual hand letter coordinates, a central Trie queries common english dictionaries to offer instant predictive word completions, greatly accelerating typing speeds.
- **Auto-Locking Mechanism**: The hand prediction smoothing tracks continuous characters and auto-appends them to words once stable for 1.0 seconds with high-confidence (> 85%), preventing letter duplication and stream flickering.
