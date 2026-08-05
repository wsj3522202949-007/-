---
id: tool-00015
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: IHeartFiction
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/sheepreaper/iheartfiction
created: 2026-07-18
updated: 2026-07-18
no: 15
category: 二、网文 / 长篇 AI 写作系统 库
repo: SheepReaper/IHeartFiction
stars: 5
url: https://github.com/sheepreaper/iheartfiction
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# SheepReaper/IHeartFiction

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sheepreaper/iheartfiction
- **Stars**：5
- **语言**：JavaScript
- **License**：MIT
- **Topics**：aspnetcore, blazor, cqrs, docker, dotnet, dotnet-aspire, entityframeworkcore, fanfiction, fiction, keycloak, minimal-apis, opensource, postgresql, vertical-slice-architecture, writing
- **GitHub 描述**：I❤️Fiction is an ambitious open-source project to build a modern, feature-rich platform for both original and fan fiction. Built on a .NET and ASP.NET Core backend with a Blazor frontend, it aims to be a viable competitor to established platforms by focusing on a clean user experience, powerful authoring tools, and a strong community.
- **本地描述**：I❤️Fiction is an ambitious open-source project to build a modern, feature-rich platform for both original and fan fiction. Built on a .NET and ASP.NET Core backend with a Blazor frontend, it aims to be a viable competitor to established platforms by focusing on a clean user experience, powerful authoring tools, and a strong community.
- **拉取时间**：2026-07-23 22:39:18

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# I❤️Fiction

[![build](https://github.com/SheepReaper/IHeartFiction/actions/workflows/build.yml/badge.svg)](https://github.com/SheepReaper/IHeartFiction/actions/workflows/build.yml)

I❤️Fiction is an ambitious open-source project to build a modern, feature-rich platform for both original and fan fiction. Built on a .NET and ASP.NET Core backend with a Blazor frontend, it aims to be a viable competitor to established platforms by focusing on a clean user experience, powerful authoring tools, and a strong community.

## Getting Started

To get the project running locally, you'll need the following installed:

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- (Optional) [Aspire CLI](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/setup-tooling?tabs=unix%2Cwindows&pivots=dotnet-cli#-aspire-cli)

Once the prerequisites are installed, you can run the project using the .NET CLI:

```bash
dotnet run --project src/aspire/IHFiction.AppHost
```

OR (If the AppHost is set up as the default startup project)

```bash
dotnet run
```

Alternatively, you can run the project using the Aspire CLI (if you have it installed).

```bash
aspire run
```

### After the stack starts (First-time Set-up)

The Keycloak realm `fiction` is pre-configured by the realm import file. However the client secrets are not. 

1. Explore the Keycloak resource properties in the Aspire Dashboard. You should find the admin user and password for the Keycloak server.
1. Once the Keycloak service status shows healthy in the Aspire Dashboard, click the link to the Keycloak server. Once in, access the fiction realm and its clients.
1. Regenerate and copy the credential (secret) for `fiction-admin-client`.
1. The first time the Aspire Dashboard launches for you, you should be prompted to provide missing secrets. You can click this message to provide the secret you just generated.
1. (Alternatively) Use the dotnet cli to update the secret `dotnet user-secrets --project ./src/aspire/IHFiction.AppHost/ set Parameters:KeycloakAdminClientSecret <YOUR_SECRET_HERE>`
1. Repeat the last two steps for `fiction-frontend` client to set the `Parameters:KeycloakAdminClientSecret` value.

## Software Stack

The project is built on the .NET platform, embracing a modern, cloud-native architecture.

- **Backend:** ASP.NET Core
- **Framework:** ASP.NET Core using Minimal APIs for a lightweight and high-performance service layer.
- **Frontend:** Blazor Web App for a rich, interactive user experience.
- **Orchestration:** .NET Aspire to manage and compose the various services that make up the application.
- **Database:** PostgreSQL for robust and scalable data storage.
- **Data Access:** Entity Framework Core (EFCore) for object-relational mapping.
- **Async Workflows & Messaging:** WolverineFx for asynchronous command/event processing and service-domain messaging.
- **Authentication:** Keycloak for secure and flexible identity and access management.
- **Containerization:** Docker and Docker Compose for consistent development and deployment environments.

## Architecture

For a detailed explanation of the project's architecture, design philosophy, and technical decisions, please see [ARCHITECTURE.md](ARCHITECTURE.md).

## Support Us

I❤️Fiction is a community-driven project. If you'd like to support our work, please consider sponsoring us.
