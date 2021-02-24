import logging
from typing import Optional
from rpi_ws281x import *
from config import config
from led_strip.effect import effects

log = logging.getLogger(__name__)

CONFIG_PREFIX = 'led_strip'


class LedStrip(object):

    def __init__(self):
        self.strip = PixelStrip(
            config.getint(CONFIG_PREFIX, 'count'),
            config.getint(CONFIG_PREFIX, 'pin'),
            config.getint(CONFIG_PREFIX, 'freq_hz'),
            config.getint(CONFIG_PREFIX, 'dma'),
            config.getboolean(CONFIG_PREFIX, 'invert'),
            config.getint(CONFIG_PREFIX, 'brightness'),
            config.getint(CONFIG_PREFIX, 'channel')
        )
        self.strip.begin()
        self.effect: Optional[Effect] = None

    def off(self):
        self.set_color(0, 0, 0)

    def get_colors(self):
        pixels = []
        for i in range(self.strip.numPixels()):
            c = self.strip.getPixelColorRGB(i)
            pixels.append({
                'r': c.r,
                'g': c.g,
                'b': c.b,
            })
        return pixels

    def set_color(self, r: int, g: int, b: int):
        self.stop_effect()
        log.info(f'Setting color to ({r}, {g}, {b})')
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(r, g, b))
        self.strip.show()

    def set_effect(self, effect_name: str):
        if effect_name not in effects:
            raise NameError()

        effect = effects[effect_name](self)
        self.stop_effect()
        self.effect = effect
        self.effect.start()

    def get_effect_names(self):
        return list(effects.keys())

    def stop_effect(self):
        if self.effect:
            self.effect.stop()
            self.effect = None
