from core.logger import logger
from core.event_bus import EventBus


def spotify_opened(app_name):
    logger.info(f"{app_name} opened successfully!")


def main():
    bus = EventBus()

    bus.subscribe("app_opened", spotify_opened)

    logger.info("Publishing Event...")

    bus.publish("app_opened", "Spotify")


if __name__ == "__main__":
    main()