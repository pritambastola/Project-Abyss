"""
Fast Command Router
"""
from brain.commands.application_commands import register as register_application_commands
from brain.commands.browser_commands import register as register_browser_commands
from brain.commands.audio_commands import register as register_audio_commands
from brain.command_registry import CommandRegistry
from brain.normalizer import Normalizer
from brain.language_parser import LanguageParser

from system.application_manager import ApplicationManager
from system.browser_manager import BrowserManager
from system.audio_manager import AudioManager

from system.display_manager import DisplayManager

from brain.commands.display_commands import (
    register as register_display_commands
)



class FastRouter:

    def __init__(self):

        self.apps = ApplicationManager()
        self.browser = BrowserManager()
        self.audio = AudioManager()
        self.parser = LanguageParser()
        self.display = DisplayManager()

        self.normalizer = Normalizer()
        self.registry = CommandRegistry()

        # -------------------------
        # Audio
        # -------------------------

        register_audio_commands(
            self.registry,
            self.audio
        )

        # -------------------------
        # Browser
        # -------------------------

        register_browser_commands(
            self.registry,
            self.browser
        )


        # -------------------------
        # Applications
        # -------------------------

        register_application_commands(
            self.registry,
            self.apps
        )

        # -------------------------
        # Display
        # -------------------------

        register_display_commands(
            self.registry,
            self.display
        )

    def execute(self, command: str):

        command = self.normalizer.normalize(command)
        command = self.parser.parse(command)

        handler, value = self.registry.match(command)

        if handler is None:
            return False

        if value is None:
            return handler()

        return handler(value)

    def close(self):
        self.apps.close_database()