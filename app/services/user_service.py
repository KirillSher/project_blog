# services/user_service.py (дополните функцию)
from werkzeug.security import generate_password_hash

from app.models.users import User, db


def register_user(username, email, password):
    # Проверка на существование пользователя с данным именем или email
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return None  # Или бросьте исключение с сообщением об ошибке

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user
