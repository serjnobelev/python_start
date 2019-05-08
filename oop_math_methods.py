# __some__ – магические методы
# математические и логические действия
# методы для работы с индексированием, слайсами, последовательностями
# методы для создания и вызова объектов
# методы для работы с атрибутами классов

class MathObject(object):
    def __init__(self, value):
        self.value = value

    # Comparing
    def __eq__(self, other):
        return self.value == other

    def __ge__(self, other):
        return self.value >= other

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    # Operations
    def __neg__(self, other):
        return -self.value

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        return self.value * other

    # to String
    def __str__(self):
        return 'MathObject: {}'.format(self.value)

class DictFunct(object):

    def __init__(self, values = None):
        if values is None:
            self.values = {}
        elif isinstance(values, dict):
            self.values = values
        else:
            raise ValueError()

    # Converting to string:
    def __str__(self):
        return str(self.values) if self.values else ''

    # Item Management
    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    # Iteration
    def __iter__(self):
        return iter(self.values)

    def __contains__(self, item):
        return item in self.values

    def __len__(self):
        return len(self.values)


# d = MathObject(4)
# print(d )

d = DictFunct({'a':1, 'b':2})
print(len(d))
print('a' in d)
d['c'] = 'some'
print(d, d['b'])


b = 0
print(bool(b) is True)