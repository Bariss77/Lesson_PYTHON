# СПИСКОВЫЕ ВЫРАЖЕНИЯ

s = []
for i in 'ser':
    s.append(i)
print(s)
# result: ['s', 'e', 'r'[

s = [i for i in 'ddd']             # та же запись но в одну строку
print(s)
# resurt: ['d', 'd', 'd']

s = [w for w in range(1, 14)]
print(s)
# result^ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

s = [w for w in range(1, 14) if w%2 == 0]        # однострочные выражения использовать только если короткая запись
print(s)
# result: [2, 4, 6, 8, 10, 12]
ra
# ---------------------------------------------------------------
# lambda
x = lambda: print('Hey!')
x()

d = lambda x, y: x + y         # записываем в переменную одноразовую безименную функцию
print(d(9, 0))
# result: 9
print(d(9, 2))
# result: 11
# ----------------------------------------------------------------
# map выполняет функцию для каждого объекта из массива

def work(value):
    return value * 2

t = [1, 2, 10]
m = map(work, t)                   # принимает два аргумента: функция и коллекция
print(m)
# result: <map object at 0x05AE92D0>
print(list(m))
# result: [2, 4, 20]                # выводит результат через list()

m = map(lambda x: x * x, [1, 2, 10])       # та же запись но короткая
print(list(m))
# result: [1, 4, 100]

# -------------------------------------------------------------------
# filter
f = filter(lambda x: x > 3, [1, 2, 3, 4, 5])
print(list(f))
# result: [4, 5]

# -------------------------------------------------------------------
#  reduce выполняет функцию для каждого объекта массива оперируя остатком
from functools import reduce
r = [1, 4, 2, 3]
result = reduce(lambda x, y: x + y, r)   # 1+4, 5+2, 7+3
print(result)
# result: 10
result = reduce(lambda x, y: x * y, r)   # 1*4, 4*2, 8*3
# result: 24

#----------------------------------------------------------------------
# ДЕКОРАТОРЫ, принимает на вход функцию и возвращает функцию


def another_function(func):          # принимает аргумент функцию func
    def other_func():                # вложеная функция other_func()
        val = "Результат от %s это %s" % (func(), eval (func()))
        return val
    return other_func()

def a_function():                 # обычная функция
    return '1 + 1'

if __name__ == '__main__':
    value = a_function()
    print(value)
# result: 1 + 1
    decorator = another_function(a_function)   # передаем a_function() функции another_function(func) в качестве аргумента
    print(decorator)
# Результат от 1 + 1 это 2

#---------------------------------------------------------------------------------------------

def another_function(func):          # принимает аргумент функцию func
    def other_func():                # вложеная функция other_func()
        val = "Результат от %s это %s" % (func(), eval (func()))

        return val
    return other_func

@another_function                 # функция a_function() будет аргументом функции another_function(func)
def a_function():                 # обычная функция
    return '1 + 1'

if __name__ == '__main__':
    value = a_function()          # вызов фунункции a_function() возвращает функцию other_func()
    print(value)
# Результат от 1 + 1 это 2

# ---------------------------------------------------------------------------------------------

def logger(function):             # задаем функцию logger с внутреней функцией inner
    def inner(x, y):
        result = function(x, y)
        print('Result is', result)
        return result
    return inner

def sum(x, y):                     # задаем две функции sum и mult
    return x + y

def mult(x, y):
    return x * y

s = logger(sum)                    # подаем на вход logger функцию  sum
s_result = s(9, 12)
print(s_result)
# result: Result is 21
        # 21
m = logger(mult)                    # подаем на вход logger функцию  mult
m(2, 5)
# result: Result is 10
print(s, m)
# result: <function logger.<locals>.inner at 0x0052DF18> <function logger.<locals>.inner at 0x0052DF60>

# ----------------------------------------------------------------------------------------

def logger(function):             # задаем функцию logger с внутреней функцией inner
    def inner(x, y):
        result = function(x, y)
        print('Result is', result)  # добавляем строку при выполднении любой из функций sum или mult
        return result
    return inner

@logger                            # используем decorator
def sum(x, y):                     # задаем две функции sum и mult
    return x + y

@logger
def mult(x, y):
    return x * y

sum(34, 7)
# result: Result is 41
mult(20,8)
# result: Result is 160
# -----------------------------------------------------------------------------------
