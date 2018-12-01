

for x in A:    # перебор элементов
    print(x)

for k in range(5): # диапазон от 0 до 4
    A[k] = A[k] ** 2 # возводим в квадрат каждый элемент массива
print (A)  # result: [1, 4, 9, 25]
# -------------------------------------------
# создаем пустой массив из тысячи элементов

A = [0] * 3
top = 0 # заполняемость массива
x = int(input())
while  x != 0 and top < 3:      # заполняем массив
    A[top] = x
    top += 1
    x = int(input())
print('---------------------------')

# то же самое, через метод append:
A = []
x = int(input())
A.append(x)   # добавляем элемент  в конец листа

A.pop()       # удаляет последний элемент листа и возвращает его

B = []         # создать из A лист B только четные
A = [1, 3, 4, 2, 2, 7, 12, 5, 8, 7]
for x in A:
    if x % 2 == 0:
        B.append(x)

print(B)
# ИЛИ возможно так:
B = [x for x in A if x % 2 == 0]
print(B)


# ---------------------------------------------

for k in range(4, -1, -1):  # переворачиваем заполненый массив "задом наперед"
    print(A[k])

# копируем массив
N = int(input())  # вводим размер массива
A = [0] * N  # создаем массив A
B = [0] * N  # создаем массив B

for k in range (N):
    A[k] = int(input())   # заполняем массив A

for k in range(N):
    B[k] = A[k]   #  копируем массив A в массив B




# -------------------------------------------
'a' in 'letter'  # ключевое слово in
# result False
'a' in 'many'
# result True
'a' not in 'letter'
# result True

len('ASD KJHG DUHTRG') # получить длину строки (вкл. пробелы)
# result 15

'Your number is: {}, {} ! Great !'. format ('8', 'some') # форматирование
# result 'Your number is: 8, some ! Great !'

my_sum = 5 + 3         # переменные
print (my_sum)         # вывод на экран
# result 8
my_text = 'asd'
my_number ='123'
print(my_text + my_number)
# result 'asd123'
my_number1 = 12
my_number2 = 23
print(my_number1 + my_number2)
# result 35

print() # вывод
input() # ввод

input ('Please, write the number:')
# result Please, write the number:(пишем) 345
# result '345'
answer = input ('Please, write the number:')
# result Please, write the number:(пишем) 345
# result '345'
print (answer)
# result '345'

if 3 > 2:             # ЕСЛИ ..., ИНАЧЕ ..
    print ('Yes')
else:
    print ('No')
# result Yes
if 3 < 2:
    print ('Yes')
else:
    print ('No')
# result  No

x=10             # цикл while
while x!=10:     # УСЛОВИЕ: x не равен 0     (с англ.: "в то время как" {УСЛОВИЕ} ":" на PYTHON "..,то.." )
    print(x)
    x=x-1        # уменьшаем шаг на 1
# result
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1
while x < 10:
    print (x)
    x = x+1
# result
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

for  char in 'yellow house':   # цикл for для переменной char в строке yellow house
    print (char)
# result
#y
#e
#l
#l
#o
#w
#
#h
#o
#u
#s
#e


#    END LESSON 1
