from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)                        # Создаем экземпляр класса
app.config.update(
    DEBUG=True,                                     # Режим отладки
    SECRET_KEY='should always be secret',          # Секретный ключ
    # Database settings:
    SQLALCHEMY_DATABASE_URI='sqlite:///people.db', # Путь к базе данных
    SQLALCHEMY_TRACK_MODIFICATIONS=False, # ????

    WTF_CSRF_ENABLE=False
)

db = SQLAlchemy(app)          # создаем объект SQLAlchemy
#--------------НИЖЕ: Создаем модель-таблицу-----------------------
class Person(db.Model):       # Таблиза будет называться Person, обозначаем поля:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # колонка id, первичный ключ, к каждому последующему значению прибавляется 1
    name = db.Column(db.String(80), nullable=False) # колонка name, длина строки не более 80 символов, пустой не может быть
    age = db.Column(db.Integer, nullable=False) # колонка age,  целое число, непустое
    job = db.Column(db.String(50)) # колонка job, строка не более 50 символов

    def to_json(self):          # создаем метод для вывода данных в json
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'job': self.job
        }
#-------------------НИЖЕ: Создаем и выводим запросы----------------------------
@app.route('/')
def index():
    people = Person.query.all()     # Выводим все записи таблицы Person
    by_name = Person.query.filter_by(name='Sveta').first() # Выводим одну запись с именем Sveta
    by_age = Person.query.filter(Person.age >=30) # выводим всех старше или равно 30
    by_job = Person.query.filter(Person.job == 'HR')  # выводим всех с работой HR
    # сложные запросы:
    sub = db.session.query(func.min(Person.age).label('min_age')).subquery()
    youngest = Person.query.join(sub, sub.c.min_age == Person.age).first()

    return jsonify({   # выводим запросы на экран, превращаем данные в строку с помощью json
        'people': [p.to_json() for p in people],
        'by_name': by_name.to_json(),
        'by_age': [p.to_json() for p in by_age],
        'by_job': [p.to_json() for p in by_job],

        'youngest': youngest.to_json(),
    })
#------------------НИЖЕ: Вносим данные в саму таблицу----------------------------------
if __name__ == '__main__':
   db.create_all()  # сздает все ранее объвленые модели-таблицы. В даном случае таблицу Person
   # Deleting all records
   Person.query.delete()  # удаляет все записи из базы данных (если надо)
   # Создаем 4 объекта (переменные) класса Person:
   ivan = Person(name='ivan', age=3)
   sveta= Person(name='Sveta', age=30, job='HR')
   semen = Person(name='Semen', age=32, job='IT')
   kolya = Person(name='Kolya', age=23, job='HR')
   # добавляем объекты в сессию:
   db.session.add(ivan)
   db.session.add(sveta)
   db.session.add(semen)
   db.session.add(kolya)
   # записываем данные в БД:
   db.session.commit()

   app.run()
