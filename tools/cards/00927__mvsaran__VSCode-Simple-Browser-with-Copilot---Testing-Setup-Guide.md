---
id: tool-00927
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: VSCode-Simple-Browser-with-Copilot---Testing-Setup-Guide
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/mvsaran/vscode-simple-browser-with-copilot---testing-setup-guide
created: 2026-07-18
updated: 2026-07-18
no: 927
category: 二、网文 / 长篇 AI 写作系统 库
repo: mvsaran/VSCode-Simple-Browser-with-Copilot---Testing-Setup-Guide
stars: 0
url: https://github.com/mvsaran/vscode-simple-browser-with-copilot---testing-setup-guide
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# mvsaran/VSCode-Simple-Browser-with-Copilot---Testing-Setup-Guide

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mvsaran/vscode-simple-browser-with-copilot---testing-setup-guide
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：This guide demonstrates how to use VSCode's built-in Simple Browser feature combined with GitHub Copilot to automatically generate test automation scripts. This workflow eliminates the need to switch between your browser and spec files when writing locators.
- **本地描述**：This guide demonstrates how to use VSCode's built-in Simple Browser feature combined with GitHub Copilot to automatically generate test automation scripts. This workflow eliminates the need to switch between your browser and spec files when writing locators.
- **拉取时间**：2026-07-23 23:06:06

---

# 🚀 VSCode Simple Browser with Copilot - Testing Setup Guide

