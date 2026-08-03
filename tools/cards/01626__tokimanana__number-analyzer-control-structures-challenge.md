---
id: tool-01626
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: number-analyzer-control-structures-challenge
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/tokimanana/number-analyzer-control-structures-challenge
created: 2026-07-18
updated: 2026-07-18
no: 1626
category: 二、网文 / 长篇 AI 写作系统 库
repo: tokimanana/number-analyzer-control-structures-challenge
stars: 0
url: https://github.com/tokimanana/number-analyzer-control-structures-challenge
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# tokimanana/number-analyzer-control-structures-challenge

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/tokimanana/number-analyzer-control-structures-challenge
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：javascript
- **GitHub 描述**：Mid-Level JavaScript Certification Training Chapter 1: JavaScript Fundamentals
- **本地描述**：Mid-Level JavaScript Certification Training Chapter 1: JavaScript Fundamentals
- **拉取时间**：2026-07-23 23:26:27

---

---
difficulty: 2
tags: codechallenge, training
chapter: "Chapter 1: JavaScript Fundamentals"
training: true
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Number Analyzer - Control Structures Challenge

## Challenge Description

In this challenge, you'll create a program that analyzes a list of numbers using conditionals and loops. You'll perform various calculations and generate a report based on the numbers.

Complete all tasks in `/src/main.js`.

## Requirements

1. Number List:
   - Create an array called `numbers` with the following values: 
     `[23, 54, 32, 87, 47, 15, 98, 6, 63, 41]`

2. Even/Odd Counter:
   - Use a loop to count how many even and odd numbers are in the `numbers` array
   - Log the results
   ```
   Even numbers: [count]
   Odd numbers: [count]
   ```

3. Range Classifier:
   - Use a loop and conditionals to classify each number as:
     - "Low" if it's less than 30
     - "Medium" if it's between 30 and 70 (inclusive)
     - "High" if it's above 70
   - Count how many numbers fall into each category
   - Log the results
   ```
   Low numbers: [count]
   Medium numbers: [count]
   High numbers: [count]
   ```

4. Sum and Average:
   - Calculate the sum of all numbers in the array
   - Calculate the average (mean) of the numbers
   - Round the average to two decimal places
   - Log the results
   ```
   Sum: [sum]
   Average: [average]
   ```

## What to Expect

Your output should look like this:

```
Even numbers: 4
Odd numbers: 6
Low numbers: 3
Medium numbers: 5
High numbers: 2
Sum: 466
Average: 46.60
```

> 💡 HINT: Remember to use appropriate loop structures (for or while) and conditional statements (if-else) to implement the required logic. Pay attention to the initial value, condition, and increment of your loops.
