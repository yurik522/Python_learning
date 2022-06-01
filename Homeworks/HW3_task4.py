'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
'''
n = int(input('Введите число: '))
print(f'{n:0b}') # самый простой способ)))
binary_list = []
while n > 0:
    binary_list.insert(0, n % 2)
    n //= 2
print(*binary_list)    