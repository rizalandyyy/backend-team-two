import unittest
from unittest.mock import MagicMock
from services.review_service import ReviewService

class TestReviewServiceGet(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.service = ReviewService()
        self.service.review_repo = self.mock_repo

    def test_get_review_by_product(self):
        mock_review_obj = MagicMock()
        mock_review_obj.to_dict.return_value = {
            'product_id': 1,
            'user_id': 2,
            'comment': 'test',
            'rating': 4
        }
        self.mock_repo.find_review_by_product.return_value = [mock_review_obj]
        reviews = self.service.get_review_by_product(1)
        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0]['product_id'], 1)

    def test_get_review(self):
        mock_review_obj = MagicMock()
        mock_review_obj.to_dict.return_value = {
            'product_id': 1,
            'user_id': 2,
            'comment': 'test',
            'rating': 4
        }
        self.mock_repo.find_review_by_user_and_product.return_value = mock_review_obj
        review = self.service.get_review(2, 1)
        self.assertEqual(review['product_id'], 1)
        self.assertEqual(review['user_id'], 2)

    def test_get_review_not_found(self):
        self.mock_repo.find_review_by_user_and_product.return_value = None
        with self.assertRaises(ValueError):
            self.service.get_review(2, 1)

    def test_get_all_reviews(self):
        mock_review_obj = MagicMock()
        mock_review_obj.to_dict.return_value = {
            'product_id': 1,
            'user_id': 2,
            'comment': 'test',
            'rating': 4
        }
        self.mock_repo.get_all_reviews.return_value = [mock_review_obj, mock_review_obj]
        reviews = self.service.get_all_reviews()
        self.assertEqual(len(reviews), 2)

    def test_get_reviews_by_user(self):
        mock_review_obj = MagicMock()
        mock_review_obj.to_dict.return_value = {
            'product_id': 1,
            'user_id': 2,
            'comment': 'test',
            'rating': 4
        }
        self.mock_repo.find_review_by_user.return_value = [mock_review_obj]
        reviews = self.service.get_review_by_user(2)
        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0]['user_id'], 2)

if __name__ == '__main__':
    unittest.main()