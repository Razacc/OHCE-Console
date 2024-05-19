from flask import Flask, request, jsonify
from miroir import Miroir
from langue import Langue
from horloge import Horloge

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def analyse():
    systeme_language = request.headers.get('Accept-Language', 'en')
    lang_code = systeme_language.split(',')[0]

    langue = Langue(lang_code)
    horloge = Horloge()
    miroir = Miroir(langue, horloge)
    
    data = request.json.get('text', '')
    resultat = miroir.analyser_chaine(data)
    return jsonify(resultat)

if __name__ == "__main__":
    app.run(debug=True)