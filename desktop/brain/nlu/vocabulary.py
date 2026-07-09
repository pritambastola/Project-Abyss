import json
from pathlib import Path


class Vocabulary:

    def __init__(self):

        folder = Path(__file__).parent.parent / "data"

        self.actions = json.load(open(folder/"actions.json"))
        self.synonyms = json.load(open(folder/"synonyms.json"))
        self.entities = json.load(open(folder/"entities.json"))
        self.intents = json.load(open(folder/"intents.json"))