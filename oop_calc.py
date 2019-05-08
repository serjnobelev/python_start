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


numb = ExtCalc(5, 1)
print(numb.count())