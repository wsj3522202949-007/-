---
id: tool-04978
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Text-Document-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/zenzue/ai-text-document-detector
created: 2026-07-18
updated: 2026-07-18
no: 4978
category: 一、去 AI 味 / Humanizer 库
repo: zenzue/AI-Text-Document-Detector
stars: 0
url: https://github.com/zenzue/ai-text-document-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 908647bc1efa8543
  - methods/改稿润色指令库.md
---

# zenzue/AI-Text-Document-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/zenzue/ai-text-document-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：zenzue/AI-Text-Document-Detector
- **拉取时间**：2026-07-25 18:01:39

---

# AI Text & Document Detector

A full-stack web application for reviewing AI-like writing signals in pasted text and uploaded documents.

The application uses multiple local AI text-detection model and vectorizer pairs. Results are intended to support human review and must not be treated as proof that content was written by AI.

## Features

* JWT-based authentication
* Short-lived access tokens
* Refresh-token rotation
* HttpOnly refresh-token cookies
* Access-token revocation after logout
* Role-based access control
* Administrator user management
* Pasted-text analysis
* Multi-file document analysis
* Maximum of five files per request
* Model-agreement reporting
* Language and input-suitability warnings
* Responsive SvelteKit interface
* Docker Compose deployment
* Environment-based CORS and origin configuration

## Technology Stack

### Frontend

* SvelteKit
* TypeScript
* SvelteKit `adapter-node`
* Tailwind CSS
* Playwright

### Backend

* Python
* Litestar
* SQLAlchemy
* SQLite
* Argon2id password hashing
* JWT authentication
* scikit-learn
* AITextDetector model artifacts

### Deployment

* Docker
* Docker Compose

The project does not include:

* Certbot
* Internal TLS termination
* An internal Nginx service
* Kubernetes configuration

HTTPS and public-domain routing can be configured separately through Nginx Proxy Manager or another reverse proxy.

---

## Quick Start

### 1. Clone the repository

```bash
git clone <repo-url>
cd detector
```

### 2. Copy the environment templates

```bash
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

### 3. Configure authentication secrets

Generate a strong JWT secret:

```bash
openssl rand -hex 64
```

Add the generated value to `.env`:

```env
JWT_SECRET_KEY=<generated-secret>
```

Set an initial administrator password:

```env
AUTH_BOOTSTRAP_ADMIN_ENABLED=true
AUTH_BOOTSTRAP_ADMIN_USERNAME=admin
AUTH_BOOTSTRAP_ADMIN_PASSWORD=<strong-temporary-password>
```

Use a unique password of at least 12 characters.

Do not use `password123`, `admin123`, or another test password in production.

After the first administrator account is created, remove the plaintext bootstrap password from `.env` and recreate the backend container.

### 4. Start the application

```bash
docker compose up -d --build
```

### 5. Check service status

```bash
docker compose ps
```

The backend may require approximately two minutes to load all model and vectorizer artifacts.

### 6. Open the application

* Web application: `http://localhost:3000`
* Frontend health: `http://localhost:3000/health`
* Backend health through the frontend proxy: `http://localhost:3000/api/health`
* API documentation through the frontend proxy: `http://localhost:3000/api/docs`

Browser requests should use the frontend `/api` proxy.

Direct access to backend port `8000` should be used only when it has intentionally been exposed for local development or QA.

---

## Authentication

Authentication is enabled by default.

The application uses:

* Argon2id password hashes
* JWT access tokens
* Rotating refresh tokens
* HttpOnly refresh-token cookies
* JWT token identifiers for logout revocation
* Role-based authorization
* Login-attempt tracking
* Persistent user storage

### Token behavior

Access tokens are short-lived and are held only in frontend memory.

Access tokens must not be stored in:

* `localStorage`
* `sessionStorage`
* IndexedDB
* Readable browser cookies

Refresh tokens are stored in an HttpOnly cookie and are not accessible to frontend JavaScript.

After the page is reloaded, the frontend restores the session by calling:

```text
POST /api/auth/refresh
```

### Logout behavior

Logout:

