from miroir import Miroir
from langue import LangueDynamique
from horloge import HorlogeSysteme
from messages_loader import load_messages

def main():
    messages = load_messages('messages.json')
    language_choice = input("Choose your language (English/French): ").strip().capitalize()
    langue_messages = next((item for item in messages if item["name"] == language_choice), None)

    if not langue_messages:
        print("Invalid language choice.")
        return

    langue = LangueDynamique(langue_messages)
    horloge = HorlogeSysteme()
    miroir = Miroir(langue, horloge)
    heure_actuelle = horloge.heure_actuelle()
    salutation = langue.saluer(heure_actuelle)
    print(salutation)
    chaine = input(langue_messages["enter_text_prompt"])
    
    while chaine != langue_messages["exit_word"]:
        resultat = miroir.analyser_chaine(chaine)
        print(resultat)
        chaine = input(langue_messages["enter_text_prompt"])
    print(langue_messages["goodbye"])

if __name__ == "__main__":
    main()
