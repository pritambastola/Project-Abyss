"""
Application Commands
"""


def register(registry, app_manager):

    registry.register(
        "open {value}",
        app_manager.open
    )