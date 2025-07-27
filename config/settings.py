import models  # noqa: F401

from flask import Flask
from instance.database import init_db
from route.index import index_router
from route.product import product_bp

def create_app(config_module="config.local"):
    """Create a Flask application instance."""
    app = Flask(__name__)
    app.config.from_object(config_module)

    # Initialize database and migration
    init_db(app)

    # Register blueprints
    app.register_blueprint(index_router)
    app.register_blueprint(product_bp)

    return app
