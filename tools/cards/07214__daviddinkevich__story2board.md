---
id: tool-07214
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: story2board
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/daviddinkevich/story2board
created: 2026-07-18
updated: 2026-07-18
no: 7214
category: 画龙补充 / 扩容入库 — 补充源
repo: daviddinkevich/story2board
stars: 264
url: https://github.com/daviddinkevich/story2board
tier: "S"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 45dc0cc4b7051d92
  - methods/QUICK_START.md
---

# daviddinkevich/story2board

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/daviddinkevich/story2board
- **Stars**：264
- **语言**：Python
- **License**：MIT
- **Topics**：deep-learning, diffusion-models, generative-ai, machine-learning, storyboards, text-to-image, training-free
- **GitHub 描述**：Official implementation for "Story2Board: A Training‑Free Approach for Expressive Storyboard Generation"
- **本地描述**：story2board
- **拉取时间**：2026-07-25 19:14:22

---

# Story2Board: A Training‑Free Approach for Expressive Storyboard Generation

**Project page:** https://daviddinkevich.github.io/Story2Board  
**Paper (arXiv):** https://arxiv.org/abs/2508.09983
**Code:** this repo

---

## Abstract

We present **Story2Board**, a training-free framework for expressive storyboard generation from natural language. Existing methods narrowly focus on subject identity, overlooking key aspects of visual storytelling such as spatial composition, background evolution, and narrative pacing. To address this, we introduce a lightweight consistency framework composed of two components: **Latent Panel Anchoring**, which preserves a shared character reference across panels, and **Reciprocal Attention Value Mixing (RAVM)**, which softly blends visual features between token pairs with strong reciprocal attention. Together, these mechanisms enhance coherence without architectural changes or fine-tuning, enabling state-of-the-art diffusion models to generate visually diverse yet consistent storyboards. We convert free-form stories into grounded panel-level prompts with an off-the-shelf LLM, and evaluate on a new **Rich Storyboard Benchmark** that measures layout diversity, background-grounded storytelling, and consistency. Qualitative/quantitative results and a user study show that Story2Board produces more dynamic, coherent, and narratively engaging storyboards than existing baselines.

<p>
    <img src="docs/teaser.webp" width="800px"/>  
    <br/>
    A training-free method for storyboard generation that balances identity consistency with cinematic layout diversity.
</p>

---

## ⚙️ Installation

### Platform Support
- ✅ Officially supported: **Linux**, Python **3.12**, CUDA **12.x**
- 💻 Windows / macOS: not officially tested, but you can try with the alternative requirements file: `requirements_all_platforms.txt`

We recommend a fresh Conda environment with Python 3.12.

---

### 1) Clone the repository

```bash
# 1) Clone the repository
git clone https://github.com/DavidDinkevich/Story2Board.git
cd Story2Board

# 2) Create and activate env
conda create -n story2board python=3.12
conda activate story2board

# 3) Install dependencies
pip install -r requirements.txt
```

> Tip: If you want a specific CUDA build of PyTorch, install PyTorch first following the official instructions, then run `pip install -r requirements.txt`.

---

## Quickstart

The entry point is `main.py`. The **required** arguments are:

- `--subject` – the main subject (e.g., “smiling boy”).
- `--ref_panel_prompt` – description of the **reference (top) panel**.
- `--panel_prompts` – one or more prompts for the remaining panel(s).
- `--output_dir` – where to save results.

Minimal skeleton:

```bash
python main.py   --subject "SUBJECT_NAME"   --ref_panel_prompt "REFERENCE_PANEL_TEXT"   --panel_prompts "PANEL_1_TEXT" "PANEL_2_TEXT" ...   --output_dir path/to/out
```

### Concrete example

```bash
python main.py   --subject "fox with shimmering fur and glowing eyes"   --ref_panel_prompt "stepping onto a mossy stone path under twilight trees"   --panel_prompts     "bounding across a fallen tree over a mist-covered ravine glowing faintly with constellations"     "perched atop a broken archway of ancient stone, vines and silver moss hanging down, the twilight sky glowing behind him"     "watching a meteor shower from the edge of a luminous lake that reflects the stars perfectly"   --output_dir outputs
```

This will generate a storyboard where the **top** panel is the reference, and each **bottom** panel reuses the same character identity while varying the scene/action.

---

## Outputs

- Generated images are written to `--output_dir`.  
- The constructed, per-panel prompts are logged for reproducibility.

---

## Method Overview (Very Brief)

- **Latent Panel Anchoring**: reuses a shared reference latent to stabilize identity across panels.  
- **RAVM (Reciprocal Attention Value Mixing)**: gently blends attention **values** between token pairs with strong reciprocal attention, preserving the model’s prior while improving cross-panel coherence.

---

## Changelog

- **21 Aug 2025**: Fixed missing line for **Latent Panel Anchoring (LPA)** in the released code (commit [34537e0](https://github.com/DavidDinkevich/Story2Board/commit/34537e02eac4e108fe1f8dae16e901d681af8887)).  
  - Restores expected behavior described in the paper.  

## BibTeX

```bibtex
@article{dinkevich2025story2board,
  title={Story2Board: A Training-Free Approach for Expressive Storyboard Generation},
  author={Dinkevich, David and Levy, Matan and Avrahami, Omri and Samuel, Dvir and Lischinski, Dani},
  journal={arXiv preprint arXiv:2508.09983},
  year={2025}
}
```

## Acknowledgements

This repository builds on the excellent open-source ecosystems of **PyTorch** and **Hugging Face Diffusers**, and uses **FLUX.1-dev** weights as the base T2I model.

related:
  - methods/QUICK_START.md
---

## License

See `LICENSE` in this repository.
