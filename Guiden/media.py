from flask import Blueprint, current_app, send_from_directory


media_blueprint = Blueprint('media', __name__)

@media_blueprint.route('/<path:filename>')
def public(filename):
    return send_from_directory(current_app.config['PUBLIC_MEDIA_ROOT'], filename)
