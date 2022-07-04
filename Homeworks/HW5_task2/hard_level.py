from random import randint

def first_move_user(total_count, max_amount):
   
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

def first_move_computer(total_count, max_amount):
    
    while total_count > 0:
       
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