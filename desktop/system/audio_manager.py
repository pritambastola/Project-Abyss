"""
Audio Manager

Controls Windows master volume.
"""

from __future__ import annotations

from pycaw.pycaw import AudioUtilities


class AudioManager:

    def __init__(self):

        self.volume = AudioUtilities.GetSpeakers().EndpointVolume # type: ignore

    def set_volume(self, percent):

        percent = int(percent)
        percent = max(0, min(100, percent))

        self.volume.SetMasterVolumeLevelScalar(
            percent / 100,
            None
        )

        return True

    def get_volume(self):

        return round(
            self.volume.GetMasterVolumeLevelScalar() * 100
        )

    def volume_up(self, step=5):

        return self.set_volume(
            self.get_volume() + step
        )

    def volume_down(self, step=5):

        return self.set_volume(
            self.get_volume() - step
        )

    def mute(self):

        self.volume.SetMute(1, None)

        return True

    def unmute(self):

        self.volume.SetMute(0, None)

        return True

    def toggle_mute(self):

        self.volume.SetMute(
            not self.volume.GetMute(),
            None
        )

        return True