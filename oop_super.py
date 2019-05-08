# super() – обращение к родителю

class Calc(object):

    def __init__(self, value):
        self.value = value

    def count(self):
        return self.value * 10


class ExtCalc(Calc):

    def __init__(self, value, k):
        super().__init__(value)
        self.k = k

    def count(self):
        prev = super().count()
        return prev * self.k

class PlusCalc(ExtCalc):

    def __init__(self, value, k, plus):
        super().__init__(value, k)
        self.plus = plus

    def count(self):
        prev = super().count()
        return prev + self.plus


numb = PlusCalc(5, 2, 3)
print(numb.count())

# print(dir(Calc))
# print(PlusCalc.__mro__) # показывает последовательность цепочки родителей