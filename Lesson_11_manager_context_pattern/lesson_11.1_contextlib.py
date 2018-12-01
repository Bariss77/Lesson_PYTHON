# Менеджерр контекста через использование генератора.
from contextlib import contextmanager

@contextmanager
def do_work(value):
    print('some work before, __enter__')
# все что до yield выполняетсЯ до выполнения некоего кода value
    yield value
# все что после yield выполняетсЯ после выполнения некоего кода value
    print('some work after, __exit__')

with do_work(14) as w:
    print(w)

# Контекстный менеджер через генератор для открытия файла:
# ?????? Не работает
@contextmanager
def do_file(filename):
    f = open(filename)
    yield f
    f.close()

with do_file(filename) as k:
    print(k)
