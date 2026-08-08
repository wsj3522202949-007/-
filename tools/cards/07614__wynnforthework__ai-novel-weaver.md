---
id: tool-07614
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 中文友好]
title: ai-novel-weaver
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/wynnforthework/ai-novel-weaver
created: 2026-07-18
updated: 2026-07-18
no: 7614
category: 画龙补充 / 扩容入库 — 补充源
repo: wynnforthework/ai-novel-weaver
stars: 1
url: https://github.com/wynnforthework/ai-novel-weaver
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 97679305b587efba
  - methods/QUICK_START.md
---

# wynnforthework/ai-novel-weaver

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/wynnforthework/ai-novel-weaver
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI小说创作
- **本地描述**：ai-novel-weaver
- **拉取时间**：2026-07-25 19:27:48

---

# AI小说编织者 (AI Novel Weaver)

AI小说编织者是一个基于Web的智能小说创作平台，旨在通过先进的AI技术协助人类创作高质量的长篇小说。系统采用复杂的管道式架构和智能体协调机制，确保长期一致性和高质量的故事生成。

## 🎯 项目概述

本项目实现了从创意孵化到作品发布的完整创作流程，核心特色是编排器驱动的自动化创作循环，从高层规划（卷和情节弧线）到微观创作（章节内容），全程AI辅助。

### 🌟 核心功能

- **🤖 自动化写作管道**：持续的"生成 → 验证 → 改进"循环确保内容质量
- **📚 分层规划系统**：系统根据故事进展自动决定生成新卷、情节弧线或章节
- **🧠 记忆织网技术**：复杂的记忆系统在数百万字的长篇小说中保持故事一致性
- **🎭 模块化智能体架构**：专门的AI智能体负责创作过程中的特定任务
- **🎨 统一创作工作台**：无缝的五阶段创作流程界面
- **🔍 一键拆书分析**：智能分析现有小说，提取创作要素

## ✨ 最新功能特性

### 🎨 统一创作工作台
- **三栏式布局**：左侧导航 + 中央工作区 + 右侧AI助手的统一界面设计
- **无缝切换**：所有功能在同一界面中完成，消除页面跳转
- **五阶段创作流程**：创意孵化 → 小说设计 → 章节管理 → 内容创作 → 预览导出
- **多模式编辑**：分屏模式、沉浸模式、对照模式等多种编辑体验
- **响应式设计**：支持面板折叠和自适应布局，适配不同屏幕尺寸
- **快捷键系统**：完整的键盘快捷键支持，提升创作效率

### 🔍 一键拆书功能
- **智能文本分析**：自动分析上传的网络小说，提取关键创作要素
- **多维度提取**：情节片段、角色信息、世界元素、故事大纲四大维度分析
- **标签系统**：自动为情节片段添加标签（开篇、爆笑、无厘头、色色等）
- **结构化展示**：分类展示分析结果，支持标签筛选和搜索
- **历史管理**：保存分析历史记录，支持重复查看和对比
- **学习参考**：从优秀作品中学习创作技巧和结构设计

### 🧠 智能体系统优化
- **智能体提示词优化**：优化了所有智能体的提示词，生成更加引人入胜、情感丰富的内容
- **中央记忆系统**：统一的记忆管理器，存储和检索世界状态、角色信息等
- **智能体协调器**：协调各个智能体的工作，确保信息流动和任务分配的合理性
- **质量控制系统**：自动评估和改进小说内容质量
- **集成创作管道**：从创意构思到内容改进的完整流程整合

### 🎯 智能模型选择系统
- **任务复杂度分析**：根据任务类型和上下文自动分析复杂度
- **智能模型选择**：自动选择最适合的AI模型处理不同任务
- **成本效益优化**：支持预算约束和成本效益比分析
- **性能监控**：模型使用情况跟踪和性能分析
- **可视化仪表板**：模型选择决策过程的可视化展示

### 📚 记忆持久化与反馈系统
- **记忆持久化**：将记忆状态保存到数据库，确保重启后数据不丢失
- **用户反馈整合**：分析用户反馈并整合到创作过程中
- **学习优化**：从历史反馈中生成学习要点，持续改进创作质量
- **版本管理**：自动保存历史版本，支持版本对比和回滚

