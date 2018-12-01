class Test():
    def __add__(selfself, other):           # метод сложения двух сущностей.
        return '0_0'                        # в результате сложения возвращаем 0_0

t = Test()                                   # создаем объект класса Test
print(t + 2)                                 # выводим результат сложения объекта и числа 0_0
# ------------------------------------------------------------------------------------------
class BadStr(str):                           # назначаем класс наследник от класса str
    def __add__(self, other):
        return str(self) + str(other)        # возвращаем сумму двух строк
t = BadStr('some')
print(t + 2)

test_02 = 'some' + str(2)                    # то же, что выше. str - магический метод
print(test_02)

# ------------------------------------------------------------------------------------

# МАГИЧЕСКИЕ МЕТОДЫ:

class MathObject(object):
    def __init__(self, value):
        self.value = value                  # создаем обект

    def __eg__(self, other):
        return self.value == other          # равно

    def __ge__(self, other):
        return self.value >= other            # и так далее
# -------------------------------------------------------------------------------------

class MathObject():
    def __init__(self):
        self.value = 2                      # назначаем переменной = 2

    def __add__(self, other):
        return self.value + other            # вызываем метод сложения

t = MathObject()                             # создаем объект переменная  = 2
print(t + 4)                                 # складываем с 4
# result: 6
print(t.__add__(4))                          # смысл тот же, разница в "читаемости"
# result: 6

# ----------------------------------------------------------------------------------------

# МАГИЧЕСКИЕ МЕТОДЫ ДЛЯ СЛОВАРЕЙ         В словарях все проверяется и сравнивается по ключам

def __getitem__(self, key):
    return self.value[key]                       # возвращает по ключу значение

def __setitem__(self, key, value):
    self.value[key] = value                      # назначает значения для ключа

def __delitem__(self, key):
    del self.values[key]                         # удаляет значение по ключу

def __contains__(self, item):
    return item in self.value                    # поиск элемента, оператор in

def __len__(self):
    return len(self.value)                       # получение длины

# -----------------------------------------------------------------------------------------

if __name__ == '__main__':
    l = ({'1key': 'some_value'})    # словарь с одним ключом и значением, работает метод __init__
    l[1] = 'item1'                                   # работает метод __setitem__
    print(str(l), l[1])                              # работают методы __str__ и __getitem__
    print('s' in l, 1 in l)                          # работает метод __contains__
    print(len(l))                                    # работает метод __len__

# ------------------------------------------------------------------------------------------
# ИМПОРТ

from normal_package.normal_file import MyClass, my_function, GLOBAL_VAR   # из пакета normal_package, модуля normal_file импортировать
                                                                          # класс MyClass, функцию my_function, глобальную переменную GLOBAL_VAR
# пакет (папка) normal_package должен быть га том же уровне где код этой программы
my_function()
print(GLOBAL_VAR)







