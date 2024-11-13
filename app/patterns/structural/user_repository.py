from werkzeug.security import generate_password_hash

from app.models import User, db


class UserRepository:
    @staticmethod
    def create_user(username, email, password):
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return None

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
