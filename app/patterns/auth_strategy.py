# app/auth_strategy.py
from werkzeug.security import check_password_hash


class AuthStrategy:
    def authenticate(self, username, password):
        raise NotImplementedError("Этот метод должен быть переопределен.")


class DatabaseAuthStrategy(AuthStrategy):
    def __init__(self, UserModel):
        self.UserModel = UserModel

    def authenticate(self, username, password):
        user = self.UserModel.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user
        return None
