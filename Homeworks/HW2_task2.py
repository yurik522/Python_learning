'''
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
'''
def second_wonderful_limit(n):
    dictionary = {}
    for i in range(1, n + 1):
        dictionary[i] = round((1 + 1/i)**i, 3)
    return dictionary

print(second_wonderful_limit(1738))
print(round(sum(dict.values(second_wonderful_limit(1738))), 3))