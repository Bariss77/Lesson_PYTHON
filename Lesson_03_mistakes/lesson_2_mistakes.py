# ошибки
# ValueError example: int('mama')
# ZeroDivisionError example: x/0
# TypeError example: len(9)
try:
    1/0
except:
    print('Error happened')
# result Error happened
try:
    1/1
except:
    print('Error happened')
# result 1.0
try:             # попытаться
    1/0          # поделить на ноль
    print('I devide by 0')
except:
    print('Error')
# result Error
try:
    1/input('Enter the number: ')
except:
    print('Error. Your number is 0')
0
# result Error. Your number is 0

try:        # если ожидаются разные ошибки
    1/int(input('x: '))
except ZeroDivisionError:
    print('/0')
except TypeError:
    print ('Wrong tipe')
except ValueError:
    print ('Bad input')
x:fff
# result Bad input

try:         # вывод ошибки на экран
    1/int(input())
except ZeroDivisionError as e:
    print (e)
# 4
# 0.25
try:         # вывод ошибки на экран
    1/int(input())
except ZeroDivisionError as e:
    print (e)
# 0
# result division by zero

try:           # отслеживание ошибки ключа в словаре
    d={'key':23}
    print(d['does not key'])
except KeyError as e:
    print ("Got it", e)
# result Got it 'does not exist' (ключ не существует)

l=[3, 9]       # отслеживание ошибка в индексе листа
try:
    l[4]
except IndexError as e:
    print (e)
# result List out of range

try:             # если щшибка то ..., иначе ....
    print(1/int(input())
except ZeroDivisionError:
    print('Nope')
else:
    print ('Else claus')
# Nope     # if enter 0
# Else claus # if enter !=0
