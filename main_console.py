from miroir import Miroir
from langue import Langue
from horloge import Horloge
import locale

def main():

    systemelanguage, encoding = locale.getlocale()
    lang_code = systeme_language.split('')[0]
    print(systemelanguage)

    langue = Langue(langcode)
    horloge = Horloge()
    miroir = Miroir(langue, horloge)

    heureactuelle = horloge.heureactuelle()
    salutation = langue.saluer(heure_actuelle)
    acquitter = langue.acquitter()
    texte_entree = langue.recuperation_de_la_traduction('enter_text_prompt')
    texte_sortie = langue.recuperation_de_la_traduction('exit_word')
    print(salutation)

    while True:
        chaine = input(f"{texte_entree}").strip()
        if chaine == texte_sortie:
             print(acquitter)
             break
        resultat = miroir.analyser_chaine(chaine)
        print(resultat)


if __name == "__main":
    main()
