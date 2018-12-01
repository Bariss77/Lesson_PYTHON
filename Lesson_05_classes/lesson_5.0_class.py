class MyClass:
    def __init__(self):               # Констпуктор
        self.x = 10                   # Задаем атрибут экземпляра класса
    def print_x(self):                # задаем метод, self - ссылка на данный экземпляр класса
        print(self.x, self.y)         # Выводим значения атрибутов экземпляра класса
c = MyClass()                         # Создаем экземпляр класса
MyClass.y = 20                        # Добавляем атрибут класса
c.print_x()                           # Выполняем метод print_x, result: 10, 20
print(c.x, c.y)                       # Другое обращение к атрибуту, result: 10, 20

# -------------------------------------------------------------------------------

class FirstClass:                       # Определяем пустой класс
    pass
FirstClass.x = 50                       # Создаем атрибут объекта класса
c1, c2 = FirstClass(), FirstClass()     # Создаем два экземпляра класса
c1.y = 10                               # Создаем атрибут экземпляра класса
c2.y = 20                               # Создаем атрибут экземпляра класса
print(c1.x, c1.y)                       # result: 50 10
print(c2.x, c2.y)                       # result: 50 20

# -------------------------------------------------------------------------------

class SecondClass:
    w = 35
    def __init__(self, value1, value2):
        self.x = value1
        self.y = value2
c = SecondClass(100, 200)
print(c.x, c.y)
SecondClass.z = 300
print(c.x, c.y, c.z)
d = SecondClass(45, 55)
print(d.x, d.y, d.z, d.w)
print(c.x, c.y, c.z, c.w)

# -------------------------------------------------------------------------------

class Car:                 # класс
    engine = 'U8 Turbo'
Car
# result: <class '__main__.Car'>
car1 = Car()
car2 = Car()
car1.engine
# result: 'V8 Turbo'
car2.engine
# result: 'V8 Turbo'
# --------------------------------------------------------------------
class Room:             # создаем класс Room
    number = 'Room 34'  # через атрибуты или поля (переменные number и floor) присваиваем свойства ('Room 34' и '4')
    floor = 4
r = Room()              # создаем объекты класса Room
r1 = Room()
print(r.number, r1.number)  # читаем атрибуты или поля объектов класса Room
# result: Room 34 Room 34
print(r.floor, r1.floor)
# result: 4 4
print(r.number, r1.floor)
# result: Room 34 4
r.number = 12              # переменные можно изменять
r.floor = '5 floor'
print(r.number, r.floor)
# result: 12 5 floor
print(r.floor, r1.number)
# result: 5 floor Room 34
# ------------------------------------------------------------------
class Door:            # создаем класс Door
    def open(self):    # функция внутри класса называется метод
        print('self is', self) # result: self is <__main__.Door object at 0х005236B0>
        print('Door is opened!') # result: Door is opened!
        self.opened = True       # ??? Присвоение нового атрибута
d = Door()           # называем обект класса Door
d.open()             # вызываем для объекта d метод open
d1 = Door()          # объект другой, а результат тот же (при помощи self)
d1.open()
# -------------------------------------------------------------------
class Terminal:       # присвоение значений атрибутам (полям) классов
    def hello(self, user_name):
        print('self is the object itself', self)
        print('Hello,', user_name)
t = Terminal()
t.hello('Nikita')   # result: self is the object itself <__main__.Terminal object at 0х022E3730>
                    # result: Hello, Nikita
t.hello('Vova')     # result: self is the object itself <__main__.Terminal object at 0х022E3730>
                    # result: Hello, Vova
# ---------------------------------------------------------------------
class Window:
    is_opened = False                        # текущее состояние закрыто
    def open(self):
        self.is_opened = not self.is_opened  # текущее состояние меняет на противоположное
        print('Window is now', self.is_opened)

w = Window()   # объекты класса Window
w1 = Window()

print('Initial state', w.is_opened, w1.is_opened)
# result: Initial state False False  (выполнение: is_opened = False   )
# result: Window is now True     (выполнение: self.is_opened = not self.is_opened)
w.open()                                         # для w вызываем метод open (открываем окно)
print('New state', w.is_opened, w1.is_opened)
# result: New state True False   (применение метода .open (меняем на противоположное) только к w, w1 остаетсе не затронутым)
# ----------------------------------------------------------------
class Car:
    def __init__(self):           # создаем конструктор
        self.color = 'red'        # передаем значения атрибутов (полей)
        self.rule = 'left'
t = Car()                         # создаем объекты
print(t.color, t.rule)
# red left
# ---------------------------------------------------------------------
class Car:
    def __init__(self, color): # создаем конструктор с переменой в значении атрибута (поля)
        self.color = color
t = Car('red')                 # создаем обекты с заданым атрибутом
t1 = Car('white')
print(t.color, t1.color)
# result: red white
# ----------------------------------------------------------------------
class Car:
    engine = 'V8 Turbo'            # заранее задаем атрибут
    def __init__(self, color):
        self.color = color
t = Car('red')                      # задаем атрибут в процесе
t1 = Car('white')
print('motor - ', t.engine,';', 'collor - ', t.color,';', 'motor - ', t1.engine,';', 'color - ', t1.color, '.')
# result: motor - U8 Turbo; collor - red; motor - U8 Turbo; color - white
# -----------------------------------------------------------------------
class Table:
    def __init__(self, number_of_legs):
        print('New table has {} legs'.format(number_of_legs))
t = Table(4)
t1 = Table(3)
# result: New table has 4 legs
# result: New table has 3 legs
# ---------------------------------------------------------------------
