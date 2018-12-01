# возведение в степень:
def exponentiation(x, n):
    a = 1
    for i in range(1, n+1):
        a = a * x
    print(a)
exponentiation(5, 3)     # result: 125

# ИЛИ через рекурсию:
def pow(x, n):
    if n == 0:
        return 1
    else:
        return pow(x, n-1) * x
print(pow(5, 3))         # result: 125
# -------------------------------------

# ФУНКЦИИ: на вход подаем два аргумента x и y, на выходе находим максимум max2
def max2(x, y):
    if x > y:
        return x
    return y

# ФУНКЦИИ: на вход подаем три аргумента x, y и z, на выходе находим максимум max3
def max3(x, y, z):
    return max2(x, max2(y, z)) # два раза вызываем фунуцию max2
print(max3(5, 2, 7))    # result: 7

# -------------------------------------
def hello_separated(name = "World", separator = "-"):   # объявляем аргументы по умолчанию
    print("Hello", name, sep=separator) # вставит "separator" между первым и вторым словом без пробелов

hello_separated(separator = "***")  # result: Hello***World

# ---------------------------------
# Создание функции:
def draw_house(window, upper_left_corner, width): # задаем аргументы: (пример) где рисовать, начальна точка, ширина
    """ Функция, которая рисует дом """ # описываем подробно функцию
    pass  # тело
input()
# --------------------------------
def is_simple_number(x):
    """ Определяет является ли число простым. Если простое, то возвращается True, а иначе - False. """
    # Документ-строка функции вызывается при помощи help(x), можно подробно описать функцию
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True

print(is_simple_number(3))           # result: True
print(is_simple_number(20))          # result: False
# -------------------------------
def array_search(A, N, x):
    """ Осуществляет поиск числа x в массиве A от 0 до N-1 индекса включительно. Возвращает индекс элемента x в массиве A, или -1, если такого нет."""
    for k in (N):
        if A[k] == x:
            return k
    return -1

def test_array_search():  # функции тестирования:
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

def test_array_search():  # функции тестирования:
    A1 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test2 - ok")
    else:
        print("#test3 - fail")

# --------------------------------------------
def invert_array(A, N):
    """ Обращаем массив поворотом задом наперед
    в рамках ндекса от 0 до N-1 """
    for k in range(N // 2):
        A[k], A[N-1-k] = A[N-1-k], A[k]

# функции для проверки
def test1_invert_array():
    A1 = [1, 2, 3, 4, 5]
    invert_array(A1, 5)
    if A1  == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("test1 - fail")

def test2_invert_array():
    A2 = [0, 0, 0, 0, 0, 0, 10]
    invert_array(A2, 7)
    if A2  == [10, 0, 0, 0, 0, 0, 0]:
        print("#test1 - ok")
    else:
        print("test1 - fail")
#--------------------------------
# циклический сдвиг влево
A = [1, 2, 3, 4, 5] # получить [2, 3, 4, 5, 1]
tmp = A[0]
N = len(A)
for k in range(N-1):
    A[k] = A[k + 1]
    A[N-1] = tmp
                                             # ЧАВОТО НЕ РАБОТАЕТ
print(A)

# циклический сдвиг вправо
A = [1, 2, 3, 4, 5] # получить [5, 1, 2, 3, 4]
tmp = A[N - 1]
for k in range(N - 2, -1, -1):
    A[k + 1] = A[k]
    A[0] = tmp

print(A)

print('-----------------------------------')

# Квадратичные сортировки

def insert_sort(A):
    """ сортировка списка A вставками """
    N = len(A)
    for k in range(1, N):
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

def choise_sort(A):
    """ сортировка списка A выбором """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    """ сортировка списка A методом пузырька """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

# функции тестирования:

def test_sort(sort_algorithm):
    print ("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))  # генерируем list [10, 11 ...19, 0, 1 .. 9]
    A_sorted = list(range(20))        # генерируем [0, 1 ...19]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

test_sort(insert_sort)
test_sort(choise_sort)
test_sort(bubble_sort)

print('-----------------------------------')
