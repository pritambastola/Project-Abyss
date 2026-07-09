import json
from pathlib import Path

from brain.nlu.models import Intent


class IntentDetector:

    def __init__(self):

        path = Path(__file__).parent.parent / "data" / "actions.json"

        with open(path, encoding="utf-8") as f:
            self.actions = json.load(f)

        self.lookup = {}

        for action, words in self.actions.items():

            for word in words:

                self.lookup[word] = action

    def detect(self, tokens, entities):

        intent = Intent()

        intent.tokens = tokens

        intent.entities = entities

        for token in tokens:

            if token in self.lookup:

                intent.action = self.lookup[token]

                break

        if entities:

            intent.target = entities[0].type

        return intent