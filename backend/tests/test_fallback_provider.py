from app.providers.fallback import FallbackProvider
from app.schemas import GenerateRequest, PostType


def test_fallback_provider_has_name():
    provider = FallbackProvider()

    assert provider.name == "fallback"


def test_fallback_provider_generates_response():
    provider = FallbackProvider()
    request = GenerateRequest(selectedText="We are hiring for a new role.")

    response = provider.generate(request, request.selectedText)

    assert response.postType == PostType.HIRING_POST
    assert response.suggestions