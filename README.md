# QueryMind 🧠

> Talk to your database in plain English — powered by Claude AI + LangChain

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com)
[![LangChain](https://img.shields.io/badge/LangChain-latest-orange)](https://langchain.com)
[![Claude](https://img.shields.io/badge/Claude-Sonnet%204-purple)](https://anthropic.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## What is QueryMind?

QueryMind is an AI-powered microservice that lets users query their PostgreSQL database using natural language. No SQL knowledge required — just ask a question and get an answer.

**"How many orders were placed last month?"** → QueryMind figures out the SQL, runs it, and returns a human-friendly answer.

---

## Features

- 🗣️ **Natural Language to SQL** — powered by Claude Sonnet + LangChain SQL Agent
- ⚡ **FastAPI** — async, production-ready REST API
- 🔒 **Secure by default** — read-only DB access, internal API key auth
- 🐘 **PostgreSQL** — works with any PostgreSQL database (local or AWS RDS)
- 🔌 **Backend agnostic** — plug into any existing backend (Ktor, Node, Laravel, etc.)

---

## Architecture

```
Your Backend (Ktor / Node / etc.)
        ↓  HTTP + API Key
    QueryMind (FastAPI)
        ↓
   LangChain SQL Agent
        ↓
   Claude Sonnet 4 (LLM)
        ↓
   PostgreSQL Database
        ↓
   Natural Language Answer
```

---

## Project Structure

```
QueryMind/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── agent.py         # LangChain SQL Agent
│   └── database.py      # DB connection
├── .env.example
├── requirements.txt
└── README.md
```

---

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/QueryMind.git
cd QueryMind
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

```bash
cp .env.example .env
```

Edit `.env`:

```env
ANTHROPIC_API_KEY=your-anthropic-api-key
DATABASE_URL=postgresql://user:password@localhost:5432/yourdb
INTERNAL_API_KEY=your-secret-internal-key
```

### 5. Run the service

```bash
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for the interactive API UI.

---

## API Usage

### `POST /ask`

```bash
curl -X POST "http://localhost:8000/ask" \
  -H "x-api-key: your-secret-internal-key" \
  -H "Content-Type: application/json" \
  -d '{"question": "How many users signed up this week?"}'
```

**Response:**

```json
{
  "answer": "There were 42 new users who signed up this week."
}
```

---

## Deployment (AWS EC2)

```bash
# Copy project to EC2
scp -r QueryMind/ ec2-user@your-ec2-ip:/home/ec2-user/

# Setup on EC2
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run as a system service (auto-restart on reboot)
sudo systemctl enable querymind
sudo systemctl start querymind
```

> See [deployment guide](#) for full systemd setup instructions.

---

## Security

- FastAPI binds to `127.0.0.1` only — never exposed publicly
- All requests require an internal API key
- Database user has `SELECT` permissions only — AI cannot modify data
- Secrets managed via `.env` / AWS Secrets Manager

---

## Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| AI Orchestration | LangChain |
| LLM | Claude Sonnet 4 (Anthropic) |
| Database | PostgreSQL |
| Language | Python 3.12 |

---

## License

MIT — free to use, modify, and distribute.

---

## Author

Built with ❤️ by [@yourusername](https://github.com/yourusername)