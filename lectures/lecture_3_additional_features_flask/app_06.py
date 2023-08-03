# Flask-SQLAlchemy

from flask import Flask
from lectures.lecture_3_additional_features_flask.models_05 import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# инициализация БД
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'

# в консоли flask init-db. создание БД
@app.cli.command("init-db")
def init_db():
    # показать ошибку с неверным wsgi.py
    # создать все таблицы
    db.create_all()
    print('OK')

# в консоли flask add-john. можно через app.route
@app.cli.command("add-john")
def add_user():
    # создаётся экземпляр класса User
    user = User(username='john', email='john@example.com')
    # добавляем экземпляр в БД (транзакция открыта, но не зафиксирована)
    db.session.add(user)
    # помещение строки в БД
    db.session.commit()
    print('John add in DB!')




if __name__ == '__main__':
    app.run(debug=True)
