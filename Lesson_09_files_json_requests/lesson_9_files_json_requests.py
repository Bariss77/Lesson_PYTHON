# имеем файл toread.txt, создаем функцию его тпрочитать:
def read_file(filename):
    print('reading file:')
    f = open(filename)   # открываем файл
    content = f.read()   # читаем
    f.close()            # закрываем

    return content       # возвращаем содержимое файла

print(read_file('C:/Users/boris/Documents/py_001/toread.txt')) # вызываем функцию
#------------------------------------
print('------------------------------')

def way_better(filename):       # другой способ считывания файла
    print ('reading file:')     # с помощью "синтаксического сахара"
    with open (filename) as f:
        return f.read()

print(way_better('C:/Users/boris/Documents/py_001/toread.txt'))
#------------------------------------
print('------------------------------')

def write_to_file(filename, content, mode = 'w'):     # mode = 'w': создаем файл new.txt (если его нет) и перезаписываем туда весь текст
    with open(filename, mode=mode) as f:
        f.write(content)

write_to_file('C:/Users/boris/Documents/py_001/new.txt', 'Some\ntext!') # mode по умолчанию 'w'

write_to_file('C:/Users/boris/Documents/py_001/new.txt', '\nList1\nList2', mode = 'a')       # mode = 'a': добавляем текст в конец файла
#------------------------------------
print('------------------------------')

text_a = (way_better('C:/Users/boris/Documents/py_001/toread.txt'))   # считываем текст toread.txt в переменную text_a
print(text_a)

write_to_file('C:/Users/boris/Documents/py_001/new.txt', text_a)    # добавляем в конец файла new.txt текст с файла toread.txt

#------------------------------------
print('------------------------------')

import json   # json переводит в строку объект

if __name__ == '__main__':
    data = way_better('C:/Users/boris/Documents/py_001/data.json.py')
    print('raw data is', data, type(data))   # печатаем объект (словарь) в строку
    print()

    obj = json.loads(data)            # из строки печатаем объект (словарь)
    print(obj, type(obj))

    print(obj['object'], obj['boolean'])
    print()

    print('dumping object to text: ') # выводим из объекта в строку
    obj['new_value'] = 'secret'       # модифицуруем объект, добавляем ключ и значение
    print(json.dumps(obj))
#------------------------------------
print('------------------------------')

import requests     # импортируем requests после инсталирования

r = requests.get('http://anostas.ru/')
print(r.status_code)  # result: 200 (или 400, или 500) 200 сервер готов, все норм
#print(r.text)  # выдает HTML код  НЕ ПОМЕЩАЕТСЯ В ОКНО cmd.exe

def get_habrahabr():    # функция - запрос к  сайту хабрхабр
    r = requests.get('http://habrahabr.ru')
    print(r.status_code)  # result: 200
    print(r.headers)      # выводит заголовки
    #print(r.content)      # выдает HTML код  НЕ ПОМЕЩАЕТСЯ В ОКНО cmd.exe

get_habrahabr()

def find_pet_by_tag(tag):
    params = {'tags': tag}
    headers = {'Accept': 'aplication/xml'}
    url = 'http://petstore.swagger.io/v2/pet/findByTags'
    r = requests.get(url, params=params, headers=headers)
    print(r.status_code, r.headers)
    print(r.content)

find_pet_by_tag('string')
