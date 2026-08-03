---
id: tool-07568
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: image-restoration-using-gan
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/tanishakhemka/image-restoration-using-gan
created: 2026-07-18
updated: 2026-07-18
no: 7568
category: 画龙补充 / 扩容入库 — 补充源
repo: tanishakhemka/image-restoration-using-gan
stars: 1
url: https://github.com/tanishakhemka/image-restoration-using-gan
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# tanishakhemka/image-restoration-using-gan

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/tanishakhemka/image-restoration-using-gan
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：image-restoration-using-gan
- **拉取时间**：2026-07-25 19:25:52

---

# Image Restoration for Damaged Artworks

## Overview

This project explores scalable, automated restoration of damaged artwork using **deep learning**, including:
- **GAN-based inpainting**
- **Diffusion models**
- **Realistic degradation simulation**
- **Perceptual and quantitative evaluation**

We introduce multiple architectures and degradation functions to simulate realistic damage (e.g., noise, stains, cracks), and evaluate performance using PSNR and SSIM.

---

## Motivation

Traditional restoration is labor-intensive, expensive, and subjective. Our system provides an assistive tool to help:
- Museums and archivists preserve cultural heritage
- Researchers test restoration techniques at scale
- AI art applications handle damaged input data

---

## Project Structure
├── diffusion-restoration.py              # Full DDPM restoration pipeline           
├── GenerateDegradation.py                # Custom degradation module           
├── image_inference.py                    # Script for inference using saved checkpoints           
├── SAClipAutoDirModel.py                 # Advanced restoration using artifact-aware CLIP           
├── ImageQualityEvaluator.py              # PSNR & SSIM evaluation module            
├── MLPS_Project_Final_code.ipynb         # GAN and UNet-based model experiments           
├── README.md                                 

---

## Dataset

- **Source**: Kaggle’s *Best Artworks of All Time*
- **Content**: 8,000+ classical and modern paintings
- **Preprocessing**:
  - Center crop + resize (256×256 or 128×128)
  - Normalization to [-1, 1]
  - Train/Val/Test split: 70/15/15

---

## Degradation Types Simulated

Implemented in `GenerateDegradation.py`:

- Gaussian noise
- Salt-and-pepper noise
- Blur
- Color fading
- Canvas cracks
- Yellowing (aging varnish)
- Stains and water damage
- Dust particles

Apply either single or combined degradations using:
bash
python GenerateDegradation.py 
--input_dir artworks
--degradation_type multiple

---

## Model Architectures

### 1. **GAN-Based Restoration**
- **Generator**: ResNet-based
- **Discriminator**: PatchGAN
- **Losses**: Adversarial + Perceptual (VGG) + L1

### 2. **Diffusion Model (DDPM)**
- **Noise Scheduler**: Linear β
- **UNet Backbone**: Time-conditioned skip-connection network
- **Training**: Noise prediction with MSE loss
- **Restoration**: Partially noised image → reverse sampling

### 3. **SA-CLIP + Diffusion Hybrid**
- **Artifact Detection**: Uses CLIP to classify dominant degradation
- **Conditioned Sampling**: Diffusion conditioned on text/image embedding
- **Final Restoration**: Consistency Decoder + NAFNet

---

## Evaluation

Implemented in `ImageQualityEvaluator.py`:
- **PSNR**
- **SSIM**
- **Visualization plots**
- Summary stats: mean, std, range

---

## How to Run

### Train the Diffusion Model

bash python diffusion-restoration.py

You can optionally modify:
- EPOCHS, TIMESTEPS, BATCH_SIZE
- Noise schedule: BETA_START, BETA_END

### Inference on New Images

bash python image_inference.py 
--checkpoint best_diffusion_model.pth 
--image_dir ./degraded/

### Advanced Artifact-Aware Restoration

bash python SAClipAutoDirModel.py 
--input artwork.jpg 
--process-all

---

## Results Summary

| Model      | PSNR ↑ | SSIM ↑ | Comments                        |
|------------|--------|--------|---------------------------------|
| U-Net      | 27.6   | 0.84   | Blurry, lacks high-frequency    |
| GAN        | 25.8   | 0.89   | Better texture & edge realism   |
| Diffusion  | ~26.5  | ~0.87  | Robust, slower inference        |
| SA-CLIP    | –      | –      | Adaptive to artifact type       |

> GANs yielded the best **visual** results; Diffusion offered more **robustness**, and SA-CLIP adds **semantic guidance**.

---

## Future Directions

- use GAN + Diffusion in a hybrid architecture
- Add **style preservation** loss to keep artistic intent
- Human-in-the-loop: let curators refine ambiguous restorations

related:
  - methods/QUICK_START.md
---

## Citation & Acknowledgments

This project was developed as part of **11-785: Intro to Deep Learning** at **Carnegie Mellon University**, Spring 2025.  

Data courtesy of **Kaggle** and restoration baselines inspired by **AutoDIR (arXiv:2310.10123)**.
