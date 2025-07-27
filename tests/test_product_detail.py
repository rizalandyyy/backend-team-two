import pytest
from instance.database import db
from models.product import Products
from models.product_detail import ProductDetails


@pytest.fixture
def app():
    from config.settings import create_app

    app = create_app("config.testing")
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()


@pytest.fixture
def sample_product(app):
    with app.app_context():
        product = Products(
            name="Test Product",
            price=100.0,
            condition="new",
            image_url="http://example.com/image.jpg",
        )
        db.session.add(product)
        db.session.commit()
        yield product
        db.session.delete(product)
        db.session.commit()


def test_create_product_detail(client, sample_product):
    payload = {
        "product_id": sample_product.id,
        "description": "A sample detail",
        "image1_url": "http://img1.com",
        "image2_url": "http://img2.com",
        "image3_url": "http://img3.com",
    }
    response = client.post("/product-details", json=payload)
    assert response.status_code == 201


def test_create_product_detail_missing_field(client):
    payload = {"description": "Missing product_id"}

    response = client.post("/product-details", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


def test_get_product_detail(client, sample_product):
    detail = ProductDetails(
        product_id=sample_product.id,
        description="Test desc",
        image1_url="url1",
        image2_url="url2",
        image3_url="url3",
    )
    db.session.add(detail)
    db.session.commit()

    response = client.get(f"/product-details/{sample_product.id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["description"] == "Test desc"
