import datetime

from flask_login import UserMixin

from app.models import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=False, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), default='user')
    avatar = db.Column(db.String(255), default='default_avatar.png')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    tags = db.relationship('Tag', backref='user_tag', lazy=True, cascade="all, delete-orphan")
    posts = db.relationship('Post', backref='author', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return self.username

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True
