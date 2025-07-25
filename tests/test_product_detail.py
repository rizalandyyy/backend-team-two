import json
import pytest
from models.product_detail import ProductDetails
from models.product import Products
from instance.database import db


@pytest.fixture
def sample_product(app, db):
    """Insert sample product for foreign key reference."""
    product = Products(
        name="Sample Product",
        price=9.99,
        condition="New",
    )  # sesuaikan field dengan model Products kamu
    db.session.add(product)
    db.session.commit()
    return product


def test_create_product_detail(client, db, sample_product):
    payload = {
        "product_id": sample_product.id,
        "description": "Deskripsi produk",
        "image1_url": "http://example.com/img1.jpg",
        "image2_url": "http://example.com/img2.jpg",
        "image3_url": "http://example.com/img3.jpg",
    }
    response = client.post(
        "/product-details/", data=json.dumps(payload), content_type="application/json"
    )
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data
    assert data["message"] == "Created"


def test_get_all_product_details(client, db, sample_product):
    # Create one manually
    detail = ProductDetails(product_id=sample_product.id, description="Test")
    db.session.add(detail)
    db.session.commit()

    response = client.get("/product-details/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert any(d["description"] == "Test" for d in data)


def test_get_single_product_detail(client, db, sample_product):
    detail = ProductDetails(product_id=sample_product.id, description="Single")
    db.session.add(detail)
    db.session.commit()

    response = client.get(f"/product-details/{detail.id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == detail.id
    assert data["description"] == "Single"


def test_update_product_detail(client, db, sample_product):
    detail = ProductDetails(product_id=sample_product.id, description="Old")
    db.session.add(detail)
    db.session.commit()

    payload = {"description": "Updated Description"}
    response = client.put(
        f"/product-details/{detail.id}",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Updated"

    updated_detail = ProductDetails.query.get(detail.id)
    assert updated_detail.description == "Updated Description"


def test_delete_product_detail(client, db, sample_product):
    detail = ProductDetails(product_id=sample_product.id, description="To delete")
    db.session.add(detail)
    db.session.commit()

    response = client.delete(f"/product-details/{detail.id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Deleted"

    deleted = ProductDetails.query.get(detail.id)
    assert deleted is None


def test_get_nonexistent_detail(client):
    response = client.get("/product-details/99999")
    assert response.status_code == 404
    data = response.get_json()
    assert data["error"] == "Not found"
