from flask import render_template, request, redirect, url_for

from app import app
from app.patterns import auth_strategy
from app.services.user_service import register_user


@app.route('/register/', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        try:
            user = register_user(
                username=request.form['username'],
                email=request.form['email'],
                password=request.form['password']
            )
            if user:
                return redirect(url_for('login'))
            else:
                return render_template("auth/register.html",
                                       error="Пользователь с таким именем или email уже существует.")
        except Exception as e:
            return render_template("auth/register.html", error=f"Ошибка регистрации: {e}")
    return render_template("auth/register.html")
