---
id: tool-01855
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: mediflow-hms
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/jayasripandiyan-prj/mediflow-hms
created: 2026-07-18
updated: 2026-07-18
no: 1855
category: 二、网文 / 长篇 AI 写作系统 库
repo: jayasripandiyan-prj/mediflow-hms
stars: 0
url: https://github.com/jayasripandiyan-prj/mediflow-hms
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# jayasripandiyan-prj/mediflow-hms

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jayasripandiyan-prj/mediflow-hms
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：MediFlow - End-to-end hospital queue management solution. Features role-based authentication (Patient/Doctor/Admin), WebSocket real-time updates, smart delay handling, medical report writing, and analytics dashboard. Tech: React, Flask, Socket.io, SQLite.
- **本地描述**：MediFlow - End-to-end hospital queue management solution. Features role-based authentication (Patient/Doctor/Admin), WebSocket real-time updates, smart delay handling, medical report writing, and analytics dashboard. Tech: React, Flask, Socket.io, SQLite.
- **拉取时间**：2026-07-23 23:33:05

---

```markdown
# MediFlow - Hospital Queue Management System

A production-ready real-time hospital queue management system that eliminates waiting room chaos. Patients receive digital tokens, doctors manage consultations with one click, and administrators get live analytics.

## Features

Patient Portal
- Digital token generation with unique format
- Real-time queue position tracking
- Estimated wait time calculation
- Token status check

Doctor Dashboard
- Live patient queue view
- One-click start and complete consultation
- Smart delay reporting with auto-return
- Today's completed patients list
- Medical report writing for each patient

Admin Panel
- Analytics dashboard with charts
- Department congestion visualization
- Peak hours analysis
- Patient medical records viewer
- Doctor management (add, update, delete)

Authentication
- Role-based access (Patient, Doctor, Admin)
- Separate login pages for each role
- Secure session management

Real-time Features
- WebSocket connections for instant updates
- Browser notifications for patients
- Live queue status bar
- Automatic UI refresh on data changes

## Tech Stack

Frontend
- React 18
- React Router for navigation
- Socket.io-client for real-time updates
- Axios for API calls
- Chart.js for analytics
- CSS3 for styling

Backend
- Python 3
- Flask framework
- Flask-SocketIO for WebSocket
- SQLite3 database
- Flask-CORS for cross-origin requests

## Project Structure

## Installation

### Prerequisites

- Node.js (v16 or higher)
- Python (v3.8 or higher)

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The backend will run on http://localhost:5000

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

The frontend will run on http://localhost:3000

## Test Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Doctor | drrajeshkumar | doctor123 |
| Doctor | drpriyasharma | doctor123 |
| Doctor | dramitpatel | doctor123 |
| Doctor | drsnehareddy | doctor123 |
| Doctor | drvikramsingh | doctor123 |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| POST | /api/register | Register new patient |
| GET | /api/doctors | Get all doctors |
| GET | /api/queue/status | Get current queue |
| POST | /api/doctor/update/:id | Update doctor status |
| POST | /api/doctor/delay/:id | Report doctor delay |
| POST | /api/doctor/complete-consultation/:id | Complete consultation |
| POST | /api/patient/report | Save medical report |
| GET | /api/admin/reports | Get all patient reports |
| POST | /api/login | Authenticate user |

## Token Format

Digital tokens follow this format: D{doctor_id}-{HHMM}-{initials}

Example: D1-1430-JS means Doctor 1, 2:30 PM, patient initials JS

## Key Features Explained

Digital Token System
Patients receive unique digital tokens immediately after registration. The token encodes doctor ID, registration time, and patient initials for easy identification.

Real-time Updates
All connected clients receive instant updates via WebSocket when any change occurs in the queue. No page refresh required.

Smart Delay Management
Doctors can report delays with custom duration. Patients receive automatic notifications with expected return time. The system auto-returns the doctor after delay expires.

Medical Records
Doctors can write medical reports after completing consultations. Reports are stored with doctor name, date, and time. Admin can view all patient records.

Role-Based Access
Three distinct roles with appropriate permissions. Patients access registration and queue viewing. Doctors access consultation management. Admin access analytics and records.

## Future Enhancements

- SMS notifications integration
- Mobile application
- PostgreSQL database support
- Multi-hospital support
- Export reports as PDF
- Patient history tracking

## Author

Jayasri Pandiyan
```
