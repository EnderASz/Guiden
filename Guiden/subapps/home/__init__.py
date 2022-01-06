from flask import Blueprint

from .views import home as home_view

home_blueprint = Blueprint(
    "home",
    __name__,
    template_folder="templates")


home_blueprint.add_url_rule('/', view_func=home_view)
home_blueprint.add_url_rule('/home', view_func=home_view)
