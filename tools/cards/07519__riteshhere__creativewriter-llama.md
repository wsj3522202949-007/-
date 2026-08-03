---
id: tool-07519
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: creativewriter-llama
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/riteshhere/creativewriter-llama
created: 2026-07-18
updated: 2026-07-18
no: 7519
category: 画龙补充 / 扩容入库 — 补充源
repo: riteshhere/creativewriter-llama
stars: 0
url: https://github.com/riteshhere/creativewriter-llama
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/QUICK_START.md
---

# riteshhere/creativewriter-llama

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/riteshhere/creativewriter-llama
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Simple Langchain application use LLama-2-7B locally
- **本地描述**：creativewriter-llama
- **拉取时间**：2026-07-25 19:24:22

---

# creativeWriter-llama



### Project Overview



This repository offers a streamlined solution for deploying local LLM applications, utilizing the Llama-2-7B model as its backbone, yet it's fully adaptable to any LLM framework. It serves as a prototype for a creative writer application, generating articles from user-defined topics. Its core functionality—prompt-based response generation from the LLM—enables the development of a tons of applications by simply altering the prompts.



-------



### How to run

1. **Repository Cloning**: Clone the repository to initiate your local setup.

2. **Download Model**: Download LLM model from the [HuggingFace](https://huggingface.co/models) and save it in `/models`

   > Download link: (https://huggingface.co/BashitAli/llama-2-7b-chat.ggmlv3.q5_K_M)

4. **Virtual Environment**: Establish an isolated environment for dependency management

   ```

   conda create -p env_name python==3.9 -y

   ```

5. Dependency Installation: Install necessary dependencies using `requirements.txt`

   ```python

   pip install -r requirements.txt

   ```

6. **Application Initialization**: Launch the application through Streamlit

   ```python

   streamlit run app.py

   ```

   

--------related:
  - methods/QUICK_START.md
---





### Re-use code for different application



The modular design of this framework permits the creation of diverse LLM applications through prompt customization:

We can implement minor modifications to get the target application as follows:



+ Prompt Customization for Application: change the prompt to get the desired result. 

```python

  ## PromptTemplate

    template = """ WRITE THE PROMPT FOR NEW APPLICATION """



    prompt = PromptTemplate(input_variables = ["input_text", "no_words", "blog_style"],

                            template = template)

```

+ Temperature: Change the value of temperature to make model response more or less creative



   







