from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder = 'templates')
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'asdfsdfssf asf dsgsdg',
    # Database setting:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
    SQLALCHEMY_TRACK_MODIFICATIONS = False,

    WTF_CSRF_ENABLED = False
)

db = SQLAlchemy(app)

class First(db.Model):            # модель таблица по имени класса First
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # поля таблицы
    name = db.Column(db.String(120))

    def __str__(self):
        return '<First %r>' % self.data

class Second(db.Model):           # вторая таблица
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_id = db.Column(db.Integer,
               db.ForeignKey('first.id'),
               nullable=False,
               index=True) # внешний ключ к таблице first, к колонке id
    # nullable=False : не может хранить данные????
    first = db.relationship(First, foreign_keys=[first_id, ])
    #  отношение с классом first при помощи внешнего ключа, присоединение столбца (joil ???)
    data = db.Column(db.String(120))

    def __str__(self):
        return '<Second %r>' %self.data

if __name__ == '__main__':
    db.create_all()           #  создаем БД и все таблицы

    f = First(name='One')     # создаем объект-запись класса First для первой таблицы
    db.session.add(f)         # добавляем его в сессию

    s = Second(first=f, data='some_data')  # передаем объект первой таблицы во вторую
    db.session.add(s)         # добавляем его в сессию

    db.session.commit()       # все commitim
    # ----------------- Создаесм запрос---------------
    all_seconds = Second.query.all()    # выбираем все данные из базы
    for second in all_seconds:          # выводим на печать
        print(second.id, second.first_id, second.data)
        print(second.first.name, second.first.id)
        print()
