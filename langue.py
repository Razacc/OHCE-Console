from abc import ABC, abstractmethod

class Langue(ABC):
    @abstractmethod
    def saluer(self) -> str:
        pass

    @abstractmethod
    def feliciter(self) -> str:
        pass

    @abstractmethod
    def acquitter(self) -> str:
        pass

class LangueFrancais(Langue):
    def saluer(self) -> str:
        return "Bonjour"

    def feliciter(self) -> str:
        return "Bien dit!"

    def acquitter(self) -> str:
        return "Au revoir"