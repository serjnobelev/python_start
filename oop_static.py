# super() – обращение к родителю

class My(object):

    def __init__(self, value):
        self.value = value

    @staticmethod
    def some_static():
        return 'static method'


print(My.some_static())