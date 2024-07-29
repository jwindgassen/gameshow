from abc import ABC, abstractmethod


class SolutionType(ABC):
    @abstractmethod
    def serialize(self) -> dict:
        raise NotImplementedError


class TextSolution(SolutionType):
    def __init__(self, text: str):
        self.text = text

    def serialize(self) -> dict:
        return {
            "type": "text",
            "text": self.text,
        }
