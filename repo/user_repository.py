from instance.database import db
from models.user import Users

class UserRepository:
    @staticmethod
    def create_user(username, email, password_hash):
        """Create a new user in the database."""
        new_user = Users(username=username, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def get_user_by_username(username):
        return Users.query.filter_by(username=username).first()

    @staticmethod
    def get_user_by_email(email):
        return Users.query.filter_by(email=email).first()
    
    @staticmethod
    def get_user_by_id(user_id):
        return Users.query.get(user_id)