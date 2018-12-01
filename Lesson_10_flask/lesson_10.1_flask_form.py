
from flask import Flask, request             # импорт flask и request(запрос)

#pip install flask_wtf
from flask_wtf import FlaskForm              # импорт форм, поля для ввода данных пользователя
from wtforms import StringField, validators  # импорт валидации форм, проверка вводимых данных на соответствие

class ContactForm(FlaskForm):                # создаем объект формы
    name = StringField(validators=[validators.Length(min=4, max=25)
    ])                                       # вводить только строку, ключ: Name, длина значения от 4 до 25 символов
    email = StringField(validators=[
    validators.Length(min=6, max=35),        # вводить только строку, ключ: E-mail, длина значения от 6 до 35 символов,
    validators.Email()                       # форма ввода как адрес Email
    ])

# Можно добавлять любое колличество полей:
    job = StringField(validators=[validators.Length(min=2, max=4)
    ])

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

@app.route('/', methods=['GET', 'POST'])     # запрос к URL "/" (//127.0.0.1:5000), с возможностью запроса GET или POST
def home():
    if request.method == 'POST':             # если запрос POST, то:
        print(request.form)                  # выводим данные POST-запроса (словарь: КЛЮЧ-ЗНАЧЕНИЕ) в консоль
        form = ContactForm(request.form)     # создаем переменную
        print(form.validate())               # выводим результат валидации в консоль

        if form.validate():                    # если валидация прошла, то возвращается valid 200
            return('valid', 200)
        else:
            return('invalid', 400)             # если валидация прошла, то возвращается invalid 400

    if request.method == 'GET':               # если запрос GET, то:
        return'hello world!', 200             # выводим hello world  200

if __name__ == '__main__':
    app.run()
