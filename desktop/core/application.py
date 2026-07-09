"""
Project-Abyss Application
"""

from core.logger import logger
from core.config import Config
from core.event_bus import EventBus


class Application:
    def __init__(self):

        self.logger = logger
        self.config = Config()
        self.event_bus = EventBus()

        self.services = {}

        logger.info("Application initialized.")

    def register_service(self, name, service):
        self.services[name] = service
        logger.info(f"Registered service: {name}")

    def get_service(self, name):
        return self.services.get(name)