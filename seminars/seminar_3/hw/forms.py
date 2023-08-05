# WTForms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
import re

# Список встроенных валидаторов, определяемых в wtforms.validators:
# === Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False):
# Проверяет адрес электронной почты. Требуется установка модуля email_validator.
# Аргументы:
# message: сообщение об ошибке, которое должно появиться в случае ошибки проверки.
# granular_messsage: сообщение об ошибке проверки из модуля email_validator (по умолчанию False).
# check_deliverability: выполняет проверку разрешения доменных имен (по умолчанию False).
# allow_smtputf8: вызывает ошибку проверки адресов, для которых требуется SMTPUTF8 (по умолчанию True).
# allow_empty_local: разрешает пустую локальную часть (т. е. @example.com), например, для проверки псевдонимов (по умолчанию False).

# === EqualTo(fieldname, message=None): сравнивает значения двух полей.
#
# Этот валидатор можно использовать для облегчения одного из наиболее распространенных сценариев формы смены пароля:
#
# Аргументы:
#
# fieldname: имя другого поля для сравнения.
# message: – сообщение об ошибке, которое должно появиться в случае ошибки проверки. Можно интерполировать с помощью %(other_label)s и %(other_name)s, чтобы обеспечить более полезную ошибку.
# Пример:
#
# from wtforms import Form, PasswordField
# from wtforms.validators import InputRequired, EqualTo
#
# class ChangePassword(Form):
#   password = PasswordField('Новый пароль', [InputRequired(),
#                       EqualTo('confirm', message='Пароли должны совпадать')])
#   confirm  = PasswordField('Повторите Пароль')
# Здесь используется валидатор InputRequired(), чтобы предотвратить попытку валидатора EqualTo() проверить, не совпадают ли пароли, если пароли не были указаны вообще. Поскольку InputRequired() останавливает цепочку проверки, то EqualTo() не запускается в случае, если поле пароля остается пустым.
#
# === InputRequired(message=None): проверяет, что для поля были предоставлены данные. Другими словами, значение поля - не пустая строка. Этот валидатор также устанавливает флаг обязательного поля формы для заполнения.
#
# ===  IPAddress(ipv4=True, ipv6=False, message=None): проверяет IP-адрес. Аргумент Ipv4 - если True, принимать адреса IPv4 как действительные (по умолчанию True). Аргумент Ipv6 - если True, принимать IPv6-адреса как действительные (по умолчанию False)
#
# ===  Length(min=- 1, max=- 1, message=None): проверяет длину строки. Аргумент min - минимальная необходимая длина строки. Если не указан, минимальная длина проверяться не будет. Аргумент max - максимальная длина строки. Если не указан, максимальная длина проверяться не будет.
#
# ===  MacAddress(message=None): проверяет MAC-адрес. Аргумент message - сообщение об ошибке, которое будет выдано в случае ошибки проверки.
#
# ===  NumberRange(min=None, max=None, message=None): проверяет, что число имеет минимальное и/или максимальное значение включительно. Это будет работать с любым сопоставимым типом чисел, таким как числа с плавающей запятой и десятичные дроби, а не только с целыми числами.
#
# ===  Optional(strip_whitespace=True): разрешает пустой ввод (необязательное поле) и останавливает продолжение цепочки проверки. Если ввод пуст, также удаляются предыдущие ошибки из поля (например, ошибки обработки). Если аргумент strip_whitespace=True (по умолчанию), то также остановит цепочку проверки, если значение поля состоит только из пробелов.
#
# ===  Regexp(regex, flags=0, message=None): проверяет поле на соответствие регулярному выражению, предоставленному пользователем. Аргумент regex - cтрока регулярного выражения для использования. Также может быть скомпилированным шаблоном регулярного выражения. Аргумент flags - используемые флаги регулярного выражения, например re.IGNORECASE. Игнорируется, если регулярное выражение не является строкой.
#
# ===  URL(require_tld=True, message=None): простая проверка URL на основе регулярного выражения. Вероятно потребуется его проверка на доступность другими способами.
#
# ===  UUID(message=None): проверяет UUID.
#
# ===  AnyOf(values, message=None, values_formatter=None): сравнивает входящие данные с последовательностью допустимых входных данных. Аргумент values ​​- последовательность допустимых входных данных. Аргумент values_formatter - функция, используемая для форматирования списка значений в сообщении об ошибке message.
#
# ===  NoneOf(values, message=None, values_formatter=None): сравнивает входящие данные с последовательностью неверных входных данных. Аргумент values ​​- последовательность допустимых входных данных. Аргумент values_formatter - функция, используемая для форматирования списка значений в сообщении об ошибке message.

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=20)])
    surname = StringField('Surname', validators=[DataRequired(), Length(max=30)])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8),
                             Regexp('.*\d+.*[a-zа-я]+.*|.*[a-zа-я]+.*\d+.*', flags=re.IGNORECASE, message='Поле "Password" должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру')])
    confirm_pas = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])