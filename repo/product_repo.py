from instance.database import db
from models.product import Products


class ProductRepository:
    @staticmethod
    def get_all():
        return Products.query.all()

    @staticmethod
    def get_by_id(product_id):
        return db.session.get(Products, product_id)

    @staticmethod
    def create(data):
        new_product = Products(**data)
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def update(product_id, data):
        product = db.session.get(Products, product_id)
        if not product:
            return None
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return product

    @staticmethod
    def delete(product_id):
        product = db.session.get(Products, product_id)
        if not product:
            return False
        db.session.delete(product)
        db.session.commit()
        return True
