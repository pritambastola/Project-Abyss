import json
from pathlib import Path


class Cleaner:

    def __init__(self):

        path = Path(__file__).parent.parent / "data" / "stopwords.json"

        with open(path, encoding="utf-8") as f:
            self.stopwords = set(json.load(f))

    def clean(self, text: str):

        text = text.lower()

        for word in self.stopwords:
            text = text.replace(word, " ")

        return " ".join(text.split())