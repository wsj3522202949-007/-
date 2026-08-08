---
id: tool-07630
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: gpt-detector
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/yiqingzhang/gpt-detector
created: 2026-07-18
updated: 2026-07-18
no: 7630
category: 画龙补充 / 扩容入库 — 补充源
repo: yiqingzhang/gpt-detector
stars: 0
url: https://github.com/yiqingzhang/gpt-detector
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 66a07ed329421e4f
  - methods/QUICK_START.md
---

# yiqingzhang/gpt-detector

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/yiqingzhang/gpt-detector
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：gpt-detector
- **拉取时间**：2026-07-25 19:28:15

---

# GPT Detector 🤖

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A robust AI-generated text detection system powered by fine-tuned RoBERTa transformers. This tool helps distinguish between human-written and machine-generated content with high accuracy.

## 🌟 Features

- **High Accuracy Detection**: Fine-tuned RoBERTa model for reliable AI text detection
- **Easy-to-Use API**: Simple Flask-based REST API for integration
- **Multiple Deployment Options**: 
  - Local inference
  - Flask web application
  - AWS SageMaker deployment
  - AWS Lambda serverless deployment
- **Comprehensive Training Pipeline**: Full training infrastructure with AWS SageMaker support
- **Production Ready**: Includes Docker configurations and Terraform IaC for cloud deployment

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Local Inference](#local-inference)
  - [Web Application](#web-application)
  - [API Usage](#api-usage)
- [Training](#training)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) CUDA-compatible GPU for faster inference

### Basic Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/gpt-detector.git
cd gpt-detector

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

### Docker Installation

```bash
# Build the inference container
cd deployment/docker
docker build -f Dockerfile.inference -t gpt-detector:latest .

# Run the container
docker run -p 5000:5000 gpt-detector:latest
```

## 🎯 Quick Start

### Using the Python API

```python
from gpt_detector.model import ROBERTAClassifier
from gpt_detector.utils import load_checkpoint, parse_arge
from transformers import RobertaTokenizer
import torch

# Load the model
args = parse_arge()
model = ROBERTAClassifier(n_classes=2, dropout_rate=0.3)
model = load_checkpoint("path/to/model.pkl", model)

# Tokenize input
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
text = "Your text to analyze here"
encoded = tokenizer(text, padding="max_length", truncation=True, return_tensors="pt")

# Make prediction
model.eval()
with torch.no_grad():
    output = model(input_ids=encoded['input_ids'], attention_mask=encoded['attention_mask'])
    prediction = torch.argmax(output, dim=-1).item()

print("Machine generated" if prediction == 0 else "Human generated")
```

### Using the Web Interface

```bash
# Start the Flask application
python src/gpt_detector/app.py

# Open your browser and navigate to
# http://localhost:5000
```

### Using the REST API

```bash
# Start the server
python src/gpt_detector/app.py

# Make a prediction request
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text to analyze here"}'
```

## 📖 Usage

### Local Inference

Run inference on a single text sample:

```bash
python examples/evaluation.py --config src/gpt_detector/config/hyperparameters.json
```

### Web Application

The web application provides a user-friendly interface for text analysis:

1. Start the Flask server:
```bash
python src/gpt_detector/app.py
```

2. Open your browser to `http://localhost:5000`
3. Enter your text in the input box
4. Click "Analyze" to get the prediction

### API Usage

#### Health Check

```bash
curl http://localhost:5000/health
```

#### Predict (Form Data)

```bash
curl -X POST http://localhost:5000/ \
  -F "text=Your text to analyze here"
```

#### Predict (JSON)

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text to analyze here"}'
```

Response:
```json
{
  "message": "Success",
  "input_data": "human generated"
}
```

## 🏋️ Training

### Local Training

1. Prepare your dataset:
```bash
python src/gpt_detector/data_process.py --config src/gpt_detector/config/hyperparameters.json
```

2. Train the model:
```bash
python src/gpt_detector/training/train.py --config src/gpt_detector/config/hyperparameters.json
```

### AWS SageMaker Training

1. Build and push the training Docker image:
```bash
./scripts/build_and_push_train.sh
```

2. Launch the training pipeline:
```bash
python src/gpt_detector/training/pipeline_train.py
```

3. Monitor training progress in the AWS SageMaker Console

### Training Configuration

Edit `src/gpt_detector/config/hyperparameters.json` to customize training:

```json
{
    "saved_model_dir": "/opt/ml/model",
    "datafolder": "data",
    "output_path": "/opt/ml/model",
    "epochs": 10,
    "train_batch_size": 16,
    "test_batch_size": 16,
    "lr": 5e-5,
    "seed": 42,
    "dropout_rate": 0.3
}
```

## 🚢 Deployment

### AWS SageMaker Deployment

```bash
# Build and push inference image
./scripts/build_and_push_inference.sh

# Deploy the model
python src/gpt_detector/training/step_deploy.py
```

### AWS Lambda Deployment

```bash
# Build and push Lambda image
./scripts/build_and_push_lambda.sh

# Deploy using Terraform
cd deployment/terraform
terraform init
terraform plan
terraform apply
```

### Docker Deployment

```bash
# Build the image
docker build -f deployment/docker/Dockerfile.inference -t gpt-detector:latest .

# Run the container
docker run -d -p 5000:5000 --name gpt-detector gpt-detector:latest
```

## 📁 Project Structure

```
gpt-detector/
├── src/
│   └── gpt_detector/
│       ├── __init__.py
│       ├── model.py              # RoBERTa classifier model
│       ├── utils.py              # Utility functions
│       ├── data_process.py       # Data preprocessing
│       ├── app.py                # Flask web application
│       ├── config/
│       │   └── hyperparameters.json
│       └── training/
│           ├── __init__.py
│           ├── train.py          # Training script
│           ├── inference.py      # SageMaker inference
│           ├── pipeline_train.py # SageMaker pipeline
│           └── step_deploy.py    # Deployment script
├── examples/
│   └── evaluation.py             # Example inference script
├── tests/
│   ├── conftest.py
│   ├── test_dataprocess.py
│   ├── test_model.py
│   ├── test_train_roberta.py
│   └── test_utils.py
├── deployment/
│   ├── docker/
│   │   ├── Dockerfile.inference
│   │   ├── Dockerfile.train
│   │   └── Dockerfile.lambda
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── ...
│   ├── handler.py                # Lambda handler
│   └── lambda-sagemaker-api.py   # Lambda SageMaker API
├── scripts/
│   ├── build_and_push_train.sh
│   ├── build_and_push_inference.sh
│   ├── build_and_push_lambda.sh
│   └── build_model.sh
├── docs/
│   └── postman/                  # API documentation
├── data/                         # Training data
├── saved_models/                 # Model checkpoints
├── templates/                    # HTML templates
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

## 🧪 Testing

Run the test suite:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src/gpt_detector --cov-report=html
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](https://github.com/yiqingzhang/gpt-detector/blob/main/CONTRIBUTING.md) for details on how to:

- Report bugs
- Suggest enhancements
- Submit pull requests
- Follow our code style

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/yiqingzhang/gpt-detector/blob/main/LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Hugging Face Transformers](https://huggingface.co/transformers/)
- Uses the [RoBERTa](https://arxiv.org/abs/1907.11692) model architecture
- Training data from [Yelp Review Full dataset](https://huggingface.co/datasets/yelp_review_full) (modified for binary classification)

## 📊 Model Performance

The model achieves strong performance on distinguishing between human-written and AI-generated text:

- **Accuracy**: ~XX% (update with your metrics)
- **Precision**: ~XX%
- **Recall**: ~XX%
- **F1 Score**: ~XX%

## 🗺️ Roadmap

- [ ] Add support for multiple languages
- [ ] Implement model explainability features (attention visualization)
- [ ] Create a browser extension for real-time detection
- [ ] Add support for detecting specific AI models (GPT-3, GPT-4, Claude, etc.)
- [ ] Improve model performance with larger datasets
- [ ] Add batch processing capabilities
- [ ] Create a public demo website

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/gpt-detector/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/gpt-detector/discussions)

related:
  - methods/QUICK_START.md
---

Made with ❤️ by the GPT Detector team
