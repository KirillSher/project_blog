# Блог на Flask

## Описание:

Это простой блог, созданный на основе фреймворка Flask. 

## Требования:

  - Python 3.6+
  - Flask
  - Flask-SQLAlchemy
  - Flask-Login
  - Flask-Admin

## Установка:

  1. Клонируйте репозиторий:
  ```shell
    git clone https://github.com/your_username/your_blog_repo.git
  ```
    
  2. Установите зависимости:  
  ```shell
    pip install -r requirements.txt
  ```
    
  3. Запустите сервер разработки:  
  ```shell
    python .\run.py
  ```
  
## Настройка:

  1. Скопируйте файл .env.example в .env и заполните его необходимыми значениями для:
    * SECRET_KEY: Секретный ключ для Flask.
    * DATABASE_URL: URL для подключения к базе данных (например, sqlite:///blog.db для SQLite).
  2. Скопируйте файл config.example.py в config.py и измените настройки (если требуется).

## Использование:

  1. Запустите сервер разработки (см. "Установка").
  2. Откройте браузер и перейдите на адрес http://127.0.0.1:5000/.
  3. Используйте блог как обычно!

## Дополнительная информация:

  - [Flask Documentation](https://flask.palletsprojects.com/)
  - [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
  - [Flask-Login Documentation](https://flask-login.readthedocs.io/)
  - [Flask-Admin Documentation](https://flask-admin.readthedocs.io/en/latest/)

## Автор:

  - KirillSher
