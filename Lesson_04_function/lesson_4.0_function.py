# ФУНКЦИИ
len ('Marry')         # example function
# result: 5
len ([1, 9])
# result: 2
def first (x):
    return x + b
x = 10
b = 2
first (x)
# result: 12
def first (x):
    return x + b
x = 15
b = 2
first (x)
# result: 17
def second (x, z):
    print (x + z)
second(12, 40)
# result: 52

def with_default (name = 'Nikita'): # функция с аргументом по умолчанию
    print ('Hello', name)
with_default ('Petr')
# result: Hello Petr
with_default ()
# result: Hello Nikita

def sum_all (*numbers):   # передаем любое кол-во аргументов
    print (numbers, type(numbers))
sum_all (1, 2)
# result: (1, 2)<class 'typle'>
sum_all (1, 8, 9, 89, 78)
# result: (1, 8, 9, 89, 78) <class 'typle'>
def any_keyword (**kwargs):    # передаем любое кол-во арг. словаря
    print (kwargs, type(kwargs))
any_keyword (k=1, some=2, wad=45)
# result: {'k':1, 'some':2, 'wad':45} <class 'dict'>

callable()    # указывает является ли аргумент в скобках функцией
print(callable(len), callable(45), callable(callable))
# result: True False True

def return_min_value():   # Нахождение минимального аргумента
    return min            # возврат функции min как объект
test=return_min_value()
min_value=test(4, 5, -9, 12)
print ('Min value is', min_value)
# result: Min value is -9

SOME_VAR = ' value ' # глобальная переменная
def print_var ():
    test = '123'     # локальная переменная (внутри тела функции)
    print (SOME_VAR, test)
print_var ()
# result:  value 123
# глобальные переменные через функцию можно только мутировать, например через .append()
# переназначать глобальные переменные через функцию НЕЛЬЗЯ

# Рекурсия, способ функции вызвать саму себя.
def factorial (n):
    if n ==0:
        return 1
    return n * factorial (n-1)
print ( factorial(4))
# 24
    
