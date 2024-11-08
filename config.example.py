import os


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI') or 'sqlite:///your_database.db'

    # Дополнительные настройки
    SQLALCHEMY_TRACK_MODIFICATIONS = False