### 📤 多格式导出功能
- **多种格式支持**：TXT、PDF、EPUB、DOCX等多种导出格式
- **灵活导出选项**：支持全部/已完成/自定义范围导出
- **元信息包含**：可选择包含章节大纲和作品元信息
- **格式自定义**：支持自定义格式设置和样式配置
- **批量导出**：支持批量导出多个章节或整本小说

## 🛠️ 技术栈

### 后端技术
- **Python 3.8+** + **FastAPI** - 现代化的异步Web框架
- **SQLAlchemy** + **Alembic** - 数据库ORM和迁移工具
- **SQLite/PostgreSQL** - 关系型数据库 + 向量数据库（语义搜索）
- **OpenRouter API** - 多模型AI服务接入
- **Pydantic** - 数据验证和序列化

### 前端技术
- **Next.js 14** + **React 18** - 现代化的前端框架
- **TypeScript** - 类型安全的开发体验
- **Tailwind CSS** - 实用优先的样式框架
- **Context API** - 状态管理
- **React Hook Form** - 表单处理

### 跨平台支持
- **Tauri** - 桌面应用打包
- **Capacitor** - 移动端应用支持
- **PWA** - 渐进式Web应用

### AI集成
- **多模型支持**：OpenAI GPT-4、Anthropic Claude、Google Gemini等
- **智能路由**：根据任务特性自动选择最适合的模型
- **成本优化**：智能的模型选择和使用策略

## 🏗️ 核心组件

### 1. 中央记忆管理器 (MemoryManager)
- 存储和更新世界状态信息
- 管理角色信息和关系网络
- 维护章节摘要和故事进度
- 提供上下文信息给各个智能体
- 支持记忆状态持久化到数据库

### 2. 智能体协调器 (AgentCoordinator)
- 协调各个智能体的工作流程
- 管理从创意构思到内容改进的完整流程
- 确保信息流动和任务分配的合理性
- 自动选择合适的智能体处理不同任务
- 支持并行处理和任务队列管理

### 3. 质量控制器 (QualityController)
- 评估章节和整本小说质量
- 自动改进章节内容
- 提供具体的改进建议
- 识别并修复常见问题
- 支持多维度质量评估

### 4. 智能模型选择器 (ModelSelector)
- 分析任务复杂度和上下文
- 根据任务特征选择最适合的模型
- 支持预算约束和成本控制
- 提供详细的选择理由和推荐
- 实时性能监控和优化

### 5. 用户反馈处理器 (FeedbackProcessor)
- 分析用户对章节和小说的反馈
- 从反馈历史中生成学习要点
- 将反馈整合到创作提示中
- 持续优化创作质量
- 支持多种反馈类型和格式

### 6. 拆书分析器 (BookAnalyzer)
- 智能分析上传的小说文本内容
- 提取情节片段并自动标签分类
- 识别角色信息和关系网络
- 分析世界观元素和设定
- 生成多层级故事大纲

### 7. 创作工作台 (CreativeWorkbench)
- 统一的三栏式创作界面
- 五阶段创作流程管理
- 多模式编辑器（分屏、沉浸、对照）
- 实时AI助手和智能建议
- 版本管理和自动保存

### 8. 导出管理器 (ExportManager)
- 支持多种格式导出（TXT、PDF、EPUB、DOCX）
- 灵活的导出范围选择
- 自定义格式设置和样式配置
- 元信息和大纲包含选项
- 批量导出和压缩功能

## 🚀 快速开始

按照以下说明在本地设置和运行项目。

### 📋 环境要求

- **Python 3.8+** 和 `pip`
- **Node.js 18+** 和 `npm`（或 `yarn`）
- **Git** 版本控制工具

### ⚙️ 后端设置

1. **克隆项目并进入后端目录：**
   ```bash
   git clone <repository-url>
   cd ai-novel-weaver/backend
   ```

2. **创建并激活虚拟环境：**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **安装Python依赖包：**
   ```bash
   pip install -r requirements.txt
   ```

