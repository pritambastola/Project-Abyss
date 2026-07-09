"""
Audio Commands
"""


def register(registry, audio):

    registry.register(
        "mute",
        audio.mute
    )

    registry.register(
        "unmute",
        audio.unmute
    )

    registry.register(
        "volume up",
        audio.volume_up
    )

    registry.register(
        "volume down",
        audio.volume_down
    )

    registry.register(
        "volume {value}",
        audio.set_volume
    )