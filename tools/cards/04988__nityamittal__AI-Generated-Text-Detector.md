---
id: tool-04988
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Generated-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/nityamittal/ai-generated-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 4988
category: 一、去 AI 味 / Humanizer 库
repo: nityamittal/AI-Generated-Text-Detector
stars: 0
url: https://github.com/nityamittal/ai-generated-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# nityamittal/AI-Generated-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/nityamittal/ai-generated-text-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：nityamittal/AI-Generated-Text-Detector
- **拉取时间**：2026-07-25 18:02:03

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**Overview**

This project implements an end-to-end text classification pipeline:

P1–P2: Two tokenizers (whitespace + improved tokenizer with normalization).

P3: Build a sparse term–document matrix (SciPy CSR) with a min-frequency cutoff.

P4–P10 (NumPy): Logistic regression via true SGD, stable sigmoid, log-likelihood tracking, convergence plots, and Kaggle submission.

P11–P18 (PyTorch): Convert SciPy→torch.sparse, define a LogisticRegression module, train with BCELoss + SGD, run L2/optimizer/tokenizer/learning-rate sweeps, and export a second Kaggle submission.

P19: Analyze top features (β weights) with and without L2.

Everything is sparse-first to avoid memory issues.

**Environment**

Python 3.8+ 
Libraries: numpy, scipy, pandas, scikit-learn, tqdm, matplotlib, torch

**Data Files**

Place these in the same directory as the notebook:

train.csv (columns: id, generation, label)
dev.csv (columns: id, generation, label)
test.csv (columns: id, generation)

In Colab, upload via the Files pane or mount Drive.

**File Outputs**

NumPy (P8–P10):

submission_numpy.csv

Optional logs/plots for LL and convergence (P8–P9)

PyTorch (P11–P18):

submission_torch_lr.csv

Logs (CSV) for plotting:

P13: p13_runA_1000steps_loss_every20.csv, p13_runB_1epoch_loss_every50.csv

P14: p14_logs_wd0.0.csv, p14_logs_wd0.001.csv, p14_logs_wd0.1.csv

P15: p15_logs_sgd.csv, p15_logs_rmsprop.csv, p15_logs_adamw.csv

P16: p16_logs_basic_whitespace.csv, p16_logs_better_tokenize.csv
+ model checkpoints p16_model_*.pt
+ cached tensors p16_*_X_train.pt, etc.

P17: p17_logs_lr_0p0001.csv, p17_logs_lr_0p005.csv, p17_logs_lr_0p05.csv

These logs let you re-plot without retraining.

**Mapping to Assignment Problems
**
Tokenization & Vectorization (P1–P3)

tokenize(text): whitespace split.

better_tokenize(text, **kwargs): lowercase, strip edge punctuation; optional normalization (URLs→<url>, @user→<user_mention>, #tag→<hashtag>, numbers→<num>).

build_vocab(texts, tokenizer, kwargs, min_freq): returns word2id.

vectorize_docs(texts, tokenizer, kwargs, word2id): SciPy CSR (counts).

add_bias_column(X): append bias column of 1s (NumPy LR).

NumPy Logistic Regression (P4–P10)

sigmoid(z): numerically stable.

log_likelihood(X, y, beta): full-data LL.

compute_gradient(xi, yi, beta): per-instance sparse gradient.

sgd_train(...): true SGD (one random row/update); optional LL logging.

logistic_regression(...): convenience wrapper (adds bias, fixed steps).

predict_proba/predict_label/predict(text, ...): helpers & single-text inference.

P8: 1000 steps, lr=5e-5, plot LL every 20 steps.

P9: Train until convergence (ΔLL < tol); plot LL & ΔLL; report Dev F1.

P10: Pick best NumPy model (Dev F1), predict on test, write submission_numpy.csv.

PyTorch Logistic Regression (P11–P18)

P11: to_sparse_tensor(csr): SciPy→torch.sparse COO.

Model: LogisticRegression(V) with parameters W (|V|) and b (scalar).

Trainer (P12): BCELoss + SGD; one random sparse row per step; periodic eval().

Experiments:

P13: 1000 steps (log every 20), then ≥1 epoch (log every 50 + Dev F1).

P14: L2 sweep via weight_decay (0, 1e-3, 1e-1); plot Loss & Dev F1.

P15: Optimizers: SGD vs RMSprop vs AdamW; plot Loss & Dev F1.

P16: Tokenizer comparison: whitespace vs better tokenizer (1 epoch, no L2).

P17: Learning rate sweep (small/medium/large).

P18: Choose best run; write submission_torch_lr.csv.

P19 (Feature Analysis)

Extract top positive/negative β words (with & without L2).

Discuss overlap, themes, whether features make sense, and which model generalizes better.

**Recommended Run Order**

Upload train/dev/test to Colab.

Run P1–P3 (tokenizers, vocab, vectorization).

NumPy (P4–P10):

P8: 1000-step LL plot.

P9: Convergence run + LL/ΔLL plots + Dev F1.

P10: submission_numpy.csv.

PyTorch (P11–P18):

P11: SciPy→torch.sparse.

P12: Base trainer (SGD + BCELoss).

P13: 1000-step sanity + 1 epoch.

P14–P17: L2/optimizer/tokenizer/lr sweeps (split across cells; logs saved).

P18: submission_torch_lr.csv.

P19: β-feature analysis and short write-up.

**Key Hyperparameters**

Tokenizer (TOK_KWARGS): normalize URLs/users/hashtags/numbers; keep internal hyphens/apostrophes; lowercase.

Vocab: MIN_FREQ = 250 (per assignment baseline).

NumPy LR: learning_rate, num_steps, and convergence (max_steps, check_every, tol).

PyTorch LR: lr, weight_decay (L2), optimizer (SGD/RMSprop/AdamW), log_every, eval_every, epochs, seed.


**Typical Results (Will Vary)**

NumPy: Dev F1 ≈ 0.75 after a solid convergence run.

PyTorch: With longer training, Dev F1 ≈ 0.78–0.79.

L2 (P14): Small L2 ~neutral/slight stability gain; large L2 slows learning and reduces F1.

Optimizers (P15): RMSprop/AdamW often learn faster early; final F1 often similar.

Tokenizers (P16): Whitespace sometimes outperforms the “better” tokenizer here (over-normalization can drop signal).

LR (P17): Too small → slow and underfit; too large → unstable; mid-range tends to win.

**Quick API Cheat Sheet**

Tokenizers:
tokenize(text) → tokens
better_tokenize(text, **TOK_KWARGS) → tokens

Vectorization:
build_vocab(train_texts, tokenizer, TOK_KWARGS, min_freq) → (word2id, freq)
vectorize_docs(texts, tokenizer, TOK_KWARGS, word2id) → csr_matrix
add_bias_column(X) → csr_matrix (+1s column)

NumPy LR:
sigmoid(z), log_likelihood(X, y, beta)
sgd_train(...), logistic_regression(...)
predict_proba, predict_label, predict(text, ...)

PyTorch LR:
to_sparse_tensor(csr) → torch.sparse_coo_tensor
LogisticRegression(V) (W, b)
predict_proba_sparse(model, X)
evaluate_dev(model, X_dev, y_dev) → (loss, f1)
Trainers for fixed steps / epochs / L2 / optimizer / tokenizer / lr sweeps