[![Made with VSCode](https://img.shields.io/badge/Made%20with-VSCode-1f425f.svg)](https://code.visualstudio.com/)
[![GitHub Copilot](https://img.shields.io/badge/AI-GitHub%20Copilot-blue)](https://github.com/features/copilot)
[![Cypress](https://img.shields.io/badge/Testing-Cypress-17202C?logo=cypress)](https://www.cypress.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Author:** 👨‍💻 Saran Kumar

---

## 📋 Overview

This guide demonstrates how to use VSCode's built-in Simple Browser feature combined with GitHub Copilot to automatically generate test automation scripts. This workflow eliminates the need to switch between your browser and spec files when writing locators.

## 🌐 What is Simple Browser?

Simple Browser is an integrated web browser within Visual Studio Code that allows you to:
- 🔍 Browse websites directly in VSCode
- 🎯 Inspect and select DOM elements visually
- 📸 Automatically capture element locators and screenshots
- 🤖 Generate test scripts using Copilot AI

## ✅ Prerequisites

- 💻 Visual Studio Code (latest version)
- 🤖 GitHub Copilot extension installed and activated
- 📚 Basic knowledge of test automation (Playwright, Cypress, Selenium, etc.)

---

## 🛠️ Setup Instructions

### 📍 Step 1: Open Simple Browser

1. Press `Ctrl + Shift + P` (Windows/Linux) or `Cmd + Shift + P` (Mac) to open the Command Palette
2. Type "Simple Browser"
3. Select **"Simple Browser: Show"** from the dropdown list
4. Enter your target URL (e.g., `https://flipkart.com`)
5. Press Enter

✨ The Simple Browser window will open within VSCode displaying your website.

### 🎯 Step 2: Element Selection Options

Once the URL loads, you'll see a toolbar with the following options:

#### **🔘 Select an Element (Single Selection)**
- Click the dropdown next to the "Start" button
- Select **"Select an Element"**
- Click on any element in the Simple Browser
- The element's locator and screenshot are automatically added to Copilot Chat

#### **🔄 Continuous Selection (Multiple Elements)**
- Click the dropdown next to the "Start" button
- Select **"Continuous Selection"**
- Click multiple elements sequentially
- Each element's locator and screenshot is captured
- Perfect for selecting multiple elements in a single workflow

### 🤖 Step 3: Generate Test Scripts with Copilot

After selecting your elements:

1. Open Copilot Chat (if not already open)
2. You'll see the captured element locators and screenshots automatically added
3. Provide a clear prompt describing your test scenario

#### 💡 Example Prompt:
```
Generate a Cypress script that:
1. Opens URL https://flipkart.com
2. Searches for "Mobiles" in the search box
3. Clicks on the search button
4. Analyzes the attached screenshots for locators
```

4. Copilot will generate a complete test script based on your captured elements
5. Review and refine the generated code as needed

---

## 🎬 Example Workflow

### 🛒 Scenario: Flipkart Product Search Test

**Step-by-step Process:**

1. 🌐 Open Simple Browser with `https://flipkart.com`
2. 🔄 Enable "Continuous Selection" mode
3. 👆 Click on:
   - Search input field
   - Search button
4. 💬 In Copilot Chat, enter:
   ```
   Generate a Cypress test script that:
   - Navigates to Flipkart
   - Enters "Mobiles" in the search box
   - Clicks the search button
   - Waits for results to load
   Use the attached element locators from the screenshots
   ```

5. ✨ Copilot generates the script with proper selectors:

```javascript
describe('Flipkart Search', () => {
  it('should search for Mobiles', () => {
    cy.visit('https://flipkart.com');
    
    // Close login popup if present
    cy.get('body').then($body => {
      if ($body.find('button._2KpZ6l._2doB4z').length) {
        cy.get('button._2KpZ6l._2doB4z').click();
      }
    });
    
    // Type "Mobiles" in the search box
    cy.get('input[title="Search for Products, Brands and More"]').type('Mobiles');
    
    // Click the search button
    cy.get('button[type="submit"]').click();
  });
});
```

**🎯 Key Features of Generated Script:**
- ✅ Automatically handles the login popup using conditional logic
- ✅ Uses descriptive selectors based on captured elements
- ✅ Includes clear comments for each action
- ✅ Ready to run with minimal modifications

---

## ⚠️ Known Limitations

### 🚧 Page Navigation Issue

**Important Note:** The Simple Browser has a limitation where page navigation doesn't always work as expected.

**📌 Observed Behavior:**
- When you search for "Mobiles" and click the search button in Simple Browser
- The page does **not** navigate to the search results page within Simple Browser
- The URL remains at the homepage

**💡 Workaround:**
1. Use Simple Browser for **element selection only**
2. For testing actual page navigation and interactions:
   - Open the URL in a regular browser
   - Use the generated script in your actual test environment
   - The script will work correctly when executed by your testing framework

**🔍 Why This Happens:**
Simple Browser is designed primarily for element inspection and static page viewing, not full browser simulation with JavaScript execution and redirects.

---

## 🎁 Benefits of This Approach

### ✅ Advantages

| Feature | Benefit |
|---------|---------|
| 🔄 **No Context Switching** | Stay within VSCode throughout your workflow |
| 👁️ **Visual Element Selection** | Click elements directly instead of inspecting HTML |
| 🎯 **Automatic Locator Generation** | No manual CSS selector or XPath writing |
| 📸 **Screenshot Documentation** | Visual reference attached automatically |
| 🤖 **AI-Powered Script Generation** | Copilot creates complete test scripts |
| ⚡ **Faster Test Development** | Reduce time spent on boilerplate code |

### ⚠️ Considerations

| Limitation | Impact |
|------------|--------|
| 🚫 **Navigation Limitations** | Cannot test multi-page flows in Simple Browser |
| ⚙️ **JavaScript Execution** | Some dynamic content may not load properly |
| ✔️ **Verification Needed** | Always test generated scripts in actual browsers |
| 🔍 **Locator Validation** | Review and adjust locators for reliability |

---

## 🏆 Best Practices

### 1️⃣ Use Descriptive Prompts
```
❌ Bad: "Generate test for this"
✅ Good: "Generate a Cypress test that validates login with valid credentials using the selected elements"
```

### 2️⃣ Capture All Necessary Elements
- ✅ Select all interactive elements in your test flow
- ✅ Include assertions elements (success messages, error alerts)
- ✅ Capture elements for both positive and negative scenarios

### 3️⃣ Refine Generated Locators
Review Copilot's suggested locators and prefer:
- 🥇 Data-testid attributes (most reliable)
- 🥈 Unique IDs
- 🥉 Specific class combinations
- ❌ Avoid: Generic classes, index-based selections

### 4️⃣ Test in Real Browser
Always validate your generated scripts in actual browser automation:
```bash
# Cypress
npx cypress open
# or
npx cypress run

# Playwright
npx playwright test

# Selenium
pytest test_file.py
```

---

## 🧪 Supported Testing Frameworks

This workflow generates scripts compatible with:

| Framework | Language | Status |
|-----------|----------|--------|
| 🌲 **Cypress** | JavaScript/TypeScript | ✅ Primary |
| 🎭 **Playwright** | JavaScript/TypeScript | ✅ Supported |
| 🔧 **Selenium** | Python, Java, JS, C# | ✅ Supported |
| 🌐 **WebdriverIO** | JavaScript/TypeScript | ✅ Supported |
| 🎪 **Puppeteer** | JavaScript/TypeScript | ✅ Supported |

💡 Simply specify your preferred framework in the Copilot prompt.

---

## 🔧 Troubleshooting

### ❓ Simple Browser Won't Open
- ⬆️ Ensure VSCode is updated to the latest version
- 🔄 Try restarting VSCode
- 🔍 Check if any extensions are conflicting

### ❓ Elements Not Selectable
- 🔍 Some elements with overlays may be difficult to select
- 🔎 Try zooming in/out in Simple Browser
- 🛠️ Use browser DevTools for complex selections

### ❓ Copilot Not Generating Code
- ✅ Verify GitHub Copilot subscription is active
- ⚙️ Check that Copilot Chat is enabled
- 💬 Try rephrasing your prompt with more details

### ❓ Generated Scripts Don't Work
- 🔍 Verify locators in actual browser DevTools
- ⚠️ Check for dynamic IDs or classes
- 🎯 Use more robust selector strategies (data-testid, aria-labels)

---

## 📚 Additional Resources

- 📖 [VSCode Simple Browser Documentation](https://code.visualstudio.com/docs/editor/vscode-web)
- 🤖 [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- 🌲 [Cypress Documentation](https://docs.cypress.io)
- 🎭 [Playwright Documentation](https://playwright.dev)

---

## 👨‍💻 Author

**Saran Kumar**

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">

### ⭐ If you found this guide helpful, please star it!

**Made with ❤️ for the Testing Community**

[![VSCode](https://img.shields.io/badge/VSCode-007ACC?logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Cypress](https://img.shields.io/badge/Cypress-17202C?logo=cypress&logoColor=white)](https://www.cypress.io/)
[![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-000000?logo=github&logoColor=white)](https://github.com/features/copilot)

</div>
