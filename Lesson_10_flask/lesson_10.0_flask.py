from flask import Flask

app = Flask(__name__)
app.config.update(     # РЕЖИМ НАСТРОЙКИ
DEBUG = True
)

@app.route('/')
def home():             # функция выполняется, когда обращаемся по этому URL-адресу
    return 'hello word!'


@app.route('/hello/<user>') # передаем параметр user, пример: http://127.0.0.1/hello/Elena
def hello_user(user):
    return 'Hello, user:' + user   # result: hello, Elena

# Сложение двух чисел, заданных в URL:
@app.route('/summa_a/<int:a>/<int:b>')
def sum_ab(a, b):
    e = a + b
    return 'Summa equally: %s' %e

# Сравниваем число в глобальной (внешней переменной)
# с числом в адресе URL:
T = 25 # глобальная переменная
@app.route('/gl/<int:a>')   # сравниваем 'T' и 'a'
def comparison_1(a):
    if a == T:
        g = 'Correctly'
    else:
        g = 'Wrong'
    return g         

if __name__ == '__main__':
    app.run()           # запускаем этот экземпляр класса flask
