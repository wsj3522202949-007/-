---
id: tool-05309
type: tool
area: 库
status: active
tags: [文风迁移, Jupyter Notebook, 协议传染, 本地优先, 英文文档, 改稿润色, 本地写作]
title: ai-text-detector
summary: 风格微调/文风迁移
source: https://github.com/manojhunasimarad/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5309
category: 一、去 AI 味 / Humanizer 库
repo: manojhunasimarad/ai-text-detector
stars: 0
url: https://github.com/manojhunasimarad/ai-text-detector
tier: "C"
use_case: "风格微调/文风迁移"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 3328f7bfa068e30f
  - methods/改稿润色指令库.md
---

# manojhunasimarad/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/manojhunasimarad/ai-text-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：This is the mini project for machine learning
- **本地描述**：This is the mini project for machine learning
- **拉取时间**：2026-07-25 18:13:49

---

# AI Text Detector

An ensemble-based machine learning system for detecting AI-generated text using multiple models (SVM, XGBoost, BERT). This project combines traditional ML and deep learning approaches for robust text authenticity detection.

## Project Structure

```
ai-text-detector/
├── src/
│   ├── app/
│   │   └── app.py              # Streamlit web application
│   ├── models/
│   │   ├── SVM/                # SVM model artifacts (pkl files)
│   │   ├── XGBOOST/            # XGBoost model artifacts (pkl files)
│   │   ├── BERT/               # BERT fine-tuned model 1
│   │   └── BERT_2/             # BERT fine-tuned model 2
│   ├── notebooks/
│   │   ├── svm_detection.ipynb              # SVM model training
│   │   ├── xgboost_detection.ipynb          # XGBoost model training
│   │   └── bert_finetuning.ipynb            # BERT fine-tuning
│   └── utils/                  # Utility functions
├── docs/
│   ├── report/                 # Project documentation and report
│   │   ├── main.tex
│   │   └── AI_Text_Detector_Report.docx
│   ├── presentation/           # Presentation slides
│   │   ├── results_overview_presentation.tex
│   │   └── AI_Text_Detector_Presentation.pptx
│   ├── datasets/               # Training and test datasets
│   │   ├── dataset_2.csv       # SVM training data (20k samples)
│   │   ├── dataset_3.csv       # XGBoost training data (20k samples)
│   │   ├── dataset_4.csv       # Additional training data (20k samples)
│   │   ├── dataset_5.csv       # Additional training data (20k samples)
│   │   └── test_dataset.csv    # Test set (5k samples)
│   ├── AI Text Detector.pdf
│   ├── Group_4_latex.pdf
│   └── ppt_format_v2.md
├── requirements.txt            # Python dependencies
├── .gitignore
└── README.md                   # This file
```

## Features

- **Multi-Model Ensemble**: Combines 4 models for robust predictions
  - TF-IDF + Linear SVM
  - TF-IDF + XGBoost (100 trees, depth 6)
  - BERT-based model 1 (fine-tuned)
  - BERT-based model 2 (fine-tuned)

- **Voting Mechanism**: 
  - Per-sentence probability threshold: 0.70
  - Hard voting rule: requires > 3 out of 4 models to agree on "AI-generated"
  - Color-coded confidence zones: strong AI → moderate AI → uncertain → moderate human → strong human

- **Interactive Web Interface**: Streamlit application for real-time text analysis

- **Sentence-Level Detection**: Highlights individual sentences with confidence scores

## Installation

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/manojhunasimarad/ai-text-detector.git
   cd ai-text-detector
   ```

2. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the Web Application

```bash
streamlit run src/app/app.py
```

Access the application at `http://localhost:8501`

### Train Models

Navigate to `src/notebooks/` and run:
- `svm_detection.ipynb` - SVM training
- `xgboost_detection.ipynb` - XGBoost training
- `bert_finetuning.ipynb` - BERT fine-tuning

## Model Architecture

### SVM & XGBoost
- **Vectorization**: TF-IDF (max_features=5000)
- **SVM**: Linear kernel with probability calibration
- **XGBoost**: 100 estimators, max_depth=6, learning_rate=0.1

### BERT Models
- **Base**: bert-base-uncased
- **Architecture**: 12 layers, 768 hidden size
- **Task**: Sequence classification (binary)
- **Fine-tuning**: 3 epochs, batch size 8, learning rate 2e-5

## Datasets

| Dataset | Samples | Human | AI | Purpose |
|---------|---------|-------|-----|------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| dataset_2 | 20,000 | 60% | 40% | SVM training |
| dataset_3 | 20,000 | 60% | 40% | XGBoost training |
| dataset_4 | 20,000 | 60% | 40% | Auxiliary |
| dataset_5 | 20,000 | 60% | 40% | Auxiliary |
| test_dataset | 5,000 | 60% | 40% | Evaluation |

## Performance Notes

- **Reproducibility**: Models saved with scikit-learn 1.6.1; current environment uses 1.8.0 (minor metric drift possible)
- **Reported Metrics**: Refer to `docs/report/main.tex` and `docs/presentation/results_overview_presentation.tex`
- **Verification Status**: All model metadata verified via static audit; see documentation for verified vs. reported metrics

## Documentation

- **Report**: [docs/report/main.tex](https://github.com/manojhunasimarad/ai-text-detector/tree/main/docs/report/main.tex) - Comprehensive technical report
- **Presentation**: [docs/presentation/results_overview_presentation.tex](https://github.com/manojhunasimarad/ai-text-detector/tree/main/docs/presentation/results_overview_presentation.tex) - Beamer slides
- **API Guide**: See Streamlit app interface

## Key Findings

1. Ensemble voting improves robustness over individual models
2. BERT models capture linguistic nuances not captured by TF-IDF approaches
3. Sentence-level detection provides interpretable results for end users
4. Strict voting (> 3 out of 4) reduces false positives

## Future Work

- [ ] Update BERT notebook to use local datasets (currently uses external Colab path)
- [ ] Full unified benchmark on test_dataset.csv with environment snapshot
- [ ] Model compression for deployment optimization
- [ ] Extended language support

## Requirements

See [requirements.txt](https://github.com/manojhunasimarad/ai-text-detector/blob/main/requirements.txt) for full dependency list. Key packages:
- streamlit
- transformers
- torch
- scikit-learn
- xgboost
- pandas
- nltk

## Authors

Manoj Hunasimarad

## License

Educational Project - MA726 Mini Project

## References

- BERT: Devlin et al., 2018
- XGBoost: Chen & Guestrin, 2016
- Scikit-learn & Transformers libraries documentation
