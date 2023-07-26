# Обработка GET-запросов

from flask import Flask, url_for, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/get/')
def get():
    # В Python версии 3.8 появился моржовый оператор (walrus operator).
    # Он записывается как := и позволяет одновременно вычислить выражение, присвоить результат переменной и вернуть это значение, например в условие.
    if level := request.args.get('level'):
        # request содержит данные, которые клиент передаёт на сервер
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    dict_args = {}
    for key, value in request.args.items():
        dict_args.update({key: value})
    return text + f'{request.args}' + '<br>' + f'{dict_args}'


if __name__ == '__main__':
    app.run(debug=True)
