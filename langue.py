import json

class Langue():

    def __init__(self, langue) -> None:
        self.langue = langue
        self.traductions = self.chargement_de_la_traduction()

    def saluer(self, heure):
        if 5 <= heure <= 12:
            return self.recuperation_de_la_traduction('greeting_morning')
        elif 12 < heure <= 17:
            return self.recuperation_de_la_traduction('greet_afternoon')
        else :
            return self.recuperation_de_la_traduction('greeting_evening')


    def feliciter(self):
        return self.recuperation_de_la_traduction('palindrome_response')

    def acquitter(self):
        return self.recuperation_de_la_traduction('goodbye')

    def chargement_de_la_traduction(self):
        with open('languages.json', 'r', encoding='utf-8') as file:
            traductions = json.load(file)
        return traductions.get(self.langue, traductions['en'])

    def recuperation_de_la_traduction(self, cle):
        return self.traductions.get(cle, "")
