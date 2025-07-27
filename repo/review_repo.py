from models.review import Reviews
from instance.database import db

class ReviewRepository:

    @staticmethod
    def find_review_by_user(user_id):
        return Reviews.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def find_review_by_product(product_id):
        return Reviews.query.filter_by(product_id=product_id).all()
    
    @staticmethod
    def find_review_by_user_and_product(user_id, product_id):
        return Reviews.query.filter_by(user_id=user_id, product_id=product_id).first()
    
    @staticmethod
    def get_all_reviews():
        return Reviews.query.all()