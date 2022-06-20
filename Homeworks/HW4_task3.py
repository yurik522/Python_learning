'''
Задайте последовательность чисел. Напишите программу, которая выведет список 
неповторяющихся элементов исходной последовательности.
'''
from random import randint
random_list = []
for i in range(1, randint(0, 30)):
    random_list.append(randint(0, 15))
new_list = []
for i in range(0, len(random_list)):
    j = random_list.count(random_list[i])
    if j > 1:
        continue
    else:
        new_list.append(random_list[i])
print(random_list)
print(new_list)
