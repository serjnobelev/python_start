import random

WORDS = ('name', 'done', 'bind', 'word')
some_word = random.choice(WORDS)
lifes = 4

def check_word(word):
    if word == some_word:
        return some_word
    else:
        res = ''
        for i, val in enumerate(some_word):
            try:
                if some_word[i] == word[i]:
                    res += some_word[i]
                else:
                    res += '_'
            except IndexError:
                break
        if len(res) < len(some_word):
            res += '_' * (len(some_word) - len(res))
        return res

while lifes != 0:
    inp = input('Угадайте слово: ')
    res = check_word(inp)
    if res == some_word:
        print('Вы угадали')
        break
    else:
        print(res)
        lifes -= 1
        if lifes != 0:
            print('У Вас осталось %s жизней' % str(lifes))
        else:
            print('Вы проиграли')
            break
