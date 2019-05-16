# модифицировать поведение функции можно с помощью декоратора
# принимает функцию и возвращает функцию
import time
import math

def logger(func):
    start = time.time()
    def inner(x, y):
        # print('Func is', func.__name__)
        return func(x, y)
    print('Time is', time.time() - start)
    return inner

def sum(x, y):
    return x + y

def mult(x, y):
    return x * y

s = logger(sum)
s_sum = s(1, 10)
print(s_sum)

m = logger(mult)(2, 3)
print(m)

# короткий вызов декоратора
@logger
def decor_sum(x, y):
    return x + y

print(decor_sum(1, 10))


