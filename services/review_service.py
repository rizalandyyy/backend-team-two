from repo.review_repo import ReviewRepository


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
