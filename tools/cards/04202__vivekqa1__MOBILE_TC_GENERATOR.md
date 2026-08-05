---
id: tool-04202
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 需API密钥, 英文文档, 改稿润色]
title: MOBILE_TC_GENERATOR
summary: 润色/改写/扩写等通用文本处理
source: https://github.com/vivekqa1/mobile_tc_generator
created: 2026-07-18
updated: 2026-07-18
no: 4202
category: 十、其他 AI 写作 / 文本工具 库
repo: vivekqa1/MOBILE_TC_GENERATOR
stars: 1
url: https://github.com/vivekqa1/mobile_tc_generator
tier: "B"
use_case: "润色/改写/扩写等通用文本处理"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# vivekqa1/MOBILE_TC_GENERATOR

- **分类**：十、其他 AI 写作 / 文本工具 库
- **链接**：https://github.com/vivekqa1/mobile_tc_generator
- **Stars**：1
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：An intelligent **test case generator** for mobile applications that automatically creates test cases from Jira stories using Claude AI and executes them with WebdriverIO.
- **本地描述**：An intelligent **test case generator** for mobile applications that automatically creates test cases from Jira stories using Claude AI and executes them with WebdriverIO.
- **拉取时间**：2026-07-24 00:04:50

---

# 📱 Mobile TC Generator

An intelligent **test case generator** for mobile applications that automatically creates test cases from Jira stories using Claude AI and executes them with WebdriverIO.

## ✨ Features

- 🤖 **AI-Powered Test Generation** - Uses Claude to generate test cases from Jira story descriptions
- 📋 **Jira Integration** - Automatically fetches stories from your Jira board
- 📱 **Multi-Platform Support** - Generate tests for iOS and Android applications
- 🧪 **WebdriverIO Framework** - Built on industry-standard mobile testing framework
- 📊 **Allure Reports** - Beautiful HTML test reports with detailed execution metrics
- 🖥️ **BDD Support** - Use Cucumber/Gherkin syntax for readable test scenarios
- ⚡ **CLI Tool** - Simple command-line interface for test generation and execution
- 🔄 **Page Object Model** - Organized test structure following best practices

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm
- Jira account with API access
- Claude API key (Anthropic)
- Appium server running (for mobile app testing)
- iOS/Android device or emulator

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/MOBILE_TC_GENERATOR.git
cd MOBILE_TC_GENERATOR

# Install dependencies
npm install

# Build TypeScript
npm run build
```

### Configuration

1. **Set up environment variables** - Create a `.env` file:
```env
JIRA_HOST=https://your-jira.atlassian.net
JIRA_USERNAME=your-email@example.com
JIRA_API_TOKEN=your-jira-api-token
CLAUDE_API_KEY=your-claude-api-key
```

2. **Update device capabilities** - Edit `capabilities.json`:
```json
{
  "ios_simulator": {
    "appium:app": "/path/to/your/app.ipa",
    "appium:deviceName": "iPhone 16 Pro",
    "appium:platformVersion": "18.0",
    "appium:automationName": "XCUITest"
  }
}
```

### Usage

#### Generate test cases from Jira

```bash
# Generate tests for a specific Jira story
npm run generate -- generate PROJ-123

# Or use the CLI directly
node dist/cli.js generate --story PROJ-123

# Development mode with auto-reload
npm run dev
```

#### Run tests

```bash
# Execute all tests
npm run test

# Or run WebdriverIO directly
npm run wdio
```

#### View test reports

After tests execute, view the Allure report:
```bash
allure serve reports/allure-results
```

## 📁 Project Structure

```
├── src/
│   ├── cli.ts                      # CLI entry point
│   ├── generators/
│   │   └── file.generator.ts       # Test file generation
│   ├── services/
│   │   ├── config.service.ts       # Configuration management
│   │   ├── executor.service.ts     # Test execution
│   │   ├── jira.service.ts         # Jira integration
│   │   ├── orchestrator.service.ts # Main workflow orchestration
│   │   └── testGenerator.service.ts# AI-powered test generation
│   ├── prompts/
│   │   └── templates.ts            # Claude prompt templates
│   ├── types/
│   │   └── index.ts                # TypeScript types
│   └── utils/
│
├── features/
│   ├── amazon.feature              # Sample feature file
│   ├── pageobjects/                # Page Object Model classes
│   └── step-definitions/           # Step implementations
│
├── generated-tests/                # Auto-generated test files
├── reports/
│   ├── allure-report/              # HTML test report
│   └── allure-results/             # Test execution results
│
├── wdio.conf.ts                    # WebdriverIO configuration
├── capabilities.json               # Device capabilities
└── package.json                    # Project dependencies
```

## 🔄 How It Works

### Workflow

1. **User Input** - Provide a Jira story ID via CLI
2. **Jira Fetch** - Retrieve story details and requirements
3. **Config Setup** - Gather device and app configuration
4. **AI Generation** - Claude AI generates test scenarios
5. **Test Creation** - Generate feature files and step definitions
6. **Execution** - Run tests on configured device/emulator
7. **Reporting** - Generate Allure report with results

### Architecture

```
┌─────────────┐
│   CLI/User  │ Input Story ID
└──────┬──────┘
       │
       ▼
