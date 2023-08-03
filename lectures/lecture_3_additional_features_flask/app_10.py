# Flask-SQLAlchemy
# Получение данных из БД

from flask import Flask, render_template
from lectures.lecture_3_additional_features_flask.models_05 import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../../instance/mydatabase.db'
# инициализация БД
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'

@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/users/')
def all_users():
    # Получить всех User из БД
    users = User.query.all()
    # print(users)
    # создаётся словарь context
    context = {'users': users}
    # print(context)
    # return render_template('base.html')
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
