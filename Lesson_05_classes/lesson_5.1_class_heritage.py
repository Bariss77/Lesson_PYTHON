# наследие

class Parent(object):               # идентично: Parent:         РОДИТЕЛЬСКИЙ КЛАСС
    def __init__(self):             # сщздаем конструктор объектов
        print('Parent inited')
        self.value = 'Parent'       # имеющих единственную переменную Parent

    def do(self):                    # печатаем текст с этой переменной
        print('Parent do(): {}'.format(self.value))

parent = Parent()                    # создаем  объект класса Parent(), в нем единственная переменная Parent
parent.do()                          # выполняем с этим объектом действия методом .do(self)
# resulr: Parent inited
#         Parent do(): Parent

class Child(Parent):                 # КОНСТРУКТОР НАСЛЕДНИКА
    def __init__(self):
        print('Child inited')
        self.value = 'Child'

child = Child()                      # присваиваем объект наследнику
print(child)
# result: Child inited
#         <__main__.Child object at 0х04c59250>
child.do()                           # выполняем с этим объектом действия методом .do(self) РОДИТЕЛЯ
# result: Parent do(): Child
# -------------------------------------------------------------------------------------------------------

class Calc(object):                   # Создаем родительский класс
    def __init__(self, number):
        self.number = number          # сщздаем объект с переменной number
    def calc_and_print(self):
        value = self.calc_value()     # перемення value принимает значение метода calc_value
        self.print_number(value)      # переменная value передается методу print_number
    def calc_value(self):
        return self.number * 10 + 2                 # считаем переменную value
    def print_number(self, value_to_print):
        print('-----')
        print('Number is', value_to_print)          # печатаем все с переменной value
        print('-----')
c = Calc(3)
c.calc_and_print()
# result: -----
#         Number is 32
#         -----

class CalcExtraValue(Calc):                           #  Сщздаем класс наследник.
    def calc_value(self):
        return self.number -100                       # возвращаем переменную number - 100

c = CalcExtraValue(3)
c.calc_and_print()                                     # вызываем метод calc_and_print родителя
# result: -----
#         Number is -97
#         -----
# ---------------------------------------------------------------------------------------
# super()  - возможность вызывать родительский метод

class Calc(object):
    def __init__(self, value):                     # родительский метод
        print('Calc constructor is called')
        self.value = value                         # называем переменную value

    def count(self):
        return self.value * 8 + 9                   # возвращаем переменную с выполнеными ар. действиями

c = Calc(1.4)
print(c.count())

class ExtendedCalc(Calc):                           # класс наследника
    def __init__(self, value, k = 1):
        super(). __init__(value)                    # вызываем родительский меод __init__ с помощью super
        print('Extender', self.value)               # печатаем переменную value в данном случае из родительского класса

        self.k = k

    def count (self):
        print('Before')
        previous = super().count()                  # назначаем переменную через родительсий метод cout

        return -1 * self.k * previous                # возвращаем результат

e = ExtendedCalc(8, k = 1.2)
print(e.count())

# ------------------------------------------------------------------------














