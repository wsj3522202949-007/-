---
id: tool-05331
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ibm-ai-developer-phyton-flask-submission-emotion-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ibm75896/ibm-ai-developer-phyton-flask-submission-emotion-detector
created: 2026-07-18
updated: 2026-07-18
no: 5331
category: 一、去 AI 味 / Humanizer 库
repo: IBM75896/ibm-ai-developer-phyton-flask-submission-emotion-detector
stars: 1
url: https://github.com/ibm75896/ibm-ai-developer-phyton-flask-submission-emotion-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# IBM75896/ibm-ai-developer-phyton-flask-submission-emotion-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ibm75896/ibm-ai-developer-phyton-flask-submission-emotion-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Emotion Detection web app using Watson NLP and Flask, detects anger, disgust, fear, joy, and sadness from text input.
- **本地描述**：Emotion Detection web app using Watson NLP and Flask, detects anger, disgust, fear, joy, and sadness from text input.
- **拉取时间**：2026-07-25 18:14:38

---

# Emotion Detection Application

## Project Overview

The project implements an **Emotion Detection Application** using the **Watson NLP Library**. It analyzes text input and identifies emotional tone across multiple emotion categories, deployed as a web application using Flask.

---

## Project Structure

```
EmotionDetection/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
├── server.py
├── test_emotion_detection.py
└── README.md
```

---

## Tasks Completed

### Task 1: GitHub Repository
Public GitHub repository containing this README.md with project name and details.

---

### Task 2: Emotion Detection Application (`emotion_detection.py`)
Created the core application function using the Watson NLP library to detect emotions from text input.

**Activity 1:** `emotion_detection.py` implements the `emotion_detector(text_to_analyse)` function, which sends a POST request to the Watson NLP Emotion Predict endpoint.

**Activity 2:** Terminal output confirms the application was successfully imported and tested without errors.

---

### Task 3: Format the Output
Modified the `emotion_detector` function to return a structured dictionary containing individual emotion scores and the dominant emotion.

**Output format:**
```python
{
    'anger': <score>,
    'disgust': <score>,
    'fear': <score>,
    'joy': <score>,
    'sadness': <score>,
    'dominant_emotion': '<emotion_name>'
}
```

**Activity 1:** Updated `emotion_detection.py` returns correct output format.  
**Activity 2:** Terminal output confirms accurate output formatting.

---

### Task 4: EmotionDetection Package (`__init__.py`)
Validated the `EmotionDetection` directory as a proper Python package by adding the required import statement in `__init__.py`.

**Activity 1:** `__init__.py` includes: `from .emotion_detection import emotion_detector`  
**Activity 2:** Terminal output confirms `EmotionDetection` is a valid, importable package.

---

### Task 5: Unit Tests (`test_emotion_detection.py`)
Wrote unit tests using Python's `unittest` framework to validate emotion detection accuracy across test phrases.

**Test cases include:**
- `"I am glad this happened"` → dominant emotion: `joy`
- `"I am really mad about this"` → dominant emotion: `anger`
- `"I feel disgusted just hearing about this"` → dominant emotion: `disgust`
- `"I am so sad about this"` → dominant emotion: `sadness`
- `"I am really afraid that this will happen"` → dominant emotion: `fear`

**Activity 1:** `test_emotion_detection.py` contains all required unit tests.  
**Activity 2:** Terminal output confirms all unit tests passed.

---

### Task 6: Web Deployment with Flask (`server.py`)
Deployed the emotion detection application as a web service using Flask, exposing an `/emotionDetector` route.

**Activity 1:** `server.py` implements Flask routes for web deployment.  
**Activity 2:** Screenshot `6b_deployment_test.png` shows successful application deployment.

---

### Task 7: Error Handling
Updated the application to gracefully handle blank or invalid input.

**Changes made:**
- `emotion_detection.py`: Returns `None` values and `None` dominant emotion when status code is `400`
- `server.py`: Detects `None` dominant emotion and returns: *"Invalid text! Please try again."*

**Activity 1:** Updated `emotion_detection.py` handles status code `400`.  
**Activity 2:** Updated `server.py` handles blank input errors.  
**Activity 3:** Screenshot `7c_error_handling_interface.png` validates error handling.

---

### Task 8: Static Code Analysis
Ran PyLint static code analysis on `server.py` to ensure code quality and PEP8 compliance.

**Activity 1:** `server.py` is compliant with PyLint standards.  
**Activity 2:** Terminal output shows a **perfect score of 10.00/10** from PyLint.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Watson NLP Library | Emotion analysis engine |
| Flask | Web framework for deployment |
| Requests | HTTP client for Watson API calls |
| unittest | Unit testing framework |
| PyLint | Static code analysis |

---

## How to Run

### 1. Install dependencies
```bash
pip install flask requests
```

### 2. Start the Flask server
```bash
python server.py
```

### 3. Access the application
Open your browser and navigate to:
```
http://localhost:5000
```

### 4. Run unit tests
```bash
python -m pytest test_emotion_detection.py
```

### 5. Run static code analysis
```bash
pylint server.py
```

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Author

Submitted as part of the **IBM AI Developer Certificate** (Developing AI Applications with Python and Flask).
