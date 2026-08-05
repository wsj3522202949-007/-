---
id: tool-05617
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 需API密钥, 英文文档, 去AI味]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/aggnim/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5617
category: 一、去 AI 味 / Humanizer 库
repo: aggnim/ai-text-detector
stars: 0
url: https://github.com/aggnim/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# aggnim/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/aggnim/ai-text-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-generated text detection using transformer models. Binary classifier distinguishing human vs ChatGPT responses with 93%+ accuracy. Compares BERT, RoBERTa, DistilBERT on HC3 dataset. Portfolio project for NLP/fraud detection applications.
- **本地描述**：AI-generated text detection using transformer models. Binary classifier distinguishing human vs ChatGPT responses with 93%+ accuracy. Compares BERT, RoBERTa, DistilBERT on HC3 dataset. Portfolio project for NLP/fraud detection applications.
- **拉取时间**：2026-07-25 18:25:21

---

# AI-Generated Text Detection: Human vs ChatGPT Q&A Classification

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Portfolio project demonstrating **binary classification** to distinguish human-written answers
from ChatGPT-generated responses in Q&A format.

---

## 🎯 Project Overview

This project implements a practical NLP system using pre-trained transformer models (BERT
RoBERTa, DistilBERT) to detect AI-generated text. It showcases:

- Systematic model comparison and evaluation
- Feature engineering with traditional ML and deep learning
- Ethical considerations in fraud detection
- Professional code structure and documentation

**Key Focus**: Leveraging existing models without fine-tuning to demonstrate rapid prototyping skills.

---

## 📊 Dataset

