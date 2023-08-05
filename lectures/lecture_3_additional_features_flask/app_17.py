# Flask-WTForm

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms_3 import LoginForm, RegistrationForm

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SECRET_KEY'] = b'ea959bc6bbd140100d66503aa6ac1242c6eb0e8d4c38b85c7ea9a9d2a8e60451'
# получение csrf - объекта для работы с формами
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/data/')
def data():
    return 'Your data!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
    # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
    # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
    ...
    return render_template('form.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)
