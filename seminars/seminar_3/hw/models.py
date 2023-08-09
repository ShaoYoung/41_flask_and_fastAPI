# Модели
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
# создаётся экземпляр
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    # лучше сделать отдельные методы у класса
    # def set_password(self, password):
    #     self.password = generate_password_hash()
    # def check_password(self, password):
# НЕ ДОПИСАНО !!!

