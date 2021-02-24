from flask import Blueprint, request
from led_strip import strip
from utils.network.decorators import json_required_params
from utils.network.response import ok

bp = Blueprint('light', __name__, url_prefix='/api/light')


@bp.route('/rgb', methods=['GET'])
def get_colors():
    colors = strip.get_colors()
    return ok(None, colors)


@bp.route('/rgb', methods=['POST'])
@json_required_params(['r', 'g', 'b'])
def set_color():
    body = request.json
    strip.set_color(body['r'], body['g'], body['b'])
    return ok()


@bp.route('/', methods=['DELETE'])
def off():
    strip.off()
    return ok()
