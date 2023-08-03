# Flask-SQLAlchemy

from flask import Flask, render_template
from random import randint

from task_1.models import db, Student, Faculty


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
# инициализация БД
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
    # создать все таблицы
    db.create_all()
    # print('OK')


@app.cli.command("add-student")
def add_students():
    for i in range(5):
        faculty = Faculty(name=f'faculty_{i}')
        db.session.add(faculty)
    for i in range(20):
        student = Student(
            name=f'name_{i}', surname='Иванов', age=20, sex=True,
            group=f'group_{i}', faculty_id=randint(0, 4))
    # добавляем экземпляр в БД (транзакция открыта, но не зафиксирована)
        db.session.add(student)
    db.session.commit()


@app.route('/get/')
def get():
    students = Student.query.all()
    # print(type(students))
    return render_template('students.html', students=students)




if __name__ == '__main__':
    app.run(debug=True)
