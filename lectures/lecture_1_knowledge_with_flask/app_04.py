# импортируем класс Flask. Стандартное начало любого приложения на Flask.
from flask import Flask

# создаём экземпляр класса Flask (приложение) и передаём название файла
app = Flask(__name__)

# Логика обработки URL

# Строка
@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    # <name> - скобки - указание на то, что это не адрес, а переменная
    return f'Привет, {name.capitalize()}!'

# Путь
@app.route('/file/<path:file>/')
def set_path(file):
    # Содержимое строки после path воспринимается как путь и попадает в переменную file независимо от количества слешей
    print(type(file))
    return f'Путь до файла "{file}"'

# Число с плавающей запятой.
@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


# Int.
@app.route('/int/<int:num>/')
def set_int(num):
    print(type(num))
    return f'Передано число {num}'


if __name__ == '__main__':
    app.run(debug=True)


