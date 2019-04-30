import random

WORDS = ('name', 'done', 'bind', 'word')
some_word = random.choice(WORDS)

unknown_char = '_'
res = list(unknown_char * len(some_word))
lifes = 5

def check_word(input, res):
    if input in some_word:
        for i, val in enumerate(some_word):
            if input == some_word[i]:
                if res[i] != some_word[i]:
                    res[i] = input
    return res


while lifes != 0:
    inp = input('Назовите букву: ')
    res = check_word(inp, res)

    if res == list(some_word):
        print('Вы угадали слово')
        break
    else:
        print(''.join(res))
        lifes -= 1
        if lifes != 0:
            print('У Вас осталось %s жизней' % str(lifes))
        else:
            print('Вы проиграли')
            break
