# Flask-SQLAlchemy
# Получение данных из БД
# Фильтрация данных

from flask import Flask, render_template, jsonify
from lectures.lecture_3_additional_features_flask.models_05 import db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../../instance/mydatabase.db'
# инициализация БД
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'

@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/users/')
def all_users():
    # Получить всех User из БД
    users = User.query.all()
    # print(users)
    # создаётся словарь context
    context = {'users': users}
    # print(context)
    # return render_template('base.html')
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def users_by_username(username):
    # запрос с фильтрацией
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)

@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    # запрос с фильтрацией по author_id
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        # jsonify - ф-ция, возвращающая не html-страницу, а json-объект
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'}), 404




if __name__ == '__main__':
    app.run(debug=True)
