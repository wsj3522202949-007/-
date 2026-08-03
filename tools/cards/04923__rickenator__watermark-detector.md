---
id: tool-04923
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: watermark-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/rickenator/watermark-detector
created: 2026-07-18
updated: 2026-07-18
no: 4923
category: 一、去 AI 味 / Humanizer 库
repo: rickenator/watermark-detector
stars: 0
url: https://github.com/rickenator/watermark-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# rickenator/watermark-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rickenator/watermark-detector
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Local browser-only AI watermark detection for text using OpenAI's statistical scheme
- **本地描述**：Local browser-only AI watermark detection for text using OpenAI's statistical scheme
- **拉取时间**：2026-07-25 17:59:33

---

# WaterMarkDetector

**Local, browser-only AI watermark detection for text.**

Detects whether text was generated using OpenAI's probabilistic watermarking scheme — no API keys, no backend, no server. Runs entirely in your browser.

## How It Works

### The Watermarking Scheme (Krenn et al., 2024)

OpenAI's watermark is a **statistical bias**, not a visible pattern. During text generation:

1. **Tokenizer:** The model's vocabulary (GPT-2, 50,257 tokens) is split into "green" and "red" lists for each token position.
2. **Context-dependent:** The green/red split depends on the **previous 2 tokens** (the context bigram), making it adaptive and unguessable.
3. **Bias:** With probability `γ` (typically 0.5), the model is biased to prefer tokens from the green list.
4. **Result:** Watermarked text has a slightly higher proportion of green-list tokens than random text — not enough for a human to notice, but statistically detectable.

### Detection

The detector reverses this process:

1. **Tokenize** the input text using GPT-2's exact BPE tokenizer (vocab + 50k merges, bundled).
2. **Generate green lists** for each token position using the same n-gram-dependent hashing:
   - Take the previous 2 token IDs as context.
   - Hash them with a secret seed to produce a per-position green list.
   - Check whether each actual token falls in its green list.
3. **Z-test:** Compare the observed green-list proportion to the expected proportion `γ = 0.5`.
   - `z = (observed − expected) / standard_error`
   - `standard_error = √(γ(1−γ) / n)` where n = token count.
4. **Decision:** If `z > 4.0`, conclude watermark likely present. The corresponding p-value is ~0.00003 — false positives on random text are statistically impossible.

### Why N-Gram Dependence Matters

The original paper uses context-dependent (2-gram) green lists, not a single global hash per token. Without n-gram context:

- Every token uses the same seed → the bias pattern is much weaker and easier to detect by chance.
- The detector loses sensitivity to the actual watermark signal.

WMD implements the full context-dependent scheme to match the original paper's methodology.

## Installation

1. Open Chrome → `chrome://extensions/`
2. Enable **Developer mode** (toggle in the top-right)
3. Click **Load unpacked**
4. Select this folder

## Usage

| Tab | What it does |
|-----|-------------|
| **Paste Text** | Paste text into the editor and click Analyze |
| **Active Page** | Extracts visible text from the current webpage (strips nav, ads, footers) and analyzes it |

### Reading Results

| Label | Meaning |
|-------|---------|
| ✅ No Watermark | Text does not show statistical watermarking patterns |
| ⚡ Suspicious | Borderline — some bias toward green-list tokens, not conclusive |
| ⚠️ Watermark Likely | Strong statistical evidence of OpenAI-style watermarking |

### Parameters

| Parameter | Default | Description |
|-----------|---------|----------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `gamma` | 0.5 | Proportion of tokens in the green list |
| `vocabSize` | 50,257 | GPT-2 vocabulary size |
| `threshold` | 4.0 | Z-score threshold for "watermark likely" |
| `seed` | 42 | Secret key for hash-based green list generation |

## Architecture

```
manifest.json          — Chrome extension manifest (MV3)
popup.html + popup.js  — UI: tabs, text input, results display
watermark.js           — Core logic: GPT-2 tokenizer + n-gram green lists + z-test
background.js          — Service worker: page text extraction, analysis routing
content.js             — Content script: page text extraction, UI cleanup
merges.txt             — Bundled GPT-2 BPE merges (50k rules)
icons/                 — Extension icons (16/48/128)
```

## Limitations

- **Only detects OpenAI-style watermarking.** Does not detect other AI watermarking schemes, steganographic methods, or post-hoc modifications.
- **Probabilistic, not definitive.** Even at z > 4.0, results are statistical conclusions, not proofs.
- **Tokenizer dependency.** Requires GPT-2's exact tokenizer. Text tokenized through other models (Llama, Qwen, etc.) will not be detected.
- **Short text sensitivity.** Below 100 words, natural word frequency variance can produce false positives. Results below 250 words should be treated as preliminary.
- **No adversarial defense detection.** Text that has been paraphrased or edited after generation may evade detection.

## Dependencies

None. This is a completely self-contained Chrome extension. The only external resource is the bundled `merges.txt` file (446 KB).

## References

- Krenn, R., et al. "Cryptographic Verification of AI-Generated Text." _arXiv preprint arXiv:2310.11530_, 2024.
- OpenAI GPT-2 tokenizer: [merges.txt](https://huggingface.co/gpt2/blob/main/merges.txt)
