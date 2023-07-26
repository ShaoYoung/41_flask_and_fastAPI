# make_response
from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Главная',
        'name': 'Харитон'
    }
    response = make_response(render_template('main.html', **context))
    # Заголовочная информация, которая идёт поверх html-страницы
    response.headers['new_head'] = 'New value'
    response.set_cookie('username', context['name'])
    return response


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
