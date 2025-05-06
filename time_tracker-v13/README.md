# 🧠 Agentic Time Tracker

An AI-powered, agentic time tracking system built with FastAPI, OpenAI, and React.

---

## 🚀 Features

- Smart AI suggestions for time entries using OpenAI
- Modular backend with ETL, AI agent, and REST API
- React + Tailwind frontend interface
- Ready for full deployment on [Render.com](https://render.com)

---

## 📦 Project Structure

```
agentic_time_tracker/
├── main.py
├── services/
├── ai_agents/
├── routes/
├── frontend/           # React + Tailwind frontend
├── requirements.txt
└── render.yaml         # Optional Render deployment config
```

---

## 🧑‍💻 Local Development

### 1. Backend (FastAPI)

```bash
# Create virtualenv and activate it
python -m venv venv
source venv/bin/activate

# Install deps
pip install -r requirements.txt

# Start FastAPI server
uvicorn main:app --reload
```

### 2. Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

> API requests are proxied to `localhost:8000` via `vite.config.js`

---

## 🤖 API Endpoints

- `GET /api/entries` – fetch time entries
- `POST /api/suggest` – get AI-suggested entry

---

## ☁️ Deployment on Render

### 1. Backend Service (FastAPI)

- New Web Service → Connect GitHub
- Build Command: `pip install -r requirements.txt`
- Start Command: `./start.sh`
- Add Env Vars:
  - `DATABASE_URL` (from Render PostgreSQL)
  - `OPENAI_API_KEY`

### 2. PostgreSQL

- Create a new PostgreSQL service on Render
- Set `DATABASE_URL` in backend env

### 3. Frontend (Static Site)

- New Static Site → `frontend/` directory
- Build Command: `npm install && npm run build`
- Publish Directory: `dist`

---

## 🔐 Environment Variables

| Key              | Description              |
|------------------|--------------------------|
| `OPENAI_API_KEY` | Your OpenAI API Key      |
| `DATABASE_URL`   | PostgreSQL DB connection |

---