1. Revokes the refresh token.
2. Adds the access-token JTI to the token blacklist.
3. Clears the refresh-token cookie.
4. Removes the frontend access token.
5. Prevents the logged-out access token from using protected endpoints.

### Roles

The supported roles are:

| Role    | Permissions                                                                                                    |
| ------- | -------------------------------------------------------------------------------------------------------------- |
| `admin` | Analyze content, upload documents, manage users, reset passwords, enable or disable users, and revoke sessions |
| `user`  | Analyze pasted text, upload documents, and manage their own profile and password                               |

Authorization is enforced by the Litestar backend. Hiding frontend controls is not considered an authorization control.

---

## Initial Administrator

The backend can create the first administrator automatically.

```env
AUTH_BOOTSTRAP_ADMIN_ENABLED=true
AUTH_BOOTSTRAP_ADMIN_USERNAME=admin
AUTH_BOOTSTRAP_ADMIN_PASSWORD=<strong-temporary-password>
AUTH_BOOTSTRAP_ADMIN_EMAIL=
```

Bootstrap behavior:

* An administrator is created only when no administrator exists.
* Existing administrator passwords are not overwritten.
* The bootstrap password must satisfy the password policy.
* Passwords are stored as Argon2id hashes.
* The plaintext password is not written to application logs.

After the first successful startup:

1. Log in as the administrator.
2. Change the administrator password when required.
3. Remove `AUTH_BOOTSTRAP_ADMIN_PASSWORD` from `.env`.
4. Recreate the backend container:

```bash
docker compose up -d --force-recreate backend
```

---

## Environment Configuration

The root `.env` file is used by Docker Compose to configure the frontend and backend containers.

### Application

| Variable                 |       Default | Description                      |
| ------------------------ | ------------: | -------------------------------- |
| `APP_ENV`                |  `production` | Application environment          |
| `LOG_LEVEL`              |        `INFO` | Logging level                    |
| `MODEL_DIR`              | `/app/models` | Backend model directory          |
| `MAX_FILES`              |           `5` | Maximum files per upload request |
| `MAX_FILE_SIZE_MB`       |          `10` | Maximum size per uploaded file   |
| `MAX_TEXT_CHARACTERS`    |      `200000` | Maximum pasted-text length       |
| `DEFAULT_VOTE_THRESHOLD` |           `2` | Default model-vote threshold     |

### Frontend

| Variable                   | Default               | Description                                                           |
| -------------------------- | --------------------- | --------------------------------------------------------------------- |
| `FRONTEND_HOST`            | `0.0.0.0`             | Frontend bind address                                                 |
| `FRONTEND_PORT`            | `3000`                | Public frontend port                                                  |
| `BACKEND_INTERNAL_URL`     | `http://backend:8000` | Private backend address used by the SvelteKit server                  |
| `FRONTEND_ALLOWED_ORIGINS` | `*`                   | Origins allowed to use unsafe methods through the SvelteKit API proxy |

`BACKEND_INTERNAL_URL` is a server-side value and must not be exposed in browser code.

Browser API requests must use relative paths such as:

```typescript
fetch('/api/auth/login');
fetch('/api/analyze/text');
fetch('/api/analyze/files');
```

### Backend

| Variable       |                                Default | Description                 |
| -------------- | -------------------------------------: | --------------------------- |
| `BACKEND_HOST` |                              `0.0.0.0` | Backend bind address        |
| `BACKEND_PORT` |                                 `8000` | Internal backend port       |
| `DATABASE_URL` | `sqlite+aiosqlite:////app/data/app.db` | Authentication database URL |

### JWT

| Variable                   |                    Default | Description                                     |
| -------------------------- | -------------------------: | ----------------------------------------------- |
| `JWT_SECRET_KEY`           |                       None | JWT signing secret                              |
| `JWT_SECRET_KEY_FILE`      |                      Empty | Optional file containing the JWT signing secret |
| `JWT_ALGORITHM`            |                    `HS256` | JWT signing algorithm                           |
| `JWT_ISSUER`               |         `ai-text-detector` | JWT issuer                                      |
| `JWT_ACCESS_AUDIENCE`      |     `ai-text-detector-web` | Access-token audience                           |
| `JWT_REFRESH_AUDIENCE`     | `ai-text-detector-refresh` | Refresh-token audience                          |
| `JWT_ACCESS_TOKEN_MINUTES` |                       `15` | Access-token lifetime                           |
| `JWT_REFRESH_TOKEN_DAYS`   |                        `7` | Refresh-token lifetime                          |
| `JWT_CLOCK_SKEW_SECONDS`   |                       `30` | Allowed clock-skew tolerance                    |

