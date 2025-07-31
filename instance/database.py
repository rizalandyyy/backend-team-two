from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *

db = SQLAlchemy()
migrate = Migrate()


def init_db(app):
    """Initialize the database and migration with the Flask app."""
    db.init_app(app)
    migrate.init_app(app, db)
