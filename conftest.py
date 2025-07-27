import pytest
from config.settings import create_app
from instance.database import db as _db  # Use the actual app's db instance
from route.product_detail_route import product_detail_bp


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
def db(app):
    """Create a new database for the test session."""
    _db.app = app
    _db.create_all()
    yield _db
    _db.drop_all()


@pytest.fixture
def client(app, db):
    """Create a test client for the Flask application."""
    return app.test_client()


@pytest.fixture
def db(app):
    """Yields the db and tears down after each test."""
    with app.app_context():
        yield _db
        _db.session.remove()
        _db.drop_all()
