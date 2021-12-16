from flask import Blueprint, current_app

from sassutils.wsgi import SassMiddleware

from .views import home as home_view

home_blueprint = Blueprint(
    "home",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/home")

if current_app.config.get('ENV') != 'production':
        home_blueprint.wsgi_app = SassMiddleware(
            home_blueprint.wsgi_app,
            {
                'Guiden': ('static/scss', 'static/css', '/static/home/css', False),
            }
        )


home_blueprint.add_url_rule('/', view_func=home_view)
home_blueprint.add_url_rule('/home', view_func=home_view)
