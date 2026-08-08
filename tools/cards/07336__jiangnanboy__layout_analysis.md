---
id: tool-07336
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: layout_analysis
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/jiangnanboy/layout_analysis
created: 2026-07-18
updated: 2026-07-18
no: 7336
category: 画龙补充 / 扩容入库 — 补充源
repo: jiangnanboy/layout_analysis
stars: 60
url: https://github.com/jiangnanboy/layout_analysis
tier: "A"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 46999456a349fa0c
  - methods/QUICK_START.md
---

# jiangnanboy/layout_analysis

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/jiangnanboy/layout_analysis
- **Stars**：60
- **语言**：Python
- **License**：None
- **Topics**：cdla, layout-detection, yolov8
- **GitHub 描述**：中文版面检测（Chinese layout detection），yolov8 is used to detect the layout of Chinese document images。
- **本地描述**：layout_analysis
- **拉取时间**：2026-07-25 19:18:17

---

### 利用yolov8对中文文档图片进行版面检测
yolov8 is used to detect the layout of Chinese document images

#### 模型下载、训练及推理
本项目根据开源中文版面数据[CDLA](https://github.com/buptlihang/CDLA)  ，利用yolov8训练两个模型8mpt与8npt，

CDLA是一个中文文档版面分析数据集，面向中文文献类（论文）场景。包含以下10个label：

|正文|标题|图片|图片标题|表格|表格标题|页眉|页脚|注释|公式|
|---|---|---|---|---|---|---|---|---|related:
  - methods/QUICK_START.md
---|
|Text|Title|Figure|Figure caption|Table|Table caption|Header|Footer|Reference|Equation|

8mpt模型与8npt模型下载：

链接：https://pan.baidu.com/s/1YakM5AYrakoG9hYN-w7mJw 

提取码：j2za

训练：
```
from ultralytics import YOLO

def train_model():
    # 加载模型
    print('model load。。。')
    model = YOLO("8npt/best.pt")  # 加载模型
    print('model load completed。。。')
    #使用模型
    model.train(data="img-layout.yaml", epochs=300, device=1)# , lr0=0.0001)  # 训练模型
    metrics = model.val()  # 在验证集上评估模型性能
```
8npt
<br/>
<p align="center">
  <a>
    <img src="8npt/results.png">
  </a>
</p>
<br/>

8mpt
<br/>
<p align="center">
  <a>
    <img src="8mpt/results.png">
  </a>
</p>
<br/>

推理：
```
from ultralytics import YOLO
def infer():
    model = YOLO('8npt/best.pt')
    results = model('img.jpg')
    print(results[0].plot())
    cv2.imwrite('result.png', results[0].plot())
```

<br/>
<p align="center">
  <a>
    <img src="result/test2_result.png">
  </a>
</p>
<br/>


#### contact

1、github：https://github.com/jiangnanboy

2、博客：https://www.cnblogs.com/little-horse/

3、邮件:2229029156@qq.com

#### reference
https://github.com/ultralytics/ultralytics

https://github.com/buptlihang/CDLA