A strong `JWT_SECRET_KEY` or `JWT_SECRET_KEY_FILE` is required when authentication is enabled.

### Authentication

| Variable                    | Default | Description                                          |
| --------------------------- | ------: | ---------------------------------------------------- |
| `AUTH_ENABLED`              |  `true` | Enables authentication                               |
| `AUTH_ALLOW_REGISTRATION`   | `false` | Enables or disables public user registration         |
| `AUTH_PASSWORD_MIN_LENGTH`  |    `12` | Minimum password length                              |
| `AUTH_PASSWORD_MAX_LENGTH`  |   `128` | Maximum password length                              |
| `AUTH_MAX_LOGIN_ATTEMPTS`   |     `5` | Maximum failed attempts during the configured window |
| `AUTH_LOGIN_WINDOW_MINUTES` |    `15` | Login-attempt tracking window                        |
| `AUTH_LOCKOUT_MINUTES`      |    `15` | Temporary login lockout duration                     |

Public registration should remain disabled unless explicitly required.

### Refresh Cookie

| Variable                   |               Default | Description                                          |
| -------------------------- | --------------------: | ---------------------------------------------------- |
| `AUTH_REFRESH_COOKIE_NAME` | `ai_detector_refresh` | Refresh-token cookie name                            |
| `AUTH_COOKIE_SECURE`       |               `false` | Sends the cookie only through HTTPS when enabled     |
| `AUTH_COOKIE_HTTP_ONLY`    |                `true` | Prevents frontend JavaScript from reading the cookie |
| `AUTH_COOKIE_SAME_SITE`    |                 `lax` | Cookie SameSite policy                               |
| `AUTH_COOKIE_PATH`         |           `/api/auth` | Cookie path                                          |

For direct local HTTP access, use:

```env
AUTH_COOKIE_SECURE=false
```

After HTTPS is configured through Nginx Proxy Manager, change it to:

```env
AUTH_COOKIE_SECURE=true
```

Then recreate the services:

```bash
docker compose up -d --force-recreate
```

---

## CORS and Origin Configuration

CORS and frontend origin rules are configured through environment variables.

### Default configuration

```env
FRONTEND_ALLOWED_ORIGINS=*

CORS_ALLOW_ORIGINS=*
CORS_ALLOW_METHODS=GET,POST,PUT,PATCH,DELETE,OPTIONS
CORS_ALLOW_HEADERS=*
CORS_ALLOW_CREDENTIALS=false
CORS_EXPOSE_HEADERS=
CORS_MAX_AGE=600
```

### Important security rule

The backend rejects this unsafe configuration:

```env
CORS_ALLOW_ORIGINS=*
CORS_ALLOW_CREDENTIALS=true
```

Wildcard backend origins must not be combined with credentialed cross-origin requests.

The browser normally communicates with the backend through the same-origin SvelteKit `/api` proxy. Refresh cookies are therefore handled through the frontend origin.

### Restricted origins

To restrict access to known domains:

```env
FRONTEND_ALLOWED_ORIGINS=https://detector.example.com
CORS_ALLOW_ORIGINS=https://detector.example.com
CORS_ALLOW_CREDENTIALS=false
```

Multiple origins can be separated by commas:

```env
FRONTEND_ALLOWED_ORIGINS=https://detector.example.com,https://www.detector.example.com
CORS_ALLOW_ORIGINS=https://detector.example.com,https://www.detector.example.com
```

Environment changes require the affected services to be recreated:

```bash
docker compose up -d --force-recreate
```

---

## Supported Input Methods

### Paste Text

Authenticated users can paste text directly into the web interface.

