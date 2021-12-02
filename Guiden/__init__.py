"""
Initial file of "Guiden" application.
"""
from flask import Flask

from sassutils.wsgi import SassMiddleware


def create_app():
    app = Flask(__name__)

    if app.config.get('ENV') == 'development':
        app.wsgi_app = SassMiddleware(
            app.wsgi_app,
            {
                'Guiden': ('static/scss', 'static/css', '/static/css', False),
            }
        )

    return app
