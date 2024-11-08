# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .users import User
from .posts import Post
from .tags import Tag
