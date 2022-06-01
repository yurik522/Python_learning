'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
'''

def negative_fibonacсi_list(k: int):
    list = [1, 0, 1]
    if k == 0:
        list = [0]
        return list
    elif k == 1:
        return list
    else:
        n = 2
        while n <= k:
            list.append(list[-1] + list[-2])  # F-n = -1**(n+1)(Fn-1 + Fn-2)
            list.insert(0, (list[-1]*(-1)**(n+1)))
            n += 1
    return list

n = int(input('Какое количество чисел Фибоначи Вы желаете видеть?: '))
print('Пожалуй, покажу вам и отрицательный ряд)')
print(negative_fibonacсi_list(n))
# for i in negative_fibonacсi_list(n):
#     print(i)
