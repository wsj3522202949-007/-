---
id: tool-05592
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: llm-generated-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/umitkayaardi/llm-generated-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5592
category: 一、去 AI 味 / Humanizer 库
repo: UmitKayaardi/llm-generated-text-detector
stars: 1
url: https://github.com/umitkayaardi/llm-generated-text-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 79609eac0ee85fb0
  - methods/改稿润色指令库.md
---

# UmitKayaardi/llm-generated-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/umitkayaardi/llm-generated-text-detector
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A scalable classification project built with PySpark to distinguish between human and LLM-generated text (GPT-4, Llama, Cohere). Using the RAID dataset, it implements comprehensive EDA and feature engineering to deliver a high-performance, data-driven solution for AI content detection and integrity.
- **本地描述**：A scalable classification project built with PySpark to distinguish between human and LLM-generated text (GPT-4, Llama, Cohere). Using the RAID dataset, it implements comprehensive EDA and feature engineering to deliver a high-performance, data-driven solution for AI content detection and integrity.
- **拉取时间**：2026-07-25 18:24:25

---

# LLM-Generated Text Detector & Analytics

## Project Overview
In the era of rapidly advancing Large Language Models (LLMs), distinguishing between human-written and machine-generated content has become a fundamental challenge for digital trust and information integrity. This project develops a scalable analytics pipeline to identify the "digital fingerprints" of various AI models including **GPT-4, Llama-Chat, and Cohere**. 

Using the **RAID (Real-world AI Detection)** benchmark dataset, this repository demonstrates how big data tools can be leveraged for robust text classification and forensic linguistic analysis.

## Key Technical Features
- **Scalable Big Data Pipeline:** Implemented using **PySpark** to ensure the architecture can handle high-volume text datasets that exceed traditional memory limits.
- **Cross-Model Benchmarking:** Comparative analysis of text generation styles across multiple state-of-the-art LLMs vs. human authors.
- **Advanced Feature Engineering:** Development of statistical features such as lexical density, word count distributions, and text complexity metrics.
- **Statistical Visualization:** Deep-dive Exploratory Data Analysis (EDA) using Seaborn and Matplotlib to uncover structural differences in AI writing.

## Tech Stack
- **Core Engine:** Apache Spark (PySpark)
- **Programming:** Python
- **Natural Language Processing:** NLTK
- **Data Visuals:** Seaborn, Matplotlib
- **Data Architecture:** Parquet-based processing for optimized I/O

## Dataset Insights
The project utilizes the **RAID dataset**, a comprehensive benchmark for AI detection.
- **Diversity:** Covers multiple generation models and diverse human-written sources.
- **Scalability:** Processed in a distributed environment to maintain performance during heavy computational tasks like tokenization and feature extraction.

## Methodology
1. **Data Orchestration:** Efficiently loading and partitioning large-scale Parquet files.
2. **Preprocessing & Filtering:** Selective filtering of specific model architectures (Llama, GPT, etc.) to analyze unique model signatures.
3. **Feature Construction:** Engineering numerical representations of text for classification readiness.
4. **Analysis & Insights:** Validating detection patterns through robust statistical visualizations.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---
*Developed as a professional case study in Scalable Machine Learning and AI Content Integrity.*