The backend validates:

* Empty content
* Whitespace-only content
* Minimum analyzable length
* Maximum character count
* Vote threshold
* Language suitability
* Repeated or meaningless content

### Upload Documents

Authenticated users can upload up to five files in one request.

Supported formats include:

* PDF
* DOC
* DOCX
* TXT
* MD
* Markdown
* RTF
* ODT

The upload endpoint expects a multipart request body.

Example:

```bash
curl \
  -X POST http://localhost:3000/api/analyze/files \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -F "files=@sample.txt" \
  -F "vote_threshold=2"
```

Multiple files use the same repeated `files` field:

```bash
curl \
  -X POST http://localhost:3000/api/analyze/files \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -F "files=@sample.txt" \
  -F "files=@sample.pdf" \
  -F "files=@sample.docx" \
  -F "vote_threshold=2"
```

Do not send uploaded files through URL query parameters.

---

## API Endpoints

### Public endpoints

| Endpoint            | Method | Description                                           |
| ------------------- | ------ | ----------------------------------------------------- |
| `/api/health`       | GET    | Backend health and model readiness                    |
| `/api/capabilities` | GET    | Supported capabilities and limits                     |
| `/api/privacy-info` | GET    | Runtime privacy and processing information            |
| `/api/auth/login`   | POST   | Authenticate a user                                   |
| `/api/auth/refresh` | POST   | Rotate the refresh token and issue a new access token |
| `/api/auth/logout`  | POST   | Revoke tokens and clear the refresh cookie            |

### Authenticated endpoints

| Endpoint                    | Method | Description                           |
| --------------------------- | ------ | ------------------------------------- |
| `/api/auth/me`              | GET    | Return the current authenticated user |
| `/api/auth/change-password` | POST   | Change the current user’s password    |
| `/api/analyze/text`         | POST   | Analyze pasted text                   |
| `/api/analyze/files`        | POST   | Analyze uploaded documents            |

### Administrator endpoints

| Endpoint                                     | Method | Description                     |
| -------------------------------------------- | ------ | ------------------------------- |
| `/api/admin/users`                           | GET    | List users                      |
| `/api/admin/users`                           | POST   | Create a user                   |
| `/api/admin/users/{user_id}`                 | GET    | Read a user                     |
| `/api/admin/users/{user_id}`                 | PATCH  | Update a user                   |
| `/api/admin/users/{user_id}/reset-password`  | POST   | Reset a user password           |
| `/api/admin/users/{user_id}/revoke-sessions` | POST   | Revoke a user’s active sessions |

---

## Model Limitations

The detector uses multiple character-level TF-IDF and linear SVM model pairs.

The available model artifacts were trained primarily for Chinese creative-writing content.

Results for the following may be unreliable:

* English text
* Myanmar text
* Thai text
* Technical documentation
* Source code
* Legal documents
* Academic writing
* Translated content
* Very short samples
* Heavily edited content

The displayed value is an **AI signal score**, not a calibrated probability.

Do not interpret the result as:

* Proof of AI authorship
* Proof of cheating
* Proof of plagiarism
* A guaranteed human-written result
* A guaranteed AI-generated result

The output should be combined with human review and other contextual evidence.

---

## Privacy

The application is designed to process submitted content temporarily.

It should not permanently store:

* Uploaded documents
* Extracted document text
* Pasted text
* Analysis content
* Raw access tokens
* Raw refresh tokens
* User passwords

The authentication database stores:

* User accounts
* Argon2id password hashes
* Refresh-token hashes
* Token identifiers
* Login-attempt records
* Token-revocation records

Submitted content and authentication secrets must not be written to application logs.

Temporary upload files should be removed after processing, including when extraction or analysis fails.

---

## Service Health

The backend loads multiple model and vectorizer artifacts during startup.

Depending on the host hardware, model loading may take approximately two minutes.

Docker health checks should use a sufficient startup period:

```yaml
start_period: 120s
```

Check status:

```bash
docker compose ps
```

Check backend logs:

```bash
docker compose logs backend
```

Check frontend logs:

```bash
docker compose logs frontend
```

