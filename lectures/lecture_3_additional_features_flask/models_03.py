# Модели
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# создаётся объект БД
db = SQLAlchemy()

# Создаётся класс, к-й наследуется от класса db.Model
class User(db.Model):
    # колонка id, тип Integer, первичный ключ
    id = db.Column(db.Integer, primary_key=True)
    # колонка username, тип строка (max длина 80), проверка уникальности, не может быть пустым
    username = db.Column(db.String(80), unique=True, nullable=False)
    # колонка email, тип строка (max длина 120), проверка уникальности, не может быть пустым
    email = db.Column(db.String(120), unique=True, nullable=False)
    # колонка created, тип DateTime, значение по умолчанию datetime.utcnow
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'User({self.username}, {self.email})'
