'''
Ввычислить число пи, (использовать формулу Нилаканта или что лучше) c заданной
 точностью d
'''
from decimal import Decimal
from decimal import getcontext
getcontext().prec = 25

# def pi(n: int, precision: float):
#     pi = 3

#     for i in range(1, n, 4):        
#         delta  = Decimal((4/((i + 1)*(i + 2)*(i + 3)) - 4/((i + 3)*(i + 4)*(i + 5))))
#         if (delta_i - delta) < precision:
#             break
#         delta_i = delta
#         pi += delta

#     print(pi)
#     print(type(pi))
def pi_nilakant(precision: float):
    pi = 3
    i = 1
    delta_i = 1
    while True:
                          # the number PI through the Nilakantha's series    
        delta  = Decimal((4/((i + 1)*(i + 2)*(i + 3)) - 4/((i + 3)*(i + 4)*(i + 5))))
        if (delta_i - delta) == precision:
            break
        delta_i = delta
        pi += delta
        i += 4
        print(pi)
d = float(input('Задайте точность определения числа pi: '))
pi_nilakant(d)

'''  3,141592653589793238462643383279 5028841971 6939937510 5820974944 5923078164 0628620899'''

# s = Decimal(1);   #Signal for the next operation # для собственного развития)
# pi = Decimal(3);

# print ("Approximation of the number PI through the Nilakantha's series\n")
# n = int(input("Enter the number of iterations: "))    

# print("\nPlease wait. Running...\n");      

# for i in range (2, n * 2, 2):
#     pi = pi + s * (Decimal(4) / (Decimal(i) * (Decimal(i) + Decimal(1)) * (Decimal(i) + Decimal(2))))
#     s = -1 * s

# print ("Aproximated value of PI :")
# print (pi)


