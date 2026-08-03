---
id: tool-01372
type: tool
area: 库
status: active
tags: [Swift, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: SkaldCraft
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/semperfitodd/skaldcraft
created: 2026-07-18
updated: 2026-07-18
no: 1372
category: 二、网文 / 长篇 AI 写作系统 库
repo: semperfitodd/SkaldCraft
stars: 0
url: https://github.com/semperfitodd/skaldcraft
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# semperfitodd/SkaldCraft

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/semperfitodd/skaldcraft
- **Stars**：0
- **语言**：Swift
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI interactive story generator
- **本地描述**：AI interactive story generator
- **拉取时间**：2026-07-23 23:19:08

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# SkaldCraft

**Forge Your Story. Shape Your Legend.**

SkaldCraft is an AI-powered storytelling app that transforms reading into an immersive, personalized adventure for every age. Inspired by Viking skalds—the legendary storytellers who shaped history through epic tales—SkaldCraft invites readers to become the heroes of their own sagas.

Whether you're an adult seeking an interactive escape or a parent guiding a child's reading journey, SkaldCraft adapts every story to the reader's age, skill level, imagination, and personal preferences.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Infrastructure Setup](#infrastructure-setup)
  - [Web Application Setup](#web-application-setup)
  - [Mobile Application Setup](#mobile-application-setup)
- [Configuration](#configuration)
  - [Terraform Variables](#terraform-variables)
  - [Environment Variables](#environment-variables)
- [OAuth Provider Setup](#oauth-provider-setup)
  - [Apple Sign In](#apple-sign-in)
  - [Google Sign In](#google-sign-in)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Author](#author)
- [License](#license)

## Features

### Personalized Interactive Stories

Every story is generated uniquely for the reader. Choose your path, alter the narrative, and watch your legend unfold across branching episodes. No two journeys are ever the same.

### Profiles for Every Reader

Create multiple profiles for yourself or your children. Each profile stores:

- Reading level (Pre-K through Adult)
- Age-appropriate story models
- Personal preferences (genres, tones, themes)
- Story history and achievements

### Adaptive Story Engine

Using advanced AI models, SkaldCraft adjusts:

- Vocabulary difficulty
- Story pacing
- Narrative tone (calm, funny, adventurous, epic)
- Episode length
- Themes based on preferences

The engine grows with the reader—like a digital skald learning their audience.

### Legendary Personalization

At the end of each story, readers provide simple feedback:

- What did you enjoy?
- What didn't work?
- What kind of adventure do you want next?

SkaldCraft remembers and learns your style over time, tailoring stories with uncanny accuracy.

## Architecture

- **Frontend**: React single-page application hosted on AWS S3 + CloudFront
- **Backend**: AWS Lambda functions with API Gateway
- **Authentication**: AWS Cognito with Apple and Google OAuth providers
- **AI Engine**: AWS Bedrock (Claude)
- **Infrastructure**: Terraform

## Prerequisites

- [Node.js](https://nodejs.org/) >= 18.x
- [Terraform](https://www.terraform.io/) >= 1.0
- [AWS CLI](https://aws.amazon.com/cli/) configured with appropriate credentials
- Apple Developer account (for Sign in with Apple)
- Google Cloud Console project (for Google Sign In)

## Getting Started

### Infrastructure Setup

1. Configure Terraform variables (see [Configuration](#configuration)):

```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your values
```

2. Deploy infrastructure:

```bash
terraform init
terraform apply
```

3. Save the outputs for application configuration:

```bash
terraform output
```

### Web Application Setup

1. Configure environment (see [Configuration](#configuration)):

```bash
cd static_site
cp .env.example .env
# Edit .env with values from terraform output
```

2. Install and run:

```bash
npm install
npm start
```

3. Build for production:

```bash
npm run build
```

### Mobile Application Setup

1. Configure secrets (see [Configuration](#configuration)):

```bash
cd mobile/SkaldCraftPackage/Sources/SkaldCraftFeature/Config
cp Secrets.swift.example Secrets.swift
# Edit Secrets.swift with values from terraform output
```

2. Open in Xcode and run:

```bash
cd mobile
open SkaldCraft.xcworkspace
```

## Configuration

### Terraform Variables

Copy `terraform/terraform.tfvars.example` to `terraform/terraform.tfvars` and fill in your values:

```bash
cp terraform/terraform.tfvars.example terraform/terraform.tfvars
```

Required variables:
- `environment` - Environment name (e.g., `dev`, `prod`)
- `region` - AWS region
- `domain` - Your domain name
- `app_name` - Application name

Optional OAuth providers (leave empty to disable):
- Apple Sign In credentials
- Google Sign In credentials

### Web Application

Copy `static_site/.env.example` to `static_site/.env` and configure with values from `terraform output`:

```bash
cp static_site/.env.example static_site/.env
```

### Mobile Application

Copy `mobile/SkaldCraftPackage/Sources/SkaldCraftFeature/Config/Secrets.swift.example` to `Secrets.swift`:

```bash
cp mobile/SkaldCraftPackage/Sources/SkaldCraftFeature/Config/Secrets.swift.example \
   mobile/SkaldCraftPackage/Sources/SkaldCraftFeature/Config/Secrets.swift
```

Configure with values from `terraform output`.

## OAuth Provider Setup

### Apple Sign In

1. Go to [Apple Developer Console](https://developer.apple.com/account/resources/identifiers/list/serviceId)

2. Create a Services ID with Sign in with Apple enabled

3. Configure the Services ID:
   - **Domains**: `{environment}.{domain}` (e.g., `prod.example.com`)
   - **Return URLs**: `https://{environment}-auth.{domain}/oauth2/idpresponse`

4. Create a Sign in with Apple key and download the `.p8` file

5. Base64 encode the private key:

```bash
base64 -i AuthKey_XXXXXXXXXX.p8
```

### Google Sign In

1. Go to [Google Cloud Console](https://console.cloud.google.com/apis/credentials)

2. Create an OAuth 2.0 Client ID (Web application)

3. Configure authorized origins:
   - `https://{environment}.{domain}`
   - `https://{environment}-auth.{domain}`

4. Configure authorized redirect URIs:
   - `https://{environment}-auth.{domain}/oauth2/idpresponse`

## Deployment

### Deploy Infrastructure

```bash
cd terraform
terraform apply
```

### Deploy Web Application

```bash
cd static_site
npm run build
cd ../terraform
terraform apply
```

The S3 bucket is automatically synced with the build directory on `terraform apply`.

### Invalidate CloudFront Cache (if needed)

```bash
aws cloudfront create-invalidation \
  --distribution-id YOUR_DISTRIBUTION_ID \
  --paths "/*"
```

## Project Structure

```
SkaldCraft/
├── mobile/                    # iOS application
│   ├── Config/               # Xcode build configurations
│   ├── SkaldCraft/           # Main app target
│   ├── SkaldCraftPackage/    # Swift Package with features
│   └── SkaldCraftUITests/    # UI tests
├── static_site/              # React web application
│   ├── public/               # Static assets
│   └── src/
│       ├── components/       # Reusable UI components
│       ├── hooks/            # Custom React hooks
│       ├── pages/            # Page components
│       ├── styles/           # Global styles and variables
│       └── utils/            # Utilities and configuration
└── terraform/                # Infrastructure as code
    ├── lambda_api/           # API Lambda function source
    └── *.tf                  # Terraform configurations
```

## Author

**Todd Bernson**
