'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''
import math

N = int(input("Введите число:")) # Factorial Calculation Using the Built-in Method
for i in range(0, N + 1):
    print(f'{i}! = {math.factorial(i)}')

def factorial(N): # Factorial Calculation Using the recursion
    if (N == 0 )or(N == 1):
        return 1
    else:
        return N * factorial(N-1)

factorial_list = []
for i in range(0, N + 1):
    factorial_list.append(factorial(i))
print(factorial_list)