'''
Напишите программу, которая принимает на вход координаты
 двух точек и находит расстояние между ними в 2D пространстве.
'''

import math

print('Введите координаты первой точки')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
print('Введите координаты вторй точки')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print(f'Расстяоние между точками = {round(distance, 2)}')