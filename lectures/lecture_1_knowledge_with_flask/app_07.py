# импортируем класс Flask. Стандартное начало любого приложения на Flask.
from flask import Flask, render_template

# создаём экземпляр класса Flask (приложение) и передаём название файла
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/index/')
def html_index():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон',
    }
    return render_template('index2.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
