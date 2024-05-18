from datetime import datetime

class Horloge:
    def heure_actuelle(self) -> int:
        pass

class HorlogeSysteme(Horloge):
    def heure_actuelle(self) -> int:
        return datetime.now().hour
