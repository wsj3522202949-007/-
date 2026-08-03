---
id: tool-01429
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Arabic_story_generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/mohammad-albarham/arabic_story_generator
created: 2026-07-18
updated: 2026-07-18
no: 1429
category: 二、网文 / 长篇 AI 写作系统 库
repo: mohammad-albarham/Arabic_story_generator
stars: 7
url: https://github.com/mohammad-albarham/arabic_story_generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# mohammad-albarham/Arabic_story_generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mohammad-albarham/arabic_story_generator
- **Stars**：7
- **语言**：Python
- **License**：MIT
- **Topics**：arabic, story
- **GitHub 描述**：Generating a story in Arabic via Gen AI
- **本地描述**：Generating a story in Arabic via Gen AI
- **拉取时间**：2026-07-23 23:20:46

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Live Gradio application 


[https://huggingface.co/spaces/pain/Arabic_story_generator](https://huggingface.co/spaces/pain/Arabic_story_generator)


# Gradio Application

<img src="image_logo.png" style="width:50%; height:auto;">


This is a Gradio application that allows you to generate an Arabic story using generative AI models.

## Installation

1. Clone this repository:

    ```shell
    git clone https://github.com/mohammad-albarham/Arabic_story_generator.git
    ```

2. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

0. Add the keys for OPEN AI API model and stability AI API in [models.py](https://github.com/mohammad-albarham/Arabic_story_generator/blob/3702d6cad85fe38ff5944d7f99f43a37d7dec151/llm_models.py#L16) and [image_generator.py](https://github.com/mohammad-albarham/Arabic_story_generator/blob/3702d6cad85fe38ff5944d7f99f43a37d7dec151/image_generator.py#L22)
1. Run the application:

    ```shell
    gradio app.py
    ```

2. Open your web browser and navigate to [http://localhost:7860](http://localhost:7860).

3. Add your a description and the needed number of pages and click on generate story.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

### Instrcutions for the contribution:

1. Please install black formatter as follows:
`pip install black`
2. Make sure to format all python files you want to change using this command on the terminal:
`black .`

You can see this tutorial for more information about the formatter: [tutorial](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)


## License

[ACADEMIC PUBLIC LICENSE](https://github.com/mohammad-albarham/Arabic_story_generator/tree/main?tab=License-1-ov-file)
