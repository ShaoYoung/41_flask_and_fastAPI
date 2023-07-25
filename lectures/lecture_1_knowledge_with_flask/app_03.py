# импортируем класс Flask. Стандартное начало любого приложения на Flask.
from flask import Flask

# создаём экземпляр класса Flask (приложение) и передаём название файла
app = Flask(__name__)


# Множественное декорирование
# Одна функция-представление может быть декорирована несколькими декораторами.
@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Феодор!'


if __name__ == '__main__':
    # запуск flask-сервера
    app.run(debug=True)

# запуск из терминала
# flask --app lectures\lecture_1_knowledge_with_flask\app_01.py run

# если есть wsgi.py, то можно запускать из терминала flask run
