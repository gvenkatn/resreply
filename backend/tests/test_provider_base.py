import pytest

from app.providers.base import ModelProvider


def test_model_provider_cannot_be_instantiated_directly():
    with pytest.raises(TypeError):
        ModelProvider()