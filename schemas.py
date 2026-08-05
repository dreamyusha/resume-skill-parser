"""
schemas.py

Pydantic data models used for request validation and response
serialization across the AI Document & Skill Parser API.
"""

    
from pydantic import BaseModel, Field

class AnalysisRequest(BaseModel):
    text: str = Field(..., min_length=10)
    target_role: str = Field(..., min_length=2)

class AnalysisResponse(BaseModel):
    match_score: int
    found_keywords: list[str]
    missing_keywords: list[str]
    summary: str