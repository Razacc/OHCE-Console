from abc import ABC, abstractmethod
from datetime import datetime

class Horloge(ABC):
    @abstractmethod
    def heure_actuelle(self) -> datetime:
        pass

class HorlogeSysteme(Horloge):
    def heure_actuelle(self) -> datetime:
        return datetime.now()