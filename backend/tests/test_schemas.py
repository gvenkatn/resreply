import pytest
from pydantic import ValidationError

from app.schemas import (
    GenerateRequest,
    GenerateResponse,
    PostType,
    Suggestion,
    Tone,
)


def test_generate_request_uses_generic_defaults():
    request = GenerateRequest(selectedText="Interesting post.")

    assert request.tone == Tone.PROFESSIONAL
    assert request.persona.role == "Professional"
    assert request.persona.goals == ["write thoughtful replies"]


def test_generate_request_accepts_custom_persona():
    request = GenerateRequest(
        selectedText="Interesting founder post.",
        persona={
            "role": "Founder",
            "goals": ["build investor relationships"],
            "style": "direct, warm, credible",
        },
    )

    assert request.persona.role == "Founder"
    assert request.persona.goals == ["build investor relationships"]


def test_generate_request_rejects_empty_text():
    with pytest.raises(ValidationError):
        GenerateRequest(selectedText="")


def test_generate_request_rejects_invalid_tone():
    with pytest.raises(ValidationError):
        GenerateRequest(selectedText="Post", tone="angry")


def test_generate_response_accepts_valid_payload():
    response = GenerateResponse(
        summary="Post about product launch.",
        postType=PostType.MILESTONE,
        replyScore=8.4,
        strategy="Respond with a specific and thoughtful note.",
        suggestions=[
            Suggestion(label="Short", text="Congrats on the launch.")
        ],
        warnings=["Review before posting."],
    )

    assert response.suggestions[0].label == "Short"
    assert response.replyScore == 8.4


def test_generate_response_rejects_invalid_score():
    with pytest.raises(ValidationError):
        GenerateResponse(
            summary="Post about product launch.",
            postType=PostType.MILESTONE,
            replyScore=20,
            strategy="Respond thoughtfully.",
            suggestions=[
                Suggestion(label="Short", text="Congrats on the launch.")
            ],
            warnings=[],
        )