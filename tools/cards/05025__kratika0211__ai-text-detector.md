---
id: tool-05025
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/kratika0211/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5025
category: 一、去 AI 味 / Humanizer 库
repo: kratika0211/ai-text-detector
stars: 0
url: https://github.com/kratika0211/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# kratika0211/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/kratika0211/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：kratika0211/ai-text-detector
- **拉取时间**：2026-07-25 18:03:20

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

🧠 AI Text Detector
A Streamlit-based web application that detects whether a piece of text is AI-generated or human-written.
Supports multiple input formats including manual text, PDF, Word documents, and images.

🚀 Features
✍️ Manual text input
📄 Upload PDF files
📝 Upload Word (.docx) documents
🖼️ Upload images (OCR supported locally)
📊 AI probability score (0–100%)
🧠 Explanation of why text is flagged
⚡ Fast and interactive UI

📂 Project Structure
ai-text-detector/
├──streamlit_app.py     # Main Streamlit UI
├──requirements.txt     # Dependencies
├──README.md            # Project documentation
└──ai_detector_model/   # (Optional) Trained model

⚙️ Installation (Local)
1. Clone the repository
git clone https://github.com/your-username/ai-text-detector.git
cd ai-text-detector
2. Install dependencies
pip install -r requirements.txt
3. (Optional) Enable OCR for images
Install Tesseract:
sudo apt install tesseract-ocr

For Windows:
Download from: https://github.com/tesseract-ocr/tesseract
4. Run the app
streamlit run streamlit_app.py

🌐 Deployment
This app can be deployed using:
Streamlit Cloud (recommended)
Hugging Face Spaces

🧠 How It Works
User uploads or inputs text
Text is extracted (PDF/Word/Image OCR)

Model analyzes patterns in:
Sentence Structure
Vocabulary Variation
Punctuation Patterns

Outputs:
AI probability score
Explanation of reasoning

🔮 Future Improvements
🔍 Highlight AI-generated sentences
📈 Confidence visualization
🤖 Integrate fine-tuned transformer model
🌐 Full deployment with backend API

🛠️ Tech Stack
Python
Streamlit
PyMuPDF (PDF processing)
python-docx
pytesseract (OCR)
Transformers (for future model integration)
🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

📄 License
This project is open-source and available under the MIT License.

👩‍💻 Author
Kratika Dariyani

⭐ If you like this project
Give it a ⭐ on GitHub!
