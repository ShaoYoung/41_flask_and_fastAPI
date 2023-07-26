# Обработка POST-запросов

from flask import Flask, url_for, render_template, request
from markupsafe import escape

app = Flask(__name__)

# обработка всех запросов
@app.route('/')
def index():
    return 'Hi!'

# обработка get-запроса
@app.get('/submit')
def submit_get():
    return render_template('form.html')

# обработка post-запроса
@app.post('/submit')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True)
