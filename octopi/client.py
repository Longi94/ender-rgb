import logging

log = logging.getLogger(__name__)


class OctoPiClient(object):

    def toggle_power(self):
        log.debug('power toggle')

    def stop_print(self):
        log.debug('stop print')
