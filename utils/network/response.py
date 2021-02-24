from flask import jsonify


def json_response(code: int, message: str = None, response=None):
    response_body = {'code': code}

    if message:
        response_body['message'] = message

    if response:
        response_body['response'] = response

    return jsonify(response_body), code


def ok(message: str = None, response=None):
    return json_response(200, message, response)
