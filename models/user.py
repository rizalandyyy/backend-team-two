import enum
from instance.database import db
from shared import crono


class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.USER, nullable=False)
    created_at = db.Column(db.DateTime, default=crono.now)
    updated_at = db.Column(db.DateTime, default=crono.now, onupdate=crono.now)

    reviews = db.relationship('Reviews', back_populates='user')


    def __repr__(self):
        return f"<User {self.username}>"
