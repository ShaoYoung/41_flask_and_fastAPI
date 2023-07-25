# импортируем класс Flask. Стандартное начало любого приложения на Flask.
from flask import Flask
from flask import render_template

# создаём экземпляр класса Flask (приложение) и передаём название файла
app = Flask(__name__)

@app.route('/index/')
def html_index():
    return render_template('index1.html')


if __name__ == '__main__':
    app.run(debug=True)
