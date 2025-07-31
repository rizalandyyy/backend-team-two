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
            f"<Review {self.id} for Products {self.product_id} by User {self.user_id}>"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "user_id": self.user_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