Verify the proxied backend health endpoint:

```bash
curl -f http://localhost:3000/api/health
```

A service that remains unhealthy after model loading should be investigated rather than treated as successfully deployed.

---

## Project Structure

```text
detector/
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   ├── controllers/
│   │   ├── database/
│   │   ├── repositories/
│   │   ├── services/
│   │   └── models/
│   ├── migrations/
│   ├── models/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   ├── static/
│   ├── tests/
│   │   └── e2e/
│   ├── package.json
│   ├── package-lock.json
│   ├── playwright.config.ts
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

The repository root should not contain temporary QA scripts, generated screenshots, Python bytecode, or accidental Node package files.

---

## Development

### Backend

```bash
cd backend

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Apply migrations:

```bash
alembic upgrade head
```

Start the development server:

```bash
python -m uvicorn app.main:app \
  --host 0.0.0.0 \
  --port 8000 \
  --reload
```

### Frontend

```bash
cd frontend

npm install
npm run dev
```

The local frontend development server should proxy `/api` requests to the configured backend.

---

## Testing

### Backend tests

```bash
cd backend
pytest -v
```

### Frontend checks

```bash
cd frontend

npm run check
npm run lint
npm run test
npm run build
```

### Playwright E2E tests

The backend and frontend services must be running before executing the E2E suite.

Start the application:

```bash
docker compose up -d --build
```

Run all WebKit tests:

```bash
cd frontend
npm run test_e2e
```

Run explicitly:

```bash
npx playwright test --project=webkit
```

Run in headed mode:

```bash
npx playwright test --project=webkit --headed
```

Run a specific test file:

```bash
npx playwright test \
  tests/e2e/homepage.spec.ts \
  --project=webkit
```

List tests without running them:

```bash
npx playwright test --list --project=webkit
```

A test being listed or configured does not mean it has passed. The application services must be running and the tests must be executed.

---

## Useful Docker Commands

Start or update:

```bash
docker compose up -d --build
```

View status:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

Restart:

```bash
docker compose restart
```

Stop:

```bash
docker compose down
```

Stop and delete persistent user data:

```bash
docker compose down --volumes
```

Deleting volumes removes the SQLite authentication database, users, refresh-token records, and login-attempt history.

Model files mounted from the project directory are not removed by deleting Docker volumes.

---

## Reverse Proxy

This project does not configure HTTPS.

To expose the application through Nginx Proxy Manager, forward the public domain to:

```text
http://DOCKER_HOST_IP:3000
```

Recommended proxy settings:

* Scheme: `http`
* Forward hostname or IP: Docker host
* Forward port: `3000`
* WebSocket support: enabled

After HTTPS is active, set:

```env
AUTH_COOKIE_SECURE=true
```

Then recreate the application:

```bash
docker compose up -d --force-recreate
```

Do not forward browser traffic directly to backend port `8000`.

---

## Security Notes

* Replace all test passwords before deployment.
* Do not commit `.env` files.
* Do not commit JWT secrets.
* Do not commit access or refresh tokens.
* Do not commit generated QA screenshots or reports containing sensitive data.
* Keep `CORS_ALLOW_CREDENTIALS=false` while using wildcard origins.
* Use explicit origins when direct cross-origin credentialed requests are required.
* Use HTTPS before enabling secure refresh cookies.
* Revoke user sessions after password resets or suspected token exposure.
* Never treat hidden frontend controls as authorization.
* Review backend logs for accidental content or token leakage before deployment.

---

## Cleanup Rules

Generated files should remain ignored by Git.

Recommended `.gitignore` entries:

```gitignore
# Python
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Frontend and Playwright
frontend/node_modules/
frontend/.svelte-kit/
frontend/build/
playwright-report/
test-results/

# QA output
qa-artifacts/
qa-results*.json
security_test_results*.json

# Root debug screenshots and temporary scripts
/*.png
/test-*.mjs
/verify-login.js

# Environment files
.env
backend/.env
frontend/.env
```

Keep production tests under:

```text
backend/tests/
frontend/tests/
frontend/tests/e2e/
```

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

MIT License
