from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class Tone(str, Enum):
    PROFESSIONAL = "professional"
    TECHNICAL = "technical"
    RECRUITER_SAFE = "recruiter-safe"
    SUPPORTIVE = "supportive"
    WITTY = "witty"


class Persona(BaseModel):
    role: str = "Software Engineer"
    interests: List[str] = Field(
        default_factory=lambda: ["AI infrastructure", "distributed systems"]
    )
    style: str = "concise, warm, technical"


class GenerateRequest(BaseModel):
    selectedText: str = Field(min_length=1, max_length=8000)
    tone: Tone = Tone.PROFESSIONAL
    persona: Persona = Field(default_factory=Persona)


class Suggestion(BaseModel):
    label: str
    text: str


class GenerateResponse(BaseModel):
    summary: str
    postType: str
    replyScore: float
    strategy: str
    suggestions: List[Suggestion]
    warnings: List[str]