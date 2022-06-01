'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
 и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

'''
from random import randint

def fill_list_integer_random(N: int):
    list = []
    for i in range(0, N):
        k = randint(-10, 10)
        list.append(k)
    return list

l = int(input('Please, input the length ouf the list: '))
list = (fill_list_integer_random(l))
i = 0
j = -1
result_list = []
# result = 0
while i < len(list)/2:
    result = list[i] * list[j]
    result_list.append(result)
    i += 1
    j -= 1
print(f'{list} \n {result_list}')