4. **配置环境变量：**
   ```bash
   # 复制环境变量模板
   cp .env.example .env
   # 编辑.env文件，设置API密钥等配置
   ```

5. **运行数据库迁移：**
   ```bash
   alembic upgrade head
   ```

6. **启动后端服务器：**
   ```bash
   uvicorn app.main:app --reload
   ```
   API将在 `http://localhost:8000` 可用。

### 🎨 前端设置

1. **进入前端目录：**
   ```bash
   cd ../frontend
   ```

2. **安装Node.js依赖包：**
   ```bash
   npm install
   # 或使用 yarn
   yarn install
   ```

3. **启动前端开发服务器：**
   ```bash
   npm run dev
   # 或使用 yarn
   yarn dev
   ```
   Web应用将在 `http://localhost:3000` 可用。

### 🔧 配置说明

#### 环境变量配置
在 `backend/.env` 文件中配置以下关键变量：

```env
# AI服务配置
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# 数据库配置
DATABASE_URL=sqlite:///./novels.db
# 生产环境使用 PostgreSQL
# DATABASE_URL=postgresql://user:password@localhost/dbname

# Redis配置（可选，用于缓存）
REDIS_URL=redis://localhost:6379

# 应用配置
DEBUG=true
LOG_LEVEL=INFO
```

#### 模型配置
在 `backend/model_config.json` 中配置不同任务类型使用的模型：

```json
{
  "creative_writing": "anthropic/claude-3-sonnet-20240229",
  "plot_development": "openai/gpt-4o",
  "character_development": "anthropic/claude-3-haiku-20240307",
  "dialogue": "openai/gpt-4o-mini",
  "world_building": "google/gemini-pro-1.5",
  "editing": "openai/gpt-4o",
  "analysis": "anthropic/claude-3-opus-20240229"
}
```

## 📖 使用指南

### 🚀 统一创作工作台使用流程

#### 1. 创意孵化阶段
1. 点击左侧导航的"创意孵化"
2. 在输入框中描述您的创作想法
3. 选择小说类型和风格偏好
4. 点击"开始创意扩展"，AI将帮您生成完整的故事框架

#### 2. 小说设计阶段
1. 切换到"小说设计"阶段
2. 完善基本信息（书名、简介、类型等）
3. 构建世界观设定和角色系统
4. 规划情节大纲和故事结构
5. 使用右侧AI助手完善各个部分

#### 3. 章节管理阶段
1. 进入"章节管理"功能
2. 创建章节结构和批量生成章纲
3. 支持网格、列表、时间线多种视图模式
4. 跟踪创作进度和章节完成状态

#### 4. 内容创作阶段
1. 选择要编辑的章节
2. 选择合适的编辑模式（分屏/沉浸/对照）
3. 使用AI辅助生成和优化内容
4. 实时保存和版本管理

#### 5. 预览导出阶段
1. 切换到"作品预览"
2. 选择阅读模式检查整体效果
3. 导出为TXT、PDF、EPUB、DOCX等格式

### 🔍 一键拆书功能使用指南

#### 访问拆书工作台
1. 打开AI小说创作平台首页
2. 点击顶部导航栏的"🔍 一键拆书"按钮
3. 进入拆书工作台界面

#### 上传和分析小说
1. 在"上传文件"标签页中，点击文件上传区域
2. 选择要分析的TXT格式小说文件（最大10MB）
3. 确认文件信息后，点击"开始分析"按钮
4. 等待AI分析完成（通常需要几分钟时间）

#### 查看分析结果
分析完成后，在"分析结果"标签页查看：

- **情节片段分析**：带标签分类的关键情节节点
- **角色信息提取**：性格特征、能力技能、关系网络
- **世界元素识别**：势力组织、重要地点、宝物功法
- **故事大纲生成**：总纲、卷纲、章纲三级结构

#### 使用分析结果
1. 使用标签筛选和搜索功能快速定位内容
2. 参考优秀作品的结构设计和创作技巧
3. 将分析结果应用到自己的创作中
4. 在"分析历史"中管理和对比多个分析结果

### 📝 传统创作功能

#### 创建新小说
1. 点击"新建小说"按钮
2. 输入小说标题和故事概念
3. 系统自动生成故事蓝图和基础结构

