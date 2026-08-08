---
id: tool-00525
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Edward-the-App
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/isaaclyman/edward-the-app
created: 2026-07-18
updated: 2026-07-18
no: 525
category: 二、网文 / 长篇 AI 写作系统 库
repo: isaaclyman/Edward-the-App
stars: 52
url: https://github.com/isaaclyman/edward-the-app
tier: "A"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d2d025362074334b
  - methods/最强写作方法论_全球最强综合版.md
---

# isaaclyman/Edward-the-App

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/isaaclyman/edward-the-app
- **Stars**：52
- **语言**：JavaScript
- **License**：NOASSERTION
- **Topics**：composition, novels, writing, writing-tool
- **GitHub 描述**：Write your first novel with the world's most helpful writing tool. (Out of business as of Dec 2021)
- **本地描述**：Write your first novel with the world's most helpful writing tool. (Out of business as of Dec 2021)
- **拉取时间**：2026-07-23 22:54:21

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Edward the App

Write your first novel.

[![Cypress.io tests](https://img.shields.io/badge/cypress.io-tests-green.svg?style=flat-square)](https://cypress.io)

## Build Setup

``` bash
# install dependencies
npm install

# serve client app with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# build and serve full-stack app at localhost:3000
npm run start
# OR
npm run server

# serve Node server app with auto reload at localhost:3000
npm run server-dev

# run Jest unit tests and API integration tests
npm run test

# run Cypress integration tests in the command line (headless)
npm run integration

# run Cypress integration tests in interactive mode
npm run cypress
```

## Environment Variables

For local development, you'll need a root-level `.env` file with the following keys:

- `DATABASE_URL={connectionString}`: A connection string for a local Postgres database. An empty database with a `public` schema and no tables should be sufficient; the ORM will create the tables and relations automatically.
- `DEBUG_DB={true|false}`: When true, all database calls will be logged to the server console.
- `NO_SSL_DB={true|false}`: When true, an SSL connection will not be used to connect to the Postgres database. This should be "true" for local development.
- `INSECURE_COOKIES={true|false}`: When true, the "secure" parameter will not be set for auth cookies. This should be "true" for local development.
- `RECAPTCHA_SECRET={secret}`: A valid Google Recaptcha site secret. If you're developing locally on /auth, you'll also need to set `window.recaptchaSiteKey` to a valid site key after page load. By default, this is set in `auth.html`.
- `SESSION_COOKIE_SECRET={secret}`: A secret to use for encrypting and decrypting session cookies.
- `BASE_URL=127.0.0.1:8080`: The base URL of the app.
- `SMTP_HOST={hostname}`: A host for sending emails via SMTP. For development, you might consider using `smtp.ethereal.email`. NOTE: you can leave the SMTP attributes blank if you're not developing email or signup functionality.
- `SMTP_USER={username}`: Your username for accessing the SMTP server.
- `SMTP_PASS={password}`: Your password for accessing the SMTP server.
- `STRIPE_SECRET_KEY={key}`: A secret key for use with the Stripe API. If you're developing locally on /auth, you'll also need to set `window.stripePublicKey` to a valid publishable key after page load. By default, this is set in `auth.html`.

## Running the app locally

`npm run dev` serves the front-end site on port 8080. `npm run server-dev` runs the API server on port 3000. Run these in separate console windows, and API requests will automatically be proxied from port 8080 to port 3000.

The webpack dev server (port 8080) will automatically redirect from routes like `/app` and `/auth` to `/app.html` and `/auth.html`. On the express server (port 3000) the original routes work without a redirect.

For best results, it's recommended to visit `127.0.0.1` instead of `localhost`.

## Tests

`npm run test` is self-contained. Do not try to run it while a local server is already running. Port 3000 must be available.

If tests fail on a fresh install of Edward, it's probably due to missing tables. Run the tests a second time.

The Cypress tests require `npm run server` to be running in order to function. I recommend that you run this (and `npm run cypress`) in the Powershell console or Linux Bash, not in the Git Bash.
