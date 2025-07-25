from instance.database import db
from shared import crono
from models.product import Product


class ProductDetails(db.Model):
    __tablename__ = "product_details"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image1_url = db.Column(db.Text, nullable=True)
    image2_url = db.Column(db.Text, nullable=True)
    image3_url = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=crono.now)
    updated_at = db.Column(db.DateTime, default=crono.now, onupdate=crono.now)

    product = db.relationship("Products", back_populates="details")

    def __repr__(self):
        return f"<ProductDetails {self.id} for Product {self.product_id}>"
