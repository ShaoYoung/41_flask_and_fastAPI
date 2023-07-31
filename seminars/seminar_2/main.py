# Все задания

from pathlib import PurePath, Path
from flask import Flask, request, render_template, abort, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'ddb4b937bfc272f7139dea217630a099cd148cc1bacec6e324d9beb0b952775a'


# обработка всех запросов
@app.route('/')
def index():
    return render_template('main.html')


@app.route('/hello')
def hello1():
    return 'Привет, хозяин!'


@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'static/image', file_name))
        return render_template('task2_1.html', file_name=file_name)
    return render_template('task2.html')


users = {
    'admin': '123',
    'user': '111'
}


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username, password) in users.items():
            return 'Вы вошли'
        return 'Неправильный логин или пароль'
    return render_template('task3.html')


@app.route('/count/', methods=['GET', 'POST'])
def count():
    if request.method == 'POST':
        text = request.form.get('text')
        count = len(text.split())
        return f'Количество слов {count}'
    return render_template('task4.html')


@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        number1 = int(request.form.get('number1'))
        number2 = int(request.form.get('number2'))
        operation = request.form.get('operation')
        if operation == 'add':
            return f'{number1 + number2}'
        elif operation == 'subtract':
            return f'{number1 - number2}'
        elif operation == 'multiply':
            return f'{number1 * number2}'
        elif operation == 'divide':
            return f'{number1 / number2}'
    return render_template('task5.html')


@app.errorhandler(403)
@app.route('/age/', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        username = request.form.get('name')
        age = int(request.form.get('age'))
        if age < 18:
            # return render_template('403.html'), 403
            return abort(403)
        return f'{username}, {age} возможен'
    return render_template('task6.html')


@app.errorhandler(403)
def forbidden(e):
    print(e)
    return render_template('403.html'), 403


@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        result = number ** 2
        return redirect(url_for('calc_square', result=result))
    return render_template('task7.html')


@app.route('/calc_square')
def calc_square():
    return request.args.get('result')


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Hello {name}', 'success')
        return redirect(url_for('form'))
    return render_template('task8.html')


if __name__ == '__main__':
    app.run(debug=True)
