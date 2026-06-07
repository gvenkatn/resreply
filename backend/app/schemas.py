from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class Tone(str, Enum):
    PROFESSIONAL = "professional"
    TECHNICAL = "technical"
    RECRUITER_SAFE = "recruiter-safe"
    SUPPORTIVE = "supportive"
    WITTY = "witty"


class PostType(str, Enum):
    HIRING_POST = "hiring_post"
    TECHNICAL_POST = "technical_post"
    MILESTONE = "milestone"
    DISCUSSION = "discussion"
    GENERIC = "generic"


class Persona(BaseModel):
    role: str = Field(default="Professional", min_length=2, max_length=80)
    goals: List[str] = Field(
        default_factory=lambda: ["write thoughtful replies"],
        min_length=1,
        max_length=10,
    )
    style: str = Field(
        default="concise, thoughtful, professional",
        min_length=3,
        max_length=160,
    )


class GenerateRequest(BaseModel):
    selectedText: str = Field(min_length=1, max_length=8000)
    tone: Tone = Tone.PROFESSIONAL
    persona: Persona = Field(default_factory=Persona)


class Suggestion(BaseModel):
    label: str = Field(min_length=1, max_length=40)
    text: str = Field(min_length=1, max_length=1000)


class GenerateResponse(BaseModel):
    summary: str = Field(min_length=1, max_length=500)
    postType: PostType
    replyScore: float = Field(ge=0, le=10)
    strategy: str = Field(min_length=1, max_length=500)
    suggestions: List[Suggestion] = Field(min_length=1, max_length=5)
    warnings: List[str] = Field(default_factory=list, max_length=5)