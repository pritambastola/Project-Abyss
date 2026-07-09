import json
from pathlib import Path


class SynonymResolver:

    def __init__(self):

        path = Path(__file__).parent.parent / "data" / "synonyms.json"

        with open(path, encoding="utf-8") as f:
            self.synonyms = json.load(f)

        self.lookup = {}

        for canonical, words in self.synonyms.items():

            for word in words:

                self.lookup[word.lower()] = canonical

    def resolve(self, tokens):

        return [
            self.lookup.get(token, token)
            for token in tokens
        ]