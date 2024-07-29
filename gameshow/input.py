from abc import ABC, abstractmethod


class InputType(ABC):
    @abstractmethod
    def serialize(self) -> dict:
        raise NotImplementedError


class BuzzerInput(InputType):
    def serialize(self) -> dict:
        return {
            "type": "buzzer",
        }


class TextInput(InputType):
    def serialize(self) -> dict:
        return {
            "type": "textInput",
        }
