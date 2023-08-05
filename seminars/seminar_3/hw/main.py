# Flask-SQLAlchemy

from flask import Flask, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
# generate_password_hash() – выполняет кодирование строки данных по стандарту PBKDF2;
# check_password_hash() – выполняет проверку указанных данных на соответствие хеша.

from hw.models import db, User
from hw.forms import RegisterForm, LoginForm

app = Flask(__name__)
# путь к БД если запуск приложения flask из консоли
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_hw.db'
# путь к БД если запуск приложения flask из PyCharm
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/users_hw.db'

# инициализация БД
db.init_app(app)

app.config['SECRET_KEY'] = b'ea959bc6bbd140100d66503aa6ac1242c6eb0e8d4c38b85c7ea9a9d2a8e60451'
# получение csrf - объекта для работы с формами
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('base.html', message='Основная страница')


@app.cli.command("init-db")
def init_db():
    # создать все таблицы
    db.create_all()
    print('DB created!')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        # получаем данные из формы
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        # print(f'{name=}, {surname=}, {email=}, {password=}')
        # получить user из БД по name или email
        # existing_user = User.query.filter((User.name == name) | (User.email == email)).first()
        existing_user = User.query.filter(User.email == email).first()
        # если existing_user существует
        if existing_user:
            error_msg = 'Email already exists.'
            # сообщение под полем email
            form.email.errors.append(error_msg)
            return render_template('form.html', form=form)

        # создаём экземпляр User
        user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return render_template('base.html', message='Регистрация прошла успешно!')
    return render_template('form.html', form=form, action='Регистрация', form_action=url_for('register'),
                           button_action='Зарегистрироваться')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # получаем данные из формы
        email = form.email.data
        password = form.password.data
        # print(f'{email=}, {password=}')
        # запрос с фильтрацией по author_id
        Users = User.query.filter_by(email=email).all()
        # print(Users)
        # print(Users[0].name, Users[0].password)
        if Users and check_password_hash(Users[0].password, password):
            # print(f'{Users[0]=}')
            return render_template('base.html', message=f'Добро пожаловать, {Users[0].name}!')
        return render_template('base.html', message='Неверный email и/или пароль!')
    return render_template('form.html', form=form, action='Логин', form_action=url_for('login'), button_action='Логин')


if __name__ == '__main__':
    app.run(debug=True)
