---
id: tool-00365
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: vflow
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/trishix/vflow
created: 2026-07-18
updated: 2026-07-18
no: 365
category: 二、网文 / 长篇 AI 写作系统 库
repo: Trishix/vflow
stars: 0
url: https://github.com/trishix/vflow
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: ae23b2511a37f94d
  - methods/最强写作方法论_全球最强综合版.md
---

# Trishix/vflow

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/trishix/vflow
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：VFLow is a node-based AI workflow builder that enables you to create, customize, and reuse AI-powered workflows entirely in your browser. Connect prompts, AI models, and data processing nodes to build powerful automation flows without writing code.
- **本地描述**：VFLow is a node-based AI workflow builder that enables you to create, customize, and reuse AI-powered workflows entirely in your browser. Connect prompts, AI models, and data processing nodes to build powerful automation flows without writing code.
- **拉取时间**：2026-07-23 22:49:45

---

# VFlow
VFLOW is a node-based AI workflow builder that enables you to create, customize, and reuse AI-powered workflows entirely in your browser. Connect prompts, AI models, and data processing nodes to build powerful automation flows without writing code.

<img width="1512" height="982" alt="Screenshot 2026-04-27 at 7 24 31 AM" src="https://github.com/user-attachments/assets/45f781bd-477b-4d20-99d1-2fad9551ff31" />



## ✨ Features

- **Drag-and-Drop Interface**: Intuitive workflow builder powered by React Flow
- **Multiple Node Types**: Prompt, AI, Markdown, Annotation, and Error nodes
- **Multi-Provider LLM Support**: Connect to OpenAI, Anthropic, Google, Groq, xAI, and OpenRouter
- **Local-First**: All workflows and API keys stored securely in your browser's localStorage
- **Template Library**: Get started quickly with pre-built workflow templates
- **Import/Export**: Share workflows as JSON files or import existing ones
- **Responsive Design**: Works on desktop and mobile devices
- **Dark/Light Mode**: Automatic theme switching based on system preferences
- **Real-time Execution**: Run workflows and see results instantly

## 🚀 Getting Started

### Prerequisites

- Node.js 20+ installed
- Modern web browser (Chrome, Firefox, Safari, or Edge)
- API keys for your preferred LLM providers (optional for initial exploration)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vflow.git
   cd vflow
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser to `http://localhost:3000`

### Usage

1. **Create a New Workflow**:
   - Click "+ New Workflow" in the sidebar
   - Give your workflow a name

2. **Add Nodes**:
   - Use the floating "+" button or sidebar to add nodes
   - Available node types:
     - **Prompt Node**: Input text or prompts
     - **AI Node**: Process prompts with LLMs (requires API key)
     - **Markdown Node**: Display formatted output
     - **Annotation Node**: Add notes and documentation
     - **Error Node**: Shows validation errors

3. **Configure Nodes**:
   - Click on any node to open its configuration panel
   - Set prompts, select models, adjust parameters

4. **Connect Nodes**:
   - Drag from output ports to input ports to create connections
   - Build chains of processing steps

5. **Run Your Workflow**:
   - Click the "▶️ Run" button in the top toolbar
   - Watch as data flows through your nodes
   - View results in Markdown nodes

6. **Manage API Keys**:
   - Access via sidebar ⚙️ Settings → API Keys
   - Add keys for providers you want to use
   - Keys are stored locally in your browser

7. **Save & Share**:
   - Workflows auto-save to localStorage
   - Export as JSON via the menu (⋯ → Export)
   - Import workflows from JSON files

## 🧩 Node Types

### Prompt Node
Input node for text prompts with optional labeling. Use to start workflows or inject static text.

### AI Node
Core processing node that connects to various LLM providers:
- **Providers**: OpenAI, Anthropic, Google, Groq, xAI, OpenRouter
- **Features**: System prompts, model selection, temperature control, reasoning toggle (where supported)
- **Requires**: Valid API key for selected provider

### Markdown Node
Output node that renders markdown with additional features:
- Copy to clipboard button
- Toggle between rendered view and raw/code view
- Supports GitHub Flavored Markdown

### Annotation Node
Free-form text node for adding documentation, notes, or comments within your workflows.

### Error Node
Internal component that displays validation errors when node data is invalid or missing required fields.

## 🤖 Supported AI Providers

VFLOW integrates with the Vercel AI SDK to support these providers:

| Provider | Popular Models | Notes |
|----------|----------------|-------|
| **OpenAI** | GPT-4o, GPT-4o mini, o1, o3 series | Industry leader |
| **Anthropic** | Claude 3.5 Sonnet, Claude 3 Opus | Strong reasoning |
| **Google** | Gemini 1.5 Pro, Gemini 1.5 Flash | Multimodal capable |
| **Groq** | Llama 3, Mixtral, DeepSeek R1 | Extremely fast inference |
| **xAI** | Grok models | Latest from xAI |
| **OpenRouter** | Hundreds of models | Aggregator service |

