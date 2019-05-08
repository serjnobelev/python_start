
class Calc(object):
    def __init__(self, number):
        self.number = number

    def calc_and_print(self):
        value = self.calc_value()
        self.print_number(value)

    def calc_value(self):
        return self.number * 10 + 2

    def print_number(self, value_to_print):
        print('Number is ', value_to_print)

class CalcMy(Calc):
    def calc_value(self):
        return self.number * 20 + 50

c = CalcMy(3)
c.calc_and_print()