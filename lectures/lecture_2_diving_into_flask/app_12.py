# Flash - сообщения


from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'ddb4b937bfc272f7139dea217630a099cd148cc1bacec6e324d9beb0b952775a'


# Необходимо добавить в Flask приложение секретный ключ.
# Простейший способ генерации такого ключа, выполнить следующие пару строк кода
# >>> import secrets
# >>> secrets.token_hex()

@app.route('/')
def index():
    return 'Hi!'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы. message = 'Форма успешно отправлена!', category = 'success'
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
