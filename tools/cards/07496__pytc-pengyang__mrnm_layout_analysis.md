---
id: tool-07496
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: mrnm_layout_analysis
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/pytc-pengyang/mrnm_layout_analysis
created: 2026-07-18
updated: 2026-07-18
no: 7496
category: 画龙补充 / 扩容入库 — 补充源
repo: pytc-pengyang/mrnm_layout_analysis
stars: 0
url: https://github.com/pytc-pengyang/mrnm_layout_analysis
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2edc2157718234b8
  - methods/QUICK_START.md
---

# pytc-pengyang/mrnm_layout_analysis

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/pytc-pengyang/mrnm_layout_analysis
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：mrnm_layout_analysis
- **拉取时间**：2026-07-25 19:23:40

related:
  - methods/QUICK_START.md
---



此存储库包含 MRNM（多模态特征和关系预测网络）的实现，这是一种用于历史文档布局分析的模型。MRNM 将多模态特征（视觉、文本和空间）与关系预测网络相结合，以检测布局元素并预测阅读顺序。

模型架构 MRNM 由三个主要部分组成：
多模态网络 ：提取并融合视觉、文本和空间特征
区域检测 ：执行布局元素检测和分类
关系预测网络 ：使用图神经网络预测读取顺序

数据集下载地址如下：
链接: https://pan.baidu.com/s/17mJgYvlaavw39zOffBcMwg 提取码: h7vk 

目录结构如下
MRNM_layout_analysis/
│
├── data_loader/               
│   ├── __init__.py
│   ├── page_data.py           
│   ├── dataset.py             
│   └── transforms.py          
│
├── models/                    
│   ├── __init__.py            # 主模型MRNM实现
│   ├── backbone/              # 基础网络
│   │   ├── __init__.py
│   │   ├── cnn.py             # CNN视觉特征提取
│   │   └── transformer.py     # Transformer相关模块
│   ├── multimodal/            # 多模态特征提取
│   │   ├── __init__.py
│   │   ├── visual.py          # 视觉特征提取
│   │   ├── text.py            # 文本特征提取
│   │   ├── spatial.py         # 空间特征提取
│   │   └── fusion.py          # 多模态融合
│   └── heads/                 # 任务头
│       ├── __init__.py
│       ├── rpn.py             # 区域建议网络
│       ├── classifier.py      # 分类头
│       └── relation_prediction.py  # 关系预测网络
│
├── utils/                     
│   ├── __init__.py
│   ├── losses.py              # 损失函数
│   ├── metrics.py             # 评估指标
│   ├── attention.py           # 注意力机制实现
│   ├── geometry.py            # 几何变换工具
│   └── edge_features.py       # 边特征提取
│
├── configs/                   
│   ├── default.yaml           # 默认配置
│   ├── train.yaml             # 训练专用配置
│   └── model.yaml             # 模型结构配置
│
├── scripts/                  
│   ├── train.py             
│   ├── test.py               
│   └── visualize.py          
│
├── tools/                     
│   ├── convert_data.py        
│   ├── create_annotations.py  
│   └── evaluate_results.py    

