from flask import Blueprint

from .views import search_page as search_page_view


search_blueprint = Blueprint(
    'search',
    __name__,
    template_folder="templates")


search_blueprint.add_url_rule(
    '/',
    view_func=search_page_view,
    defaults={'page': 0})
search_blueprint.add_url_rule(
    '/<int:page>',
    view_func=search_page_view)

