from abc import ABC, abstractmethod

from app.schemas import GenerateRequest, GenerateResponse


class ModelProvider(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        request: GenerateRequest,
        safe_text: str,
    ) -> GenerateResponse:
        raise NotImplementedError