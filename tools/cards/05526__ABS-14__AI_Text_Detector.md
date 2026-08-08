---
id: tool-05526
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI_Text_Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/abs-14/ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5526
category: 一、去 AI 味 / Humanizer 库
repo: ABS-14/AI_Text_Detector
stars: 0
url: https://github.com/abs-14/ai_text_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8e29d040653cd677
  - methods/改稿润色指令库.md
---

# ABS-14/AI_Text_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/abs-14/ai_text_detector
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ABS-14/AI_Text_Detector
- **拉取时间**：2026-07-25 18:21:57

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector

This project is an AI text detector that classifies text as either related to AI or not. It uses a Support Vector Machine (SVM) classifier trained on a sample dataset and provides a web interface using Streamlit.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The AI Text Detector is a simple machine learning application that distinguishes between AI-related texts and non-AI-related texts. It is built using Python's scikit-learn library for the SVM classifier and Streamlit for the web interface.

## Features

- Train an SVM classifier on sample data.
- Classify text as AI-related or not.
- Display the classification result.
- Show the sample data distribution in a pie chart.
- Update the data distribution dynamically based on the classification results.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ABS-14/AI_Text_Detector
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app_UI.py
    ```

2. Open your web browser and go to `http://localhost:8501` to interact with the AI Text Detector.

### Code Explanation

- **Training the Model**: The SVM classifier is trained on a small dataset of AI-related and non-AI-related texts.
- **Predicting Text**: The classifier predicts whether an input text is AI-related or not.
- **Dynamic Chart**: The distribution of AI and non-AI texts is shown in a pie chart and updates dynamically based on user input.

### Example

1. **Model Information**: Displays the accuracy of the trained model.
2. **Sample Data Distribution**: Shows the initial distribution of AI and non-AI texts.
3. **Classify Text**: Enter text to classify and see the updated distribution chart.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ABS-14/AI_Text_Detector/blob/main/LICENSE) file for details.
