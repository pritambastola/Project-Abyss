"""
Display Commands
"""


def register(registry, display):

    
    registry.register(
        "brightness up",
        display.brightness_up
    )

    registry.register(
        "brightness down",
        display.brightness_down
    )

    registry.register(
        "brightness {value}",
        display.set_brightness
    )
