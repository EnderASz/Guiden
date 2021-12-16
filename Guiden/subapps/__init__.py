from flask import Blueprint

from . import home

subapps_blueprint = Blueprint('subapps', __name__)

subapps_blueprint.register_blueprint(home.home_blueprint)

__all__ = [
    "home",
]
