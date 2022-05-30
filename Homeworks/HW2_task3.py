'''
Реализуйте алгоритм перемешивания списка.
'''
from random import randint
N = int(input('Задайте длину списка: '))

def fill_list_integer(N: int):
    list = []
    for i in range(0, N):
        list.append(i + 1) 
    return list

def shuffle_list (list: list):
    new_list = []
    copy_list = list.copy() # для отслеживания совпадения элементов
    i = 0 # счетчик позиции в новом списке
    while len(list) > 0:
        k = randint(0, len(list) - 1)        
        new_list.append(list[k])
        if new_list[i] == copy_list[i]: # для исключения совпадения со старым списком
            tmp = new_list[i]
            new_list[i] = new_list[i-1]
            new_list[i-1] = tmp
            list.pop(k) #удаляем элемент из списка для искллючения повторений
        else:
            list.pop(k)
            i += 1              
    return new_list
list = fill_list_integer(N)
print(list)
print(shuffle_list(list))

# def shuffle_list_easy(list: list): # возможны совпадения элементов со старым списком, особенно в
#     new_list = []                  # списках малой длины3
#     while len(list) > 0:
#         k = randint(0, len(list) - 1)        
#         new_list.append(list[k])
#         list.pop(k)
                   
#     return new_list
# print(shuffle_list_easy(list))