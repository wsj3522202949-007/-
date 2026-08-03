---
id: tool-05249
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Based_Phishing_Email_Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/koushikos/ai-based_phishing_email_detector
created: 2026-07-18
updated: 2026-07-18
no: 5249
category: 一、去 AI 味 / Humanizer 库
repo: koushikos/AI-Based_Phishing_Email_Detector
stars: 1
url: https://github.com/koushikos/ai-based_phishing_email_detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# koushikos/AI-Based_Phishing_Email_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/koushikos/ai-based_phishing_email_detector
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A beginner-friendly Python project that uses Machine Learning to classify email text as either **Phishing** or **Legitimate**. This project demonstrates the use of Natural Language Processing (NLP) and classification algorithms for cybersecurity applications.
- **本地描述**：A beginner-friendly Python project that uses Machine Learning to classify email text as either **Phishing** or **Legitimate**. This project demonstrates the use of Natural Language Processing (NLP) and classification algorithms for cybersecurity applications.
- **拉取时间**：2026-07-25 18:11:35

---

# AI-Based Phishing Email Language Detector

A beginner-friendly Python project that uses Machine Learning to classify email text as either **Phishing** or **Legitimate**. This project demonstrates the use of Natural Language Processing (NLP) and classification algorithms for cybersecurity applications.

## Project Structure

```
AI-Based Phishing Email Language Detector/
├── phishing_detector.py      # Main Python script with CLI interface
├── streamlit_app.py          # Web interface using Streamlit
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Features

- **Machine Learning Classification**: Uses TF-IDF vectorization and Logistic Regression
- **Text Preprocessing**: Includes tokenization, stopword removal, and lemmatization
- **Sample Dataset**: Built-in demo dataset with 10 phishing and 10 legitimate emails
- **Command Line Interface**: Interactive terminal-based prediction
- **Web Interface**: Optional Streamlit web app for user-friendly interaction
- **Clear Results**: Displays prediction with confidence levels

## How It Works

### Model Working Principle (Simple Explanation)

1. **Text Preprocessing**:
   - Convert email text to lowercase
   - Remove special characters and numbers
   - Split text into words (tokenization)
   - Remove common words like "the", "a", "is" (stopwords)
   - Convert words to their base form (lemmatization)

2. **Feature Extraction (TF-IDF)**:
   - TF-IDF (Term Frequency-Inverse Document Frequency) converts text into numbers
   - It gives higher weight to words that are important but not too common
   - Creates a numerical representation of each email

3. **Machine Learning Classification**:
   - Logistic Regression learns patterns from the training data
   - It finds the relationship between word patterns and email types
   - For new emails, it calculates probabilities and makes predictions

4. **Prediction**:
   - Input email is preprocessed and converted to TF-IDF features
   - Model calculates the probability of being phishing vs legitimate
   - Returns the most likely classification

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Command Line Version
```bash
python phishing_detector.py
```

### Step 3: (Optional) Run the Web Interface
```bash
streamlit run streamlit_app.py
```

## Usage

### Command Line Interface
1. Run the script
2. The model will train automatically on the sample dataset
3. Enter email text when prompted
4. Type 'quit' to exit
5. Get instant predictions with warnings

### Web Interface
1. Run the Streamlit app
2. Paste email text in the input box
3. Click "Check Email" to get results
4. View prediction and confidence levels

## Sample Input Examples

### Phishing Email Example:
```
Urgent: Your account has been compromised. Click here to reset your password immediately!
```

### Legitimate Email Example:
```
Meeting reminder: Team standup at 10 AM tomorrow in conference room A.
```

## Technical Details

- **Algorithm**: Logistic Regression (can be easily changed to Naive Bayes)
- **Vectorization**: TF-IDF with max 1000 features and n-grams (1,2)
- **Preprocessing**: NLTK for stopwords and WordNet lemmatizer
- **Accuracy**: Typically 80-90% on the demo dataset (varies with data)

## Customization

### Adding Your Own Dataset
Replace the `create_sample_dataset()` function with your own CSV loading:

```python
def load_custom_dataset():
    df = pd.read_csv('your_dataset.csv')
    return df
```

### Changing the Algorithm
Replace LogisticRegression with other classifiers:

```python
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
```

## Educational Value

This project is perfect for:
- Learning Machine Learning basics
- Understanding NLP preprocessing
- Exploring cybersecurity applications
- College AI/ML mini-projects
- Portfolio demonstrations

## Future Enhancements

- Add more sophisticated features (email headers, sender analysis)
- Implement real-time email scanning
- Add support for multiple languages
- Integrate with email clients
- Add model persistence (save/load trained models)

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project!

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**Note**: This is a demonstration project using a small sample dataset. For production use, train on larger, real-world datasets and combine with other security measures.
