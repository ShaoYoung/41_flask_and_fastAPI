# Генерация URL-адресов

from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>'
    text += f'Функция {url_for("test_url", num=42,data="new_data") = }<br>'
    text += f'Функция {url_for("test_url", num=42,data="new_data", pi=3.14515) = }<br>'
    return text


if __name__ == '__main__':
    app.run(debug=True)
