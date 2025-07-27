from models.product_detail import ProductDetails
from instance.database import db


def get_details_by_product_id(product_id):
    return ProductDetails.query.filter_by(product_id=product_id).first()


def get_detail_by_id(detail_id):
    return ProductDetails.query.get(detail_id)


def create_product_detail(detail):
    db.session.add(detail)


def update_product_detail():
    pass  # SQLAlchemy tracks changes


def delete_product_detail(detail):
    db.session.delete(detail)
