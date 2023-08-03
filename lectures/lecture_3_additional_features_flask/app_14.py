# Flask-WTForm

from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SECRET_KEY'] = b'ea959bc6bbd140100d66503aa6ac1242c6eb0e8d4c38b85c7ea9a9d2a8e60451'
# получение csrf - объекта для работы с формами
csrf = CSRFProtect(app)

"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


# Если вы хотите отключить защиту от CSRF-атак для определенной формы, вы можете использовать декоратор csrf.exempt:
# Лучше защиту не отключать
@app.route('/form', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    return 'No CSRF protection!'



if __name__ == '__main__':
    app.run(debug=True)
