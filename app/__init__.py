import os

from flask import Flask

from app.models import db
from config import Config

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

from app.routes.auth import login, auth_bp
from app.routes import auth, home, profile, admin, posts
app.register_blueprint(auth_bp, url_prefix='/auth')  # Все маршруты будут начинаться с /auth

app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
