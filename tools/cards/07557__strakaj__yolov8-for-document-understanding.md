---
id: tool-07557
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: yolov8-for-document-understanding
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/strakaj/yolov8-for-document-understanding
created: 2026-07-18
updated: 2026-07-18
no: 7557
category: 画龙补充 / 扩容入库 — 补充源
repo: strakaj/yolov8-for-document-understanding
stars: 7
url: https://github.com/strakaj/yolov8-for-document-understanding
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# strakaj/yolov8-for-document-understanding

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/strakaj/yolov8-for-document-understanding
- **Stars**：7
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：yolov8-for-document-understanding
- **拉取时间**：2026-07-25 19:25:33

related:
  - methods/QUICK_START.md
---

# YOLOv8 for document understanding


## Insallation


Environment should have with torch>=1.7 (`[yolov8](yolov8/README.md)`) for example:
```bash
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```

Install YOLOv8 requirements:
```bash
pip install -r yolov8/requirements.txt
```

Install DocILE library:
```bash
pip install docile-benchmark
```

## Training and prediction
Before running the code it is necessary to edit the dataset config file: `yolov8/ultralytics/datasets/docile.yaml`.
The file contains information about the dataset:
 - path: `<path/to/docile/dataset>`
 - cache_location: `<folder/for/yolo/to/save/cache/files>`

YOLOv8 config file with parameters is located at: `yolov8/ultralytics/yolo/cfg/default.yaml`

### Train
```bash
python yolov8/train.py \
    --model_name yolov8x \
    --data_path ylov8/ultralytics/datasets/docile.yaml \
    --epochs 30 \
    --lr0 0.001 \
    --batch 8 \
    --imgsz 1280 \
    --workers 8 \
    --optimizer AdamW \
    --model yolov8x.pt \
    --char_grid_encoder three_digit_0 \
    --ch 6 \
    --seed 0 \
    --hsv_h 0.0 \
    --hsv_s 0.0 \
    --hsv_v 0.0 \
    --scale 0.0 \
    --fliplr 0.0 \
    --mosaic 0.0 
```
The above code will reproduce KILE results, to reproduce LIR results, `epochs` should be changed to `50` and `seed` to `1`

### Predict
```bash
python yolov8/predict.py \
    --run_path <path/to/yolov8/output/folder> \
    --dataset_path <path/to/docile/dataset>
```

### Predict on separate images
```bash
pip install easyocr
```
```bash
python yolov8/predict_image.py \
    --checkpoint_path <path/to/checkpoint.pt> \
    --output_path <path/to/output/folder> \
    --data_path <path/to/folder/with/images>
```
