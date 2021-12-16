"""
Initial file of "Guiden" application.
"""
from flask import Flask

from sassutils.wsgi import SassMiddleware

from .default_configs import Config, DevelopmentConfig
from . import mongo

from .subapps import subapps_blueprint


def create_app():
    app = Flask(__name__)

    enviroment = app.config.get('ENV')
    app.config.from_object(
        DevelopmentConfig
        if enviroment != 'production'
        else Config)
    if not app.config.from_envvar('GUIDEN_CFG', True):
        print(" * WARNING: Custom config could not be found. Application "
              f"currently use only default config for {enviroment}.")

    if enviroment != 'production':
        app.wsgi_app = SassMiddleware(
            app.wsgi_app,
            {
                'Guiden': ('static/scss', 'static/css', '/static/css', False),
            }
        )

    app.register_blueprint(subapps_blueprint)

    mongo.init(app)

    return app
