from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from werkzeug.security import generate_password_hash

from app import app, db
from app.models import User, Post, Tag


class UserAdmin(ModelView):
    form_base_class = SecureForm

    # Хэшируем пароль при создании нового пользователя
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.password = generate_password_hash(model.password, method='pbkdf2:sha256', salt_length=8)
        return super(UserAdmin, self).on_model_change(form, model, is_created)


# Инициализация админ-панели
admin = Admin(app, name='Блог Admin', template_mode='bootstrap3')

# Добавление представлений для моделей
admin.add_view(UserAdmin(User, db.session, name='Пользователи'))
admin.add_view(ModelView(Post, db.session, name='Посты'))
admin.add_view(ModelView(Tag, db.session, name='Теги'))
