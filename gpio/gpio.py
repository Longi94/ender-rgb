import logging
import RPi.GPIO as GPIO
from config import config
from led_strip import strip
from octopi import client

log = logging.getLogger(__name__)

BOUNCE_TIME = 200

POWER_BUTTON_PIN = config.getint('gpio', 'power_button_pin')
LED_BUTTON_PIN = config.getint('gpio', 'led_button_pin')
STOP_BUTTON_PIN = config.getint('gpio', 'stop_button_pin')


def detect_callback(pin):
    log.info(f'Got callback on pin {pin}')
    if pin == POWER_BUTTON_PIN:
        client.toggle_power()
    elif pin == LED_BUTTON_PIN:
        strip.toggle()
    elif pin == STOP_BUTTON_PIN:
        client.stop_print()


def init():
    GPIO.setmode(GPIO.BCM)

    log.info(f'Power button pin: {POWER_BUTTON_PIN}')
    log.info(f'Stop button pin: {STOP_BUTTON_PIN}')
    log.info(f'LED button pin: {LED_BUTTON_PIN}')

    GPIO.setup(POWER_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(STOP_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(POWER_BUTTON_PIN, GPIO.FALLING, callback=detect_callback, bouncetime=BOUNCE_TIME)
    GPIO.add_event_detect(STOP_BUTTON_PIN, GPIO.FALLING, callback=detect_callback, bouncetime=BOUNCE_TIME)
    GPIO.add_event_detect(LED_BUTTON_PIN, GPIO.FALLING, callback=detect_callback, bouncetime=BOUNCE_TIME)

    log.info('Initialized GPIO pins')


def close():
    log.info('GPIO cleanup')
    GPIO.cleanup()
