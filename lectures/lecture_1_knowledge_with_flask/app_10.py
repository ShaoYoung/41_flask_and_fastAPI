# импортируем класс Flask. Стандартное начало любого приложения на Flask.
from flask import Flask, render_template

# создаём экземпляр класса Flask (приложение) и передаём название файла
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/users/')
def users():
    _users = [{'name': 'Никанор',
               'mail': 'nik@mail.ru',
               'phone': '+7-987-654-32-10',
               },
              {'name': 'Феофан',
               'mail': 'feo@mail.ru',
               'phone': '+7-987-444-33-22',
               },
              {'name': 'Оверран',
               'mail': 'forest@mail.ru',
               'phone': '+7-903-333-33-33',
               }, ]
    context = {'users': _users}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