#### 一键成书
1. 点击"一键成书"按钮
2. 输入创作参数和要求
3. 系统自动创建小说并生成多个章节

#### 智能模型选择
- 系统根据任务复杂度自动选择最适合的模型
- 支持手动配置模型偏好
- 提供成本控制和预算约束
- 可视化模型选择决策过程

## 🔌 API端点

### 拆书分析API
- `POST /api/v1/book-analysis/upload` - 上传小说文件
- `POST /api/v1/book-analysis/analyze` - 开始分析小说
- `GET /api/v1/book-analysis/status/{analysis_id}` - 获取分析状态
- `GET /api/v1/book-analysis/result/{analysis_id}` - 获取分析结果
- `GET /api/v1/book-analysis/list` - 获取分析历史列表

### 自动创作API
- `POST /api/v1/auto-novel/create` - 一键创建小说
- `POST /api/v1/auto-novel/generate-section` - 生成小说章节
- `POST /api/v1/auto-novel/download/{novel_id}` - 下载小说文件
- `GET /api/v1/auto-novel/quality/{novel_id}` - 分析小说质量

### 章节管理API
- `POST /api/v1/chapters/arcs/{arc_id}/chapters` - 创建新章节
- `PUT /api/v1/chapters/{chapter_id}` - 更新章节内容
- `POST /api/v1/chapters/{chapter_id}/improve` - 自动改进章节

### 小说管理API
- `GET /api/v1/novels` - 获取小说列表
- `POST /api/v1/novels` - 创建新小说
- `GET /api/v1/novels/{novel_id}` - 获取小说详情
- `PUT /api/v1/novels/{novel_id}` - 更新小说信息
- `DELETE /api/v1/novels/{novel_id}` - 删除小说

### 流水线管理API
- `POST /api/v1/pipeline/{novel_id}/start` - 启动创作流水线
- `GET /api/v1/pipeline/{novel_id}/status` - 获取流水线状态
- `POST /api/v1/pipeline/{novel_id}/stop` - 停止流水线

## 🧪 测试

### 运行功能测试
```bash
cd backend
python test_novel_features.py
```

该脚本将测试：
- 新建章节功能
- 自动生成功能
- 一键成书功能
- 任务系统功能

### 运行集成测试
```bash
cd backend
python test_integrated_pipeline.py
```

测试智能体协调器和质量控制系统的集成功能。

### API测试
使用内置的FastAPI文档进行API测试：
- 访问 `http://localhost:8000/docs` 查看Swagger UI
- 访问 `http://localhost:8000/redoc` 查看ReDoc文档

## ⚠️ 注意事项

### 基本要求
1. **API密钥**：确保设置正确的API密钥，推荐使用OpenRouter API访问多种模型
2. **数据库迁移**：添加新功能后需要运行数据库迁移
3. **成本控制**：智能模型选择和质量控制可能增加API调用，注意成本控制
4. **内存使用**：处理长篇小说时注意内存使用，建议定期清理不必要的记忆数据

### 文件和格式
5. **文件格式**：拆书功能目前仅支持TXT格式，文件大小限制为10MB
6. **编码格式**：确保上传的文件使用UTF-8编码
7. **文件命名**：避免使用特殊字符，推荐使用中文或英文字母

### 系统兼容性
8. **浏览器兼容性**：创作工作台推荐使用Chrome、Firefox、Safari、Edge等现代浏览器
9. **网络连接**：AI功能需要稳定的网络连接，离线状态下仅支持基本编辑功能
10. **设备性能**：推荐使用配置较高的设备以获得更好的使用体验

### 数据安全
11. **自动保存**：系统会自动保存创作内容，但建议定期手动导出备份
12. **版本管理**：重要修改前建议手动创建版本快照
13. **隐私保护**：上传的文件仅用于分析，不会泄露给第三方

## ⌨️ 快捷键

| 快捷键 | 功能 |
|--------|------|
| `Ctrl + S` | 保存当前内容 |
| `Ctrl + N` | 创建新章节 |
| `Ctrl + E` | 导出作品 |
| `Ctrl + F` | 搜索内容 |
| `Ctrl + Shift + A` | 切换AI助手 |
| `Ctrl + Shift + P` | 切换预览模式 |
| `ESC` | 关闭对话框 |
| `Ctrl + Z` | 撤销操作 |
| `Ctrl + Y` | 重做操作 |

