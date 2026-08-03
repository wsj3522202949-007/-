---
id: tool-05383
type: tool
area: 库
status: active
tags: [TTS, Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 本地写作]
title: youtube-ai-slop-audio-detector
summary: 小说转语音/有声书
source: https://github.com/emilzmmn04/youtube-ai-slop-audio-detector
created: 2026-07-18
updated: 2026-07-18
no: 5383
category: 一、去 AI 味 / Humanizer 库
repo: emilzmmn04/youtube-ai-slop-audio-detector
stars: 0
url: https://github.com/emilzmmn04/youtube-ai-slop-audio-detector
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# emilzmmn04/youtube-ai-slop-audio-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/emilzmmn04/youtube-ai-slop-audio-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Colab experiment for transcript-routed synthetic speech detection in YouTube videos
- **本地描述**：Colab experiment for transcript-routed synthetic speech detection in YouTube videos
- **拉取时间**：2026-07-25 18:16:32

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# YouTube AI-Slop Audio Detector

An experimental Google Colab pipeline that combines two weak-but-complementary signals:

1. fetch the video's existing YouTube captions with timestamps;
2. score the complete transcript in overlapping 24-, 48-, and 96-word windows;
3. merge every timestamped region above the text-routing threshold and cover it with overlapping 4-second audio clips;
4. score those clips with a synthetic-speech detector; and
5. rank the video from 0–100 using the five strongest voice-model results and export the evidence.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/emilzmmn04/youtube-ai-slop-audio-detector/blob/main/youtube_ai_slop_detector_colab.ipynb)

## Run it

1. Open the Colab notebook using the badge above.
2. Choose **Runtime → Change runtime type → T4 GPU**.
3. Run the setup and configuration cells.
4. Paste a YouTube URL. The notebook installs a Colab-side PO-token provider for `yt-dlp`; if YouTube still blocks the datacenter IP, it prompts for a media upload while still using the URL for captions.
5. Run the remaining cells in order.

The notebook saves:

- `transcript.json` — timestamped YouTube-caption output;
- `transcript_windows.csv` — transcript-window AI-writing scores;
- `detected_text_regions.csv` — merged timestamp regions selected by the text model;
- `clip_scores.csv` — synthetic-voice scores for every slice inside those regions; and
- `run_summary.json` — experimental video-level aggregates.

## Models

- Transcript source: YouTube captions via [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api)
- Text routing: [`GeorgeDrayson/modernbert-ai-detection-raid-mage`](https://huggingface.co/GeorgeDrayson/modernbert-ai-detection-raid-mage)
- Synthetic voice: [`SpeechAntiSpoofingBenchmarks/Wav2Vec2-Small-AntiDeepfake-NDA`](https://huggingface.co/SpeechAntiSpoofingBenchmarks/Wav2Vec2-Small-AntiDeepfake-NDA), an Arena-hosted 95M-parameter detector trained on real and synthetic speech

## Important limitations

- Transcript detection is used only to select timestamped regions for audio analysis. AI-written text does not prove that a voice is synthetic.
- The routing threshold controls recall: lower values send more transcript regions to the audio model.
- This transcript-first design can miss TTS reading human-written text; measure router recall separately from voice-model recall.
- Scores are not calibrated for YouTube. The notebook reports evidence; its provisional threshold is not a production blocking rule.
- Video/channel-disjoint evaluation and YouTube/AAC/Opus re-encoding tests are required before comparing accuracy.
- The audio detector is released under **CC BY-NC-SA 4.0**. This repository's MIT license covers only the code and notebook, not downloaded models or datasets.
- YouTube downloads from Colab can occasionally be blocked. File upload is included as a fallback.
- The PO-token helper is [`bgutil-ytdlp-pot-provider`](https://github.com/Brainicism/bgutil-ytdlp-pot-provider), installed and run only inside the Colab VM.

## Local execution

This project is intentionally Colab-first. Local model execution is not required. The notebook can still be structurally validated with:

```bash
python3 tests/validate_notebook.py
```

## License

The repository code is MIT-licensed. Third-party models and datasets retain their own licenses.
