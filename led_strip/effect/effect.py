import threading
import time
from typing import Optional


class Effect(object):

    def __init__(self, strip, period: int = 50):
        self.strip = strip
        self.period = period
        self.running = False
        self.thread: Optional[threading.Thread] = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False

    def run(self):
        iteration = 0
        while self.running:
            self.update(iteration)
            self.strip.strip.show()
            iteration += 1
            time.sleep(self.period / 1000.0)

    def update(self, i: int):
        raise NotImplementedError()
