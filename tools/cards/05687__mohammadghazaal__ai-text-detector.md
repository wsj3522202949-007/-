---
id: tool-05687
type: tool
area: 库
status: active
tags: [文风迁移, Python, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: ai-text-detector
summary: 风格微调/文风迁移
source: https://github.com/mohammadghazaal/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5687
category: 一、去 AI 味 / Humanizer 库
repo: mohammadghazaal/ai-text-detector
stars: 0
url: https://github.com/mohammadghazaal/ai-text-detector
tier: "C"
use_case: "风格微调/文风迁移"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: af7a5a4acffe771a
  - methods/改稿润色指令库.md
---

# mohammadghazaal/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mohammadghazaal/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：mohammadghazaal/ai-text-detector
- **拉取时间**：2026-07-25 18:27:54

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI vs Human Text Detector — ModernBERT-large + LoRA

```
src/detector/
  data.py      load_data, tokenize_df
  model.py     build_model (LoRA), FocalLossTrainer, compute_metrics, ci95
train.py       CONFIG + training loop (imports detector)
app.py         Gradio demo UI
pyproject.toml makes `src/` importable via `pip install -e .`
```

## Setup
```bash
pip install -e .
pip install -r requirements.txt
```

## Run
```bash
python train.py --smoke-test      # sanity check, seconds
python train.py                   # full run: ModernBERT-large + LoRA, 3 seeds
cp -r output/best_model_seed42 saved_model
python app.py                     # Gradio UI, localhost:7860
```

## VS Code + Colab GPU
Edit locally in VS Code. Push to GitHub. Open `colab_launcher.ipynb` in Colab
(Runtime → GPU), update the clone URL, run all cells — trains on free T4.

## Settings
LoRA r=64/α=128 (all-linear), focal loss γ=2.0, lr=1e-4, fp16 + gradient
checkpointing, early stopping (patience=5), 3-seed 95% CI.
