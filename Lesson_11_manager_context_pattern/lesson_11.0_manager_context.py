# Менеджер контекста. Выполняет дейчтвия до некоторой логики, и после выполнения этой логики.
# Менеджер контекста при открытии и закрытии файла.
class File(object):                         # создаем класс, объекты которого принимает значения
    def __init__(self, filename, mode):     # файл и метод его открытия (чтение или запись или ..)
        print('__init__')
        self.filename = filename
        self.mode = mode

    def __enter__(self):                     # магический метод
        print('opening file')                # пишем "opening file"
        self.open_file = open(self.filename, self.mode)   # открываем файл, методом mode
        return self.open_file                # возвращаем файл, в данном случае в переменную 'f', строка 18

    def __exit__(self, *args):               # в данном случае на 20 строчке, после выполнения кода "f.write('some data')"
        print('closing file')                # начинает работать магический метод __init__
        self.open_file.close()               # файл закрывается

with File('to_open.txt', 'w') as f:
    f.write('some data')
# С помощью менеджера контеста в данном случае всегда файл будет закрываться в конце
# даже если выскочит ошибка в процессе его открытия.
# Это дает стабильность работы.
# Not how error is handled:
with File ('does-not-exist', 'r') as new_file:
    print(new_file.read())
