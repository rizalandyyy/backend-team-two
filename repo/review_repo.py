from models.review import Reviews
from instance.database import db


class ReviewRepository:

    @staticmethod
    def find_by_user(user_id):
        return Reviews.query.filter_by(user_id=user_id).all()

    @staticmethod
    def find_by_product(product_id):
        return Reviews.query.filter_by(product_id=product_id).all()

    @staticmethod
    def find_by_user_and_product(user_id, product_id):
        return Reviews.query.filter_by(user_id=user_id, product_id=product_id).first()

    @staticmethod
    def get_all():
        return Reviews.query.all()

    @staticmethod
    def create(data):
        review = Reviews(**data)
        db.session.add(review)
        db.session.commit()
        return review

    @staticmethod
    def update(existing_review, data):
        for key, value in data.items():
            setattr(existing_review, key, value)
        db.session.commit()
        return existing_review

    @staticmethod
    def delete(review):
        db.session.delete(review)
        db.session.commit()
