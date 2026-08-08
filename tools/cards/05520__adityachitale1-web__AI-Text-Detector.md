---
id: tool-05520
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/adityachitale1-web/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5520
category: 一、去 AI 味 / Humanizer 库
repo: adityachitale1-web/AI-Text-Detector
stars: 0
url: https://github.com/adityachitale1-web/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 556d36e495d0b294
  - methods/改稿润色指令库.md
---

# adityachitale1-web/AI-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/adityachitale1-web/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：adityachitale1-web/AI-Text-Detector
- **拉取时间**：2026-07-25 18:21:44

---

# AI Text Detector — BrightPress (Deliverable 2)

A Streamlit dashboard that reads a piece of text and answers one question:
**did a HUMAN write this, or an AI?** — with a confidence score and an honest
account of when it cannot be trusted.

It serves the **Round-2** detector produced by the notebook in `../Deliverable 1`,
which was hardened through the GAN-style attack → retrain loop.

## Files

| File | Purpose |
|------|------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `app.py` | The Streamlit dashboard |
| `requirements.txt` | Python dependencies for Streamlit Cloud |
| `.streamlit/config.toml` | App theme |
| `.gitignore` | Keeps large model files / secrets out of Git |

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

If a `detector/` folder (saved by the notebook via `trainer2.save_model('detector')`)
sits next to `app.py`, or in `../Deliverable 1/detector`, the app loads it automatically.

## Deploy through GitHub → Streamlit Community Cloud

GitHub cannot hold the ~250 MB fine-tuned model, so publish the model to the
**Hugging Face Hub** and point the app at it with a secret.

### 1. Push your trained detector to the Hugging Face Hub

Run this once after the notebook finishes (Part 7 saved `./detector`):

```python
from huggingface_hub import HfApi, login
login()  # paste a HF token with write access
HfApi().create_repo("your-username/brightpress-detector", exist_ok=True)
HfApi().upload_folder(
    folder_path="detector",
    repo_id="your-username/brightpress-detector",
)
```

This uploads the model **and** `metrics.json`, so the dashboard shows your real
measured false-positive rate and scoreboard.

### 2. Push this folder to GitHub

```bash
git init
git add .
git commit -m "BrightPress AI text detector dashboard"
git branch -M main
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
```

### 3. Create the app on Streamlit Community Cloud

1. Go to <https://share.streamlit.io> and sign in with GitHub.
2. **New app** → pick your repo and branch.
3. Set **Main file path** to `Deliverable 2/app.py` (or `app.py` if this folder is the repo root).
4. Open **Advanced settings → Secrets** and add:

   ```toml
   MODEL_ID = "your-username/brightpress-detector"
   ```

5. **Deploy.**

The app resolves its model in this order: `MODEL_ID` secret → local `detector/` →
`../Deliverable 1/detector` → untrained base weights (with a warning).

## Responsible-use note

The dashboard always shows the **measured false-positive rate** and a mandatory
disclaimer: *never use this tool as sole evidence against a person.* Clean,
formulaic, or non-native-English writing is disproportionately flagged — see the
policy memo (Deliverable 3).
