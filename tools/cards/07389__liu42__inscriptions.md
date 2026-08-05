---
id: tool-07389
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 中文友好, 本地写作]
title: inscriptions
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/liu42/inscriptions
created: 2026-07-18
updated: 2026-07-18
no: 7389
category: 画龙补充 / 扩容入库 — 补充源
repo: liu42/inscriptions
stars: 37
url: https://github.com/liu42/inscriptions
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# liu42/inscriptions

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/liu42/inscriptions
- **Stars**：37
- **语言**：JavaScript
- **License**：None
- **Topics**：computer-vision, flask, image-classification, object-detection, onnxruntime, opencv, webapp, yolo, yolov8
- **GitHub 描述**：2024 年 MathorCup 数学应用挑战赛 B 题，基于 YOLOv8 的甲骨文原始拓片图像单字分割识别模型。
- **本地描述**：inscriptions
- **拉取时间**：2026-07-25 19:20:26

---

# Inscriptions 甲骨文识别系统

*<u>v2.0.0 新变化：项目使用 C/S 架构重新实现。</u>*

## 项目简介

本项目取材自 2024 年 MathorCup 数学应用挑战赛 B 题，基于 YOLOv8 的甲骨文原始拓片图像单字分割识别系统。针对原始拓片图像中的甲骨文文字分割识别包括以下两个阶段：

- 目标检测：基于 YOLOv8 目标检测模型，对甲骨文文字所在的矩形区域进行提取。

- 字符识别：基于 YOLOv8 图像分类模型，对文字图像进行分类，判断该字形所代表的具体字符内容。

同时实现基于 [Flask](https://flask.palletsprojects.com/en/stable/) 的后端推理接口和 Web UI 可视化界面。

## 截图展示

!`[效果展示](./assets/screenshot.jpg "效果展示")`

## 性能评估

本项目训练数据集来自 [殷契文渊](https://jgw.aynu.edu.cn/)，对原始数据集进行了增强，采用 YOLOv8s 模型进行训练，能识别 其中195 中不同的甲骨文字符，模型各项指标如下：

| mAP50 | mAP50-95 | Precision | Recall | Top1_acc | Top5_acc |
|:-----:|:--------:|:---------:|:------:|:--------:|:--------:|
| 0.928 | 0.608    | 0.905     | 0.865  | 0.897    | 0.969    |

## 使用说明

首先需要安装本项目依赖的各种库和工具包。

```shell-session
pip install -r requirements.txt
```

可以在本项目 Releases 中下载训练好的模型权重文件并移动到目录 servers/models 下，运行以下命令以启动服务端程序。

```shell-session
python -m flask --app servers.server:app run --host=0.0.0.0 --port=8080
```

本项目识别程序默认的配置文件为 servers/configs/config.toml，其中各个字段的描述如下。

| 字段名                    | 字段描述                                      |
|:----------------------:|:--------------------------------------related:
  - methods/QUICK_START.md
---:|
| providers              | 模型推理 ONNX Runtime Execution Providers 列表。 |
| precision              | 推理运算精度，可取 "fp32"（单精度）或 "fp16"（半精度）。       |
| detection-model-path   | 目标检测模型加载路径。                               |
| recognition-model-path | 字符识别模型加载路径。                               |
| conf-threshold         | 目标检测置信度阈值。                                |
| iou-threshold          | 目标检测非极大值抑制 IoU 阈值。                        |

客户端程序位于 clients 目录下，可通过各种前端服务器部署。此外还需要安装配置并启动 [Nginx](https://nginx.org/en/) 服务进行后端服务和前端服务之间的反向代理。

如果需要使用自己的数据集训练模型，则需要安装 Ultralytics 框架，参照 [Ultralytics 官方文档](https://docs.ultralytics.com/) 进行模型的训练，最后将模型转换为 ONNX 格式进行部署即可。

```shell-session
pip install ultralytics
```
