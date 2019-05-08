class Car:
    def __init__(self, color = 'white'):
        self.color = color

c = Car('red')

print(c.color)

class Room:
    number = 'Room 23'
    floor = 4

r1 = Room()
r2 = Room()

print(r1.number, r2.number)
print(r1.floor, r2.floor)

class Door:
    def open(self):
        print('self is ', self)
        print('Door is opened!')
        self.opened = True

d = Door()
print(d)
d.open()

print(d.opened)

class Terminal:
    def hello(self, name):
        print('Hello, ', name)

t = Terminal()
t.hello('Serj')


class Window:
    is_opened = False

    def open(self):
        self.is_opened = not self.is_opened

w1 = Window()
print(w1.is_opened)
w1.open()
print(w1.is_opened)