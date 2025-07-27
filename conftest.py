import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from config.settings import create_app
from instance.database import db as _db  # Use the actual app's db instance
from route.product_detail_route import product_detail_bp


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "testsecret"

    _db.init_app(app)  # Use _db here
    JWTManager(app)

    bcrypt = Bcrypt(app)
    app.extensions["bcrypt"] = bcrypt

    # ✅ REGISTER ROUTES
    app.register_blueprint(product_detail_bp, url_prefix="/product-details")

    with app.app_context():
        _db.create_all()
        yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    """Yields the db and tears down after each test."""
    with app.app_context():
        yield _db
        _db.session.remove()
        _db.drop_all()
