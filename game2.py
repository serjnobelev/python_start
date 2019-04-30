import random

words = ('name', 'done', 'bind', 'word')
some_word = words[random.randint(0, len(words) - 1)]
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
            print('У Вас осталось ' + str(lifes) + ' жизней')
        else:
            print('Вы проиграли')
            break
