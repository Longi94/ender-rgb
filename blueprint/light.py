from flask import Blueprint, request
from led_strip import strip
from utils.network.decorators import json_required_params
from utils.network.response import ok
from utils.network.exc import BadRequestException

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


@bp.route('/effect', methods=['GET'])
def get_effects():
    return ok(None, strip.get_effect_names())


@bp.route('/effect', methods=['DELETE'])
def stop_effect():
    strip.stop_effect()
    return ok()


@bp.route('/effect/<effect_name>', methods=['POST'])
def set_effect(effect_name):
    try:
        strip.set_effect(effect_name)
    except NameError:
        raise BadRequestException('effect does not exist')
    return ok()


@bp.route('/', methods=['DELETE'])
def off():
    strip.off()
    return ok()
