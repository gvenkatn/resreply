from app.reply_service import generate_fallback_response
from app.schemas import GenerateRequest, PostType, Tone


def test_fallback_classifies_hiring_post():
    request = GenerateRequest(
        selectedText="We are hiring engineers for a new role.",
        tone=Tone.RECRUITER_SAFE,
    )

    response = generate_fallback_response(request)

    assert response.postType == PostType.HIRING_POST
    assert response.replyScore == 8.5


def test_fallback_classifies_technical_post():
    request = GenerateRequest(
        selectedText="Latency matters in AI engineering systems.",
        tone=Tone.TECHNICAL,
    )

    response = generate_fallback_response(request)

    assert response.postType == PostType.TECHNICAL_POST
    assert response.suggestions[0].label == "Technical"


def test_fallback_redacts_email_from_summary():
    request = GenerateRequest(
        selectedText="Contact me at user@example.com for details.",
    )

    response = generate_fallback_response(request)

    assert "[REDACTED_EMAIL]" in response.summary
    assert "user@example.com" not in response.summary