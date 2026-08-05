"""
main.py - Resume & Document Keyword Extractor
"""

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from schemas import AnalysisRequest, AnalysisResponse

app = FastAPI(
    title="Skill Parser API",
    description="Extracts and scores technical keywords from resume text."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hardcoded skill sets for simple keyword matching
TECH_SKILLS = [
    "Python", "FastAPI", "Docker", "SQL", "Pydantic", 
    "Git", "REST", "AWS", "Kubernetes", "Linux"
]

def parse_text(text: str):
    normalized = text.lower()
    found = [skill for skill in TECH_SKILLS if skill.lower() in normalized]
    missing = [skill for skill in TECH_SKILLS if skill not in found]
    return found, missing


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalysisResponse)
def analyze_document(payload: AnalysisRequest):
    found, missing = parse_text(payload.text)
    
    total = len(TECH_SKILLS)
    score = round((len(found) / total) * 100) if total > 0 else 0
    
    summary = f"Matched {len(found)}/{total} target skills for {payload.target_role}."

    return AnalysisResponse(
        match_score=score,
        found_keywords=found,
        missing_keywords=missing,
        summary=summary,
    )