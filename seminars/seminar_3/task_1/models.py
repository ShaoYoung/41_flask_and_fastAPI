# Модели
from flask_sqlalchemy import SQLAlchemy

# создаётся экземпляр
db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Boolean, nullable=False)
    group = db.Column(db.String(10), nullable=False)
    faculty_id = db.Column(db.ForeignKey('faculty.id'))

    def __repr__(self):
        return f'Student({self.name}, {self.surname})'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # ссылка на Student
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty({self.name})'


