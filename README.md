# OHCE-Console

Application Python permettant de renvoyer une chaine de caractères à l'envers. Elle vous salue et vous dit au-revoir en fonction de l'heure de la journée. L'application est en deux partie, avec une fonctionnant depuis la console et l'autre depuis une api à l'aide de Flask.

## Schéma d'architecture

TODO

## Prérequis

- Python 3.x
- pip
- virtualenv

## Installation

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/Razacc/OHCE-Console.git
    ```

2. Créez un environnement virtuel (optionnel) :

    ```bash
    python -m venv env
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Lancer l'application en mode console

Pour exécuter l'application en mode console, utilisez le script `main_console.py` :

1. Assurez-vous d'être à la racine du projet.
2. Exécutez la commande suivante :

    ```bash
    python main_console.py
    ```

## Lancer l'application en mode API

Pour exécuter l'application en mode API, utilisez le script `main_api.py` :

1. Assurez-vous d'être à la racine du projet.
2. Exécutez la commande suivante :

    ```bash
    python main_api.py
    ```

3. L'API sera accessible à l'adresse `http://127.0.0.1:5000`.

## Utilisation de l'API avec Postman

Pour tester l'API avec Postman, suivez ces étapes :

1. Ouvrez Postman.
2. Créez une nouvelle requête POST.
3. Configurez l'URL de la requête à `http://127.0.0.1:5000/api`.
4. Dans l'onglet "Headers", ajoutez une clé `Accept-Language` avec la valeur de la langue souhaitée (`en` pour l'anglais, `fr` pour le français).
5. Dans l'onglet "Body", sélectionnez le type `raw` et le format `JSON`.
6. Ajoutez un JSON avec le texte à traiter, par exemple :

    ```json
    {
        "text": "texte à traiter"
    }
    ```

7. Envoyez la requête.

## Equipe du projet

- Paul BARDOU
- Thierry PETHE
- Pablo CAZIN
- Thomas ESPINASSE
- Rémi AGERON
