from flask import Blueprint

from . import home
from . import search

subapps_blueprint = Blueprint('', __name__)

subapps_blueprint.register_blueprint(home.home_blueprint)
subapps_blueprint.register_blueprint(
    search.search_blueprint,
    url_prefix='/search')

__all__ = [
    "home",
    "search",
]
