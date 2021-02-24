from .effect import Effect
from led_strip.color import wheel


class RainbowCycle(Effect):

    def __init__(self, strip):
        super(RainbowCycle, self).__init__(strip, 20)

    def update(self, i: int):
        strip = self.strip.strip
        j = i % 256
        for k in range(strip.numPixels()):
            strip.setPixelColor(k, wheel((int(k * 256 / strip.numPixels()) + j) & 255))
