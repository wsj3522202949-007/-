---
id: tool-05113
type: tool
area: 库
status: active
tags: [CSS, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-CONTENT-DETECTOR
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/iviwebooi/ai-content-detector
created: 2026-07-18
updated: 2026-07-18
no: 5113
category: 一、去 AI 味 / Humanizer 库
repo: IviweBooi/AI-CONTENT-DETECTOR
stars: 2
url: https://github.com/iviwebooi/ai-content-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 105b3bc5ec61e830
  - methods/改稿润色指令库.md
---

# IviweBooi/AI-CONTENT-DETECTOR

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/iviwebooi/ai-content-detector
- **Stars**：2
- **语言**：CSS
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A full-stack web application that detects AI-generated content in academic or written submissions. Users can upload documents (.pdf, .docx, .txt) or paste text for analysis. The system uses transformer-based models from Hugging Face to return an AI-likelihood score, highlight suspicious text, and provide a detailed downloadable report.
- **本地描述**：A full-stack web application that detects AI-generated content in academic or written submissions. Users can upload documents (.pdf, .docx, .txt) or paste text for analysis. The system uses transformer-based models from Hugging Face to return an AI-likelihood score, highlight suspicious text, and provide a detailed downloadable report.
- **拉取时间**：2026-07-25 18:06:37

---

# AI Content Detector (AICD)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![React](https://img.shields.io/badge/React-19.1.1-blue.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.8.0-red.svg)](https://pytorch.org/)

**GitLab Repository:** [https://gitlab.cs.uct.ac.za/bxxivi004/AI-CONTENT-DETECT](https://gitlab.cs.uct.ac.za/bxxivi004/AI-CONTENT-DETECT)

A sophisticated full-stack web application that detects AI-generated content in academic and written submissions using advanced machine learning techniques. The system combines CNN-based neural networks with pattern detection algorithms to provide accurate AI content analysis with detailed reporting capabilities.

## 🚀 Features

### Core Detection Capabilities
- 🤖 **Advanced AI Detection**: CNN-based neural network model with 87.66% accuracy
- 📊 **Ensemble Analysis**: Combines multiple detection methods for improved reliability
- 🎯 **Confidence Scoring**: Detailed confidence metrics and likelihood classification
- 📝 **Multi-format Support**: Analyze text, PDF, DOCX, and TXT files
- 🔍 **Pattern Recognition**: Identifies AI-specific writing patterns and structures

### User Experience
- 💻 **Modern UI**: Responsive React-based interface with intuitive design
- 📈 **Interactive Visualizations**: Real-time analysis results with highlighted suspicious content
- 📄 **Comprehensive Reports**: Downloadable PDF reports with detailed analysis
- ⚡ **Real-time Processing**: Fast analysis with progress indicators
- 📱 **Mobile Responsive**: Optimized for all device sizes

### Security & Analytics
- 🔐 **Firebase Authentication**: Secure user management and session handling
- 📊 **Usage Analytics**: Track detection patterns and system performance
- 🛡️ **Privacy Protection**: Secure content processing with no data retention
- 🚦 **Rate Limiting**: Daily submission limits to prevent abuse
- 🔒 **Secure File Handling**: Safe document processing and temporary storage

### Enterprise Features
- 📈 **Analytics Dashboard**: Comprehensive usage statistics and insights
- 🎛️ **Admin Controls**: User management and system monitoring
- 📋 **Audit Trails**: Complete logging of detection activities
- 🔄 **API Integration**: RESTful API for third-party integrations

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 19.1.1 with Vite build tool
- **Routing**: React Router DOM 7.8.1
- **State Management**: React Context API
- **Authentication**: Firebase Auth 12.2.1
- **File Processing**: PDF.js, Mammoth.js for document parsing
- **Testing**: Jest with React Testing Library
- **Styling**: Modern CSS with responsive design

### Backend
- **Framework**: Flask 2.3.3 with CORS support
- **Server**: Gunicorn for production deployment
- **Authentication**: Firebase Admin SDK 6.2.0
- **Database**: Firebase Firestore for user data and analytics

### AI/ML Components
- **Deep Learning**: PyTorch 2.8.0 for CNN model inference
- **NLP**: Transformers 4.35.0, NLTK 3.8.1, spaCy 3.7.2
- **Model**: Custom CNN trained on AI/human text datasets
- **Pattern Detection**: Heuristic-based AI content analysis
- **Ensemble Methods**: Multiple detection algorithms combined

### Development & Testing
- **Testing**: Pytest for backend, Jest for frontend
- **Code Quality**: ESLint, Black, Flake8
- **Documentation**: Comprehensive API and deployment guides

## 📁 Project Structure

```
AI-CONTENT-DETECTOR/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/          # Main application pages
│   │   ├── contexts/       # React context providers
│   │   ├── services/       # API and external services
│   │   └── hooks/          # Custom React hooks
│   ├── tests/              # Frontend test suites
│   └── public/             # Static assets
├── backend/                 # Flask backend API
│   ├── routes/             # API endpoint definitions
│   ├── services/           # Business logic and external services
│   ├── utils/              # AI detection utilities
│   ├── predictor_model/    # CNN model implementation
│   ├── tests/              # Backend test suites
│   └── CNN Model Complete/ # Trained model files
├── diagrams/               # System architecture diagrams
└── docs/                   # Additional documentation
    ├── DEPLOYMENT_GUIDE.md
    ├── FIREBASE_SETUP.md
    ├── ANALYTICS_SETUP.md
    └── USER_MANUAL.md
```

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v16 or later)
- **Python** (3.8 or later)
- **npm** or **yarn**
- **Git**
- **Firebase Account** (for authentication and analytics)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/AI-CONTENT-DETECTOR.git
   cd AI-CONTENT-DETECTOR
   ```

2. **Backend Setup**:
   ```bash
   cd backend
   
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Set up environment variables
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Frontend Setup**:
   ```bash
   cd frontend
   
   # Install dependencies
   npm install
   
   # Set up environment variables
   cp .env.example .env
   # Edit .env with your Firebase configuration
   ```

4. **Firebase Configuration**:
   - Follow the [Firebase Setup Guide](https://github.com/IviweBooi/AI-CONTENT-DETECTOR/blob/main/FIREBASE_SETUP.md)
   - Configure authentication and Firestore
   - Set up security rules

### Running the Application

1. **Start the Backend Server**:
   ```bash
   cd backend
   python app.py
   ```
   Backend will run on `http://localhost:5001`

2. **Start the Frontend Development Server**:
   ```bash
   cd frontend
   npm run dev
   ```
   Frontend will run on `http://localhost:5173`

3. **Access the Application**:
   Open your browser and navigate to `http://localhost:5173`

## 📖 Usage

### Basic Analysis
1. **Sign up/Login** using the authentication system
2. **Choose Input Method**: Paste text directly or upload a document (PDF, DOCX, TXT)
3. **Submit for Analysis**: Click "Analyze" to process the content
4. **Review Results**: View AI likelihood score, confidence metrics, and highlighted suspicious content
5. **Download Report**: Generate and download detailed PDF reports

### Advanced Features
- **Batch Processing**: Analyze multiple documents
- **Custom Thresholds**: Adjust detection sensitivity
- **Historical Analysis**: View past detection results
- **Analytics Dashboard**: Monitor usage patterns and system performance

## 🧪 Testing

For a comprehensive overview of our testing strategy, see the **[Testing Plan](https://github.com/IviweBooi/AI-CONTENT-DETECTOR/blob/main/TESTING_PLAN.md)** which includes:
- Summary testing plan table with all four testing levels
- Detailed mapping of current tests to testing categories
- Test execution matrix and quality metrics
- Complete testing implementation details

### Frontend Tests
```bash
cd frontend
npm test                    # Run all tests
npm run test:watch         # Run tests in watch mode
npm run test:dashboard     # Generate test dashboard
```

### Backend Tests
```bash
cd backend
pytest                     # Run all tests
pytest --cov              # Run with coverage
pytest -v                 # Verbose output
```

### Integration Tests
```bash
# Run comprehensive test suite
python backend/test_e2e_workflow.py
python backend/test_frontend_api.py    # Frontend-backend integration
```

### Testing Levels Coverage
- **Class Testing**: 16+ unit test files covering individual components and classes
- **Integration Testing**: 7+ integration test files for component interactions
- **Validation Testing**: End-to-end workflow and acceptance testing
- **System Testing**: Performance, security, and stress testing

## 🚀 Deployment

Comprehensive deployment guides are available:
- [Deployment Guide](https://github.com/IviweBooi/AI-CONTENT-DETECTOR/blob/main/DEPLOYMENT_GUIDE.md) - Complete deployment instructions
- [Firebase Setup](https://github.com/IviweBooi/AI-CONTENT-DETECTOR/blob/main/FIREBASE_SETUP.md) - Authentication and database setup
- [Analytics Setup](https://github.com/IviweBooi/AI-CONTENT-DETECTOR/blob/main/ANALYTICS_SETUP.md) - Usage tracking configuration
- [Security Rules](https://github.com/IviweBooi/AI-CONTENT-DETECTOR/blob/main/SECURITY_RULES_SETUP.md) - Firestore security configuration

## 📊 API Documentation

### Core Endpoints

#### Content Detection
```http
POST /api/detect
Content-Type: application/json

{
  "text": "Content to analyze..."
}
```

#### File Upload
```http
POST /api/upload
Content-Type: multipart/form-data

file: [uploaded file]
```

#### Analytics
```http
GET /api/analytics/usage
Authorization: Bearer <token>
```

For complete API documentation, see the [API Reference](https://github.com/IviweBooi/AI-CONTENT-DETECTOR/blob/main/backend/README.md).


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/IviweBooi/AI-CONTENT-DETECTOR/blob/main/LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check our comprehensive guides in the `/docs` folder
- **Issues**: Report bugs and feature requests on GitHub Issues
- **Troubleshooting**: See [TROUBLESHOOTING.md](https://github.com/IviweBooi/AI-CONTENT-DETECTOR/blob/main/TROUBLESHOOTING.md)
- **User Manual**: Detailed usage instructions in [USER_MANUAL.md](https://github.com/IviweBooi/AI-CONTENT-DETECTOR/blob/main/USER_MANUAL.md)

## 🏆 Acknowledgments

- Built for CSC3003S Capstone Project 2025
- CNN model trained on diverse AI/human text datasets
- Special thanks to the open-source community for the amazing tools and libraries

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**Note**: This is an academic project developed for educational purposes. Ensure compliance with your institution's policies when using AI detection tools.
