'''2. Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход 
определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все
 конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота "интеллектом"'''

from random import randint

print('Привет, дорогой друг. Давай поиграем в интересную игру.\n \
    поделим между собой много конфет. Кто заберет последнюю\n \
    тому достанутся все')

total_count = int(input('Выбери, сколько конфет будем делить:'))
max_amount = int(input('Выбери, сколько конфет можно будет забирать за один раз:'))
print('А теперь давай бросим монетку, кто будет ходить первым)')
user_choice = input('Орел - жми 1. Решка - жми 0:\n')
input('Бросай монету(жми ввод)\n')
toss_coin = randint(0, 0)
print(toss_coin)
def first_move_user():
    global total_count
    
    while total_count > 0:
       
        user_count = int(input('Твой ход: \n'))
        if  user_count <= 0:
            print('Неправильный ход, нужно взять хотя бы одну конфету')
            continue
        if user_count > max_amount:
            print('Неправильный ход, можно брать не более %d конфет' %(max_amount))
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
        comp_count = randint(1, max_amount)
        total_count = total_count - comp_count
        if (total_count == 0) or (total_count < 0):
            print(f'Я забираю {total_count + comp_count} конфет \n Конфеты закончились)')                
            print('В этот раз победа за мной, ох и объемся же я сегодня (:')
            break
        print(f'Я забираю {comp_count} конфет \n Осталось {total_count} конфет')

def first_move_computer():
    global total_count

    while total_count > 0:
       
        comp_count = randint(1, max_amount)

        total_count = total_count - comp_count
        if (total_count == 0) or (total_count < 0):
            print(f'Я забираю {total_count + comp_count} конфет \n Конфеты закончились)')                
            print('В этот раз победа за мной, ох и объемся же я сегодня (:')
            break
        print(f'Я забираю {comp_count} конфет \n Осталось {total_count} конфет')
        user_count = int(input('Твой ход: \n'))
        while  user_count <= 0:
            print('Неправильный ход, нужно взять хотя бы одну конфету')
            user_count = int(input('Твой ход: \n'))
                    
        while user_count > max_amount:
            print('Неправильный ход, можно брать не более %d конфет' %(max_amount))
            user_count = int(input('Твой ход: \n'))
            
        while total_count < 0:            
           total_count = total_count + user_count
           print(f'Осталось только {total_count} конфет')
           user_count = int(input('Твой ход: \n'))
        total_count = total_count - user_count
        
        if total_count == 0:
            print('Поздравляю, ты выиграл')
            break
        else:
            print(f'осталось {total_count} конфет')

if int(user_choice) == toss_coin:
    
    first_move_user()
else:
    
    first_move_computer()

      



    
    

