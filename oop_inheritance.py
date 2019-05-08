
class Parent:
    def __init__(self):
        print('Parent init')
        self.name = 'Parent'

    def do(self):
        print('Parent do(): {}'.format(self.name))


class Child(Parent):
    def __init__(self):
        print('Child init')
        self.name = 'Child'

# parent = Parent()
# parent.do()

child = Child()
child.do()

print(Child.__mro__)