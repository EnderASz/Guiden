from flask import Blueprint

from .views import login as login_view


auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='templates')

auth_blueprint.add_url_rule('/', view_func=login_view)
auth_blueprint.add_url_rule('/login', view_func=login_view)
