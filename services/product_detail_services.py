from models.product_detail import ProductDetails
from repo import product_detail_repo
from instance.database import db


def get_details_by_product_id(product_id):
    detail = product_detail_repo.get_details_by_product_id(product_id)
    if not detail:
        raise ValueError("Product detail not found")
    return detail


def get_detail_by_id(detail_id):
    detail = product_detail_repo.get_detail_by_id(detail_id)
    if not detail:
        raise ValueError("Product detail not found")
    return detail


def create_product_detail(data):
    detail = ProductDetails(
        product_id=data["product_id"],
        description=data.get("description"),
        image1_url=data.get("image1_url"),
        image2_url=data.get("image2_url"),
        image3_url=data.get("image3_url"),
    )
    product_detail_repo.create_product_detail(detail)
    db.session.commit()
    return detail


def update_product_detail(detail_id, data):
    detail = product_detail_repo.get_detail_by_id(detail_id)
    if not detail:
        raise ValueError("Product detail not found")

    detail.description = data.get("description", detail.description)
    detail.image1_url = data.get("image1_url", detail.image1_url)
    detail.image2_url = data.get("image2_url", detail.image2_url)
    detail.image3_url = data.get("image3_url", detail.image3_url)

    db.session.commit()
    return detail


def delete_product_detail(detail_id):
    detail = product_detail_repo.get_detail_by_id(detail_id)
    if not detail:
        raise ValueError("Product detail not found")
    product_detail_repo.delete_product_detail(detail)
    db.session.commit()
