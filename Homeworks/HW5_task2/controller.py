from random import randint

def first_move():
    print('А теперь давай бросим монетку, кто будет ходить первым)')
    user_choice = int(input('Орел - жми 1. Решка - жми 0:\n'))
    input('Бросай монету(жми ввод)\n')
    toss_coin = randint(0, 0)
    print(toss_coin)
    return True if user_choice == toss_coin else False

def choice_level():
    print('Выбери сложность игры: 1 - простая; 2 - сложная')
    return True if input() == '1' else  False