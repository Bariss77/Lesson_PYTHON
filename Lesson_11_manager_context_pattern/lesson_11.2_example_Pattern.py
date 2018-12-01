# Пример повторяющего кода и устранение через паттерное проэктированиеЖ
# First example:
class Person(object):                  # Сщздаем два класса с одинаковой логикой
    def say(self):
        print('I am a person!')

class Teacher(object):
    def tell_about_yourself(self):
        print('I am a teacher!')

c = Person()                           # Сщздаем объекты классов
print(c.say())                         # result: I am a person!
b = Teacher()
print(b.tell_about_yourself())         # result: I am a teacher!

# Убираем дублирование кода, тот же результат:
class Person2(object):                 # Сщздаем два класса, второй наследует первый.
    role = 'person'                    # Объявляем атрибут класса

    def say2(self):                    # Объявляем метод класса, через подстановку атрибута.
        print('I am a {}!'.format(self.role))

class Teacher2(Person2):
    role = 'teacher'

a = Person2()
print(a.say2())                        # result: I am a person!
d = Teacher2()
print(d.say2())                         # result: I am a teacher!


# Second example:
class  Square(object):
    def __init__(self, size):
        self.height = size
        self.width = size
        print('Area is %d' % (self.height * self.width))

    def __str__(self):
        return 'Square with area: %d' % (self.width * self.height)

s = Square(size=10)
print(s.__str__())              # Считаем площадь квадрата

# Убираем дублирование кода, тот же результат:
class  Square2(object):
    def __init__(self, size):
        self.height = size
        self.width = size
        print('Area is %d' % (self.get_area()))

    def get_area(self):
        return self.height * self.width

    def __str__(self):
        return 'Square with area: %d' % (self.get_area())

s = Square2(size=15)
print(s.__str__())              # Считаем площадь квадрата
