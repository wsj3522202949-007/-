---
id: tool-00584
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-Study-Group-Copilot
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ymh1122/ai-study-group-copilot
created: 2026-07-18
updated: 2026-07-18
no: 584
category: 二、网文 / 长篇 AI 写作系统 库
repo: Ymh1122/AI-Study-Group-Copilot
stars: 0
url: https://github.com/ymh1122/ai-study-group-copilot
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

# Ymh1122/AI-Study-Group-Copilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ymh1122/ai-study-group-copilot
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Turn solitary writing and studying into a collaborative, AI-powered experience. AI Study Group Copilot brings together specialized AI agents—each with a distinct role—to support your thinking, research, and visualization in real time, all within a clean, split-screen interface.
- **本地描述**：Turn solitary writing and studying into a collaborative, AI-powered experience. AI Study Group Copilot brings together specialized AI agents—each with a distinct role—to support your thinking, research, and visualization in real time, all within a clean, split-screen interface.
- **拉取时间**：2026-07-23 22:56:06

---

🎓 **AI Study Group Copilot**

**AI Study Group Copilot** is an immersive, multi-agent collaborative platform designed to transform solitary writing and studying into an interactive team experience.

Unlike traditional chatbots, this application adopts a **Split-Screen Workbench** approach: you focus on creating content on the left, while specialized AI agents (**Reviewers**, **Researchers**) provide real-time, task-specific scaffolding on the right.

---

### 🚀 Key Features

- **👥 Multi-Agent System:**
  - **Mark (The Logic Reviewer):** Critiques your logic and argumentation structure without rewriting your text.
  - **Amy (The Researcher):** Fetches relevant data, facts, and citations to support your claims.
  - **Susu (The Visual Designer):** Transforms your text into visual mind maps and flowcharts using Mermaid.js.

- **💾 Context Memory:**
  - Automatically saves all discussion content to maintain continuous conversation history
  - Preserves context after page refresh or re-entry
  - Unified conversation history displayed in WeChat-like chat interface
  - Clear context button to delete all history records
  - Implementation using browser localStorage for persistent storage
  - JSON serialization for efficient data storage and retrieval
  - Automatic synchronization between session state and localStorage

- **🎨 Visual Diagram Generation:**
  - Automatic generation of Mermaid.js flowcharts or mind maps based on your content
  - Real-time visualization of logical structures and relationships
  - Interactive diagram display with zoom and scroll capabilities
  - Optimized rendering using Mermaid.js v8.14.0 for better compatibility
  - Debugging information showing raw Mermaid code and validation status
  - Fallback mechanisms to ensure diagram generation even when AI output is invalid

- **🖥️ Split-Screen UI:** A distraction-free editor on the left paired with an AI feedback feed on the right.

- **⚡ Powered by Qwen:** Utilizes the fast and cost-effective `qwen-plus` model for near-instant feedback.

- **🔍 Unknown-Free Interaction:** Agents do not chat idly; they only respond when triggered by your content submission.

---

### 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/AI-Study-Group-Copilot.git
   cd AI-Study-Group-Copilot
   ```
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure Environment Variables**
Create a .env file in the root directory and add your DashScope API Key:
    ```bash
    DASHSCOPE_API_KEY=your_qwen_api_key_here
    ```
4. **Run the Application**
    ```bash
    streamlit run app.py
    ```
    The application will be accessible at http://localhost:8501 by default.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

### 📂 Project Structure
```bash
    AI-Study-Group-Copilot/
    ├── agents/                 # Agent Logic
    │   ├── base_agent.py       # Base class for Qwen interaction
    │   ├── reviewer.py         # Logic for 'Mark' (Logic Reviewer)
    │   ├── researcher.py       # Logic for 'Amy' (Researcher)
    │   └── visualizer.py       # Logic for 'Susu' (Visual Designer) - Converts text to Mermaid.js diagrams
    ├── app.py                  # Main Streamlit UI application with split-screen interface
    ├── requirements.txt        # Python dependencies
    └── .env                    # API Keys (Not included in repo)
```

### 🧠 Technical Implementation Details

- **Context Memory System:** 
  - Implements localStorage-based persistence to maintain conversation history across page reloads
  - Unified conversation history stored in a single array with sender information
  - Chat messages displayed in WeChat-like interface with distinct bubbles for each participant
  - Automatic saving of all discussion content for continuous conversation experience
  - Clear context functionality to reset all conversation histories

- **Visual Diagram Rendering:** 
  - Uses Mermaid.js library (v8.14.0) to render interactive flowcharts and mind maps directly in the browser
  - Custom `VisualizerAgent` class that transforms text into Mermaid code with automatic chart type detection
  - Fallback mechanisms to generate default charts when model output is invalid
  - Real-time visualization with zoom and scroll capabilities in a fixed-height container
  - Debugging information display showing raw Mermaid code and validation status
  - Code sanitization to remove unwanted markdown markers from model outputs

- **Agent Specialization:** 
  - Each agent has customized prompts and processing logic tailored to their specific roles
  - `ReviewerAgent` focuses on logical structure and argumentation critique
  - `ResearcherAgent` specializes in fetching relevant data and citations
  - `VisualizerAgent` converts text content into visual representations using Mermaid.js

- **Error Handling:** 
  - Robust error handling and fallback mechanisms ensure consistent user experience even when individual components fail
  - VisualizerAgent includes multiple fallback strategies for generating valid Mermaid code
  - Input validation and sanitization for all user-provided content
  - Graceful degradation when API calls fail or return unexpected responses
  - Comprehensive exception handling with detailed logging for debugging purposes

### 🎨 VisualizerAgent Implementation Details

The `VisualizerAgent` is responsible for transforming textual content into visual diagrams using Mermaid.js syntax. Key features include:

- **Automatic Chart Type Detection:** Analyzes content structure to determine whether to generate a flowchart (`graph TD`) or mind map (`mindmap`)
- **Content Analysis:** Identifies key concepts, relationships, and hierarchical structures in the text
- **Code Sanitization:** Removes common formatting artifacts like markdown code block markers that may be included by the model
- **Validation & Fallback:** Validates generated Mermaid code and provides default diagrams when validation fails
- **Default Templates:** Includes context-aware default templates (e.g., university-related content generates education-themed mind maps)
- **Error Resilience:** Comprehensive error handling ensures that even if the model produces invalid output, a usable diagram is still generated
