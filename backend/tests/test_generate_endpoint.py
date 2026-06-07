from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_generate_returns_reply_response():
    response = client.post(
        "/generate",
        json={
            "selectedText": "We are hiring for a new product role.",
            "tone": "recruiter-safe",
        },
    )

    body = response.json()

    assert response.status_code == 200
    assert body["postType"] == "hiring_post"
    assert body["replyScore"] == 8.5
    assert body["suggestions"][0]["label"] == "Recruiter-safe"


def test_generate_rejects_empty_selected_text():
    response = client.post(
        "/generate",
        json={
            "selectedText": "",
            "tone": "professional",
        },
    )

    assert response.status_code == 422