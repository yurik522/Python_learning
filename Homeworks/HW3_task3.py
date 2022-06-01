'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.

Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
from random import random

n = int(input('Please, input the length ouf the list: '))
m = int(input('Please, Specify Rounding Precision:'))
float_list = []
for i in range(0, n):
    float_list.append(round(random()*20, m))
print(float_list)

fraction_list = []  

for i in float_list:  # gethering fraction parts into a list
    fraction_list.append(round((i - int(i)), m))
print(fraction_list)
result = round((max(fraction_list) - min(fraction_list)), m)
print(result)