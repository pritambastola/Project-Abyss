from core.logger import logger
from core.config import Config


class Application:
    """
    Central application object.

    Holds references to every major service used by
    Project-Abyss.
    """

    def __init__(self):

        logger.info("Creating Application...")

        self.logger = logger
        self.config = Config()

        self.event_bus = None
        self.registry = None

        self.voice = None
        self.brain = None
        self.memory = None
        self.vision = None
        self.ui = None

        logger.info("Application created successfully.")