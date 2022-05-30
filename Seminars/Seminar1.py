# number_1 = int(input())
# number_2 = int(input())
# if number_2 == number_1 ** 2:
# 	print('Да')
# else:
# 	print('Нет')

'''  2. Напишите программу, которая на вход 
принимает 5 чисел и находит максимальное
из них.'''
# l = []
# n = int(input('Введите количество'))
# for i in range(1, n + 1)
#     l.append(int(input(f'Введите число {i}: ')))

''' Определить наибольшее число
из списка '''

# spec_list = [1, 2, 55, 8, 6, 3]
# i = 0
# max_number = spec_list[i]22

# while i < len(spec_list):
#     if spec_list[i] > max_number:
#         max_number = spec_list[i]
#     i += 1
# print(max_number)

# my_list = []
# for i in range(5):
#     my_list.append(int(input(f"Введите число №{i+1}: ")))
# print(my_list)

# max = my_list[0]
# for i in my_list:
#     if i > max: max = i
# print(max)

'''  1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    *Примеры:*
    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, '''
# N = int(input( 'Введите число: '))
# print(*[i for i in range(N*-1, N+1)])

# print('Введите число:')
# number=abs(int(input()))
# print()
# my_list=[]
# for i in range (-number,number+1):
#     my_list.append(i)
# print(*my_list)

'''Напишите программу, которая принимает на вход число и проверяет, 
кратно ли оно 5 и 10 или 15, но не 30.'''

# print('Введите число:')
# number=abs(int(input()))
# if number % 5 == 0

print('Введите число:')
number=int(input())

if (number % 5==0 and number%10==0 or number%15==0) and not number%30==0:
    print('условие выполняется')
else:
    print('не выполняется')    

