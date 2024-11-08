from flask import render_template, request, redirect, url_for, session
from flask_login import login_required, current_user, logout_user, login_user, LoginManager

from app import app
from app.patterns.auth_strategy import DatabaseAuthStrategy
from app.models.users import User

# Инициализируйте LoginManager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Логируем данные перед аутентификацией
        app.logger.debug(f'Username: {username}, Password: {password}')

        # Используем стратегию аутентификации
        auth_strategy = DatabaseAuthStrategy(User)
        user = auth_strategy.authenticate(username, password)

        if user:
            login_user(user)  # Используем Flask-Login для входа пользователя
            return redirect(url_for("index"))

    return render_template("auth/login.html")


@app.route('/logout/')
@login_required  # Защита маршрута: требуется авторизованный пользователь
def logout():
    logout_user()  # Используем Flask-Login для выхода
    return redirect(url_for("index"))


# Теперь можно защитить другие маршруты
@app.route('/protected_route/')
@login_required
def protected_route():
    return "This is a protected route. Welcome, {}!".format(current_user.username)
