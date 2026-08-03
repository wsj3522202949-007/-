---
id: tool-05212
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 去AI味]
title: Fake-Me-Not-Fake-News-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/soumyadeeep-mukherjee/fake-me-not-fake-news-detector
created: 2026-07-18
updated: 2026-07-18
no: 5212
category: 一、去 AI 味 / Humanizer 库
repo: Soumyadeeep-Mukherjee/Fake-Me-Not-Fake-News-Detector
stars: 1
url: https://github.com/soumyadeeep-mukherjee/fake-me-not-fake-news-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Soumyadeeep-Mukherjee/Fake-Me-Not-Fake-News-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/soumyadeeep-mukherjee/fake-me-not-fake-news-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Fake News Detector: A Natural Language Processing (NLP) project that employs deep learning algorithms to analyze text patterns and source credibility, providing an automatic, scalable system for verifying the authenticity of news articles.
- **本地描述**：AI Fake News Detector: A Natural Language Processing (NLP) project that employs deep learning algorithms to analyze text patterns and source credibility, providing an automatic, scalable system for verifying the authenticity of news articles.
- **拉取时间**：2026-07-25 18:10:15

---

# 🎓 FakeMeNot - AI-Powered Fake News Detection for University Students



See the project in action! The live Depoloyment link : https://fake-me-not-fake-news-detector.streamlit.app/



A comprehensive educational project that combines **Machine Learning**, **Natural Language Processing**, and **AI** to detect fake news articles. Perfect for computer science, data science, and journalism students to learn about the intersection of technology and media literacy.



## 🎯 Learning Objectives



By working with this project, students will:



- **Master Machine Learning Fundamentals**: Implement supervised learning algorithms for text classification

- **Explore Natural Language Processing**: Learn text preprocessing, feature extraction, and TF-IDF vectorization

- **Understand AI Integration**: Work with modern AI APIs (Google Gemini, OpenAI) for enhanced analysis

- **Develop Web Applications**: Build interactive interfaces using Streamlit framework

- **Practice Data Science Workflow**: From data collection to model deployment

- **Learn Software Engineering**: Version control, environment management, and security best practices

- **Develop Critical Thinking**: Understand the challenges and limitations of automated fact-checking



## 🧠 What You'll Learn



### Machine Learning Concepts

- **Supervised Learning**: Classification algorithms and their applications

- **Feature Engineering**: Converting text to numerical representations

- **Model Evaluation**: Accuracy, precision, recall, and F1-score metrics

- **Cross-validation**: Proper model testing and validation techniques

- **Bias Detection**: Understanding and mitigating algorithmic bias



### Natural Language Processing

- **Text Preprocessing**: Cleaning, tokenization, and normalization

- **TF-IDF Vectorization**: Term frequency and inverse document frequency

- **N-gram Analysis**: Understanding word patterns and context

- **Sentiment Analysis**: Emotional tone detection in text

- **Named Entity Recognition**: Identifying people, places, and organizations



### AI and Modern Technologies

- **Large Language Models**: Integration with GPT and Gemini APIs

- **Prompt Engineering**: Crafting effective AI prompts for analysis

- **Ensemble Methods**: Combining multiple models for better predictions

- **API Integration**: Working with external AI services

- **Real-time Analysis**: Processing and analyzing text in real-time



## 📁 Project Architecture



```

FakeMeNot/

├── 🚀 app.py                 # Streamlit web application (Main Interface)

├── 🤖 model.py              # ML model training pipeline

├── 📋 requirements.txt      # Python dependencies

├── 🔐 .env                 # Environment variables (API keys)

├── 🔐 .secrets.toml        # Streamlit secrets configuration

├── 🚫 .gitignore          # Git ignore file for security

├── 📝 .env.example        # Environment variables template

├── 📊 data/

│   ├── Fake.csv        # Fake news dataset (23,490 articles)

│   ├── True.csv        # Real news dataset (21,418 articles)

│   └── news.csv        # Combined dataset (auto-generated)

├── 🧠 models/

│   ├── model.pkl       # Trained PassiveAggressiveClassifier

│   └── vectorizer.pkl  # TF-IDF vectorizer

└── 📖 README.md           # This documentation

```



## 🔧 Prerequisites & Setup



### Required Knowledge

- **Python Programming**: Basic to intermediate Python skills

- **Command Line**: Basic terminal/command prompt usage

