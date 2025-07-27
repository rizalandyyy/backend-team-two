import pytest
from config.settings import create_app
from instance.database import db as _db
from models.product import Products


@pytest.fixture(scope="session")
def app():
    """Create a Flask application instance for testing."""
    app = create_app("config.testing")
    with app.app_context():
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
def sample_product(db):
    """Create and return a sample product ID."""
    product = Products(
        name="Test Product",
        price=99.99,
        condition="new",
        image_url="http://example.com/image.jpg",
    )
    db.session.add(product)
    db.session.commit()
    return product.id  # return only the ID to avoid DetachedInstanceError
