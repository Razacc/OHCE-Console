from langue import Langue
from horloge import Horloge

class Miroir:
    def __init__(self, langue: Langue, horloge: Horloge):
        self.langue = langue
        self.horloge = horloge

    def analyser_chaine(self, chaine: str) -> str:
        miroir = chaine[::-1]
        heure_actuelle = self.horloge.heure_actuelle()
        salutation = self.langue.saluer(heure_actuelle)

        if chaine == miroir:
            felicitation = self.langue.feliciter()
            return f"{salutation} {miroir} {felicitation}"
        return f"{salutation} {miroir}"
