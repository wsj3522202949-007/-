---
id: tool-05662
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Smart-Food-Nutrition-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/adarshzolekar/smart-food-nutrition-detector
created: 2026-07-18
updated: 2026-07-18
no: 5662
category: 一、去 AI 味 / Humanizer 库
repo: AdarshZolekar/Smart-Food-Nutrition-Detector
stars: 2
url: https://github.com/adarshzolekar/smart-food-nutrition-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: be877be19a732f3f
  - methods/改稿润色指令库.md
---

# AdarshZolekar/Smart-Food-Nutrition-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/adarshzolekar/smart-food-nutrition-detector
- **Stars**：2
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Smart Food Nutrition Detector is an AI-powered food analyzer that detects food items from text or images and provides their nutritional breakdown.
- **本地描述**：Smart Food Nutrition Detector is an AI-powered food analyzer that detects food items from text or images and provides their nutritional breakdown.
- **拉取时间**：2026-07-25 18:27:01

---

## Smart Food Nutrition Detector



![Python](https://img.shields.io/badge/Python-3.9-blue)  ![Flask](https://img.shields.io/badge/Flask-Backend-lightgrey)  ![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-yellow)  ![HTML5](https://img.shields.io/badge/HTML5-Markup-orange)  ![CSS3](https://img.shields.io/badge/CSS3-Design-blue)  ![Google Colab](https://img.shields.io/badge/Google%20Colab-ML-green) 



Smart Food Nutrition Detector is a nutrition analyzer that helps users understand the nutritional value of their food. It supports both search by food name and image-based food recognition.

I have created a dataset for this on Hugging Face : https://huggingface.co/datasets/adarshzolekar/foods-nutrition-dataset



---



## About this project



This project was developed as an internship project with Edunet Foundation to demonstrate practical skills in full-stack development, machine learning and nutrition data analysis. 



---



## Features



- Search Bar: Search for food items by name



- Image Upload: Upload a food image, detect the item and see nutrients



- Nutrition Info: Energy, Carbs, Protein, Fat, Sugar, Fibre, Cholesterol, Calcium



- Clean UI: Results shown in cards with nutrient breakdown



- Tech Stack: Python, Flask, HTML, CSS, JavaScript, Google Colab



- Dataset: https://huggingface.co/datasets/adarshzolekar/foods-nutrition-dataset



---



## How to Use



1. Search Mode



Enter a food item in the search bar (e.g., banana, pizza, dosa).



The detector will display nutritional info:

```

Calories

Carbohydrates

Protein

Fat

Free Sugar

Fibre

Cholesterol

Calcium

```



2. Image Upload Mode



Upload a clear food image.



The app detects the food and shows its nutritional breakdown.



---



## Setup Instructions



1. Backend

   ```

   cd backend

   python -m venv .venv

   source .venv/bin/activate 

   pip install --upgrade pip

   pip install -r requirements.txt

   python app.py

   ```

   Backend runs at: http://localhost:5000



2. Frontend

   ```

   cd frontend

   python -m http.server 8000

   ```

   Frontend runs at: http://localhost:8000



3. Google Colab (Optional)



   Use colab/build_labels_and_validate.ipynb to:



   Prepare labels.json



   Validate image recognition with CLIP.



---



## Built With



- Python (Flask, Pandas, Torch, CLIP)



- HTML / CSS / JavaScript



- Google Colab (dataset preparation)



- foods-nutrition-dataset for Indian food items.



---



## Validation checklist



- foods.csv present and columns spelled as shown



- labels.json present and includes all aliases



- Search returns rows for common items



- Image detection returns candidates and at least one match for clear photos.





---



## Example Output



Search “banana” →



- Calories: 89 kcal

- Carbs: 22.8 g

- Protein: 1.1 g

- Fat: 0.3 g

- Free Sugar: 12.2 g

- Fibre: 2.6 g

- Cholesterol: 0 mg

- Calcium: 5 mg



---



## Future Improvements 



- Add micronutrient details (vitamins, minerals).



- Support multiple foods in a single image.



- Add portion size estimation from image.



- Enable user-specific diet tracking and history.



- Provide meal recommendations based on health goals.



- Support voice-based food input.



- Integrate barcode scanning for packaged foods.



related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---



## Contributing



Contributions are welcome! Fork the repo, make changes and submit a PR.



<p align="center">

  <a href="#top">

    <img src="https://img.shields.io/badge/%E2%AC%86-Back%20to%20Top-blue?style=for-the-badge" alt="Back to Top"/>

  </a>

</p>













