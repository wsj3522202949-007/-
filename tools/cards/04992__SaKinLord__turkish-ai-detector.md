---
id: tool-04992
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: turkish-ai-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sakinlord/turkish-ai-detector
created: 2026-07-18
updated: 2026-07-18
no: 4992
category: 一、去 AI 味 / Humanizer 库
repo: SaKinLord/turkish-ai-detector
stars: 0
url: https://github.com/sakinlord/turkish-ai-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: caa9d2e041bea8cd
  - methods/改稿润色指令库.md
---

# SaKinLord/turkish-ai-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sakinlord/turkish-ai-detector
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Turkish AI text detector runtime
- **本地描述**：Turkish AI text detector runtime
- **拉取时间**：2026-07-25 18:02:12

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Turkish AI Detector

Turkish AI text detector runtime using language-model curvature signals and a document-level meta-classifier.

The runtime configuration:

- Model: `ytu-ce-cosmos/Turkish-Llama-8b-v0.1`
- Segment policy: 15-50 words, minimum 3 words per sentence-like unit
- Calibrated human/generated score distributions
- Document classifier: 10 statistical segment features

## Runtime Note

This repository does not include datasets or model weights. The model is downloaded from Hugging Face at runtime.

The Llama-8B detector requires a capable GPU for practical inference speed. It is not practical for live use on a 4GB VRAM laptop.

## Project Layout

```text
turkish-ai-detector/
├── turkish_ai_detector/
│   ├── __init__.py
│   ├── __main__.py
│   ├── defaults.py
│   ├── segmentation.py
│   ├── curvature.py
│   ├── probability.py
│   ├── document.py
│   └── pipeline.py
├── requirements.txt
├── pyproject.toml
├── .python-version
├── .gitignore
└── LICENSE
```

Private datasets, experiment scripts, raw outputs, reports, and model files are intentionally excluded.

## Installation

```bash
pip install -r requirements.txt
```

Editable local install:

```bash
pip install -e .
```

## Python Usage

```python
from turkish_ai_detector import Detector

detector = Detector()
report = detector.analyze("Analiz etmek istediğiniz Türkçe metni buraya girin.")

print(report.ai_score)
print(report.label)
print(report.confidence)
print(report.to_json(include_segments=False))
```

## Command Line Usage

```bash
python -m turkish_ai_detector "Analiz etmek istediğiniz Türkçe metin."
python -m turkish_ai_detector --file makale.txt
python -m turkish_ai_detector --json --file makale.txt
```

## How It Works

1. Turkish text is normalized and grouped into sentence-aligned segments.
2. Each segment is scored with a Fast-DetectGPT-style curvature signal.
3. The raw score is converted to a generated-text probability using calibrated Gaussian densities.
4. Document-level statistics are extracted from all segments.
5. A frozen Logistic Regression-style meta-classifier produces the final AI score and label.

## Limitations

- This detector is a statistical signal, not ground truth.
- Short text is less reliable because it produces too few segments.
- Changing the model, domain, segmentation policy, or calibration requires retesting.
- Paraphrasing and manual editing can reduce detectability.
- Full inference requires GPU resources for practical speed.

## License

MIT. See [LICENSE](https://github.com/SaKinLord/turkish-ai-detector/blob/main/LICENSE).

## Reference

Bao, G., Zhao, Y., Teng, Z., Yang, L., & Zhang, Y. (2023).
*Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature.*
[arXiv:2310.05130](https://arxiv.org/abs/2310.05130)
