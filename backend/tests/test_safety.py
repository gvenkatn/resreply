from app.safety import clamp_text, redact_pii


def test_redact_pii_removes_email():
    text = "Contact me at user@example.com"

    assert redact_pii(text) == "Contact me at [REDACTED_EMAIL]"


def test_redact_pii_removes_phone():
    text = "Call me at +1 555-123-4567"

    assert redact_pii(text) == "Call me at [REDACTED_PHONE]"


def test_redact_pii_removes_secret():
    text = "api_key=abc123 should not leak"

    assert redact_pii(text) == "[REDACTED_SECRET] should not leak"


def test_clamp_text_truncates_long_input():
    text = "a" * 10

    assert clamp_text(text, max_chars=5) == "aaaaa..."


def test_clamp_text_strips_short_input():
    assert clamp_text("  hello  ") == "hello"