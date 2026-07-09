"""
Natural Language Normalizer
"""

from __future__ import annotations


class Normalizer:

    def __init__(self):

        self.replacements = {

            # Wake words
            "hey jarvis": "",
            "jarvis": "",

            # Politeness
            "please": "",
            "can you": "",
            "could you": "",
            "would you": "",
            "for me": "",

            # Open
            "launch": "open",
            "start": "open",
            "run": "open",
            "fire up": "open",

            # Browser
            "google": "search",

            # Audio
            "increase volume": "volume up",
            "raise volume": "volume up",
            "turn up volume": "volume up",

            "decrease volume": "volume down",
            "lower volume": "volume down",
            "turn down volume": "volume down",

            # Brightness
            "increase brightness": "brightness up",
            "raise brightness": "brightness up",

            "decrease brightness": "brightness down",
            "lower brightness": "brightness down",
        }

    def normalize(self, text: str) -> str:

        text = text.lower().strip()

        for phrase in sorted(self.replacements.keys(), key=len, reverse=True):
            text = text.replace(phrase, self.replacements[phrase])

        return " ".join(text.split())