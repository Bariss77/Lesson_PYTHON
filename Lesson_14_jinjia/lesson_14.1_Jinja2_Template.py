
from jinja2 import Template # встроенная библиотека для шаблонов

def simple_hello_world():
    t = Template('Hello {{ something }}!') # Шаблон
    result = t.render(something='World')   # Подстановка

    print(result)

simple_hello_world()
#------------------------------------
def for_example(iterable=None): # по умолчанию iterable = None
    if iterable is None:
        iterable = range(1,  11)  # переменная содержит диапозон от 1 до 11

    t = Template("""
My favorite number: {% for n in array %}{{ n }}{% endfor %}
""") # шаблон с логикой, внутри преременная n - результат подстановки  array
     
    result = t.render(array=iterable)  # передаем array
    print(result)  # выводим результат

for_example()  # вызываем функцию
#--------------------------------------
def if_example(value):             # Пример с if
    t = Template("""
    {% if value %} True!
    {% else %} False.
    {% endif %}
    """)

    result = t.render(value=value)
    print(result)

if_example(True)
if_example('')
#--------------------------------------
