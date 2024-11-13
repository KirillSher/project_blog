# services/user_service.py (дополните функцию)

from app.patterns.structural.user_repository import UserRepository


def register_user(username, email, password):
    user_repository = UserRepository()
    return user_repository.create_user(username, email, password)
