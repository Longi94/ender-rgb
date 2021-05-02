import logging
import requests
from config import config

CONFIG_PREFIX = 'octopi'

log = logging.getLogger(__name__)


class OctoPiClient(object):

    def __init__(self):
        self.base_url = config.get(CONFIG_PREFIX, 'base_url')
        self.api_key = config.get(CONFIG_PREFIX, 'api_key')

    def request(self, method: str, path: str, body: dict = None):
        url = f'{self.base_url}/{path}'
        headers = {
            'X-Api-Key': self.api_key
        }
        return requests.request(method, url, headers=headers, json=body)

    def get(self, path: str):
        return self.request('GET', path)

    def post(self, path: str, body: dict = None):
        return self.request('POST', path, body)

    def command(self, path: str, command: str):
        return self.post(path, {'command': command})

    def plugin_command(self, plugin: str, command: str):
        return self.command(f'plugin/{plugin}', command)

    def toggle_power(self):
        log.debug('power toggle')
        return self.plugin_command('psucontrol', 'togglePSU')

    def stop_print(self):
        log.debug('stop print')
        return self.command('jon', 'cancel')
