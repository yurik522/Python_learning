# import zipfile
# import os


# dir_path = os.getcwd()
# files_path = [file_path for file_path in os.listdir(dir_path) if os.path.isfile(file_path)]
# zip_path = os.path.join(dir_path, 'new.zip')
# zip_file = zipfile.ZipFile(zip_path, 'w')
# for file_path in files_path:
#     zip_file.write(file_path)
# zip_file.close


# dir_path = os.getcwd()
# files_path = [file_path for file_path in os.listdir(dir_path) if os.path.isfile(file_path)]
# zip_path = os.path.join(dir_path, 'new.zip')
# # zip_file = zipfile.ZipFile(zip_path, 'w')

# with zipfile.ZipFile(zip_path, 'w') as zip_file:
#     for file_path in files_path:
#         zip_file.write(file_path)

''''2. Для натурального n создать словарь индекс-значение, состоящий из 
элементов последовательности 3n + 1.
    *Пример:*
    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
'''
# n = int(input('Введите число:'))
# my_dict = {}
# for i in range(1, n+1):
#     my_dict[i] = 3*i+1
# print(my_dict)

# n = int(input('Введите число: '))
# dict = {i: 3*i + 1 for i in range(1, n + 1)}
# print(dict)

# text_user1 = input('введите два слова:')
# text_user2 = input('введите ещё два слова:')
# result = 0
# for i in text_user1:
#     for k in text_user2:
#         if k == i:    
#             result += 1
# print(f'Символы повторяются {result} раз')

# first_string = input('Введите первую строку: ')
# second_string = input('Введите вторую строку: ')
# a = set(first_string)
# b = set(second_string)
# print(a)
# print(b)
# c = (a & b)
# print(len(c))


day_number = int(input('Пожалуйста, введите номер дня недели:'))
if  (day_number == 6) or (day_number == 7):
    print('Сегодня можно остаться дома)')
elif 0 < day_number < 6 :
    print('Собрирайся на работу, д6орогой друг :(')
else :
    print('Я не понимаю тебя, мой друг, попробуй еще')
    
# language = "german"
# daytime = "morning"
# if language == ("english" or "german"):
#     if daytime == "morning" :
#         print("Good morning")
#     else:
#         print("Good evening")
# else:
#     if daytime == "morning":
#         print("Доброе утро")
#     else:
#         print("Добрый вечер")

m = 8**0.6666666666666667

print(round(m, 5))