from random import randint
total_count = int(input('Выбери, сколько конфет будем делить:'))
max_amount = int(input('Выбери, сколько конфет можно будет забирать за один раз:'))
print('А теперь давай бросим монетку, кто будет ходить первым)')
user_choice = input('Орел - жми 1. Решка - жми 0:\n')
input('Бросай монету(жми ввод)\n')
toss_coin = randint(1, 1)
print(toss_coin)

if int(user_choice) == toss_coin:
    while total_count > 0:
        user_count = int(input('Твой ход: \n'))
        if user_count > max_amount:
            print('Неправильный ход, можно брать не более %d конфет' %(max_amount))
            continue
        if  user_count <= 0:
            print('Нужно взять хотя бы одну конфету')
            continue
        total_count = total_count - user_count
        if total_count < 0:            
           total_count = total_count + user_count
           print(f'Осталось только {total_count} конфет')
           continue
        elif total_count == 0:
            print('Поздравляю, ты выиграл')
            break
        else:
            print(f'осталось {total_count} конфет')
        if not total_count % (max_amount + 1): 
            comp_count = randint(1, max_amount)
            total_count = total_count - comp_count
        else:
            comp_count = total_count % (max_amount + 1)
            total_count = total_count - comp_count
        if (total_count == 0) or (total_count < 0):
            print(f'Я забираю {total_count + comp_count} конфет \n Конфеты закончились)')                
            print('В этот раз победа за мной, ох и объемся же я сегодня (:')
            break
        print(f'Я забираю {comp_count} конфет \n Осталось {total_count} конфет')