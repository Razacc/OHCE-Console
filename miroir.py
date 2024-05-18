from langue import Langue
from horloge import Horloge

class Miroir:
    def __init__(self, langue: Langue, horloge: Horloge):
        self.langue = langue
        self.horloge = horloge

    def analyser_chaine(self, chaine: str) -> str:
        miroir = chaine[::-1]
        salutation = self.langue.saluer()
        acquittement = self.langue.acquitter()
        if chaine == miroir:
            felicitation = self.langue.feliciter()
            return f"{salutation} {miroir} {felicitation} {acquittement}"
        return f"{salutation} {miroir} {acquittement}"
