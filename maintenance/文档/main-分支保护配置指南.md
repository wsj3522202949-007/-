---
id: main-分支保护配置
type: guide
area: 管理
status: active
tags: [CI, 分支保护, GitHub, 必需检查]
title: main 分支保护配置指南
summary: 把 CI 状态检查设为 main 合并前置条件，未过线代码无法合入。
created: 2026-08-08
updated: 2026-08-08
---

# main 分支保护配置指南

> 目标：**未通过 CI 的代码无法合并进 main**。GitHub 支持把状态检查设为
> 合并前置条件（branch protection rule）。配置一次后永久生效，
> 这是"CI 必须全绿"从纸面约定变成平台强制的关键一步。

## 一、必需检查清单（6 项）

ci.yml 使用双平台矩阵，每个矩阵变体是独立的状态检查。需要在
分支保护规则中**全部勾选**：

| 状态检查名 | 对应 job | 平台 |
|---|---|---|
| `syntax / py-compile (windows-latest)` | 语法编译 | Windows |
| `syntax / py-compile (ubuntu-latest)` | 语法编译 | Linux |
| `unit / tests (windows-latest)` | 单元测试 | Windows |
| `unit / tests (ubuntu-latest)` | 单元测试 | Linux |
| `gate / run-all (windows-latest)` | 章节门禁 | Windows |
| `gate / run-all (ubuntu-latest)` | 章节门禁 | Linux |

> 勾选前这些检查名必须至少真实出现一次（任意 PR/push 跑过），
> 否则 GitHub 下拉列表里找不到。若列表为空，先 push 一次触发 CI。

## 二、配置步骤（网页操作，约 2 分钟）

1. 打开仓库页面 → **Settings** → **Branches**
2. 在 **Branch protection rules** 点 **Add rule**
3. Branch name pattern 填 `main`
4. 勾选 **Require a pull request before merging**
   - 可选：Require approvals = 1（个人仓库可不开）
5. 勾选 **Require status checks to pass before merging**
   - 打开 **Require branches to be up to date before merging**
   - 在搜索框逐个选中上表 6 项（名称含括号，注意别漏）
6. 勾选 **Do not allow bypassing the above settings**（可选，管理员也走 CI）
7. 点 **Create** 保存

## 三、验证配置生效

```powershell
# 用 API 查询分支保护规则（需要 GH_TOKEN 或有权限的 token）
gh api repos/wsj3522202949-007/-/branches/main/protection
# 期望输出包含 required_status_checks.contexts 且含 6 项
```

无 gh 时可在网页 Settings → Branches 确认规则已列出。

## 四、配套约定（写入仓库记忆）

- 所有修改必须走 PR，禁止直接 push main（保护规则强制）
- PR 标题用中文描述改动；CI 全绿后由 PR 作者合并
- 若 CI 红灯，先修门禁再合并，禁止"先合后补"
- 紧急修复走 `--no-verify` 会绕过钩子但**无法绕过远端 CI 保护**，
  所以分支保护是钩子之上的第二道强制

## 五、与本地门禁的关系（三层防线）

| 层 | 机制 | 强制力 |
|---|---|---|
| 1 | pre-commit 钩子（本地） | 本机生效，可 --no-verify 绕过 |
| 2 | CI 状态检查（远端，本章配置） | 平台强制，无法绕过 |
| 3 | 恢复演练 + 季度验证（nightly） | 定期验证三层仍有效 |

> 三层缺一不可：钩子挡本地低级错误，CI 挡漏网，演练保证灾备可恢复。