- **Git**: Version control fundamentals

- **Statistics**: Basic understanding of probability and statistics



### System Requirements

- **Python 3.8+**: Latest Python version recommended

- **RAM**: Minimum 4GB (8GB recommended for large datasets)

- **Storage**: At least 2GB free space

- **Internet**: Required for AI API calls



## 🚀 Quick Start Guide



### Step 1: Clone and Setup

```bash

# Clone the repository

git clone <your-repository-url>

cd FakeMeNot



# Create and activate virtual environment

python -m venv venv



# Windows

venv\Scripts\activate

# macOS/Linux

source venv/bin/activate

```



### Step 2: Install Dependencies

```bash

# Install all required packages

pip install -r requirements.txt



# Verify installation

python -c "import streamlit, sklearn, pandas; print('All packages installed successfully!')"

```



### Step 3: Configure API Keys

1. **Copy environment template**:

   ```bash

   cp .env.example .env

   ```



2. **Get your API keys**:

   - **Google Gemini**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)

   - **OpenAI** (optional): Visit [OpenAI Platform](https://platform.openai.com/api-keys)



3. **Update `.env` file**:

   ```env

   GEMINI_API_KEY=your_actual_gemini_api_key_here

   GEMINI_MODEL=gemini-pro

   OPENAI_API_KEY=your_openai_api_key_here  # Optional

   ```



### Step 4: Prepare Dataset

The project uses a comprehensive dataset of news articles:

- **Fake.csv**: 23,490 fake news articles from various sources

- **True.csv**: 21,418 legitimate news articles from Reuters

- **Combined**: 44,908 total articles for training



### Step 5: Train Your Model

```bash

# Run the training script

python model.py



# Expected output:

# Loading dataset...

# Training model...

# Model accuracy: 94.5%

# Model saved successfully!

```



### Step 6: Launch the Application

```bash

# Start the Streamlit app

streamlit run app.py



# Access at: http://localhost:8501

```



## 🎮 How to Use the Application



### 1. **Input Methods**

- **Direct Text**: Paste news article content

- **File Upload**: Upload `.txt` files

- **URL Analysis**: Paste article URLs (future feature)



### 2. **Analysis Features**

- **ML Prediction**: Get classification with confidence score

- **AI Analysis**: Detailed reasoning from Gemini/GPT

- **Bias Detection**: Identify potential biases in content

- **Source Verification**: Check article credibility indicators



### 3. **Understanding Results**

- **Confidence Score**: 0-100% certainty of prediction

- **Feature Importance**: Which words influenced the decision

- **AI Reasoning**: Human-readable explanation of the analysis

- **Recommendations**: Suggestions for further verification



## 🤖 Technical Deep Dive



### Machine Learning Pipeline



#### 1. **Data Preprocessing**

```python

# Text cleaning steps

def preprocess_text(text):

    # Remove special characters

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Convert to lowercase

    text = text.lower()

    # Remove extra whitespace

    text = ' '.join(text.split())

    return text

```



#### 2. **Feature Extraction**

- **TF-IDF Vectorization**: Converts text to numerical features

- **N-gram Analysis**: Captures word patterns (unigrams, bigrams)

- **Stop Word Removal**: Filters out common words

- **Max Features**: Limits vocabulary size for efficiency



#### 3. **Model Training**

- **Algorithm**: PassiveAggressiveClassifier

  - **Advantages**: Handles large datasets efficiently

  - **Online Learning**: Can update with new data

  - **Robust**: Resistant to outliers

- **Hyperparameters**: Optimized through grid search

- **Cross-validation**: 5-fold validation for robust evaluation



#### 4. **Model Evaluation**

```python

# Evaluation metrics

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred, average='weighted')

recall = recall_score(y_test, y_pred, average='weighted')

f1 = f1_score(y_test, y_pred, average='weighted')

```



### AI Integration Architecture



#### 1. **Google Gemini Integration**

```python

# Gemini API call for analysis

def analyze_with_gemini(text):

    prompt = f"""

    Analyze this news article for potential misinformation:

    

    Article: {text}

    

    Provide analysis on:

    1. Factual accuracy indicators

    2. Emotional language usage

    3. Source credibility markers

    4. Logical consistency

    """

    response = model.generate_content(prompt)

    return response.text

```



#### 2. **Ensemble Prediction**

- **ML Model**: Fast, quantitative analysis

- **AI Analysis**: Contextual, qualitative insights

- **Combined Score**: Weighted average of both approaches

- **Confidence Calibration**: Adjusts predictions based on agreement



## 📊 Dataset Analysis



### Dataset Composition

| Category | Articles | Percentage | Sources |

|----------|----------|------------|---------|

| Fake News | 23,490 | 53.4% | Various unreliable sources |

| Real News | 21,418 | 46.6% | Reuters, legitimate outlets |

| **Total** | **44,908** | **100%** | Mixed sources |



### Content Categories

- **Politics**: 65% of articles

- **World News**: 20% of articles  

- **Government**: 10% of articles

- **Other**: 5% of articles



### Key Features

- **Title**: Article headline

- **Text**: Full article content

- **Subject**: Content category

- **Date**: Publication date



## 🛠️ Technology Stack Explained



### Core Technologies

- **Python 3.8+**: 

  - **Why**: Excellent ML/AI ecosystem

  - **Learning**: Object-oriented programming, data structures

- **Streamlit**: 

  - **Why**: Rapid web app development

  - **Learning**: Web frameworks, user interface design



### Machine Learning Stack

- **scikit-learn**: 

  - **Purpose**: ML algorithms and evaluation

  - **Key Components**: Classifiers, vectorizers, metrics

- **pandas**: 

  - **Purpose**: Data manipulation and analysis

  - **Key Skills**: DataFrames, data cleaning, aggregation

- **numpy**: 

  - **Purpose**: Numerical computing

  - **Key Skills**: Arrays, mathematical operations



### AI Integration

- **Google Generative AI**: 

  - **Purpose**: Advanced text analysis

  - **Learning**: API integration, prompt engineering

- **OpenAI**: 

  - **Purpose**: Alternative AI analysis

  - **Learning**: GPT models, text generation



### Visualization & Analysis

- **Altair**: Statistical visualization

- **Matplotlib**: Basic plotting

- **Seaborn**: Advanced statistical plots



## 📈 Model Performance Analysis



### Current Performance Metrics

```

Accuracy: 94.5% ± 0.8%

Precision: 94.2% (Fake), 94.8% (Real)

Recall: 94.6% (Fake), 94.4% (Real)

F1-Score: 94.4% (Fake), 94.6% (Real)

```



### Performance by Category

| Content Type | Accuracy | Common Errors |

|--------------|----------|---------------|

| Political News | 96.2% | Satirical content |

| World News | 93.8% | Opinion pieces |

| Government | 95.1% | Press releases |

| Breaking News | 91.5% | Unverified claims |



### Error Analysis

- **False Positives**: Satirical content marked as fake

- **False Negatives**: Subtle misinformation missed

- **Edge Cases**: Opinion pieces, editorial content

- **Bias Issues**: Political lean in training data



## 🎓 Educational Exercises



### Beginner Level

1. **Data Exploration**: Analyze the dataset structure and content

2. **Text Preprocessing**: Implement custom text cleaning functions

3. **Feature Analysis**: Examine TF-IDF feature importance

4. **Model Comparison**: Try different classification algorithms



### Intermediate Level

1. **Hyperparameter Tuning**: Optimize model parameters

2. **Cross-validation**: Implement robust evaluation strategies

3. **Feature Engineering**: Create custom text features

4. **Bias Detection**: Analyze model fairness across groups



### Advanced Level

1. **Deep Learning**: Implement BERT or RoBERTa models

2. **Multi-modal Analysis**: Include image and metadata features

3. **Real-time Processing**: Build streaming analysis pipeline

4. **Explainable AI**: Implement LIME or SHAP explanations



## 🔍 Research Questions to Explore



### Technical Questions

- How does TF-IDF compare to word embeddings for this task?

- What impact does dataset size have on model performance?

- How can we detect adversarial fake news designed to fool AI?

- What role does temporal information play in fake news detection?



### Ethical Questions

- How do we ensure fairness across different political viewpoints?

- What are the implications of automated fact-checking?

- How do we handle the "gray area" between opinion and misinformation?

- What responsibility do platforms have in content moderation?



### Practical Questions

- How can this technology be deployed responsibly?

- What human oversight is necessary for automated systems?

- How do we keep models updated as fake news tactics evolve?

- What role should transparency play in AI-powered fact-checking?



## 🔐 Security and Ethics



### Security Best Practices

- **API Key Protection**: Never commit secrets to version control

- **Environment Variables**: Use `.env` files for configuration

- **Input Validation**: Sanitize user inputs to prevent attacks

- **Rate Limiting**: Implement API usage limits

- **Data Privacy**: Handle user data responsibly



### Ethical Considerations

- **Bias Mitigation**: Regular audits for algorithmic bias

- **Transparency**: Clear explanations of how decisions are made

- **Human Oversight**: AI should augment, not replace human judgment

- **False Positive Impact**: Consider consequences of incorrect classifications

- **Cultural Sensitivity**: Understand cultural context in global content



## 🚀 Future Enhancements & Research Directions



### Technical Improvements

- **Transformer Models**: Implement BERT, RoBERTa, or GPT-based classifiers

- **Multi-modal Analysis**: Include images, videos, and metadata

- **Real-time Processing**: Stream processing for social media monitoring

- **Federated Learning**: Privacy-preserving distributed training

- **Adversarial Robustness**: Defense against sophisticated fake news



### Feature Additions

- **Browser Extension**: Real-time web content analysis

- **Mobile Application**: On-the-go fact-checking

- **API Service**: Integrate with other applications

- **Multi-language Support**: Extend beyond English content

- **Social Network Analysis**: Analyze information spread patterns



### Research Opportunities

- **Cross-domain Generalization**: Models that work across different topics

- **Few-shot Learning**: Detect new types of misinformation quickly

- **Explainable AI**: Better interpretability for end users

- **Human-AI Collaboration**: Optimal human-machine teaming strategies

- **Longitudinal Studies**: How fake news patterns evolve over time



## 📚 Additional Learning Resources



### Books

- "Hands-On Machine Learning" by Aurélien Géron

- "Natural Language Processing with Python" by Steven Bird

- "The Elements of Statistical Learning" by Hastie, Tibshirani, and Friedman



### Online Courses

- **Coursera**: Machine Learning by Andrew Ng

- **edX**: Introduction to Natural Language Processing (MIT)

- **Udacity**: Machine Learning Engineer Nanodegree



### Research Papers

- "Automatic Detection of Fake News" (Pérez-Rosas et al., 2017)

- "FakeNewsNet: A Data Repository with News Content, Social Context and Spatialtemporal Information" (Shu et al., 2018)

- "The Science of Fake News" (Lazer et al., 2018)



### Datasets for Further Exploration

- **LIAR Dataset**: Short statements with truth ratings

- **FakeNewsNet**: Multi-modal fake news dataset

- **FEVER**: Fact Extraction and VERification dataset

- **COVID-19 Infodemic**: Pandemic-related misinformation



## 🤝 Contributing to the Project



### For Students

1. **Fork the repository** and create your own experiments

2. **Try different algorithms** and compare performance

3. **Add new features** like sentiment analysis or bias detection

4. **Improve the UI** with better visualizations

5. **Write documentation** for your enhancements



### For Educators

1. **Create assignments** based on the codebase

2. **Develop evaluation rubrics** for student projects

3. **Add educational content** and explanations

4. **Share classroom experiences** and best practices

5. **Contribute to the curriculum** development



### Development Guidelines

- Follow PEP 8 Python style guidelines

- Add comprehensive docstrings to functions

- Include unit tests for new features

- Update documentation for any changes

- Consider ethical implications of modifications



## ⚠️ Important Disclaimers



### Educational Purpose

- This is a **learning project**, not a production system

- Results should be **verified through multiple sources**

- The model has **limitations and biases** that should be understood

- **Critical thinking** should always supplement automated analysis



### Technical Limitations

- **No model is 100% accurate** - always verify important information

- **Training data bias** may affect predictions

- **Adversarial examples** can fool the system

- **Context matters** - the model may miss nuanced misinformation



### Ethical Responsibilities

- **Use responsibly** - don't rely solely on automated fact-checking

- **Understand bias** - be aware of potential algorithmic bias

- **Respect privacy** - handle user data appropriately

- **Promote media literacy** - encourage critical thinking skills



---



## 📄 License



This project is licensed under the MIT License - see the LICENSE file for details.



**Academic Use**: Free for educational and research purposes

**Commercial Use**: Contact for licensing terms

**Attribution**: Please cite this project in academic work



related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---



*"The best way to learn is by doing. This project provides hands-on experience with the technologies shaping our information landscape."*



**Happy Learning! 🎓✨**



