---
id: tool-01606
type: tool
area: 库
status: active
tags: [Java, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: storybook-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/vishtechie07/storybook-generator
created: 2026-07-18
updated: 2026-07-18
no: 1606
category: 二、网文 / 长篇 AI 写作系统 库
repo: vishtechie07/storybook-generator
stars: 1
url: https://github.com/vishtechie07/storybook-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# vishtechie07/storybook-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/vishtechie07/storybook-generator
- **Stars**：1
- **语言**：Java
- **License**：None
- **Topics**：ai-images, generative-ai, java, openai, storytelling
- **GitHub 描述**：Java-based web application for generating AI stories with images using OpenAI API
- **本地描述**：Java-based web application for generating AI stories with images using OpenAI API
- **拉取时间**：2026-07-23 23:25:53

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Story Book Generator

A Java-based web application that generates interactive children's stories with AI-generated images and PDF export functionality. This application combines OpenAI's GPT-3.5-turbo for story generation and DALL-E 3 for image creation, providing a complete story creation and management system.

## Features

### 🎨 Story Generation
- **AI-Powered Stories**: Generate engaging children's stories using OpenAI's GPT-3.5-turbo
- **Image Integration**: Automatically create accompanying images using DALL-E 3
- **Custom Prompts**: Input your own story ideas and watch them come to life
- **Real-time Processing**: Fast story and image generation with progress feedback

### 📱 Web Interface
- **Modern UI**: Beautiful, responsive web interface built with Tailwind CSS
- **User-Friendly**: Simple form-based input for story prompts
- **API Key Management**: Secure API key input (never stored server-side)
- **Error Handling**: Comprehensive error handling with user-friendly messages

### 📚 Story Management
- **Browser Session Storage**: Stories are automatically saved to your browser's localStorage
- **Story History**: View all generated stories in a clean, organized interface
- **Story Previews**: See story summaries and metadata at a glance
- **Easy Management**: Remove individual stories or clear entire history

### 📄 PDF Export
- **Professional PDFs**: Generate high-quality PDF documents with embedded images
- **Proper Formatting**: Clean typography with proper spacing and layout
- **Image Integration**: Images are properly scaled and embedded in the PDF
- **Download Ready**: One-click PDF download functionality

### 🔧 Technical Features
- **MCP Server**: Implements Model Context Protocol for tool integration
- **Standalone Application**: Single JAR file with all dependencies included
- **Cross-Platform**: Runs on Windows, macOS, and Linux
- **Memory Efficient**: Optimized for performance with proper resource management

## Requirements

- **Java 11 or higher**
- **OpenAI API Key** (get one at [OpenAI Platform](https://platform.openai.com/))
- **Internet Connection** (for API calls to OpenAI)

## Installation

1. **Clone or Download** this repository
2. **Build the application**:
   ```bash
   mvn clean package
   ```
3. **Run the server**:
   ```bash
   java -jar target/storybook-generator-1.0.0.jar
   ```

## Usage

### Starting the Application

1. **Run the JAR file**:
   ```bash
   java -jar target/storybook-generator-1.0.0.jar
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:8080
   ```

### Creating Stories

1. **Enter your OpenAI API key** in the provided field
2. **Write a story prompt** (e.g., "A brave little mouse who wants to be a knight")
3. **Click "Generate Story with AI"**
4. **Wait for processing** - the system will:
   - Generate the story text using GPT-3.5-turbo
   - Create images using DALL-E 3
   - Display the complete story with embedded images

### Managing Stories

1. **View Story History**: Click "View Story History" to see all your generated stories
2. **Download PDFs**: Click "Download PDF" on any story to generate a PDF version
3. **Remove Stories**: Use the "Remove" button to delete stories from your history
4. **Clear History**: Use "Clear History" to remove all stories at once

### PDF Generation

- **Automatic Saving**: Stories are automatically saved to your browser's session storage
- **High Quality**: PDFs include properly formatted text and embedded images
- **Professional Layout**: Clean typography with proper margins and spacing
- **Multiple Images**: Supports stories with multiple images

## Architecture

### Components

- **WebUIServer**: Main HTTP server providing the web interface
- **StoryGenerator**: Core logic for story and image generation
- **PDF Generator**: Creates PDF documents with embedded images
- **Browser Storage**: Client-side story management using localStorage

### API Integration

- **OpenAI Chat Completions**: For story text generation
- **OpenAI Image Generation**: For DALL-E 3 image creation
- **Secure Communication**: All API calls use HTTPS with proper authentication

### Data Flow

1. User enters prompt and API key
2. Server generates story using OpenAI GPT-3.5-turbo
3. Server extracts image prompts from story
4. Server generates images using DALL-E 3
5. Server displays story with embedded images
6. Story is saved to browser localStorage
7. User can download PDF or manage stories

## Configuration

### Environment Variables
No environment variables are required. All configuration is done through the web interface.

### API Keys
- OpenAI API keys are entered through the web interface
- Keys are used only for the current session
- Keys are never stored on the server

### Port Configuration
- Default port: 8080
- Can be changed by modifying the `PORT` constant in `WebUIServer.java`

## Troubleshooting

### Common Issues

**"Story generation failed"**
- Check your OpenAI API key
- Ensure you have sufficient API credits
- Verify internet connection

**"Image generation failed"**
- DALL-E 3 may reject certain prompts for safety reasons
- Try rephrasing your story prompt
- Some prompts may be filtered by OpenAI's safety system

**"PDF download not working"**
- Ensure pop-ups are allowed for the site
- Check browser download settings
- Try a different browser if issues persist

**"Server won't start"**
- Ensure Java 11+ is installed
- Check if port 8080 is available
- Run with `java -version` to verify Java installation

### Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge

## Development

### Building from Source

```bash
# Clone the repository
git clone <repository-url>
cd storybook-generator-java-agent

# Build the project
mvn clean package

# Run the application
java -jar target/storybook-generator-1.0.0.jar
```

### Project Structure

```
src/main/java/com/example/mcp/
├── WebUIServer.java          # Main web server and UI
├── MCPServer.java           # MCP protocol implementation
└── StoryGenerator.java      # Story and image generation logic
```

### Dependencies

- **Gson**: JSON processing for API communication
- **iText PDF**: PDF generation and document creation
- **Java HTTP Server**: Built-in HTTP server functionality

## License

This project is provided as-is for educational and personal use.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your OpenAI API key and credits
3. Ensure Java 11+ is properly installed
4. Check browser console for JavaScript errors

## Version History

- **v1.0.0**: Initial release with story generation, image creation, PDF export, and browser session storage
