from abc import ABC, abstractmethod

class Langue(ABC):
    @abstractmethod
    def saluer(self, heure: int) -> str:
        pass

    @abstractmethod
    def feliciter(self) -> str:
        pass

    @abstractmethod
    def acquitter(self) -> str:
        pass

class LangueDynamique(Langue):
    def __init__(self, messages: dict):
        self.messages = messages

    def saluer(self, heure: int) -> str:
        if 6 <= heure < 18:
            return self.messages["greeting_morning"]
        else:
            return self.messages["greeting_evening"]

    def feliciter(self) -> str:
        return self.messages["palindrome_response"]
    
    def acquitter(self) -> str:
        return self.messages["goodbye"]
