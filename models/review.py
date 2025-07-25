from instance.database import db
from shared import crono


class Reviews(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # e.g., 1 to 5 stars
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=crono.now)
    updated_at = db.Column(db.DateTime, default=crono.now, onupdate=crono.now)

    product = db.relationship("Products", back_populates="reviews")
    user = db.relationship("Users", back_populates="reviews")

    def __repr__(self):
        return (
            f"<Review {self.id} for Product {self.product_id} by User {self.user_id}>"
        )
