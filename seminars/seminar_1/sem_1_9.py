# Задание №9
# 📌 Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# 📌 Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.


from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def base():
    context = {
        'title': 'Главная',
        'date_time': datetime.now().strftime('%A, %H:%M, %d.%m.%Y')
    }
    return render_template('base_9.html', **context)


@app.route('/clothes/')
def clothes():
    title = 'Одежда'
    goods = {
        'Куртка мужская': 10000,
        'Куртка женская': 15000,
        'Куртка детская': 8000,
    }
    return render_template('clothes.html', title=title, goods=goods)


@app.route('/shoes/')
def shoes():
    title = 'Обувь'
    goods = {
        'Кроссовки': 8000,
        'Валенки': 12000,
        'Тапки': 5000,
    }
    return render_template('shoes.html', title=title, goods=goods)


@app.route('/accessories/')
def accessories():
    title = 'Аксессуары'
    goods = {
        'Галстук': 3000,
        'Шнурки': 300,
        'Шарик': 200,
    }
    return render_template('accessories.html', title=title, goods=goods)


if __name__ == '__main__':
    app.run(debug=True)
