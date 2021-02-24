from typing import List
from flask import Blueprint
from . import light

blueprints: List[Blueprint] = [
    light.bp
]
