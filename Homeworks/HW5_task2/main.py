from user_interface import parameters_game as param
import easy_level as easy
import hard_level as hard
from controller import first_move as first
from controller import choice_level as ch_l

print('Привет, дорогой друг. Давай поиграем в интересную игру.\n \
поделим между собой много конфет. Кто заберет последнюю\n \
тому достанутся все')

total_count, max_amount = param()

if ch_l():
    if first():
         easy.first_move_user(total_count, max_amount)
    else:
        easy.first_move_computer(total_count, max_amount) 
else:
    if first():
        hard.first_move_user(total_count, max_amount)
    else:
        hard.first_move_computer(total_count, max_amount) 
