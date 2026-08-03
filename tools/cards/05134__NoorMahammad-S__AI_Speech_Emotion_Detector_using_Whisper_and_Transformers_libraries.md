---
id: tool-05134
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI_Speech_Emotion_Detector_using_Whisper_and_Transformers_libraries
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/noormahammad-s/ai_speech_emotion_detector_using_whisper_and_transformers_libraries
created: 2026-07-18
updated: 2026-07-18
no: 5134
category: 一、去 AI 味 / Humanizer 库
repo: NoorMahammad-S/AI_Speech_Emotion_Detector_using_Whisper_and_Transformers_libraries
stars: 7
url: https://github.com/noormahammad-s/ai_speech_emotion_detector_using_whisper_and_transformers_libraries
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# NoorMahammad-S/AI_Speech_Emotion_Detector_using_Whisper_and_Transformers_libraries

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/noormahammad-s/ai_speech_emotion_detector_using_whisper_and_transformers_libraries
- **Stars**：7
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：This project demonstrates a simple pipeline for Speech Emotion Recognition using Whisper for speech recognition, RoBERTa for text representation extraction, and BART for emotion detection.
- **本地描述**：This project demonstrates a simple pipeline for Speech Emotion Recognition using Whisper for speech recognition, RoBERTa for text representation extraction, and BART for emotion detection.
- **拉取时间**：2026-07-25 18:07:24

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ```                AI & ML Project                ```

# AI Speech Emotion Detector using Whisper and Transformers libraries
This project demonstrates a simple pipeline for Speech Emotion Recognition using Whisper for speech recognition, RoBERTa for text representation extraction, and BART for emotion detection.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies.

```bash
pip install -r requirements.txt
```

## Usage

1. Replace `"path_to_your_audio_file.wav"` in the `main()` function of `main.py` with the path to your actual audio file.

2. Run the main:

```bash
python main.py
```

The script will process the audio file, recognize speech using Whisper, extract text representation with RoBERTa, and detect emotion with BART.

## Configuration

- `main.py`: Main script that integrates Whisper, RoBERTa, and BART for speech emotion recognition.

## Models Used

- RoBERTa: [roberta-base](https://huggingface.co/roberta-base)
- BART: [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli)
- Whisper: [whisper-large](https://huggingface.co/whisper-large)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 
