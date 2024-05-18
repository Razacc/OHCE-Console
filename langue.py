from abc import ABC, abstractmethod

class Langue(ABC):
    @abstractmethod
    def saluer(self, heure: int) -> str:
        pass

    @abstractmethod
    def feliciter(self) -> str:
        pass

    @abstractmethod
    def acquitter(self, heure: int) -> str:
        pass

class LangueFrancais(Langue):
    def saluer(self, heure: int) -> str:
        if 6 <= heure < 12:
            return "Bonjour"
        elif 12 <= heure < 18:
            return "Bon après-midi"
        elif 18 <= heure < 22:
            return "Bonsoir"
        else:
            return "Bonne nuit"
    
    def feliciter(self) -> str:
        return "Bien dit!"
    
    def acquitter(self, heure: int) -> str:
        if 6 <= heure < 12:
            return "Bonne journée"
        elif 12 <= heure < 18:
            return "Bon après-midi"
        elif 18 <= heure < 22:
            return "Bonne soirée"
        else:
            return "Bonne nuit"
