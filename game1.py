import random

some_digit = random.randint(1, 100)

def check_digit():
    inp = input('Число: ')
    d = int(inp)

    if d == some_digit:
        print('Вы угадали')

    elif d > some_digit:
        print('Меньше')
        return check_digit()

    elif d < some_digit:
        print('Больше')
        return check_digit()


check_digit()