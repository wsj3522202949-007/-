---
id: tool-00091
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: script-storyboard-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/sdinesh01/script-storyboard-generator
created: 2026-07-18
updated: 2026-07-18
no: 91
category: 二、网文 / 长篇 AI 写作系统 库
repo: sdinesh01/script-storyboard-generator
stars: 1
url: https://github.com/sdinesh01/script-storyboard-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# sdinesh01/script-storyboard-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sdinesh01/script-storyboard-generator
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：Prj files for NLP/AI illustration generator
- **本地描述**：Prj files for NLP/AI illustration generator
- **拉取时间**：2026-07-23 22:41:32

---

# script-storyboard-generator

### Goal: Use natural language processing methodologies to distill movie scripts into prompts to create AI generated storyboards

I would like to test the current capacity of AI image generators to assist creative workflows in film. Illustration and storyboarding is a crucial process in film and television pre-production and encompasses writing, blocking, FX, sound, and cinematographic design. The goal is to develop a workflow that can assist visual artists with preliminary design.

Task challenges:
1. Meaningfully summmarize information from compositionally rigid documents (movie scripts)
2. Compose prompts for AI generators that maximize efficiency and accuracy (using MidJourney, Stable Diffusion, etc.)
3. Build a short application with a summarization + Stable Diffusion model pipeline

**Files:** script_summarizer.py (Streamlit app), project_report.pdf (written report with project methodology, results, and discussion), summary_gen.py (pipeline for summarization, can be run without Streamlit), data_cleaning.py (original scripts for data cleaning).

## Run the streamlit app locally
In a virtual environment, locate `requirements.txt` and `script_summarizer.py` in the directory.
Run the following:
```
pip install -r requirements.txt
python script_summarizer.py
streamlit run [user folder]/script_summarizer.py
```
**NOTE**: If a GPU is available, uncomment lines 50, 51, 79, 80 in `script_summarizer.py` to increase processing speed. Without GPU, the Stable Diffusion model will take 25-30 minutes to run on a machine with 16 GB RAM. 

## Dataset documentation

Title: **movie_scenes_by_header.csv** <br>
Description: This dataset contains the scripts for _28 Days Later, Isle of the Dead, Jurassic Park, Pan’s Labyrinth,_ and _Whiplash_. <br>
Data Source: I used five manually encoded scripts from [Kaggle](https://www.kaggle.com/datasets/gufukuro/movie-scripts-corpus) for my analysis. I went with manual encoding to minimize the effect of machine learning miscodings on my overall project. Human mislabeling is also possible since this dataset was user created. I used regex statements to split headings and their respective text. <br>
Date Created: March 10, 2023 <br>
Last Modified: April 20, 2023<br>

Size: 85.6 KB —  6 columns, 580 entries<br>
Format: Comma-separated values <br>
Encoding: UTF-8 <br>

Columns: scriptID, sceneID, header, text <br>
Column Descriptions: 
* scriptID: type (integer), unique integer identifier for each movie <br>
* sceneID: type (integer), unique integer identifier for each scene per movie <br>
* header: type (object), one of four scene headings (scene_heading, text, dialog, speaker_heading) <br>
* text: type (object), text that follows the header in the script <br>
* upper: type(object, list), extracted uppercase words from the screenplay text. Uppercase words in screenplay indicate important characters, blockings, camera angles, etc. <br>
* tokens: type(object), preprocessed text from the `text` column <br>
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
Title: **movie_scenes.csv** <br>
Description: This dataset contains the scripts for _28 Days Later, Isle of the Dead, Jurassic Park, Pan’s Labyrinth,_ and _Whiplash_. <br>
Data Source: I used five manually encoded scripts from [Kaggle](https://www.kaggle.com/datasets/gufukuro/movie-scripts-corpus) for my analysis. I went with manual encoding to minimize the effect of machine learning miscodings on my overall project. Human mislabeling is also possible since this dataset was user created. Data was created by using regex statements to split scripts into a dataframe, and then the dataframes for all scripts were concatenated. <br>
Date Created: March 10, 2023 <br>
Last Modified: April 20, 2023<br>

Size: 50.6 KB —  4 columns, 34 entries<br>
Format: Comma-separated values <br>
Encoding: UTF-8 <br>

Columns: scriptID, sceneID, text, upper <br>
Column Descriptions: 
* scriptID: type (integer), unique integer identifier for each movie <br>
* sceneID: type (integer), unique integer identifier for each scene per movie <br>
* text: type (object), entire text of the scene, screenplay headings included <br>
* upper: type(object, list), extracted uppercase words from the screenplay text. Uppercase words in screenplay indicate important characters, blockings, camera angles, etc. <br>