## 🎯 使用建议

### 新手作者
1. 从创意孵化器开始，让AI帮助扩展想法
2. 使用小说设计中心建立完整框架
3. 逐步完善章节内容，不要追求一次完美
4. 多使用拆书功能学习优秀作品

### 经验作者
1. 直接进入内容创作阶段
2. 利用AI辅助优化现有内容
3. 使用批量操作提高效率
4. 充分利用质量控制系统

### 团队协作
1. 使用导出功能分享作品
2. 利用版本管理跟踪修改
3. 通过AI建议保持风格一致
4. 定期备份和同步数据

## 🆘 故障排除

### 常见问题

**Q: 如何恢复意外删除的内容？**
A: 系统自动保存历史版本，可在修改历史中找回。如果无法找回，请检查导出的备份文件。

**Q: AI助手不响应怎么办？**
A: 检查网络连接和API密钥配置，或刷新页面重试。如果问题持续，请查看控制台错误信息。

**Q: 如何备份我的作品？**
A: 使用导出功能定期导出作品到本地，支持多种格式。建议设置自动备份计划。

**Q: 可以同时编辑多个小说吗？**
A: 当前版本支持单小说编辑，多小说支持在开发中。可以通过导出/导入功能切换项目。

**Q: 拆书分析失败怎么办？**
A: 检查文件格式是否为TXT，文件大小是否超过10MB，文件编码是否为UTF-8。

**Q: 如何提高AI生成内容的质量？**
A: 提供更详细的上下文信息，使用质量控制功能，适当调整模型选择策略。

### 技术支持

如遇到技术问题，请：
1. 查看系统日志获取详细错误信息
2. 检查环境配置和依赖安装
3. 参考GitHub Issues或提交新问题
4. 联系开发团队获取支持

## 🔄 更新日志

### v1.0.0 (当前版本)
- ✅ 统一创作工作台
- ✅ AI辅助创作功能
- ✅ 一键拆书分析
- ✅ 多模式编辑器
- ✅ 可视化管理
- ✅ 多格式导出
- ✅ 快捷键系统
- ✅ 智能体协调系统
- ✅ 质量控制系统
- ✅ 记忆持久化

### 计划功能
- 🔄 多小说项目管理
- 🔄 团队协作功能
- 🔄 云端同步
- 🔄 移动端APP
- 🔄 语音输入
- 🔄 更多AI模型选择
- 🔄 实时协作编辑
- 🔄 智能推荐系统

## 🤝 贡献

我们欢迎所有形式的贡献！

### 如何贡献

1. **Fork** 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 **Pull Request**

### 贡献指南

- 遵循现有的代码风格和约定
- 为新功能添加适当的测试
- 更新相关文档
- 确保所有测试通过
- 提供清晰的提交信息

### 报告问题

如果您发现了bug或有功能建议，请：
1. 检查是否已有相关Issue
2. 使用Issue模板创建新问题
3. 提供详细的重现步骤
4. 包含系统环境信息

## 📄 许可证

本项目采用 MIT 许可证。详情请参阅 [LICENSE](https://github.com/wynnforthework/ai-novel-weaver/blob/main/LICENSE) 文件。

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者和用户！

特别感谢：
- OpenAI、Anthropic、Google 等AI服务提供商
- FastAPI、Next.js、React 等开源框架
- 所有测试用户和反馈提供者

## 📞 联系我们

- **项目主页**: [GitHub Repository](https://github.com/your-username/ai-novel-weaver)
- **问题反馈**: [GitHub Issues](https://github.com/your-username/ai-novel-weaver/issues)
- **讨论交流**: [GitHub Discussions](https://github.com/your-username/ai-novel-weaver/discussions)

related:
  - methods/QUICK_START.md
---

**开始您的AI辅助创作之旅吧！** 🚀✍️📚

> 让AI成为您创作路上的最佳伙伴，一起编织出精彩的故事世界！
