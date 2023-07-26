# cookie


from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    # создаём макет ответа
    response = make_response("Cookie установлен")
    # устанавливаем cookie (ключ username, значение admin)
    response.set_cookie('username', 'admin')
    return response


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
