# Задание №9
# 📌 Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# 📌 Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def html_task_9():
    return render_template('task_9.html')


if __name__ == '__main__':
    app.run(debug=True)
