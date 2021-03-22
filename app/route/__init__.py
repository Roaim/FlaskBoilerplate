from flask_jwt_extended import JWTManager
from ..errors import handle_errors
from .user_route import bp as user_bp
from .address_route import bp as address_bp


jwt = JWTManager()


def init_app(app):
    jwt.init_app(app)
    app.url_map.strict_slashes = False
    handle_errors(app)
    app.register_blueprint(user_bp)
    app.register_blueprint(address_bp)
