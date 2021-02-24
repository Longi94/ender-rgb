import logging
from flask import Flask
from blueprint import blueprints
from logging_config import logging_config
from config import config
from utils.network import log_endpoints
from utils.network.response import json_response
from utils.network.exc import HttpException
from _version import __version__

log = logging.getLogger(__name__)

app = Flask(__name__)

for bp in blueprints:
    app.register_blueprint(bp)


@app.errorhandler(HttpException)
def handle_http_exception(e: HttpException):
    return json_response(e.code, e.message)


@app.errorhandler(Exception)
def handle_error(e):
    return json_response(500, str(e))


if __name__ == '__main__':
    logging_config()
    port = int(config.get('server', 'port'))
    log.info(f'Running ender-rgb {__version__} on port {port}')
    log_endpoints(log, app)

    app.run(host='0.0.0.0', port=port)
