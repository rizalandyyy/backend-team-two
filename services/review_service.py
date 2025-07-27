from repo.review_repo import ReviewRepository
from datetime import datetime

class ReviewService:
    def __init__(self):
        self.review_repo = ReviewRepository()

    def get_review_by_user(self, user_id):
        reviews = self.review_repo.find_review_by_user(user_id)
        if not reviews:
            raise ValueError('Review tidak ditemukan.')
        return [review.to_dict() for review in reviews]
    
    def get_review_by_product(self, product_id):
        reviews = self.review_repo.find_review_by_product(product_id)
        if not reviews:
            raise ValueError('Review tidak ditemukan.')
        return [review.to_dict() for review in reviews]
    
    def get_review(self, user_id, product_id):
        review = self.review_repo.find_review_by_user_and_product(user_id, product_id)
        if not review:
            raise ValueError('Review tidak ditemukan.')
        return review.to_dict()

    def get_all_reviews(self):
        reviews = self.review_repo.get_all_reviews()
        return [review.to_dict() for review in reviews]
