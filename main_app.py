from flask import Flask, request
from miroir import Miroir
from langue import LangueFrancais
from horloge import HorlogeSysteme

app = Flask(__name__)

@app.route('/analyse', methods=['POST'])
def analyse():
    langue = LangueFrancais()
    horloge = HorlogeSysteme()
    miroir = Miroir(langue, horloge)
    
    data = request.data.decode('utf-8')
    resultat = miroir.analyser_chaine(data)
    return resultat

if __name__ == "__main__":
    app.run(debug=True)