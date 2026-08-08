---
id: tool-05106
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/shashankpandey04/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5106
category: 一、去 AI 味 / Humanizer 库
repo: shashankpandey04/ai-text-detector
stars: 0
url: https://github.com/shashankpandey04/ai-text-detector
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
content_hash: 6e090c51e75fd70d
  - methods/改稿润色指令库.md
---

# shashankpandey04/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/shashankpandey04/ai-text-detector
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：nlp, python
- **GitHub 描述**：An advanced Natural Language Processing (NLP) model designed to distinguish between AI-generated and human-written text using machine learning techniques.
- **本地描述**：An advanced Natural Language Processing (NLP) model designed to distinguish between AI-generated and human-written text using machine learning techniques.
- **拉取时间**：2026-07-25 18:06:21

---

# 🤖 AI Text Detector

An advanced Natural Language Processing (NLP) model designed to distinguish between AI-generated and human-written text using machine learning techniques.

## 🌟 Features

### 🧠 **Core NLP Capabilities**
- **TF-IDF Vectorization**: Converts text into numerical features using Term Frequency-Inverse Document Frequency
- **SGD Classification**: Uses Stochastic Gradient Descent with logistic loss for binary classification
- **Incremental Learning**: Supports continuous model improvement with new training data
- **Confidence Scoring**: Provides probability scores for both AI and Human predictions

### 🖥️ **Multiple Interfaces**
1. **Command Line Training** (`main.py`) - Interactive model training
2. **Command Line Detection** (`detect.py`) - Terminal-based text analysis
3. **Web Interface** (`web.py`) - Modern browser-based UI with 2025 design aesthetics

### 🎨 **Modern Web UI Features**
- **Glassmorphism Design** - Frosted glass effects with backdrop blur
- **Floating Animations** - Dynamic particle background
- **3D Hover Effects** - Interactive perspective transforms
- **Responsive Layout** - Optimized for all screen sizes
- **Real-time Analysis** - Instant predictions with loading animations

## 📋 Requirements

```
pandas
scikit-learn
joblib
flask
```

## 🚀 Quick Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train Your Model
```bash
python main.py
```
- Enter text samples when prompted
- Type `exit` to stop training
- Model automatically saves as `ai_detector.joblib`

### 3. Test the Model

**Command Line Interface:**
```bash
python detect.py
```

**Web Interface:**
```bash
python web.py
```
Then open `http://127.0.0.1` in your browser

## 📁 Project Structure

```
Application AI/
├── main.py              # Model training interface
├── detect.py            # CLI detection tool
├── web.py              # Flask web server
├── templates/
│   └── index.html      # Modern web interface
├── requirements.txt    # Python dependencies
├── training_data.csv   # Training dataset (auto-generated)
├── ai_detector.joblib  # Trained model (auto-generated)
└── README.md          # This file
```

## 🔧 Usage Guide

### Training the Model (`main.py`)

1. **Start Training Session**
   ```bash
   python main.py
   ```

2. **Add Training Data**
   - Enter text samples (AI-generated or human-written)
   - Currently hardcoded to label as human text (`is_ai = 0`)
   - Change `is_ai = 1` in code for AI-generated samples

3. **Model Requirements**
   - Need both AI and human samples to train
   - Minimum 5 samples recommended for evaluation metrics
   - Model saves automatically after each addition

### Detection Methods

#### CLI Detection (`detect.py`)
```bash
python detect.py
# Enter text when prompted
# Get instant predictions with confidence scores
```

**Output Format:**
```
Prediction: Human
Confidence Score: Human: 0.8762, AI: 0.1238
```

#### Web Interface (`web.py`)
```bash
python web.py
# Open browser to http://127.0.0.1
# Paste text and click "Analyze Text"
```

**Features:**
- Interactive text input with syntax highlighting
- Real-time prediction results
- Animated confidence score display
- Mobile-responsive design

## 📊 Technical Details

### Machine Learning Pipeline
1. **Text Preprocessing**: TF-IDF vectorization with English stop words removal
2. **Feature Extraction**: Converts text to numerical feature vectors
3. **Classification**: SGD classifier with logistic loss function
4. **Model Persistence**: Joblib serialization for model saving/loading

### Model Architecture
- **Vectorizer**: TfidfVectorizer (stop_words='english')
- **Classifier**: SGDClassifier (loss="log_loss", max_iter=1000)
- **Pipeline**: Scikit-learn Pipeline for streamlined processing
- **Evaluation**: Classification report with precision, recall, F1-score

### Data Format
- **Training Data**: CSV format with 'text' and 'is_ai' columns
- **Labels**: Binary classification (0=Human, 1=AI)
- **Storage**: Automatic CSV persistence for incremental learning

## 🎯 Model Performance

### Training Stages
1. **Initial Stage** (< 5 samples): Trains on all available data
2. **Evaluation Stage** (≥ 5 samples): 80/20 train-test split with metrics
3. **Class Validation**: Ensures both AI and human samples are present

### Output Metrics
- **Precision**: Accuracy of positive predictions
- **Recall**: Completeness of positive predictions  
- **F1-Score**: Harmonic mean of precision and recall
- **Support**: Number of samples per class

## 🛠️ Customization

### Training Configuration
- Modify `is_ai` value in `main.py` to change label assignment
- Adjust `test_size` in train-test split for different evaluation ratios
- Change `max_iter` in SGDClassifier for convergence tuning

### Web Interface Customization
- Edit `templates/index.html` for UI modifications
- Modify CSS variables in `:root` for color scheme changes
- Adjust animation parameters for different visual effects

### Model Parameters
- **TF-IDF Settings**: Modify n-gram range, min/max document frequency
- **SGD Parameters**: Tune learning rate, regularization, loss function
- **Pipeline Steps**: Add additional preprocessing or feature engineering

## 🚦 Troubleshooting

### Common Issues

**Model Not Found Error**
```
❌ Error: Model file 'ai_detector.joblib' not found.
```
**Solution**: Run `python main.py` first to train and save a model

**Single Class Error**
```
⚠️ Only 1 class found. Need both AI-generated and human-written text
```
**Solution**: Add samples from both classes by changing `is_ai` value

**Port Already in Use**
```
Address already in use
```
**Solution**: Change port in `web.py` or kill existing process

### Performance Tips
- **Minimum Data**: Use at least 20-50 samples per class for reliable results
- **Text Length**: Longer texts (100+ words) generally produce better predictions
- **Diverse Samples**: Include various writing styles and topics
- **Regular Retraining**: Update model with new data periodically

## 📈 Future Enhancements

### Planned Features
- **Batch Processing**: Analyze multiple texts simultaneously
- **Export Functionality**: Save results to CSV/JSON formats  
- **Advanced Metrics**: ROC curves, confusion matrices
- **Model Comparison**: A/B testing between different algorithms
- **API Integration**: RESTful API for external applications

### Model Improvements
- **Deep Learning**: Integration with transformer models (BERT, GPT)
- **Ensemble Methods**: Combine multiple classifiers
- **Feature Engineering**: Advanced NLP features (sentiment, readability)
- **Cross-Validation**: More robust model evaluation

## 📝 License

This project is open-source and available for educational and research purposes.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this AI text detection system.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**Built with ❤️ using Python, Scikit-learn, and Flask**
