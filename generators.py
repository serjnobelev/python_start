import sys

print(sys.getsizeof(1))
print(sys.getsizeof('ab'))
print(sys.getsizeof('бв'))
print(sys.getsizeof([1]))
print(sys.getsizeof([1,2,'ab']))

x = range(0,10)
print(sys.getsizeof(x))
print(sys.getsizeof(range(0,10)))
print(sys.getsizeof(list(x)))

m = [f for f in '213']
c = (f for f in '213') # generator
print(c)
print(list(c))