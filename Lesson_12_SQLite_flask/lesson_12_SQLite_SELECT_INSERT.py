import sqlite3

from flask import Flask

print('----Извлекаем из таблицы все:----')
conn = sqlite3.connect('C:/Users/boris/Documents/Lesson_PYTHON/Lesson_12_SQLite_flask/weightP.db')  # конектимся с БД
curs = conn.cursor()                     # создаем курсор

curs.execute("SELECT * FROM weight")   # создаем запрос SQL
rows = curs.fetchall()           # извлекаем данные из таблицы в переменную
for row in rows:
    print (row)     # выводим в консоль

print('----Вносим данные в таблицу "100.0"----')
curs.execute("INSERT INTO weight(weight) VALUES('100.0')")
conn.commit()

print('----Вносим данные подстановкой "112.5"----')
W = ('112.5', )   # пишем данные в виде кортежа: (.., .., ..)
curs.execute("INSERT INTO weight(weight) VALUES(?)", (W))  # подставляем данные в запрос
conn.commit()

print('----Проверяем----')
curs.execute("SELECT * FROM weight")   # создаем запрос SQL
rows = curs.fetchall()           # извлекаем данные из таблицы в переменную
for row in rows:
    print (row)     # выводим в консоль
print('----Выводим данные в браузер----')
app = Flask(__name__)
app.config.update ( DEBUG=True )

@app.route('/')
def home():
    w = str(row[1])
    return ((w[:10]) + " " + (row[2]))  # так или иначе форматируем данные

app.run()
