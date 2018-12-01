s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
r = range(0,21)

for i in s:       # одинаково с нижним кодом
    print(i)

print('-' *20)
# ---------------------------------------------------------
for i in r:       # одинаково с верхним кодом
    print(i)

print('-' *20)
# -----------------------------------------------------------
import sys
print(sys.getsizeof(10))       # размер занимаемой памяти
# resurt: 14

print(sys.getsizeof(10000))      # размер занимаемой памяти
# resurt: 14

print(sys.maxsize)               # макс. число
# result: 2147483647

print(sys.maxsize + 1)
# result: 2147483648

print(sys.getsizeof(''))         # размер пустой строки
# result: 25
print(sys.getsizeof('a'))         # размер  строки
# result: 26
print(sys.getsizeof('abc'))         # размер  строки
# result: 28

print(sys.getsizeof([ ]))         # размер пустого списка
# result: 36
print(sys.getsizeof([1]))         # размер  списка
# result: 40
print(sys.getsizeof([1, 2, 3]))         # размер  списка
# result: 48

print(sys.getsizeof([1, 2, 3, 'abs']))   # размер  списка  и строки
# result: 52

print('-' *20)
# -----------------------------------------------------------

x = range(0, 10, 2)
print(sys.getsizeof(x))
# result: 24

x = range(0, 100, 2)
print(sys.getsizeof(x))
# result: 24

y = (list(range(0,100)))
print(y)
# result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34 ......]
print(sys.getsizeof(y))
# result: 508
# ВЫВОД генератор позволяет экономить память и не хранить все значения, так как знает как их получить

print('-' *20)
# -----------------------------------------------------------

# Генератор чисел фибоначи
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

x = fib()
print(x)
# result: <generator object fib at 0x004DF060>      ОБЪЕКТ - ГЕНЕРАТОР

print(next(x))             # запускаем генератор через next
# result: 0
print(next(x))
# result: 1                #  0 + 1 = 1
print(next(x))
# result: 1
print(next(x))
# result: 2                #  1 + 1 = 2
print(next(x))
# result: 3                #  1 + 2 = 3
print(next(x))
# result: 5                #  2 + 3 = 5
print(next(x))
# result: 8                #  3 + 5 = 8
# и т. д.

print('-' *20)
# -----------------------------------------------------------

a = iter([2, 4, 6, 8])             # итератор
print(a)
# result: <list_iterator object at 0*021C0C90>
print(next(a))
# result: 2
print(next(a))
 # result: 4
print(next(a))
 # result: 6
print(next(a))
 # result: 8
# print(next(a))
# .........StopIteration       кончились значения в списке a

print('-' *20)
# -----------------------------------------------------------

def cities():                 # список превращаем в итератолр
    arr = ['Moskow', 'Novosibirsk', 'Perm', 'Irkutsk', 'Tula']
    return iter(arr)         # возвращаем итератор

a = cities()                 # создаем генератор
print(next(a))
# result: Moskow
print(next(a))
# result: Novosibirsk   и так далее
