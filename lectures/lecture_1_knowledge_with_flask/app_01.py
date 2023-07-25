# импортируем класс Flask. Стандартное начало любого приложения на Flask.
from flask import Flask

# создаём экземпляр класса Flask (приложение) и передаём название файла
app = Flask(__name__)


# приложение app использует метод route в качестве декоратора
@app.route('/')
def hello_world():
    return 'Hello World!'
    # return str(42)


# если файл запускается напрямую, код ниже будет выполнен
if __name__ == '__main__':
    # запуск flask-сервера
    app.run(debug=True)

# запуск из терминала
# flask --app lectures\lecture_1_knowledge_with_flask\app_01.py run
