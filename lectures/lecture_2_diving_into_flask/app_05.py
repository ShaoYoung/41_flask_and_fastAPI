# Обработка POST-запросов

from flask import Flask, url_for, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
