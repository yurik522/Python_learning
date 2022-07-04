'''Напишите программу, удаляющую из текста все слова, содержащие "абв".'''

user_input = input('Please, input text:\n').split()
processed_text = list(filter(lambda x: not 'абв' in x, user_input ))
print(*processed_text)