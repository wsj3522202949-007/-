---
id: tool-01877
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AiStoryGenerator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/9618664099/aistorygenerator
created: 2026-07-18
updated: 2026-07-18
no: 1877
category: 二、网文 / 长篇 AI 写作系统 库
repo: 9618664099/AiStoryGenerator
stars: 0
url: https://github.com/9618664099/aistorygenerator
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 9618664099/AiStoryGenerator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/9618664099/aistorygenerator
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：9618664099/AiStoryGenerator
- **拉取时间**：2026-07-23 23:33:42

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

import os
import streamlit as st
from huggingface_hub import InferenceClient

# Set HuggingFace token
HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(api_key=HF_TOKEN)

def generate_story(prompt):
    system_message = "You are a creative writing assistant."
    user_message = f"Write a short, imaginative story based on this prompt: {prompt}"
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct",
        messages=messages,
        max_tokens=512,
        temperature=0.8,
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.set_page_config(page_title="AI Story Generator", layout="centered")
st.title("📚 AI Story Generator from Prompts")
st.markdown("Enter a creative prompt and let AI write a story for you!")

prompt = st.text_area("✍️ Enter your story prompt:", height=150)

if st.button("🚀 Generate Story"):
    if not prompt.strip():
        st.warning("⚠️ Please enter a story prompt.")
    else:
        with st.spinner("🧠 Generating..."):
            try:
                story = generate_story(prompt)
                st.success("🎉 Here's your story:")
                st.write(story)
            except Exception as e:
                st.error(f"❌ Error: {e}")

# Python cache files
__pycache__/
*.py[cod]
*.pyo
# Virtual environment folders
.env/
.venv/
venv/
ENV/
env/
# Jupyter Notebook checkpoints
.ipynb_checkpoints/
# System files
.DS_Store
Thumbs.db
# VSCode settings (optional)
.vscode/
# Streamlit secrets (DO NOT push this to GitHub)
.streamlit/secrets.toml
# Logs or temporary files (if any)
*.log
