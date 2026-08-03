---
id: tool-07161
type: tool
area: 库
status: active
tags: [文风迁移, Python, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: ppocr-fine-tune
summary: 风格微调/文风迁移
source: https://github.com/bensonchow123/ppocr-fine-tune
created: 2026-07-18
updated: 2026-07-18
no: 7161
category: 画龙补充 / 扩容入库 — 补充源
repo: bensonchow123/ppocr-fine-tune
stars: 0
url: https://github.com/bensonchow123/ppocr-fine-tune
tier: "C"
use_case: "风格微调/文风迁移"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# bensonchow123/ppocr-fine-tune

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/bensonchow123/ppocr-fine-tune
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ppocr-fine-tune
- **拉取时间**：2026-07-25 19:12:42

related:
  - methods/QUICK_START.md
---

# PP-OCRv5 Fine-Tune
The actual code is at the company server at drow, the training data is avaliable there.

## 1. Create Training Dataset
- Go to `data-annotation-notes` to run PPOCRLabel on the server to label training data.
- Requires an X server installed on your PC
- The labeling program can be ran on your PC instead, but it is extremely slow if you don't have a PC with > 8GB of vram and > 10GB of ram and be able to run paddle paddle in GPU mode, which uses CUDA.

## 2. Train the Model
Using all 3 GPUs, remember to test GPU load with nvidia-smi
Paste the following one by one
```bash
tmux new-session -d -s ppocr-training
tmux attach-session -t ppocr-training
cd /home/drow/projects/ppocr-v5-fine-tune
source .venv/bin/activate
cd PaddleOCR
python3 -m paddle.distributed.launch --gpus '0,1,2' tools/train.py \
  -c ../finetuning-misc/PP-OCRv5_server_rec.yml \
  -o Global.pretrained_model=../finetuning-misc/PP-OCRv5_server_rec_pretrained.pdparams
```

tmux detach: Ctrl+b then d  
tmux reattach:
```bash
tmux attach-session -t ppocr-training
```

## 3. Evaluate / Export Model
Select the best epoch (replace `iter_epoch_xx`):
```bash
python3 tools/export_model.py \
  -c ../finetuning-misc/PP-OCRv5_server_rec.yml \
  -o Global.checkpoints=./output/PP-OCRv5_server_rec/iter_epoch_xx \
     Global.save_inference_dir=./PP-OCRv5_server_rec_infer
```

## 4. Test the Fine-Tuned Model
```bash
cd /home/drow/projects/ppocr-v5-fine-tune
python paddle-model-test.py
```
