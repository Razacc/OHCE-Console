import json

def load_messages(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)