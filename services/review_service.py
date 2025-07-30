from repo.review_repo import ReviewRepository
from models.review import Reviews
from instance.database import db


class ReviewService:
    def __init__(self):
        self.repo = ReviewRepository()

    def get_reviews_by_user(self, user_id):
        reviews = self.repo.find_by_user(user_id)
        if not reviews:
            raise ValueError("No reviews found for this user.")
        return [review.to_dict() for review in reviews]

    def get_reviews_by_product(self, product_id):
        reviews = self.repo.find_by_product(product_id)
        if not reviews:
            raise ValueError("No reviews found for this product.")
        return [review.to_dict() for review in reviews]

    def get_review(self, user_id, product_id):
        review = self.repo.find_by_user_and_product(user_id, product_id)
        if not review:
            raise ValueError("Review not found.")
        return review.to_dict()

    def get_all_reviews(self):
        reviews = self.repo.get_all()
        return [review.to_dict() for review in reviews]

    def create_review(self, data):
        # Prevent duplicate review by same user for same product
        existing = self.repo.find_by_user_and_product(
            data["user_id"], data["product_id"]
        )
        if existing:
            raise ValueError("Review already exists for this product by the user.")

        new_review = Reviews(
            user_id=data["user_id"],
            product_id=data["product_id"],
            rating=data["rating"],
            comment=data.get("comment", ""),
        )
        db.session.add(new_review)
        db.session.commit()
        return new_review.to_dict()

    def update_review(self, user_id, product_id, data):
        review = self.repo.find_by_user_and_product(user_id, product_id)
        if not review:
            raise ValueError("Review not found.")

        # Ownership check already handled in route using get_jwt_identity

        if "rating" in data:
            review.rating = data["rating"]
        if "comment" in data:
            review.comment = data["comment"]

        db.session.commit()
        return review.to_dict()

    def delete_review(self, user_id, product_id):
        review = self.repo.find_by_user_and_product(user_id, product_id)
        if not review:
            raise ValueError("Review not found.")

        # Ownership check already handled in route using get_jwt_identity

        db.session.delete(review)
        db.session.commit()
