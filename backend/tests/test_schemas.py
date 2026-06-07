import pytest
from pydantic import ValidationError

from app.schemas import GenerateRequest, GenerateResponse, Suggestion, Tone


def test_generate_request_uses_defaults():
    request = GenerateRequest(selectedText="Interesting AI infra post.")

    assert request.tone == Tone.PROFESSIONAL
    assert request.persona.role == "Software Engineer"


def test_generate_request_rejects_empty_text():
    with pytest.raises(ValidationError):
        GenerateRequest(selectedText="")


def test_generate_response_accepts_suggestions():
    response = GenerateResponse(
        summary="Post about AI infrastructure.",
        postType="technical_post",
        replyScore=8.4,
        strategy="Ask a thoughtful technical question.",
        suggestions=[
            Suggestion(label="Short", text="Great point on reliability.")
        ],
        warnings=["Review before posting."]
    )

    assert response.suggestions[0].label == "Short"
    assert response.replyScore == 8.4