from abc import ABC, abstractmethod


class QuestionType(ABC):
    @abstractmethod
    def serialize(self) -> dict:
        raise NotImplementedError


class TextQuestion(QuestionType):
    def __init__(self, text: str):
        self.text = text

    def serialize(self) -> dict:
        return {
            "type": "text",
            "text": self.text,
        }