**Source**: [HC3 (Human-ChatGPT Comparison Corpus)](https://huggingface.co/datasets/Hello-SimpleAI/HC3)

- **Language**: English
- **Format**: Question-Answer pairs
- **Sample Size**: 2,000-5,000 examples (subset for efficiency)
- **Balance**: 50% human / 50% ChatGPT responses
- **Domains**: Open Q&A, Finance, Medicine, Wiki

**Why HC3?**
- Professionally curated, saves data collection time
- Real-world Q&A format
- Multiple domains test generalization
- Well-documented and actively maintained

---

## 🔬 Methodology

### Phase 1: Baseline Model (Traditional ML)

**Features**:
- TF-IDF vectorization
- Text statistics (length, vocabulary richness, punctuation)
- N-gram patterns

**Classifiers**:
- Logistic Regression (interpretable baseline)
- Random Forest (capture non-linear patterns)

**Expected Performance**: 70-80% accuracy

---

### Phase 2: Transformer Models

**Approach**: Extract embeddings from frozen pre-trained models + simple classification head

**Models Compared**:

| Model | Parameters | Speed | Use Case |
|-------|------------|-------|----------|
| **BERT-base** | 110M | Moderate | General baseline |
| **RoBERTa-base** | 125M | Moderate | Optimized variant |
| **DistilBERT** | 66M | Fast | Efficient deployment |

**Why No Fine-tuning?**
- Time constraint (5-day project)
- Focus on embedding quality understanding
- Lower computational requirements
- Demonstrates feature extraction skills

---

### Phase 3: Evaluation & Analysis

**Metrics**:
- Accuracy, Precision, Recall, F1-Score
- Confusion matrices
- Inference speed (tokens/second)
- Model size comparison

**Analysis**:
- Error analysis on misclassified examples
- Embedding visualizations (t-SNE/PCA)
- Performance vs efficiency trade-offs

---

## 🛠️ Technical Stack

```
Python 3.10+
├── PyTorch 2.0+               # deep learning framework
├── Transformers (HuggingFace) # pre-trained models
├── scikit-learn               # traditional ML & metrics
├── pandas/numpy               # data manipulation
├── matplotlib/seaborn         # visualization
└── datasets (HuggingFace)     # dataset loading
```

---

## 📁 Project Structure

```
ai-text-detector/
├── notebooks/
│   ├── 01_data_exploration.ipynb    # EDA & dataset analysis
│   ├── 02_baseline_model.ipynb      # traditional ML approach
│   └── 03_transformer_models.ipynb  # BERT/RoBERTa/DistilBERT/Analysis
├── data/
│   ├── train.csv                    # 1,897 samples (72.2%)
│   ├── val.csv                      # 335 samples (12.8%)
│   └── test.csv                     # 394 samples (15.0%)
├── results/
│   ├── complete_model_comparison.csv
│   ├── feature_importance.csv
│   ├── baseline_results.json
│   ├── complete_results.json
│   ├── data_exploration_stats.json
│   └── *.png                        # all visualizations
├── REPORT.md                        # detailed technical analysis
├── requirements.txt
├── .gitignore
└── README.md
```
*Note: The `src/` directory was not implemented to prioritize rapid prototyping in notebooks.
For production deployment, code refactoring into modular utilities would be recommended.*

---

## 🚀 Installation & Usage

### Setup

```bash
# clone repository (or download ZIP)
git clone https://github.com/aggnim/ai-text-detector.git
cd ai-text-detector

# install dependencies
pip install -r requirements.txt
```

**Note on Virtual Environments**: While virtual environments (`venv`) are best practice for production projects, this prototype was developed without one due to local environment constraints. For quick experimentation, direct installation works fine if you're comfortable managing your Python packages globally.

### Running the Notebooks

```bash
# launch Jupyter in the project directory
jupyter notebook

# navigate to notebooks/ and open:
# 01_data_exploration.ipynb → start here
# 02_baseline_model.ipynb
# 03_transformer_models.ipynb
```

**First-time setup**: The first time you run the notebooks, they will automatically download:
- HC3 dataset from HuggingFace (~50MB)
- Pre-trained model weights (BERT, RoBERTa, DistilBERT, ~500MB each)

This may take 5-10 minutes depending on your internet connection.

---

## 📈 Expected Results

| Model | Accuracy | F1-Score | Type |
|-------|:--------:|:--------:|:----:|
| Logistic Regression (TF-IDF) | ~75% | ~74% | Statistical |
| Random Forest | ~78% | ~77% | Statistical |
| RoBERTa-base | ~87-92% | ~88% | Transformer |
| DistilBERT | ~83-88% | ~84% | Transformer |
| BERT-base | ~85-90% | ~86% | Transformer |


*Estimates based on similar text classification tasks.*

## 📈 Actual Results

| Model | Accuracy | F1-Score | ROC-AUC | Key Characteristics |
|-------|:--------:|:--------:|:-------:|---------------------|
| Length-Only Baseline | 84.3% | 84.7% | 84.3% | Single feature (word_count > 55) |
| Logistic Regression (TF-IDF) | 82.7% | 82.4% | 88.3% | 519 features (stats + TF-IDF) |
| Random Forest | 91.9% | 91.9% | 96.6% | Best traditional ML approach |
| RoBERTa-base | 93.7% | 93.7% | 98.5% | Optimized pre-training |
| DistilBERT | 92.1% | 92.0% | 97.7% | Fastest inference (66M params) |
| **BERT-base** | **93.9%** | **94.0%** | **98.7%** | **Best overall performance** |

---

## ⚠️ Limitations & Trade-offs

### Known Limitations

1. **Training Data Bias**: Models trained on ChatGPT 3.5 may not generalize to GPT-4,
    Claude, or other models
2. **Domain Specificity**: Performance may degrade on specialized domains (legal,
    technical writing)
3. **Language Limitation**: English-only; multilingual detection requires different
    models
4. **Adversarial Robustness**: Not tested against paraphrasing or prompt engineering
    attacks
5. **Temporal Drift**: AI writing styles evolve; periodic retraining needed

### Design Trade-offs

| Choice | Benefit | Cost |
|--------|---------|------|
| Pre-trained models (no fine-tuning) | Fast development, lower compute | ~5-10% accuracy vs fine-tuned |
| Subset sampling (2k-5k examples) | Quick experimentation | May miss rare patterns |
| English-only focus | Better model availability | Not multilingual |
| Simple classification head | Easier debugging, faster inference | Less model capacity |

---

## 🔒 Ethical Considerations

### Responsible Use

**✅ Intended Applications**:
- Content moderation systems (with human review)
- Academic integrity tools (as supportive evidence, not proof)
- Research on AI text characteristics

**❌ Misuse Risks**:
- Automatic rejection without human verification
- Discriminating against non-native speakers
- Privacy violations (analyzing private communications)

### False Positive Risks

- **Human text flagged as AI**: Risk to reputation
- **Mitigation**: Always implement human-in-the-loop review
- **Transparency**: Communicate model limitations to users

### Bias Awareness

Training data reflects specific demographics and domains. Model may perform worse on:
- Non-native English speakers
- Technical/specialized writing
- Informal/creative writing styles

### Recommendations

1. Use as **decision support**, not automated judgment
2. Provide **explainability** (highlight suspicious patterns)
3. Allow **appeals process** for flagged content
4. Regular **auditing** for bias and drift
5. Clear **documentation** of capabilities and limits

---

## 📝 Results & Analysis

### Model Comparison

| Model | Test Accuracy | Test F1-Score | Test ROC-AUC | Type | Key Characteristics |
|-------|:-------------:|:-------------:|:------------:|------|---------------------|
| **Length-Only Baseline** | **84.3%** | **84.7%** | **84.3%** | Statistical | Single feature (word_count > 55) |
| Logistic Regression | 82.7% | 82.4% | 88.3% | Statistical | 519 features (stats + TF-IDF) |
| Random Forest | 91.9% | 91.9% | 96.6% | Statistical | Best traditional ML approach |
| DistilBERT | 92.1% | 92.0% | 97.7% | Transformer | Fastest inference (66M params) |
| RoBERTa | 93.7% | 93.7% | 98.5% | Transformer | Optimized pre-training |
| **BERT** | **93.9%** | **94.0%** | **98.7%** | **Transformer** | **Best overall performance** |

!`[Transformer Confusion Matrices](results/transformer_confusion_matrices.png)`

### Key Findings

1. **Length is a surprisingly powerful discriminator**: A simple 55-word threshold
    achieves 84.3% accuracy
2. **Transformers provide incremental gains**: +2% improvement over Random Forest,
    capturing semantic patterns beyond surface statistics
3. **All three transformer models perform similarly**: 92-94% accuracy range, suggesting
    robust semantic embeddings
4. **Trade-off exists**: Random Forest offers 92% accuracy with faster inference and lower
    computational requirements

**Top Discriminative Features** (from Random Forest):
- `word_count` (14.5% importance) - ChatGPT responses average 121 words vs 47 for humans
- TF-IDF vocabulary patterns (cumulative ~40%) - Distinctive word choices and n-grams
- `lexical_diversity` (5.7%) - AI text shows more varied vocabulary
- `sentence_count` (12.8%) - ChatGPT writes longer, more structured sentences

See `REPORT.md` for detailed analysis and error breakdowns.

---

## 🔮 Future Improvements

### Short-term (if time permits)

- ⬜ Add ensemble voting classifier
- ⬜ Implement explainability (LIME/SHAP)
- ⬜ Test on domain-specific subsets

### Long-term Extensions

- ⬜ Fine-tune models on HC3 dataset
- ⬜ Multi-class classification (GPT-3.5 vs GPT-4 vs Claude)
- ⬜ Multilingual support (mBERT, XLM-RoBERTa)
- ⬜ Real-time API deployment (FastAPI)
- ⬜ Adversarial robustness testing
- ⬜ Synthetic data augmentation

---

## 📚 References

### Dataset

- **HC3 Paper**: Guo et al. (2023) - "How Close is ChatGPT to Human Experts? Comparison Corpus
     Evaluation, and Detection" ([arXiv:2301.07597](https://arxiv.org/abs/2301.07597))
- **HuggingFace Dataset**: [Hello-SimpleAI/HC3](https://huggingface.co/datasets/Hello-SimpleAI/HC3)

### Models

- **BERT**: Devlin et al. (2018) - [arXiv:1810.04805](https://arxiv.org/abs/1810.04805)
- **RoBERTa**: Liu et al. (2019) - [arXiv:1907.11692](https://arxiv.org/abs/1907.11692)
- **DistilBERT**: Sanh et al. (2019) - [arXiv:1910.01108](https://arxiv.org/abs/1910.01108)

### Related Work

- "Detecting ChatGPT: A Survey of the State of Detecting AI-Generated Text" - [arXiv:2309.07689](https://arxiv.org/abs/2309.07689)
- OpenAI's AI Text Classifier (2023) - [Blog Post](https://openai.com/blog/new-ai-classifier-for-indicating-ai-written-text)

---

## 👤 About This Project

**Context**: Portfolio project for AI engineering internship application

**Timeline**: 5-day rapid prototype (October 2025)

**Learning Objectives**:
- Practical NLP pipeline development
- Transformer model usage (HuggingFace ecosystem)
- Scientific methodology (hypothesis → experimentation → analysis)
- Ethical awareness in AI deployment
- Engineering trade-offs (speed vs accuracy, simplicity vs performance)

**Author**: Aggnia Marina  
**Contact**: aggnia.m@outlook.com  
**LinkedIn**: https://www.linkedin.com/in/aggnim  
**Date**: October 2025

---

## 📄 License

MIT License

---

## 🙏 Acknowledgments

- **Anthropic** for Claude AI assistance in project design
- **HuggingFace** for datasets and model hosting infrastructure
- **Hello-SimpleAI** for creating and maintaining the HC3 dataset
- **Probayes** for internship opportunity inspiration

---

## 📞 Contact & Feedback

Questions, suggestions, or collaboration opportunities? Feel free to:

- Open an issue on GitHub
- Connect on LinkedIn: [Aggnia Marina](https://www.linkedin.com/in/aggnim)
- Email: aggnia.m@outlook.com

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

*This project demonstrates practical AI engineering skills while maintaining ethical awareness of
fraud detection implications. It prioritizes working prototypes over perfectionism, reflecting real-world development constraints.*

**⭐ If you find this project useful, please consider starring the repository!**