API keys are stored locally and never sent to any server.

## 🛠️ Technology Stack

- **Framework**: [Next.js 15](https://nextjs.org/) (App Router)
- **UI Library**: [shadcn/ui](https://ui.shadcn.com/) built on [Radix UI](https://www.radix-ui.com/)
- **Styling**: [Tailwind CSS 4](https://tailwindcss.com/)
- **State Management**: [Zustand](https://zustand-demo.pmnd.rs/) with persistence
- **Workflow Engine**: [React Flow](https://reactflow.dev/) (@xyflow/react)
- **AI Integration**: [Vercel AI SDK](https://sdk.vercel.ai/docs)
- **Notifications**: [Sonner](https://sonner.emilkowal.ski/)
- **Forms**: [React Hook Form](https://react-hook-form.com/) with [Zod](https://zod.dev/) validation

## 📁 Project Structure

```
vflow/
├── app/                      # Next.js App Router
│   ├── layout.tsx            # Root layout with theme provider
│   ├── page.tsx              # Home page
│   ├── globals.css           # Tailwind CSS configuration
│   └── not-found.tsx         # 404 page
├── components/               # React components
│   ├── nodes/                # Workflow node implementations
│   │   ├── AiNode.tsx        # AI processing node
│   │   ├── PromptNode.tsx    # Input/text node
│   │   ├── MarkdownNode.tsx  # Output display node
│   │   ├── AnnotationNode.tsx # Notes/documentation
│   │   └── ErrorNode.tsx     # Error display
│   ├── workflow/             # Workflow builder components
│   │   ├── WorkflowCanvas.tsx # React Flow canvas
│   │   ├── NodeCard.tsx       # Node wrapper component
│   │   ├── AddNodeButtons.tsx # Node creation UI
│   │   ├── ImportDialog.tsx   # JSON import
│   │   └── panels/           # Floating panels
│   │       └── WorkflowPanels.tsx
│   ├── layout/                # Layout components
│   │   ├── AppSidebar.tsx     # Main sidebar
│   │   └── Logo.tsx          # App logo
│   ├── api/                   # API management
│   │   └── ApiKeys.tsx        # API key management
│   └── ui/                    # shadcn/ui components
├── features/                 # Feature-based modules
│   ├── workflow/              # Workflow feature
│   │   ├── stores/             # State management
│   │   │   └── workflow-store.ts
│   │   └── templates.ts       # Built-in templates
│   ├── ai/                    # AI integration
│   │   ├── client.ts          # AI provider configurations
│   │   └── api-key-store.ts   # API key storage
│   └── canvas/                # Canvas execution
│       └── compute.ts        # Node execution logic
├── lib/                       # Utilities
│   ├── utils.ts               # General utilities
│   └── cn.ts                  # Class name merger
├── hooks/                     # Custom React hooks
├── types/                     # TypeScript types
│   └── base-node.ts           # Node type definitions
└── public/                    # Static assets
```

## 🔧 Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

### Environment Variables

No server-side environment variables required. All data is stored locally in the browser.

## 📚 Documentation

For more detailed information, see:

- [Node Reference](https://github.com/Trishix/vflow/blob/main/docs/nodes.md) - Detailed node specifications
- [AI Provider Setup](https://github.com/Trishix/vflow/blob/main/docs/ai-providers.md) - Guide to configuring LLM providers
- [Workflow Templates](https://github.com/Trishix/vflow/blob/main/docs/templates.md) - Overview of built-in templates
- [Keyboard Shortcuts](https://github.com/Trishix/vflow/blob/main/docs/shortcuts.md) - Productivity tips

*Note: Documentation files are placeholders - contribute to help build them!*

## 🤝 Contributing

We welcome contributions to make VFLOW better! Please read our [Contributing Guidelines](https://github.com/Trishix/vflow/blob/main/CONTRIBUTING.md) for details on:

- Reporting bugs
- Suggesting features
- Submitting pull requests
- Development setup
- Coding standards

**Note**: CONTRIBUTING.md is currently a placeholder - help us create it!

### Contribution Process

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙋‍♂️ Support

- **Documentation**: Check the docs/ directory (in progress)
- **Issues**: Report bugs or request features on GitHub Issues
- **Discussions**: Join community discussions on GitHub Discussions

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Trishix/vflow/blob/main/LICENSE) file for details.

## 👏 Acknowledgments

- [Vercel AI SDK](https://sdk.vercel.ai/) for LLM integrations
- [React Flow](https://reactflow.dev/) for the workflow engine
- [shadcn/ui](https://ui.shadcn.com/) for beautiful UI components
- [Radix UI](https://www.radix-ui.com/) for accessible primitives
- [Tailwind CSS](https://tailwindcss.com/) for styling
- [Zustand](https://zustand-demo.pmndrs/) for state management

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

