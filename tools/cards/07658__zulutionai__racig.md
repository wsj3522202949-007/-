---
id: tool-07658
type: tool
area: 库
status: active
tags: [RAG, Python, 协议宽松, 本地优先, 英文文档, 人物设定, 本地写作]
title: racig
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/zulutionai/racig
created: 2026-07-18
updated: 2026-07-18
no: 7658
category: 画龙补充 / 扩容入库 — 补充源
repo: zulutionai/racig
stars: 9
url: https://github.com/zulutionai/racig
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls: []
related:
  - methods/QUICK_START.md
---

# zulutionai/racig

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/zulutionai/racig
- **Stars**：9
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：RaCig: A RAG-based Character-Consistent Story Image Generation Model
- **本地描述**：racig
- **拉取时间**：2026-07-25 19:29:07

related:
  - methods/QUICK_START.md
---

<div align="center">
<h1><a href="https://arxiv.org/abs/2506.12517">RaCig: A RAG-based Character-Consistent Story Image Generation Model</h1>
<a href='https://github.com/ZulutionAI/RaCig'><img src='https://img.shields.io/badge/GitHub-ZulutionAI-red?logo=github'></a>
<a href='https://huggingface.co/ZuluVision/RaCig'><img src='https://img.shields.io/badge/🤗%20Hugging%20Face-Model-blue'></a>
<a href='https://huggingface.co/datasets/ZuluVision/RaCig-Data'><img src='https://img.shields.io/badge/🤗%20Hugging%20Face-Dataset-green'></a>
 <a href='https://arxiv.org/abs/2506.12517'><img src='https://img.shields.io/badge/arXiv-2506.12517-b31b1b.svg'></a>   
<a href='https://github.com/ZulutionAI/RaCig/stargazers'><img src='https://img.shields.io/github/stars/ZulutionAI/RaCig?style=social'></a>

</div>


### 1. Multi-charater image generation with rich motion
<div align="center">
<img src="assets/teaser.png" alt="Teaser Image" width="700"/>
</div>

### 2. Model structure preview
<div align="center">
<img src="assets/model_structure.png" alt="Model Structure" width="700"/>
</div>


## 📖 Overview

RaCig is designed to generate images based on textual prompts and reference images for characters (referred to as "Characters"). It leverages several models and techniques, including:

*   Text-to-image retrieval (using CLIP)
*   IP-Adapter for incorporating reference image features (face and body/clothes)
*   ControlNet for pose/skeleton guidance
*   Action Direction DINO for action direction recognition
*   A pipeline (`RaCigPipeline`) to orchestrate the generation process.

The pipeline can handle multiple characters ("Characters") in a single scene, defined by their names, gender, and reference images (face and clothes).

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ZulutionAI/RaCig.git
    cd RaCig
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download necessary models and retrieval datasets:**
    
    Models: https://huggingface.co/ZuluVision/RaCig

    Put the models under checkpoint as follow:
    
    ```
    ./models/
    ├── action_direction_dino/
    │   └── checkpoint_best_regular.pth
    ├── controlnet/
    │   └── model.safetensors
    ├── image_encoder/
    │   ├── config.json
    │   ├── model.safetensors
    │   └── pytorch_model.bin
    ├── ipa_weights/
    │   ├── ip-adapter-plus-face_sdxl_vit-h.bin
    │   └── ip-adapter-plus_sdxl_vit-h.bin
    └── sdxl/
        └── dreamshaper.safetensors
    ```

    Retrieval datasets: https://huggingface.co/datasets/ZuluVision/RaCig-Data

    ```
    ./data
    ├── MSDBv2_v7
    ├── Reelshot_retrieval
    └── retrieve_info
    ```
## 💻 Usage
### Inference
1.  **Run Inference:**
    ```python
    python inference.py
    ```
2.  Generated images, retrieved images, and skeleton visualizations will be saved in the `output/` directory by default.
·
### Gradio

```python
python run_gradio.py
```


For more detailed instruction, see `[Gradio Interface Instructions (EN)](docs/gradio_instruction_en.md)` or `[Gradio Interface Instructions (中文)](docs/gradio_instruction_cn.md)`


## 🛠️ Training

1. We only train the controlnet, to make it recognize the feature map better. (The fused feature map after injecting IP information is quite hard for controlnet to constrain the pose, so we slightly finetune the controlnet)

2. We use the retrieval dataset to finetune it. The dataset structure is organized as above.

```bash
bash train.sh
```

## 🤝 Contributing



## ❤️ Acknowledgements

This project is based on the work of the following open-source projects and contributors:

* [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) - Image Prompt Adapter developed by Tencent AI Lab
* [xiaohu2015](https://github.com/xiaohu2015) 
