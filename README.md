# Resume Skill Parser API

A lightweight FastAPI service that scans resume text or candidate bios against common tech stack keywords. It calculates a simple match score and lists missing skills based on the target role provided.

## Features
- **Data Validation:** Uses Pydantic schemas to validate incoming JSON payloads.
- **Async Endpoints:** Built using FastAPI's async route handlers.
- **Swagger Docs:** Built-in interactive documentation available directly at `/docs`.



## Project Layout

text
.
├── main.py          # API endpoints and skill matching logic
├── schemas.py       # Pydantic request & response models
├── requirements.txt # Project dependencies
└── README.md

## 🛠️ Tech Stack

| Layer            | Technology |
|-------------------|------------|
| Language           | Python 3.10+ |
| Web Framework      | FastAPI |
| Validation Layer   | Pydantic v2 |
| ASGI Server        | Uvicorn |
| Deployment Target  | Render.com |


## 💻 Local Setup

Clone the repository, create a virtual environment, install dependencies, and run the server:

bash
# 1. Clone the repository
git clone https://github.com/<your-username>/ai-document-skill-parser-api.git
cd ai-document-skill-parser-api

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the development server
uvicorn main:app --reload


The API will be available at http://127.0.0.1:8000
Interactive docs: http://127.0.0.1:8000/docs



## 📡 API Reference

### GET /health

Health check for uptime monitoring and deployment platforms.

**Response**
json
{
  "status": "healthy"
}


### `POST /analyze`

Analyzes document text against a target role and returns a keyword match report.

**Sample Request**
json
POST /analyze
Content-Type: application/json

{
  "text": "Experienced backend engineer skilled in Python, FastAPI, Docker and Git. Built REST APIs.",
  "target_role": "Backend Developer"
}


**Sample Response**
  json
{
  "match_score": 42,
  "found_keywords": ["Python", "FastAPI", "Docker", "Git", "REST"],
  "missing_keywords": ["SQL", "Pydantic", "AWS", "Kubernetes", "CI/CD", "Linux", "Async"],
  "summary": "This document is a moderate match for the 'Backend Developer' role, scoring 42% against 12 evaluated keywords. Found: Python, FastAPI, Docker, Git, REST. Consider adding: SQL, Pydantic, AWS, Kubernetes, CI/CD, Linux, Async."
}




## ☁️ Deployment (Render.com — Free Tier)

1. Push this repository to GitHub.
2. Go to [render.com](https://render.com) and sign in with GitHub.
3. Click **New +** → **Web Service** and select this repository.
4. Configure the service:
   - **Environment:** Python 3
   - **Build Command:** pip install -r requirements.txt
   - **Start Command:** uvicorn main:app --host 0.0.0.0 --port $PORT
   - **Instance Type:** Free
5. Click **Create Web Service**. Render will build and deploy automatically on every push to your default branch.
6. Once live, your Swagger docs will be available at:
https://<your-service-name>.onrender.com/docs



