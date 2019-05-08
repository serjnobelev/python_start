# Инкапсуляция работает не совсем строго

class Example(object):
    def __init__(self):
        self.a = 1 # public
        self._b = 2 # protected
        self.__c = 3 # private
        print('A: {}, B: {}, C: {}'.format(self.a, self._b, self.__c))

    def call(self):
        print('Called')

ex = Example()
print(ex.a)
print(ex._b)

