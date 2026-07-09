import json
from pathlib import Path

from brain.nlu.models import Entity


class EntityExtractor:

    def __init__(self):

        folder = Path(__file__).parent.parent / "data"

        with open(folder / "entities.json", encoding="utf-8") as f:
            self.entities = json.load(f)

    def extract(self, tokens):

        found = []

        text = " ".join(tokens)

        for entity_type, values in self.entities.items():

            for value in values:

                if value.lower() in text:

                    found.append(
                        Entity(
                            entity_type,
                            value
                        )
                    )

        return found