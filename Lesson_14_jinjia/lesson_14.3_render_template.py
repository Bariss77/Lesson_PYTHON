import random

from flask import Flask, render_template  # функция шаблонов

app = Flask(__name__, template_folder='templates') # шаблоны в указанной папке
app.config.update (
DEBUG = True
)

@app.route('/')
def index():
    report_data = [random.randint(0, 20) for _ in range(25)] #  вызываем случайное число от 0 до 20, 25 раз
    return render_template('report.txt', data=report_data)  # переменную data используем внутри шаблона report.txt

def my_name():
    return'Nikita'
app.jinja_env.globals.update(my_name=my_name) # используем глобальную переменную в шаблонах по вызову функции my_name()

def passing_variable(variable):
    return 'Variable was %s' % variable
app.jinja_env.globals.update(passing_variable=passing_variable)

app.run()
