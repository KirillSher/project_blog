import datetime

from app.models import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    views = db.Column(db.Integer, nullable=True, default=0)
    likes = db.Column(db.Integer, nullable=True, default=0)

    tags = db.relationship('Tag', backref='post_tag', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return self.title
