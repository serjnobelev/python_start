# лямбда функции – анонимные функции, позволяют создавать функции только для одного раза
# могут занить только одну строку
# использовать крайне редко, некоторые её не используют принципиально

d = lambda x, y: x + y
print(d(2,4))

def double(val):
    return val * 2

l = [1, 2, 3, 4, 5]
m1 = map(double, l)
# map return generator
print(list(m1))

m2 = map(lambda x: x * 2, l)
print(list(m2))

f = filter(lambda x: x > 2, l)
print(list(f))

# когда нужно перемножить все числа в списке – используем reduce
# reduce – выполняет функцию для каждого объекта из массива входных параметров, оперируя остатком

from functools import reduce
r = [1, 2, 3, 4]
r1 = reduce(lambda x, y: x + y, r)
r2 = reduce(lambda x, y: x *  y, r)
print(r1)
print(r2)