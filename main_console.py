from miroir import Miroir
from langue import LangueFrancais
from horloge import HorlogeSysteme

def main():
    langue = LangueFrancais()
    horloge = HorlogeSysteme()
    miroir = Miroir(langue, horloge)
    
    chaine = input("Entrez une chaîne: ")
    resultat = miroir.analyser_chaine(chaine)
    print(resultat)

if __name__ == "__main__":
    main()