┌──────────────────────┐
│  Orchestrator        │ Controls workflow
│  (Main Brain)        │
└──┬──┬──┬──┬──────────┘
   │  │  │  │
   ▼  ▼  ▼  ▼
 Jira Config Test Generator Executor
 Service Service Service Service
   │      │      │         │
   ▼      ▼      ▼         ▼
Results: Feature files → Test Scenarios → WebdriverIO → Allure Reports
```

## 🛠️ Development

### Scripts

- `npm run build` - Compile TypeScript to JavaScript
- `npm run dev` - Run CLI in development mode
- `npm run generate` - Build and run test generator
- `npm run test` - Execute WebdriverIO tests
- `npm run wdio` - Run WebdriverIO directly

### Technologies

- **Language**: TypeScript
- **Testing Framework**: WebdriverIO
- **Mobile Automation**: Appium
- **BDD**: Cucumber/Gherkin
- **AI**: Claude API (Anthropic)
- **API Client**: Jira.js
- **Reporting**: Allure Reports
- **CLI**: Commander.js

## 📝 Example

Generate a complete test suite from a single Jira story:

```bash
npm run generate -- generate AMZ-1234
```

This will:
1. ✅ Fetch "AMZ-1234" from Jira
2. ✅ Ask for device configuration
3. ✅ Generate test scenarios using Claude
4. ✅ Create feature files and step definitions
5. ✅ Output generated tests in `generated-tests/` directory

Output structure:
```
generated-tests/
├── AMZ-1234.feature
├── AMZ-1234.steps.ts
└── AMZ-1234.page.ts
```

## 🧪 Sample Test (BDD Format)

```gherkin
Feature: Amazon Mobile App Testing

Scenario: User can search for products
  Given I am on the Amazon homepage
  When I search for "iPhone 15"
  Then I should see relevant search results
  And each result should display price and rating
```

## 📊 Sample Report

After execution, Allure generates detailed reports showing:
- Test execution timeline
- Pass/fail statistics
- Step-by-step details
- Screenshots and attachments
- Environment information
- Historical trends

## 🔐 Security

- Store sensitive credentials in `.env` file (not tracked in git)
- Never commit API keys or tokens
- Use Jira API tokens instead of passwords
- Rotate API keys regularly

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Issue: Appium server connection failed
- Ensure Appium server is running: `appium`
- Check device/emulator is started
- Verify capabilities.json has correct paths

### Issue: Jira authentication error
- Verify JIRA_HOST, JIRA_USERNAME, and JIRA_API_TOKEN in .env
- Check Jira API token has correct permissions
- Ensure user has access to the project

### Issue: Claude API errors
- Verify CLAUDE_API_KEY is valid
- Check API quota hasn't been exceeded
- Ensure network connectivity

## 📚 Documentation

- [Architecture Guide](ARCHITECTURE_MAP.md)
- [Deployment Guide](DEPLOYMENT_GUIDE.md)
- [Setup Instructions](MOBILE_TC_GENERATOR_SETUP.md)
- [Presentation Guide](PRESENTATION_GUIDE.md)

## 🎯 Roadmap

- [ ] Support for multiple test frameworks (pytest, unittest)
- [ ] Cloud device integration (BrowserStack, Sauce Labs)
- [ ] Advanced test analytics and ML-based optimization
- [ ] CI/CD pipeline templates
- [ ] Mobile performance testing
- [ ] Accessibility testing modules

## 📧 Support

For issues, questions, or suggestions, please:
- Open an [Issue](https://github.com/yourusername/MOBILE_TC_GENERATOR/issues)
- Start a [Discussion](https://github.com/yourusername/MOBILE_TC_GENERATOR/discussions)
- Contact the team

related:
  - methods/QUICK_START.md
---

**Built with ❤️ for mobile test automation**

Made with TypeScript • Powered by Claude AI • Tested with WebdriverIO • Reported by Allure
