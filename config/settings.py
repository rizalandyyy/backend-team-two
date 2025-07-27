import models  # noqa: F401

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from instance.database import init_db
from route.index import index_router
from route.product_routes import product_bp
from route.auth import auth_bp


def create_app(config_module="config.local"):
    """Create a Flask application instance."""
    app = Flask(__name__)
    app.config.from_object(config_module)

    # Initialize Flask extensions
    bcrypt = Bcrypt()
    jwt = JWTManager()
    bcrypt.init_app(app)
    jwt.init_app(app)
    app.extensions["bcrypt"] = bcrypt
    app.extensions["jwt"] = jwt

    # Initialize database and migration

    init_db(app)

    # Register blueprints
    app.register_blueprint(index_router)
    app.register_blueprint(product_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
