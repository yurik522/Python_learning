# a = [1, 2, 3]
# b = a
# b.append(333)
# print(*a)
# from copy import deepcopy

'''Реализуйте алгоритм задания случайных чисел
без использования встроенного генератора
псевдослучайных чисел'''
from datetime import datetime as dt

# def my_random(min, max):
#     rnd = dt.now().microsecond
#     scale = max - min
#     return int(rnd/1000000 * scale + min)

# print(my_random(10, 50))


'''Задайте список. Напишите программу, которая определяет, присутствует
ли в заданном списке строк некое число'''

# my_list = ["123", "234", '123', "567", '5', '8']

# def is_number_in(number):
#     for item in my_list:
#         if str(number) in item:
#             return True
#     return False
# print(is_number_in(4))

""""""
# def find_number(num, lst):
#     return str(num) in lst or num in lst



list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"] # "qwe" 3
list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] # "йцу" 5
list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"] # "йцу" -1
list4 = ["123", "234", 123, "567"] # 123 -1
list5 = [] # -1

# def find_index_to_in (lst, str):
#     count = 0
#     for i in lst:
#         if str(i) == str:
#             count +=1

''''''
def find_second(str, lst):
    if lst.count(str) > 1:
        return lst.index(str, lst.index(str) + 1)
    return "-1"

print(find_second("qwe", list1))
''''''
def find_second(lst):
    for i in range(len(lst)):
        if lst.count(lst[i]) > 1:
            return (lst[i], lst.index(lst[i], i + 1))
    return "-1"

'''Для натурального N создать множество: 1, -3, 9, -27, 81'''
def creat_set(n):
    if n == 1:
         return 1
    else:
         n = -n
    return n**n
''''''
def give_me_mnojestvo(N):
    return [(-3) ** i for i in range(N)]

print(give_me_mnojestvo(5))
''''''
n = int(input('Введите число:'))
for i in range(0, n+1):
    print((-3)**i)


'''Сформировать сисок из N членов последовательности. 
Список записать в файл "number_list.txt" (в одну строку - одно число).
'''
