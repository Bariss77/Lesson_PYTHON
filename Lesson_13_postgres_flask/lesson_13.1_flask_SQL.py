from datetime import date

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import validators, fields

import psycopg2        # библиотека раюоты python с postgres

try:          # создаем exception, если соединение выдаст ошибку (БД не существует, неправильные параметры, и т.д.)
    conn = psycopg2.connect(          # создаем connection,
        user='postgres',              # указываем параметры соединения с сервером DB SQL
        password='bs200609',
        database='tceh_db',
        host='localhost',
        port=5433,
    )
except Exception as ex:   # выкидываем ошибку
    print('I am unable to connect to the database', ex)
    raise ex

app = Flask(__name__) # если законектились, создаем экземпляр класса flask
app.config.update({   # настройки
    'DEBUG':True,
    'SECRET_KEY':'very-secret',
    'WTF_CSRF_ENABLED':False,
})

class ObservationForm(FlaskForm): # создаем форму 
    observation_date = fields.DateField(default=date.today) # валидируем данные поля observation_date
    people_available = fields.IntegerField(    # валидируем данные поля people_available
        validators=[validators.NumberRange(min=0)] )

@app.route('/', methods=['GET', 'POST'])      # адрес запросов '/'
def index():
    cur = conn.cursor() # получаем объект cursor, результат конекта, с которым мы будем совершать действия: вставка, чтение и т.д.
    # Проаеряем работу при помощи сайта Postman
    if request.method == 'POST':              # если метод POST , то отправляем данные через форму
        form = ObservationForm(request.form)  # создаем форму, передаем в нее данные пользователя
        if form.validate():                   # вызываем метод валидации
            od, pa = form.observation_date.data, form.people_available.data
                                    # если данные валидны разрешаем данные вставить в таблицу
            cur.execute(            # вызываем SQL запрос
                                    # вносим данные пользователя так, чтобы пользователь не мог изменить запрос (""иньекция SQL")
                                    # задаем  SQL строку, не вызывая сами данные
                """INSERT INTO public.observations(
                    observation_date, people_available) VALUES (
                    %(observation_date)s, %(people_available)s)""", # метод формата строки внутри SQL
                    # передаем вставку данных как словарь методом форматирования
                {'observation_date': od.strftime('%Y-%m-%d'), 'people_available': pa}
            )             # если не выполнитть следующий метод commit, при перезагрузке сервера новые данные исчезнут
            conn.commit() # без commit обрабатываеся только текущая сессия, после  commit данные записываютчя в БД окончательно
            return str('posted')
        else:
            return str(form.errors)
    else:                      # иначе (ели метод GET)
        cur.execute(           # вызываем SQL запрос
            """SELECT * from public.observations;"""
        )
        data = cur.fetchall()  # достаем все данные из базы по запросу, сделаному execute
        return str(data)       # возвращаем данные строкой


if __name__ == '__main__':
    app.run(debug=True)
