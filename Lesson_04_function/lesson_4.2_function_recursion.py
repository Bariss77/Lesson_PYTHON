# Рекурсия
def matryoshka(n):
    if n ==1:                           # крайний случай
        print("Матрешечка")
    else:
        print("Верх матрешки n=", n)
        matryoshka(n-1)
        print("Низ матрешки n=", n)

matryoshka(5)
#-------------------------------------------------------------
# Рисуем вложенные квадраты

import graphics as gr

window = gr.GraphWin("Russian game", 600, 600) # обозначаем размер окна, где будем рисовать
alpha = 0.2
def fractal_rectangle(A, B, C, D, deep=10): # A, B, C, D точки с парами координат, deep глубина рекурсии (рисуем десять квадратов)
    if deep < 1:  # крайний случай
        return
        # РИТСУЕМ ВНЕШНИЙ КВАДРАТ:
    #gr.Line(gr.Point(*A), gr.Point(*B)). draw(window)  # создать линию из точек *A и *B(* так как более одной коордтинаты) и нарисовать в окне
    #gr.Line(gr.Point(*B), gr.Point(*C)). draw(window)
    #gr.Line(gr.Point(*C), gr.Point(*D)). draw(window)
    #gr.Line(gr.Point(*D), gr.Point(*A)). draw(window)
    for M, N in (A, B), (B, C), (C, D), (D, A):
         gr.Line(gr.Point(*M), gr.Point(*N)). draw(window) # ЦИКЛ ЗАМЕНЯЕТ ВЕРХНИЕ ЧЕТЫРЕ СТРОКИ
    # рисуем вложеный квадрат со сдвигом alpha:
    A1 = (A[0]*(1-alpha)+B[0]*alpha, A[1]*(1-alpha)+B[1]*alpha)
    B1 = (B[0]*(1-alpha)+C[0]*alpha, B[1]*(1-alpha)+C[1]*alpha)
    C1 = (C[0]*(1-alpha)+D[0]*alpha, C[1]*(1-alpha)+D[1]*alpha)
    D1 = (D[0]*(1-alpha)+A[0]*alpha, D[1]*(1-alpha)+A[1]*alpha)
    fractal_rectangle(A1, B1, C1, D1, deep-1)

fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), deep=100)

#-------------------------------------------------------------
# ФАКТОРИАЛ:

# n! = (n - 1)! * n

def f(n):
    assert n>=0, "Факториал отрицательного ч. не определен" # утверждаем, что n неотрицательное, иначе ошибка
    if n == 0:
        return 1
    return f(n-1)*n

print(f(3))

# Алгоритмс Эвклида: НАЙБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ ДЛЯ ДВУХ ЦЕЛЫХ ЧИСЕЛ:

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(2, 5)) # result: 1
print(gcd(6, 9)) # result: 3
#-------------------------------------------------------------
# Генерация всех перестановок:
# {1, 2, 3, .........N} - числа
# Nx * (N(x) - 1) * (N(x) - 2) * ....* 2 * 1 = N! (N факториал колличество всех перестановок)
def generate_number(N, M, prefix=None):   # N - система счисления, M - кол-во чисел, prefix - список
    """ Генерирует все числа (с лидирующими незначащими нулями) в N-ричной системе счисления (N <= 0)
        длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()

generate_number(3, 4)

#-------------------------------------------------------------
def find(number, A):
    """ Ищет A и возвращает True, если такой есть, и False, если такой нет
    """
    for x in A:
        if number == x:
            return True
    return False

def generate_permutation(N, M=-1, prefix=None):
    """Генерация всех перестановок N чисел в M позициях,
       с префиксом prefix
    """
    M = N if M == -1 else M   # если не задан M, то M = -1 по умолчанию, соответственно M приобретает значение Nself.
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=", ", sep="")    # выводим в строку, чрез запятую
        return
    for number in range(1, N+1):
        if find(number, prefix):     # исключаем повторяющиеся комбинации
            continue
        prefix.append(number)
        generate_permutation(N, M-1, prefix)
        prefix.pop()

generate_permutation(4, 3)
