---
id: tool-01048
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: file-operations-mcp
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/huseyinkaracif/file-operations-mcp
created: 2026-07-18
updated: 2026-07-18
no: 1048
category: 二、网文 / 长篇 AI 写作系统 库
repo: huseyinkaracif/file-operations-mcp
stars: 0
url: https://github.com/huseyinkaracif/file-operations-mcp
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# huseyinkaracif/file-operations-mcp

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/huseyinkaracif/file-operations-mcp
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A Model Context Protocol (MCP) server that provides secure file operation tools for AI assistants. Supports reading, writing, listing files and directories with built-in security features.
- **本地描述**：A Model Context Protocol (MCP) server that provides secure file operation tools for AI assistants. Supports reading, writing, listing files and directories with built-in security features.
- **拉取时间**：2026-07-23 23:09:33

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# File Operations MCP Server

A Model Context Protocol (MCP) server that provides secure file operation tools for AI assistants. This server allows safe reading, writing, and listing of files within configured directories.

## Features

- **Read Files**: Read file contents with customizable encoding
- **Write Files**: Write content to files with encoding options
- **List Directories**: Browse directory contents with optional hidden file inclusion
- **File Existence Check**: Verify if files or directories exist
- **Security**: Path validation to prevent directory traversal attacks
- **TypeScript**: Fully typed for better development experience

## Available Tools

### `read_file`
Read the contents of a file.

**Parameters:**
- `path` (string, required): Path to the file to read
- `encoding` (string, optional): File encoding (default: 'utf8')

### `write_file`
Write content to a file.

**Parameters:**
- `path` (string, required): Path to the file to write
- `content` (string, required): Content to write to the file
- `encoding` (string, optional): File encoding (default: 'utf8')

### `list_directory`
List files and directories in a given path.

**Parameters:**
- `path` (string, required): Path to the directory to list
- `includeHidden` (boolean, optional): Include hidden files (default: false)

### `file_exists`
Check if a file or directory exists.

**Parameters:**
- `path` (string, required): Path to check for existence

## Installation

1. Clone or download this project
2. Install dependencies:
```bash
npm install
```

3. Build the TypeScript code:
```bash
npm run build
```

## Usage

### Running the Server Directly
```bash
npm start
```

### Development Mode
```bash
npm run dev
```

### Adding to Cursor

To use this MCP server with Cursor, add the following configuration to your MCP settings:

1. Open Cursor Settings (Cmd/Ctrl + ,)
2. Go to "Features" → "Model Context Protocol"
3. Add a new server configuration:

```json
{
  "file-operations": {
    "command": "node",
    "args": ["/absolute/path/to/file-operations-mcp/build/index.js"],
    "env": {}
  }
}
```

Or add to your `~/.cursor/mcp.json` file:

```json
{
  "mcpServers": {
    "file-operations": {
      "command": "node",
      "args": ["/absolute/path/to/file-operations-mcp/build/index.js"]
    }
  }
}
```

## Security

This server implements several security measures:

- **Path Validation**: All file paths are validated to prevent directory traversal attacks
- **Allowed Directories**: Only files within the current working directory are accessible by default
- **Safe Path Resolution**: Uses Node.js path utilities to safely resolve file paths

### Customizing Allowed Directories

To modify which directories the server can access, edit the `ALLOWED_DIRECTORIES` array in `src/tools/file-tools.ts`:

```typescript
const ALLOWED_DIRECTORIES = [
  process.cwd(), // Current working directory
  '/path/to/your/safe/directory',
  // Add more allowed directories as needed
];
```

## Example Responses

### Successful File Read
```json
{
  "success": true,
  "message": "File read successfully: /path/to/file.txt",
  "data": {
    "content": "Hello, World!",
    "path": "/path/to/file.txt"
  }
}
```

### Directory Listing
```json
{
  "success": true,
  "message": "Directory listed successfully: /path/to/directory",
  "data": {
    "files": [
      {
        "name": "example.txt",
        "path": "/path/to/directory/example.txt",
        "isDirectory": false,
        "isFile": true,
        "size": 1024,
        "lastModified": "2024-01-15T10:30:00.000Z"
      }
    ],
    "count": 1
  }
}
```

### Error Response
```json
{
  "success": false,
  "message": "Failed to read file: ENOENT: no such file or directory",
  "data": null
}
```

## Development

### Scripts
- `npm run build`: Compile TypeScript to JavaScript
- `npm start`: Run the compiled server
- `npm run dev`: Build and run in one command
- `npm run watch`: Watch for changes and recompile

### Project Structure
```
file-operations-mcp/
├── src/
│   ├── index.ts              # Main server implementation
│   ├── tools/
│   │   └── file-tools.ts     # File operation implementations
│   └── types/
│       └── index.ts          # TypeScript type definitions
├── build/                    # Compiled JavaScript (after build)
├── package.json
├── tsconfig.json
└── README.md
```

## Requirements

- Node.js >= 18.0.0
- npm or yarn package manager

## License

MIT License - see package.json for details.
by Hüseyin Karacif

## Contributing

Feel free to open issues or submit pull requests to improve this MCP server! 
