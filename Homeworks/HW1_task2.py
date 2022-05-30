'''
Напишите программу для. проверки истинности утверждения 
¬(X v Y v Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
x = False 
y = False
z = True
print(not(x or y or z) == (not x and not y and not z))
