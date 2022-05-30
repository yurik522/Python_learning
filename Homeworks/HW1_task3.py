'''
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
 
Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''
x = int(input('Введите координату x:'))
y = int(input('Введите координату y:'))

if (x > 0 ) and (y > 0):
    print("first quarter")
elif (x < 0 ) and (y > 0):
    print("second quarter")
elif (x < 0) and (y < 0):
    print("third quarter")
elif (x > 0) and (y < 0):
    print("third quarter")
elif x == 0:
    print("The point lies on the x-axis")
else:
    print("The point lies on the y-axis")

