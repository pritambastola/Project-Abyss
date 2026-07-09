"""
Display Manager

Controls screen brightness.
"""

from __future__ import annotations

import screen_brightness_control as sbc


class DisplayManager:

    def set_brightness(self, value):

        value = max(0, min(100, int(value)))

        sbc.set_brightness(value)

        return True

    def get_brightness(self):

        return sbc.get_brightness()[0]

    def brightness_up(self, step=10):

        return self.set_brightness(
            self.get_brightness() + step
        )

    def brightness_down(self, step=10):

        return self.set_brightness(
            self.get_brightness() - step
        )