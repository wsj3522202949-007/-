---
id: tool-07590
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: art_inpainting
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/venkatasivanaga/art_inpainting
created: 2026-07-18
updated: 2026-07-18
no: 7590
category: 画龙补充 / 扩容入库 — 补充源
repo: venkatasivanaga/art_inpainting
stars: 1
url: https://github.com/venkatasivanaga/art_inpainting
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# venkatasivanaga/art_inpainting

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/venkatasivanaga/art_inpainting
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：art_inpainting
- **拉取时间**：2026-07-25 19:26:33

---

# 🎨 Prior-Guided Art Inpainting with Local Edge-Tuned Texture Enhancement

## 🧠 Overview
This project restores damaged artworks — such as scratched, cracked, or missing regions — while preserving the original artistic style, brushwork, and texture.  
It combines **prior-guided inpainting** with **edge-tuned local enhancement** to produce curator-friendly restorations that maintain authenticity and transparency.

The system learns from both damaged and undamaged artworks and reconstructs missing areas with style-consistent textures.  
A lightweight UI allows users to upload an image, define a mask (manually or automatically), and preview restorations with change heatmaps before exporting results.

---

## 📁 Project Structure
```
Art_Inpainting/
├─ README.md
├─ env.yml                  # conda env (Windows CUDA) – or use requirements.txt on macOS
├─ requirements.txt         # minimal pip env (macOS / CPU/MPS friendly)
├─ .gitignore
├─ pyproject.toml           # Optional: project metadata / build
├─ git_repo_link.txt        # Handy link/reference to this repo
├─ setup.ipynb              # One-time environment & sanity checks
│
├─ configs/
│  ├─ data.yaml             # paths, image size, split sizes
│  └─ inpaint_gan.yaml      # model + loss weights + training params
│
├─ data/     #contains the info about data
│
│
└─ src/
   ├─ __init__.py
   ├─ api.py               # FastAPI server (/api/inpaint)
   ├─ data.py              # dataset, transforms, split builder, loader
   ├─ infer.py             # CLI inference over images/folders
   ├─ losses.py            # LossBundle (+masked L1, boundary L1, LPIPS, Gram, TV)
   ├─ masks.py             # mask generators (irregular + edge/ridge)
   ├─ model.py             # GatedUNet + PatchDiscriminator + utils
   ├─ setup.ipynb          # notebook helper (optional)
   └─ train.py             # training loop
├─ web/
│  ├─ ui.typescript       # Interface
│
├─ reports/                   # Contains IEEE reports
└─ notes/                   # experiments, TODOs, ablation notes
             # README.md
```

---

## 🧩 Problem Context
Museums and archives face challenges with digitized artworks suffering from cracks, tears, or missing regions.  
Manual digital retouching is time-consuming and subjective.  

This project provides an AI-based restoration pipeline that:
- Preserves **style consistency** (brushwork, color harmony, surface grain)
- Maintains **sharp boundaries** using edge-aware guidance
- Offers **transparent restorations** via heatmaps and watermarked exports

---

## 🖼️ Datasets

### 1. Damaged & Undamaged Artworks (Kaggle)
- **Source:** [Kaggle - Damaged and Undamaged Artworks](https://www.kaggle.com/datasets/pes1ug22am047/damaged-and-undamaged-artworks)
- **Usage:** Primary dataset for classifier training and inpainting experiments  
- **Download:**
  ```bash
  kaggle datasets download -d pes1ug22am047/damaged-and-undamaged-artworks -p data/kaggle_art_damage --unzip
  ```

### 2. Art Images — Clear and Distorted (Kaggle)
- **Source:** [Kaggle - Art Images Clear and Distorted](https://www.kaggle.com/datasets/sankarmechengg/art-images-clear-and-distorted)
- **Usage:** Auxiliary dataset for self-supervised inpainting and robustness testing  
- **Download:**
  ```bash
  kaggle datasets download -d sankarmechengg/art-images-clear-and-distorted -p data/kaggle_art_clear_distorted --unzip
  ```

---

## 🧮 Frameworks & Libraries
- **PyTorch**, **TorchVision**, **PyTorch Lightning**
- **OpenCV**, **scikit-image**, **NumPy**, **Matplotlib**
- **LPIPS**, **pytorch-fid** for perceptual metrics
- **Streamlit** or **Gradio** for UI


---

## 🚀 How to Run

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/venkatasivanaga/Art_Inpainting.git
cd Art_Inpainting
```

### 2. Download Datasets
```bash
Run the dataset download commands above or execute `setup.ipynb`.
```
### 3. Generate Masks (irregular + crack-like)
```bash
python -m src.masks \
  --image-root "data/unpaired_dataset_art" \
  --out data/masks \
  --per-image 2 \
  --edge crack --frangi
```
### 4. Make Train/Val/Test Splits
```bash
python -m src.data \
  --data-config configs/data.yaml \
  --make-splits \
  --out data/splits

```
Outputs text files of image basenames in data/splits/ (e.g., train.txt, val.txt, test.txt).
### 5. Train the Inpainting GAN
```bash
python -m src.train \
  --data-config configs/data.yaml \
  --config configs/inpaint_gan.yaml \
  --splits data/splits \
  --out runs/gan_512
```

Model: Gated-Conv U-Net + seam-focused PatchGAN

Losses: masked L1, boundary L1, LPIPS, Gram(style), TV

Checkpoints & logs will appear under runs/gan_512/.

### 6. Inference (CLI)

Single image
```bash
python -m src.infer \
  --image path/to/damaged.jpg \
  --mask  path/to/mask.png \
  --ckpt  runs/gan_512/best.pt \
  --out   outputs/restored.png
```

Batch folder
```bash
python -m src.infer \
  --input path/to/folder_or_image \
  --checkpoint runs/gan_512/best.pt \
  --output outputs/
```
### 7. Start the REST API (FastAPI)
```bash 
uvicorn api:app --app-dir src --host 0.0.0.0 --port 8000
# Docs: http://127.0.0.1:8000/docs
```
### 8. Run the streamlit interface (two-panel demo)

Left: upload damaged image (and optional mask).

Right: “Show results” for paired demo or wire to the API.
---

## 🗓️ Implementation Timeline

| Week | Focus | Outcome |
|------|--------|----------|
| Oct 20–26 | Data pipeline & mask generation | Dataset ready, EDA complete |
| Oct 27–Nov 2 | Baseline classifier + basic UI | Functional classifier & mock UI |
| Nov 3–16 | Core inpainting model | Prior-guided restoration working |
| Nov 17–30 | Seam sharpening + UX | Interactive demo (Streamlit) |
| Dec 1–11 | Final polish | Presentation-ready results |

---

## 🖼️ Sample Outputs (UI)

**Stage 1 — Home page UI**  
![UI — empty state](Results/Interface.jpg)

**Result 1**  
![UI — Output1](Results/Output1.jpg)

**Result 2**  
![UI — Output2](Results/Output2.jpg)

--- 

## 🙏 Acknowledgments

LaMa, Gated Convolution inpainting, LPIPS, and PatchGAN ideas that inspired components of this repo. Thanks to dataset contributors on Kaggle.

related:
  - methods/QUICK_START.md
---

## 👩‍💻 Author
**Venkata Siva Reddy Naga**  
_Data Science | vs.naga@ufl.edu 

