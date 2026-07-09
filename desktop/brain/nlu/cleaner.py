import json
from pathlib import Path


class Cleaner:

    def __init__(self):

        path = Path(__file__).parent.parent / "data" / "stopwords.json"

        with open(path, encoding="utf-8") as f:
            self.stopwords = set(json.load(f))

    def clean(self, text):

        words = text.lower().split()

        words = [
            word
            for word in words
            if word not in self.stopwords
        ]

        return " ".join(words)