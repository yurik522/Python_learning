'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
from random import randint

def fill_list_integer_random(N: int):
    list = []
    for i in range(0, N):
        k = randint(-50, 50)
        list.append(k)
    return list

a = int(input('Please, input length a list:'))
new_list = (fill_list_integer_random(a))
print(new_list)
result = 0
for i in range(1, len(new_list), 2):
    result += new_list[i]
    
print(f'The sum of elements of odd positions is equal to {result}')
