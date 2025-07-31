from instance.database import db
from models.product_detail import ProductDetails


class ProductDetailRepository:
    @staticmethod
    def get_all():
        return ProductDetails.query.all()

    @staticmethod
    def get_by_id(detail_id):
        return db.session.get(ProductDetails, detail_id)

    @staticmethod
    def create(data):
        new_detail = ProductDetails(**data)
        db.session.add(new_detail)
        db.session.commit()
        return new_detail

    @staticmethod
    def update(detail_id, data):
        detail = db.session.get(ProductDetails, detail_id)
        if not detail:
            return None
        for key, value in data.items():
            setattr(detail, key, value)
        db.session.commit()
        return detail

    @staticmethod
    def delete(detail_id):
        detail = db.session.get(ProductDetails, detail_id)
        if not detail:
            return False
        db.session.delete(detail)
        db.session.commit()
        return True
