# Flask-SQLAlchemy

from flask import Flask
from lectures.lecture_3_additional_features_flask.models_05 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# инициализация БД
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'

# обработчик команды init-db в командной строке
# предварительно надо импортировать этот модуль в wsgi.py
# flask init-db
@app.cli.command("init-db")
def init_db():
    # показать ошибку с неверным wsgi.py
    # создать все таблицы
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)
