import sys
import random

# print(sys.getsizeof(1))
# print(sys.getsizeof('ab'))
# print(sys.getsizeof('бв'))
# print(sys.getsizeof([1]))
# print(sys.getsizeof([1,2,'ab']))

# x = range(0,10)
# print(sys.getsizeof(x))
# print(sys.getsizeof(range(0,10)))
# print(sys.getsizeof(list(x)))

m = [f for f in '213']
c = (f for f in '213') # generator
print(c)
print(list(c))

# чаще используют такую запись
# числа Фиббоначи
# yield возвращает значение, но не останавливает вывод
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib()
# next(gen)
# next(gen)
# next(gen)
# next(gen) # generator сработает от последнего числа в yield
# print(next(gen))

fibonachi = []
i = 0
while i < 10:
    fibonachi.append(next(gen))
    i += 1

print(fibonachi)

# генератор работает с одним значением только один раз
# как только знакончились значения в генераторе, возникнет Exception
# работает только с yield и сраюатывает только при вызове – next()

# если что-то можно завернуть в генератор – лучше использовать его,
# он потребляет меньше памяти, так как хранит только последнее значение

def str_gen1():
    yield 'val1'

str1 = str_gen1()
print(next(str1))
# print(next(str1)) # возникнет ошибка, так как закончились значения иттератора

def str_gen2():
    yield 'val3'
    yield 'val4'

str2 = str_gen2()
print(next(str2))
print(next(str2))

# из массива получить генератор
def cities():
    arr = [
        'Киев', 'Днепр', 'Бердянск'
    ]
    return iter(arr)

print(cities())

cit = cities()

while True:
    try:
        print(next(cit))
    except:
        StopIteration
        print('End of Iter')
        break

# fib_gen = fib()
# for index, _ in enumerate(range(0, 10)): # _ – имя переменной, которое использовать не планируется, так принято
#     print(index, next(fib_gen))

def some_nmb():
    while True:
        yield random.random()


s_nmb = some_nmb()

t = 0
while t < 10:
    print(round(next(s_nmb) * 100))
    t += 1
