import os

from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True     # Режим наладки. Можно изменять код без остановки сервера (Без ctrl+C)
# Настройки окружения бывают: локальные, девелопмент, продакшн
# При DEBUG=True выводятся подробные ошибки

app.config['SECRET_KEY'] = 'some secret' # здесь ключ не спрятан
# app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
# Секретные настройки, прячут при помощи модуля 'os.environ', посредством переменных окружения
# До запуска пайтона задаются заранее переменные окружения. Они и могут являться секретными.
# Обычно записывают все настройки, как словарь:
#app.config.update(
#    DEBUG=True,
#    SECRET_KEY='some key',
#    ....
#)
@app.route('/', methods=['GET', 'POST'])
def home():
    return 'hello world!', 200

if __name__ == '__main__':
    app.run()
