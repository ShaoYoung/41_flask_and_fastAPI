# Модели
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# создаётся объект БД
db = SQLAlchemy()


# Создаётся класс User, к-й наследуется от класса db.Model
class User(db.Model):
    # колонка id, тип Integer, первичный ключ. создавать везде
    id = db.Column(db.Integer, primary_key=True)
    # колонка username, тип строка (max длина 80), проверка уникальности, не может быть пустым
    username = db.Column(db.String(80), unique=True, nullable=False)
    # колонка email, тип строка (max длина 120), проверка уникальности, не может быть пустым
    email = db.Column(db.String(120), unique=True, nullable=False)
    # колонка created, тип DateTime, значение по умолчанию datetime.utcnow
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # создание связи между Post и User
    # взаимодействие с Post, backref - обратная ссылка, lazy=True - ленивый режим
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.username}, {self.email})'


# Создаётся класс User, к-й наследуется от класса db.Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # внешний ключ (ссылка на user.id)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Post({self.title}, {self.content})'


# создаётся класс Comment
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Comment({self.content})'
