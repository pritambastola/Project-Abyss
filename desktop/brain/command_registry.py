"""
Command Registry
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable


@dataclass
class Command:
    pattern: str
    regex: re.Pattern
    handler: Callable


class CommandRegistry:

    def __init__(self):
        self.commands: list[Command] = []

    def register(self, pattern: str, handler: Callable):

        regex = re.escape(pattern)

        regex = regex.replace(
            re.escape("{value}"),
            r"(.+)"
        )

        regex = "^" + regex + "$"

        self.commands.append(
            Command(
                pattern,
                re.compile(regex, re.IGNORECASE),
                handler
            )
        )

    def match(self, text: str):

        text = text.strip()

        for command in self.commands:

            match = command.regex.match(text)

            if not match:
                continue

            if len(match.groups()) == 0:
                return command.handler, None

            return command.handler, match.group(1).strip()

        return None, None