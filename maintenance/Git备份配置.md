---
id: maintenance-git备份配置
type: guide
area: 库
status: active
tags: [Git, 备份, 异地备份, 版本控制]
title: Git 备份配置指南
summary: 配置 Git 本地版本控制与私有异地备份，确保知识库安全。
source: 内部制定
created: 2026-08-04
updated: 2026-08-04
related:
  - maintenance/灾备策略.md
  - maintenance/换电脑恢复说明书.md
---

# Git 备份配置指南

> 本指南详细说明如何配置 Git 本地版本控制与私有异地备份。
> 确保知识库在本地损坏或换电脑时可以快速恢复。

---

## 📋 目录

1. [前提条件](#前提条件)
2. [初始化 Git 仓库](#初始化-git-仓库)
3. [配置 Git 用户信息](#配置-git-用户信息)
4. [创建 .gitignore](#创建-gitignore)
5. [首次提交](#首次提交)
6. [配置异地备份](#配置异地备份)
7. [GitHub 私有仓库配置](#github-私有仓库配置)
8. [Gitee 私有仓库配置](#gitee-私有仓库配置)
9. [配置自动推送](#配置自动推送)
10. [验证备份](#验证备份)

---

## ✅ 前提条件

- [ ] 已安装 Git（[下载地址](https://git-scm.com/downloads)）
- [ ] 已安装 Python 3.8+
- [ ] 已有 GitHub 或 Gitee 账号
- [ ] 知识库目录已初始化：`e:\个人知识库\`

---

## 🚀 初始化 Git 仓库

### 步骤 1：打开 PowerShell

```powershell
# 进入知识库目录
cd e:\个人知识库
```

### 步骤 2：初始化 Git 仓库

```powershell
# 初始化 Git 仓库
git init

# 输出应显示：
# Initialized empty Git repository in e:/个人知识库/.git/
```

### 步骤 3：验证初始化

```powershell
# 检查 .git 目录是否存在
dir .git

# 检查 Git 状态
git status
```

---

## 👤 配置 Git 用户信息

```powershell
# 配置用户名
git config user.name "Your Name"

# 配置邮箱
git config user.email "your.email@example.com"

# 验证配置
git config --list
```

**注意**：这里的用户名和邮箱会记录在每次提交中，建议使用真实信息。

---

## 📝 创建 .gitignore

创建 `.gitignore` 文件，排除不需要版本控制的文件：

```powershell
# .gitignore
# 自动生成文件
reports/
tools/scripts/validation/__pycache__/
*.pyc
*.pyo

# 系统文件
.DS_Store
Thumbs.db
desktop.ini

# IDE 文件
.vscode/
.idea/
*.swp
*.swo

# 临时文件
*.tmp
*.temp
*.log
*.bak

# 大文件（>10MB）
*.zip
*.tar.gz
*.rar
*.7z

# 缓存
__pycache__/
node_modules/
```

**创建命令**：
```powershell
@"
# 自动生成文件
reports/
tools/scripts/validation/__pycache__/
*.pyc
*.pyo

# 系统文件
.DS_Store
Thumbs.db
desktop.ini

# IDE 文件
.vscode/
.idea/
*.swp
*.swo

# 临时文件
*.tmp
*.temp
*.log
*.bak

# 大文件（>10MB）
*.zip
*.tar.gz
*.rar
*.7z

# 缓存
__pycache__/
node_modules/
"@ | Out-File -FilePath .gitignore -Encoding UTF8
```

---

## 📦 首次提交

```powershell
# 添加所有文件
git add -A

# 查看状态
git status

# 提交
git commit -m "feat: 初始化知识库仓库"
```

**Commit Message 规范**：
- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `chore:` 构建/工具变更

---

## 🌐 配置异地备份

### 选择异地备份方案

| 方案 | 优点 | 缺点 | 推荐度 |
|---|---|---|---|
| GitHub 私有仓库 | 稳定、速度快、集成好 | 需要科学上网 | ⭐⭐⭐⭐⭐ |
| Gitee 私有仓库 | 国内速度快、免费 | 偶尔不稳定 | ⭐⭐⭐⭐ |
| 自建 Git 服务器 | 完全可控 | 需要服务器 | ⭐⭐⭐ |

**推荐方案**：GitHub 私有仓库（最稳定）

---

## 🐙 GitHub 私有仓库配置

### 步骤 1：创建私有仓库

1. 登录 [GitHub](https://github.com/)
2. 点击右上角 `+` -> `New repository`
3. 填写仓库信息：
   - Repository name: `private-knowledge-base`
   - Description: `个人知识库私有备份`
   - 选择 `Private`
   - 勾选 `Add a README file`（可选）
4. 点击 `Create repository`

### 步骤 2：获取远程仓库地址

```powershell
# SSH 方式（推荐）
git@github.com:yourname/private-knowledge-base.git

# HTTPS 方式
https://github.com/yourname/private-knowledge-base.git
```

### 步骤 3：添加远程仓库

```powershell
# 添加远程仓库
git remote add origin git@github.com:yourname/private-knowledge-base.git

# 验证远程仓库
git remote -v

# 输出应显示：
# origin  git@github.com:yourname/private-knowledge-base.git (fetch)
# origin  git@github.com:yourname/private-knowledge-base.git (push)
```

### 步骤 4：推送代码

```powershell
# 重命名主分支为 main
git branch -M main

# 推送代码
git push -u origin main

# 输出应显示：
# Enumerating objects: 100, done.
# Counting objects: 100% (100/100), done.
# Writing objects: 100% (100/100), 10.23 MiB | 2.00 MiB/s, done.
# Total 100 (delta 10), reused 0 (delta 0)
# To github.com:yourname/private-knowledge-base.git
#  * [new branch]      main -> main
```

---

## 🟢 Gitee 私有仓库配置

### 步骤 1：创建私有仓库

1. 登录 [Gitee](https://gitee.com/)
2. 点击右上角 `+` -> `新建仓库`
3. 填写仓库信息：
   - 仓库名称: `private-knowledge-base`
   - 仓库介绍: `个人知识库私有备份`
   - 选择 `私有`
   - 勾选 `使用Readme文件初始化`（可选）
4. 点击 `创建`

### 步骤 2：获取远程仓库地址

```powershell
# SSH 方式
git@gitee.com:yourname/private-knowledge-base.git

# HTTPS 方式
https://gitee.com/yourname/private-knowledge-base.git
```

### 步骤 3：添加远程仓库

```powershell
git remote add origin git@gitee.com:yourname/private-knowledge-base.git
git branch -M main
git push -u origin main
```

---

## ⏰ 配置自动推送

### 方案 1：Windows 任务计划（推荐）

```powershell
# 创建每日自动推送任务
schtasks /create /tn "GitAutoPush" /tr "cd e:\个人知识库 && git add -A && git commit -m 'auto: daily backup' && git push" /sc daily /st 23:00 /f

# 查看任务
schtasks /query /tn "GitAutoPush"

# 删除任务（如需）
schtasks /delete /tn "GitAutoPush" /f
```

**说明**：
- `/tn` 任务名称
- `/tr` 要执行的命令
- `/sc` 计划频率（daily=每日）
- `/st` 开始时间（23:00）
- `/f` 强制覆盖已有任务

### 方案 2：Git Hook（提交时自动推送）

创建 `.git/hooks/post-commit`：

```bash
#!/bin/sh
git push origin main
```

设置执行权限：
```powershell
git config core.hooksPath .git/hooks
```

### 方案 3：VS Code 任务（适合开发者）

在 `.vscode/tasks.json` 中添加：

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Git Auto Push",
      "type": "shell",
      "command": "cd e:\\个人知识库 && git add -A && git commit -m 'auto: backup' && git push",
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "problemMatcher": []
    }
  ]
}
```

---

## ✅ 验证备份

### 验证本地备份

```powershell
# 检查 Git 日志
git log --oneline

# 查看最近提交
git log -5

# 查看文件历史
git log --all --full-history -- "**/*.md"
```

### 验证异地备份

1. 访问 GitHub/Gitee 仓库页面
2. 确认文件列表与本地一致
3. 确认提交历史与本地一致

### 测试恢复

```powershell
# 创建临时目录
mkdir C:\tmp\backup-test
cd C:\tmp\backup-test

# 克隆仓库
git clone git@github.com:yourname/private-knowledge-base.git test-restore

# 验证文件
dir test-restore

# 清理
cd e:\个人知识库
Remove-Item -Recurse -Force C:\tmp\backup-test
```

---

## 📋 备份配置检查清单

- [ ] Git 仓库已初始化
- [ ] Git 用户信息已配置
- [ ] .gitignore 已创建
- [ ] 首次提交已完成
- [ ] 异地备份仓库已创建
- [ ] 远程仓库已配置
- [ ] 代码已推送到远程
- [ ] 自动推送已配置
- [ ] 备份已验证
- [ ] 恢复测试已通过

---

## 🔧 常见问题

### Q1: Git 命令不可用

**问题**：`git: command not found`

**解决**：
1. 下载 Git：[https://git-scm.com/downloads](https://git-scm.com/downloads)
2. 安装时勾选 "Add to PATH"
3. 重启 PowerShell

### Q2: SSH 密钥配置

**问题**：无法通过 SSH 推送

**解决**：
1. 生成 SSH 密钥：
   ```powershell
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```
2. 添加 SSH 密钥到 GitHub/Gitee
3. 测试连接：
   ```powershell
   ssh -T git@github.com
   ```

### Q3: 大文件推送失败

**问题**：推送大文件超时

**解决**：
1. 检查 `.gitignore` 是否排除大文件
2. 使用 Git LFS：
   ```powershell
   git lfs install
   git lfs track "*.zip"
   git lfs track "*.tar.gz"
   ```

---

## 📚 参考文档

- [Git 官方文档](https://git-scm.com/doc)
- [GitHub 文档](https://docs.github.com/)
- [Gitee 文档](https://gitee.com/help)
- [灾备策略](灾备策略.md)

---

> 本文件是 Git 备份配置的完整指南。
> 按照本指南配置后，知识库将具备完整的本地版本控制和异地备份能力。
> 最后更新时间：2026-08-04
